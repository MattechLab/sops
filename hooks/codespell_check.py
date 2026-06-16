"""mkdocs build hook: run codespell before building the site."""

import os
import subprocess
import sys


def on_pre_build(config):
    if os.environ.get("SKIP_SPELLCHECK_HOOKS"):
        return
    repo_root = os.path.dirname(os.path.abspath(config["config_file_path"]))
    result = subprocess.run([sys.executable, "-m", "codespell_lib", "."], cwd=repo_root)
    if result.returncode != 0:
        raise SystemExit("codespell found spelling errors, aborting mkdocs build")
