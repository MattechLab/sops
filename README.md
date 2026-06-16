# Mat-Tech Lab SOPS

A repo for bootstrapping and maintaining SOPs: https://mattechlab.github.io/sops/

Workflow for editing sops:

- Install the env for sops

  ``` bash
  conda create -n sops python=3.10 
  conda activate sops
  cd SOPS
  pip install -r requirements.txt
  npm install
  conda env config vars set JUPYTER_PLATFORM_DIRS=1 -n sops
  conda activate sops
  ```

  `npm install` installs [cspell](https://cspell.org/), used to spellcheck the docs (requires [Node.js](https://nodejs.org/)).

  `JUPYTER_PLATFORM_DIRS=1` silences a `jupyter_core` deprecation warning printed by the `mkdocs-jupyter` plugin on every build; setting it as a conda env var (rather than in a build hook) guarantees it's set before mkdocs starts, since mkdocs imports `mkdocs-jupyter` before any of its own hooks run. The env var only takes effect after reactivating the environment, hence the second `conda activate sops`.

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
  Now you can visualize the website build locally, probably at http://127.0.0.1:8000/sops/. On push the website will be automatically deployed online. 
- Deploy the site to the github page

``` bash
  git add .
  git commit -m 'your comment'
  git push
  ```

The workflow in the .github/workflows will take care of the deployment
with the same function as

``` bash
 mkdocs gh-deploy
 ```
