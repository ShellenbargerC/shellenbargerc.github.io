# Cameron's portfolio

## Install this update

Extract the ZIP and copy its contents into your existing shellenbargerc.github.io checkout, replacing matching files. Include .github, scripts, courses.json, and the HTML files. Keep any additional labs you have added. Commit and push to your default branch. Keep Settings → Pages → Source set to GitHub Actions.

The workflow publishes index.html, projects.html, labs.html, the compatibility redirect about.html, and the generated content index. It supports master and main; adjust it if your default branch has another name. Your address remains https://shellenbargerc.github.io/.

## Site pages

- Home (index.html): About Me introduction, Projects callout, NCL accomplishment, Certifications section, approach to documenting work, and GitHub contact link. Its main action opens Projects.
- Projects (projects.html): separate Course Projects and Personal Projects sections. Class buttons open the lab library scoped to the selected course.
- Lab Library (labs.html): folders and viewable files, including course-scoped links.

Navigation is Home / Projects / Lab Library. There is no separate About destination. The old about.html address redirects to Home so existing links continue to work. Edit your biography in index.html.

## Upload labs

On GitHub, open the portfolio repository, navigate to the appropriate folder, choose Add file → Upload files, then commit to the default branch. Once Publish portfolio in Actions finishes, the library updates automatically. You can also copy files into these folders locally, commit, and Push origin in GitHub Desktop.

- Python Essentials (SL) (2026AU-CYBR-2101-C535): content/coursework/PythonEssentials/
- Server Management (2026AU-NET-2220-C535): content/coursework/ServerManagement/
- Cisco CCNA Security (2026AU-CYBR-2102-C535): content/coursework/CiscoCCNASecurity/
- Personal projects: content/independent/YourProject/

Keep each week's or lab's files in a subfolder if desired. Nested folders and original file names are preserved. The full five-file PythonEssentials folder from your supplied Playbook archive is included unchanged. Empty courses use .gitkeep to retain their folders; these files are not shown in the library.

Each immediate subfolder under content/independent/ automatically becomes a Personal Projects card. The three current classes are configured as Course Projects cards in projects.html. Course display names are in courses.json; folder paths stay short and stable.

Uploads go to this portfolio repo. The separate Playbook repository is not synchronized. All files published here are public; dotfiles being omitted from the listing does not make them private.

## Previews

Text, Markdown, Python and common code/config files display as source; lab scripts are never executed by the indexer. Images display inline. PDFs use the browser's PDF viewer. DOCX files get an extracted text preview, with their original formatting available by download. Other files, such as Packet Tracer files, spreadsheets, and ZIPs, are downloadable. Text previews are limited to about 512 KB, while original downloads remain complete.

## Local preview

From this folder, with Python 3:

```sh
python scripts/build_content.py
python -m http.server 8000
```

Open http://localhost:8000/ . A server is needed for the library and Projects page to fetch the index. GitHub generates the index automatically during publishing.

## Accomplishments and certifications

Home features the supplied NCL Spring 2026 team summary: Royal Flush placed 229th out of 3,634 teams, scoring 2,395 / 3,000 with 83.4% completion. It is explicitly labeled a team result. The individual result and all four original screenshots are accessible under the expandable competition records. Badge percentiles differ from the report placements, so no combined percentile claim is made. Files are in assets/accomplishments/ and are copied automatically by the workflow.

The Certifications section is an explicit placeholder until credential names, issuers, dates, and verification links are provided. Competition badges are not presented as professional certifications.

## Visible accomplishment badges

The NCL card displays the supplied Platinum badge directly, using CSS to frame the badge artwork from the unchanged screenshot. The full screenshot remains available on click.

An Eagle Scout accomplishment records Troop 200 BSA, its 184th Eagle Scout recognition, and a rank date of June 24, 2025, using the information supplied by Cameron. It includes the troop's recognition quote. The Eagle Scout emblem loads from the Sam Houston Area Council graphics collection (https://communications.shacbsa.org/e); a styled Eagle Scout text decal is shown if the external image cannot load. The council is credited as the artwork source, not as Cameron's troop or awarding council. These recognitions remain under Accomplishments, separate from Certifications.
