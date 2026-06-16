"""mkdocs build hook: run cspell before building the site."""

import os
import subprocess


def on_pre_build(config):
    repo_root = os.path.dirname(os.path.abspath(config["config_file_path"]))
    cspell_bin = os.path.join(repo_root, "node_modules", ".bin", "cspell")
    result = subprocess.run([cspell_bin, "--no-progress", "**/*.md"], cwd=repo_root)
    if result.returncode != 0:
        raise SystemExit("cspell found spelling errors, aborting mkdocs build")
