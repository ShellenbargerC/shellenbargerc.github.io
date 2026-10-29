# Cameron's portfolio and lab library

The homepage features selected projects. The Lab library automatically lists all files and nested folders under `content/coursework/` and `content/independent/`.

The full PythonEssentials folder from the supplied Playbook archive is copied unchanged into `content/coursework/PythonEssentials/`. Its five original files include two Python source files, a README, an explanation, and an output screenshot.

## Install this update

Extract this ZIP, then copy all its contents into your existing `shellenbargerc.github.io` checkout, replacing matching files. Include `.github` and the new `scripts` and `content` folders. Commit and push to your default branch. No deletion of the repository or Git history is needed for this update.

Keep Settings → Pages → Source set to GitHub Actions. The updated workflow generates the file index, then publishes the website. It supports master and main. If your default branch has another name, update `.github/workflows/pages.yml`.

## Upload new labs through GitHub

1. Open the portfolio repository on GitHub (not the original Playbook repository).
2. Navigate to `content/coursework/PythonEssentials/` for Python coursework. Open the desired lab subfolder if it exists.
3. Choose Add file → Upload files. Upload your files or drag in a lab folder to preserve its structure, then commit the upload to the default branch.
4. Wait for Publish portfolio in the Actions tab to finish. The Lab library will show the uploaded files under the matching folders automatically. Refresh the browser if necessary.

For another class, add a folder inside `content/coursework/`. For personal projects, use `content/independent/`. Upload a folder through GitHub's uploader or copy it into your checkout with GitHub Desktop. Nested folders are supported. Deleting or renaming files also updates the listing on the next publication.

Example paths:

- `content/coursework/PythonEssentials/Lab2.1.13/Lab2.1.13.py`
- `content/coursework/PythonEssentials/Lab2.2.1/notes.md`
- `content/coursework/Networking/Lab1/topology.png`
- `content/independent/MyGame/screenshots/gameplay.png`

Only a GitHub commit is needed. You do not edit the HTML or generated JSON to add lab files. Uploading to the original Playbook repository does not synchronize automatically; upload to the portfolio content folders instead. Featured homepage cards are curated separately.

All published content is public. Upload only material you want visible on your portfolio. Dotfiles are omitted from the listing, but are not a safe place for secrets in a public repository.

## Supported previews

- Python, Markdown, plain text, and common code/config files: readable source preview. Markdown is shown as text. HTML and scripts display as source in the viewer; lab scripts are never executed by the indexer.
- PNG, JPEG, GIF, WebP, AVIF: image preview.
- PDF: browser PDF viewer, with a download link.
- DOCX: extracted text preview; download the original for its formatting, tables, and images.
- Other formats, such as Packet Tracer `.pkt`, ZIP, or spreadsheets: download links.

Text previews are limited to about 512 KB; complete files remain downloadable. Individual file links can be shared. Original file names are preserved. GitHub upload and repository limits still apply.

## Local preview

GitHub automatically generates the index when publishing. To preview locally, run from the website folder with Python 3:

```sh
python scripts/build_content.py
python -m http.server 8000
```

Open http://localhost:8000/ . Opening labs.html directly as a local file cannot fetch the index in most browsers. A generated index for the current five files is included in this ZIP.

## Customize

Edit the `projects` array in index.html for featured cards. The site has one real Python Essentials card linking to the original Playbook and the lab library. Update the About text as your portfolio develops. Styles are defined inside each HTML file.

This update has not been published. Your address stays https://shellenbargerc.github.io/ after you push it.
