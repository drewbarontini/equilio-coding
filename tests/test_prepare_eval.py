"""Check evaluation isolation and provenance, without grading agent prose."""

import importlib.util
import json
from pathlib import Path
import shutil
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("prepare_eval", ROOT / "scripts/prepare-eval.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PrepareEvalTests(unittest.TestCase):
    def test_run_isolated_from_sources_and_evaluator_reply(self):
        run = MODULE.prepare(ROOT, ["frame-ambiguity", "loop-small-fix"])
        self.addCleanup(shutil.rmtree, run)
        manifest = json.loads((run / "run.json").read_text())
        self.assertEqual(manifest["skill_fingerprints"], MODULE.fingerprints(ROOT / "skills"))
        self.assertEqual(manifest["source_commit"], MODULE.git(ROOT, "rev-parse", "HEAD"))
        self.assertEqual(MODULE.git(run / "loop-small-fix", "remote"), "")
        self.assertEqual(MODULE.git(run / "loop-small-fix", "status", "--porcelain"), "")
        self.assertEqual(MODULE.git(run / "loop-small-fix", "rev-parse", "HEAD"),
                         manifest["baseline_heads"]["loop-small-fix"])
        self.assertFalse((run / "frame-ambiguity/reply.md").exists())
        self.assertFalse((run / "frame-ambiguity/addition.md").exists())
        source = ROOT / "evals/cases/frame-ambiguity/workspace/issue.md"
        before = source.read_bytes()
        (run / "frame-ambiguity/issue.md").write_text("Isolated edit\n")
        self.assertEqual(source.read_bytes(), before)
        entrypoint = run / "skills/equilio-frame/SKILL.md"
        entrypoint.write_text(entrypoint.read_text() + "\nChanged snapshot\n")
        self.assertNotEqual(MODULE.fingerprints(run / "skills"), manifest["skill_fingerprints"])

    def test_unknown_case_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.prepare(ROOT, ["missing-case"])

    def test_review_snapshots_preserve_comparison_and_hide_reviewer_reply(self):
        cases = ["review-authority", "review-mechanical", "review-discussions"]
        run = MODULE.prepare(ROOT, cases)
        self.addCleanup(shutil.rmtree, run)
        manifest = json.loads((run / "run.json").read_text())
        self.assertEqual(manifest["cases"], cases)
        for case in cases:
            source = ROOT / "evals/cases" / case / "workspace"
            workspace = run / case
            self.assertFalse((workspace / "reply.md").exists())
            self.assertEqual(MODULE.git(workspace, "remote"), "")
            self.assertEqual(MODULE.git(workspace, "status", "--porcelain"), "")
            for path in source.rglob("*"):
                if path.is_file():
                    self.assertEqual((workspace / path.relative_to(source)).read_bytes(),
                                     path.read_bytes())
            (workspace / "pr.md").write_text("Changed isolated snapshot\n")
            self.assertNotEqual((workspace / "pr.md").read_bytes(),
                                (source / "pr.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
