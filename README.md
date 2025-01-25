# Mat-Tech Lab SOPS

A repo for bootstrapping and maintaining SOPs: https://mattechlab.github.io/sops/

Workflow for editing sops:

- Install the env for sops

  ``` bash
  conda create -n sops python=3.10 
  conda activate sops
  cd SOPS
  pip install -r requirements.txt
  ```

- Add the new markdown in the folder desired, eg: `/docs/data-collection/`data-collection_DEBI_protocol.md
- Save pictures in the folder: `/docs/assets/`
- Add the created markdown file in the `mkdocs.yml`
 ![mkdocs_structure](/docs/assets/README/image.png)

- Use MkDocs to build the static site

  ``` bash
  mkdocs build

  ```

- Serve the site locally during development

  ``` bash
  mkdocs serve
  ```

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
