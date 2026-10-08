"""Verify standalone reference bundles and read-only freshness checks."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/sync-references.py"


class ReferenceBundles(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        (self.root / "scripts").mkdir()
        shutil.copy2(SCRIPT, self.root / "scripts/sync-references.py")
        (self.root / "references").mkdir()
        (self.root / "references/work-artifact.md").write_text(
            "# Work\n\nRead [PR guidance](pull-request.md).\n"
        )
        (self.root / "references/pull-request.md").write_text(
            "# PR\n\nUse [the template](../.github/pull_request_template.md).\n"
        )
        (self.root / ".github").mkdir()
        (self.root / ".github/pull_request_template.md").write_text("## Summary\n")
        self.skill = self.root / "skills/equilio-frame"
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text(
            "---\nname: equilio-frame\ndescription: Frame a problem.\n---\n"
            "Read [the contract](references/work-artifact.md).\n"
        )

    def run_sync(self, *arguments):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts/sync-references.py"), *arguments],
            capture_output=True, text=True,
        )

    def install(self):
        result = self.run_sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        installed = self.root / "installed"
        shutil.copytree(self.skill, installed / self.skill.name)
        return installed

    def test_standalone_install_retains_guidance_after_source_removal(self):
        installed = self.install()
        shutil.rmtree(self.root / "references")
        shutil.rmtree(self.root / ".github")
        bundle = installed / self.skill.name / "references"
        guidance = (bundle / "pull-request.md").read_text()
        self.assertIn("[the template](pull-request-template.md)", guidance)
        self.assertEqual((bundle / "pull-request-template.md").read_text().split("\n\n", 1)[1], "## Summary\n")
        self.assertTrue((bundle / "work-artifact.md").is_file())

    def test_check_reports_source_drift_without_repairing_it(self):
        self.install()
        original = (self.skill / "references/work-artifact.md").read_bytes()
        (self.root / "references/work-artifact.md").write_text("# Changed work\n")
        result = self.run_sync("--check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("changed references/work-artifact.md", result.stdout)
        self.assertEqual((self.skill / "references/work-artifact.md").read_bytes(), original)

    def test_installed_check_reports_changed_instructions_and_missing_guidance(self):
        installed = self.install()
        directory = installed / self.skill.name
        (directory / "SKILL.md").write_text("Outdated instructions\n")
        (directory / "references/work-artifact.md").unlink()
        result = self.run_sync("--installed", str(installed))
        self.assertEqual(result.returncode, 1)
        self.assertIn("changed SKILL.md", result.stdout)
        self.assertIn("missing references/work-artifact.md", result.stdout)
        self.assertEqual((directory / "SKILL.md").read_text(), "Outdated instructions\n")

    def test_matching_selection_does_not_require_unselected_skills(self):
        installed = self.install()
        other = self.root / "skills/equilio-map"
        other.mkdir()
        (other / "SKILL.md").write_text("Other skill\n")
        result = self.run_sync("--installed", str(installed))
        self.assertEqual(result.returncode, 0)
        self.assertIn("equilio-frame: CURRENT", result.stdout)
        self.assertIn("equilio-map: NOT INSTALLED", result.stdout)

    def test_missing_installation_is_reported_without_creating_files(self):
        installed = self.root / "missing"
        result = self.run_sync("--installed", str(installed))
        self.assertEqual(result.returncode, 1)
        self.assertFalse(installed.exists())

    def test_regeneration_removes_only_obsolete_generated_guidance(self):
        self.install()
        obsolete = self.skill / "references/obsolete.md"
        obsolete.write_text("<!-- Generated from references/obsolete.md; old export. -->\n")
        notes = self.skill / "references/notes.md"
        notes.write_text("Personal notes\n")
        result = self.run_sync("--check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("obsolete references/obsolete.md", result.stdout)
        result = self.run_sync()
        self.assertEqual(result.returncode, 0)
        self.assertFalse(obsolete.exists())
        self.assertEqual(notes.read_text(), "Personal notes\n")

    def test_unbundled_reference_prevents_generation(self):
        (self.root / "references/work-artifact.md").write_text(
            "Read [missing detail](../outside.md).\n"
        )
        result = self.run_sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn("reference leaves the bundle", result.stdout)
        self.assertFalse((self.skill / "references").exists())


if __name__ == "__main__":
    unittest.main()
