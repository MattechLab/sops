# Mat-Tech Lab SOPS

A repo for bootstrapping and maintaining SOPs: <https://mattechlab.github.io/sops/>

Workflow for editing sops:

- Set up your environment, using one of the options below

  ### Option A: conda (local install)

  ``` bash
  conda create -n sops python=3.10 
  conda activate sops
  cd SOPS
  pip install -r requirements.txt
  npm install
  conda env config vars set JUPYTER_PLATFORM_DIRS=1 NO_MKDOCS_2_WARNING=true -n sops
  conda activate sops
  ```

  `npm install` installs [cspell](https://cspell.org/), used to spellcheck the docs (requires [Node.js](https://nodejs.org/)).

  `JUPYTER_PLATFORM_DIRS=1` silences a `jupyter_core` deprecation warning printed by the `mkdocs-jupyter` plugin on every build; setting it as a conda env var (rather than in a build hook) guarantees it's set before mkdocs starts, since mkdocs imports `mkdocs-jupyter` before any of its own hooks run. The env var only takes effect after reactivating the environment, hence the second `conda activate sops`.

  `NO_MKDOCS_2_WARNING=true` silences `mkdocs-material`'s built-in announcement about breaking changes coming in MkDocs 2.0 ([details](https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/)), printed on every build/serve; same reasoning as above applies for setting it as a conda env var rather than in a hook.

  ### Option B: VS Code Dev Container

  Skip the local conda/npm setup entirely and open the repo in a [VS Code Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) (`Dev Containers: Reopen in Container`), which builds a container with Python, Node, and all dependencies already installed (see `Dockerfile` / `.devcontainer/devcontainer.json`). Requires Docker and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Once reopened in the container, every command below (`mkdocs build`, `mkdocs serve`, `codespell`, `npx cspell`, ...) works exactly as in Option A, from the integrated terminal.

- Add the new markdown in the folder desired, eg: `/docs/data-collection/`data-collection_DEBI_protocol.md
- Save pictures in the folder: `/docs/assets/`
- Add the created markdown file in the `mkdocs.yml`
 ![mkdocs_structure](/docs/assets/README/image.png)

- Use MkDocs to build the static site

  ``` bash
  mkdocs build

  ```

  `mkdocs build` (and `mkdocs serve`) automatically run [codespell](https://github.com/codespell-project/codespell) and [cspell](https://cspell.org/) on the docs before building, and abort the build if either finds a spelling error.

  To run them independently of MkDocs:

  ``` bash
  codespell
  npx cspell --no-progress "**/*.md"
  ```

- Serve the site locally during development

  ``` bash
  mkdocs serve
  ```

  Now you can visualize the website build locally, probably at <http://127.0.0.1:8000/sops/>. On push the website will be automatically deployed online.
- Deploy the site to the github page

``` bash
  git add .
  git commit -m 'your comment'
  git push
```

### What happens when you push

- **Pushing to any branch** runs [`.github/workflows/tests.yml`](.github/workflows/tests.yml): two parallel jobs, `codespell` and `cspell`, just spellchecking the docs. Nothing is built or deployed.
- **Pushing to `mkdocs`** instead runs [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) (`tests.yml` skips this branch, since the same checks happen here too):
  1. `codespell` and `cspell` jobs run first (same as above).
  2. Once both pass, the `build` job checks out this branch into `mkdocs/` and the `gh-pages` branch into `www/`, wipes `www/`'s tracked files, then runs `mkdocs build -d ../www/` to regenerate the static site there (skipping its own spellcheck hooks, since the jobs above already checked this push).
  3. The `Deploy` step commits and pushes whatever changed in `www/` straight to `gh-pages` — that's the branch actually served at <https://mattechlab.github.io/sops/>.
- If either spellchecker fails, the build/deploy never runs, so a typo on `mkdocs` won't reach the live site.

This is the automated equivalent of running `mkdocs gh-deploy` locally — you never need to run that yourself.
