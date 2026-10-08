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


if __name__ == "__main__":
    unittest.main()
