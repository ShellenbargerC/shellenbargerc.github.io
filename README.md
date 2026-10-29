# Cameron's portfolio — fresh start

A first design with one Projects section, Coursework / Independent filters, search, project detail dialogs, and mobile layouts. No package installation or build step is needed. Open index.html in your browser to preview it.

The three example projects are explicitly placeholders. Replace them before publishing. No old site content or photos were migrated; the header uses your name and the contact button points to your GitHub profile.

## Add your work

Edit the `projects` array near the bottom of index.html. Each project has title, category (`coursework` or `independent`), kind (`network`, `security`, or `build`), tags, summary, challenge, approach, and learned. Add optional sourceUrl and demoUrl for links. Add image (for example `assets/network-lab.png`) and imageAlt for a screenshot. Store screenshots in an assets folder. Duplicate an object to add another project; remove the preview notice when all examples have been replaced.

The About section intentionally leaves your biography open. Edit that copy and the introduction directly in index.html. Colors and typography are at the top of its style block.

## Replace the existing site and keep its address

Keep the repository named `shellenbargerc.github.io`. Keep your downloaded original ZIP as a backup. This archive is a replacement site, not an overlay: remove the old tracked site files and old workflows when installing it. Simply uploading index.html alongside the existing files will leave the old Jekyll setup in place.

For a local checkout, first ensure there are no unrelated uncommitted changes. Create a branch, remove the old tracked files with `git rm -r .`, then copy the CONTENTS of this folder, including .github, into the checkout. Commit and review the replacement diff before merging into the default branch. The removal is recorded in Git history, so the old files can still be recovered. Do not delete the repository itself.

In the repository's Settings → Pages, set Source to GitHub Actions. The included workflow publishes index.html and assets without Jekyll or Ruby. It runs on pushes to master or main. If your default branch has a different name, update the workflow. After merging, check the Actions tab for a successful Publish portfolio run.

The public address remains https://shellenbargerc.github.io/. This package has not been uploaded to GitHub or published.
