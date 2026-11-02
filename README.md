# Cameron Shellenbarger — portfolio

Complete replacement for https://shellenbargerc.github.io/ using the existing layout and current project/lab content.

## Replace the existing site and publish

Use the same **ShellenbargerC/shellenbargerc.github.io** repository. Keeping that repository keeps your site address unchanged.

1. In GitHub Desktop, select this repository and choose **Repository → Show in Explorer**.
2. Make a backup outside that folder. Move the old repository contents into the backup, **leaving the existing `.git` folder in the repository**. Do not delete the repository folder or its `.git` folder. In Explorer, use **View → Show → Hidden items** if needed to see `.git` and `.github`.
3. Extract the replacement ZIP. Open its `shellenbargerc.github.io` folder and copy **all of its contents** into your existing repository folder. Include `.github`, `.gitignore`, and `.nojekyll`. Copy the contents, not the enclosing folder. `index.html`, `projects.html`, `files.html`, `content`, `assets`, `scripts`, and `.github` must all be directly in the repository root.
4. On GitHub, open this repository's **Settings → Pages → Build and deployment → Source**, and choose **GitHub Actions**. The workflow is already included; you do not need to add a Jekyll or Static HTML template.
5. In GitHub Desktop, review the changes, enter a commit message such as `Restore portfolio and repair Pages build`, click **Commit to master**, then **Push origin**. If your branch is named `main`, commit there instead; both names are supported.
6. Open **Actions → Publish portfolio** on GitHub. Wait for the newest run to finish successfully. It builds and validates the pages, indexes the current lab folders, uploads the public site, and deploys it.
7. Open https://shellenbargerc.github.io/ and refresh with **Ctrl+F5**. Check Projects and File Library too.

Do not upload the ZIP itself into the repository. GitHub Desktop publishes the extracted files.

If a deployment failed before you switched Pages to GitHub Actions, open the failed run and choose **Re-run all jobs**, or use **Actions → Publish portfolio → Run workflow** after your workflow commit has been pushed.

## What was repaired

The uploaded snapshot had renamed `content/independent/EagleScout` to `content/independent/Eagle Scout Project`. Its photo-pair configuration still referenced the former location. Running the original indexer reproduced a `ValueError` for `independent/EagleScout/before/checkerboards.jpg`, which stopped the workflow before publication. The snapshot also lacked root `index.html` and `files.html`, which the staging step required.

This replacement restores both pages, updates all Eagle Scout links/photo paths to the current folder, retains all seven comparisons, rebuilds the stale index, and removes the unused Jekyll build files. Missing optional comparison images now generate warnings and omit just the incomplete pair, rather than blocking the whole site. Required pages and scripts still fail validation with a clear error if missing.

All 47 files supplied under `content/` are retained unchanged. Forty are public indexed files; five `.gitkeep` placeholders and the two previously excluded bridge-approach photos are not published. The original images and three older course-summary directories are also kept in the source replacement for reference. They are not part of the current public File Library.

The homepage, accomplishments, certifications, course cards, personal-project cards, gallery layout, Markdown formatting, source toggle, PDF previews, code previews, and downloads are retained. The Avalanche homepage card opens the newest immediate subfolder, currently `Avalanche Network Infrastructure/V1`. Folder creation order uses the first Git commit adding a file in that folder; editing an older folder does not make it newest. When dates tie, names break the tie in natural descending order, so V10 sorts after V2.

Old `EagleScout` and `Avalanche-Network-Simulation` File Library links are supported through `folder-aliases.json`.

## Add labs and project versions

Add files beneath the appropriate existing directory, then commit and push:

- `content/coursework/PythonEssentials/`
- `content/coursework/ServerManagement/`
- `content/coursework/CiscoCCNASecurity/`
- `content/independent/Avalanche Network Infrastructure/V1/`
- `content/independent/Eagle Scout Project/`

For a new Avalanche version, create a sibling folder such as `V2` inside `Avalanche Network Infrastructure`, put the version's files inside it, then commit and push. The folder must contain at least one tracked file; Git does not save empty folders. The homepage card will automatically follow the newest version folder after the site publishes.

Markdown (`.md` or `.MD`) opens formatted. Python and other source files display as code. Images, PDFs, and Word text have previews; other file types can be downloaded. PDF previews depend on the visitor's browser, and the download link remains available.

You do not need to hand-edit `content-index.json`. GitHub Actions regenerates it on every push. Renaming a folder used by a gallery requires updating `photo-pairs.json`, `courses.json`, and any related links/aliases. Adding files inside existing folders does not.

## Preview locally (optional)

Requires Python 3. No package installation is needed, and no lab code is executed.

```text
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

Open http://localhost:8000/. Opening an HTML file directly by double-clicking does not let the browser fetch the File Library index.

## Build layout

`scripts/build_site.py` checks required pages, runs the content indexer, stages the public files into `_site/`, and validates page links and indexed file availability. Only the pages, assets, and indexed content are published. The `_site` folder is ignored by Git and rebuilt automatically. The repository contains one Pages workflow: `.github/workflows/pages.yml`.

Official Pages publishing instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
