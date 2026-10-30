# Cameron's portfolio

## Install this update

Extract the ZIP and copy its contents into your existing shellenbargerc.github.io checkout, replacing matching files. Include .github, scripts, courses.json, and the HTML files. Keep any additional labs you have added. Commit and push to your default branch. Keep Settings → Pages → Source set to GitHub Actions.

The workflow publishes index.html, projects.html, files.html, the compatibility redirect about.html, and the generated content index. It supports master and main; adjust it if your default branch has another name. Your address remains https://shellenbargerc.github.io/.

## Site pages

- Home (index.html): About Me introduction, Projects callout, NCL accomplishment, Certifications section, approach to documenting work, and GitHub contact link. Its main action opens Projects.
- Projects (projects.html): separate Course Projects and Personal Projects sections. Class buttons open the lab library scoped to the selected course.
- File Library (files.html): folders and viewable files, including course-scoped links.

Navigation is Home / Projects / File Library. There is no separate About destination. The old about.html address redirects to Home so existing links continue to work. Edit your biography in index.html.

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

The Certifications section now lists CompTIA IT Fundamentals+ (ITF+), with user-supplied CompTIA ID COMP001022059449. No issue date or individual verification link was supplied. Competition badges are not presented as professional certifications.

## Visible accomplishment badges

The NCL card displays the supplied Platinum badge directly, using CSS to frame the badge artwork from the unchanged screenshot. The full screenshot remains available on click.

An Eagle Scout accomplishment records Troop 200 BSA, its 184th Eagle Scout recognition, and a rank date of June 24, 2025, using the information supplied by Cameron. It includes the troop's recognition quote. The Eagle Scout emblem loads from the Sam Houston Area Council graphics collection (https://communications.shacbsa.org/e); a styled Eagle Scout text decal is shown if the external image cannot load. The council is credited as the artwork source, not as Cameron's troop or awarding council. These recognitions remain under Accomplishments, separate from Certifications.

## Eagle Scout project entry

The Eagle Scout accomplishment now has a brief project summary and links to projects.html#eagle-scout-project. The Personal Projects section contains an expandable Alum Creek Park Renovation project entry. Following its direct link opens the entry automatically. The auto-generated Eagle Scout project card links to that entry, while its Open project files button opens the public summary in the lab library.

The summary is under content/independent/EagleScout/Project-Summary.md. The original completed PDF contains private contact information and signatures and is deliberately not copied into the public site. The entry uses the completed report's scope and totals, excluding proposed tasks that were not carried out. No project completion year is inferred from the workbook's month/day fields.

## Project overview in File Library

The Projects page contains only project cards; there is no Eagle Scout dropdown below them. View project opens files.html?folder=independent%2FEagleScout, showing the full overview and supporting files. The homepage accomplishment button opens the same view. An old labs.html link redirects to files.html, preserving its folder and file parameters in browsers with JavaScript.

Before/after photos were not present in the supplied workbook. Add the original project photos under content/independent/EagleScout/before/ and content/independent/EagleScout/after/. After publication they appear automatically in labeled galleries in the project's File Library view. Other project images appear under More photos. Clicking a photo opens its full file preview, and the overview link returns to the project. No placeholder or invented project photos are included.

## CompTIA ITF+

The Certifications section lists CompTIA IT Fundamentals+ (ITF+) with CompTIA ID COMP001022059449, supplied by Cameron. The badge artwork loads from the CompTIA-issued badge page on Credly; a text badge is displayed if the external image is unavailable. About this certification links to the issuer's general badge description, not to a verified individual credential record. No issue date or credential status was inferred.

## Curated project photos

Eight selected photographs from the supplied Projectpics archive are included as four matched before/after comparisons in the Eagle Scout project's File Library overview. Areas: outdoor checkerboards, bridge-side planting bed, circular planting island, and corner bed beside the stepping stones. Duplicate frames are omitted. The corner-bed after photo is labeled to indicate neighboring work is still underway.

Selected original filenames and captions are recorded in photo-pairs.json. HEIC images were decoded to JPEG, scaled to a maximum dimension of 1600 pixels, and saved without camera metadata for browser compatibility and page weight. No scene content was generated or retouched. The source photos remain in the supplied archive. The indexer validates both files in each pair before publishing; include photo-pairs.json when copying this update. Unpaired future photo uploads still use the automatic before/after galleries.

## Additional comparisons

Three more pairs were appended without changing the existing four pairs or their image files: gazebo surroundings (IMG_7984 / IMG_8024), tree-side planting bed (IMG_8006 / IMG_8034), and a wider bridge-approach view (IMG_7959 / IMG_8021). The gallery now contains seven comparisons and fourteen photographs. Captions distinguish the gazebo's wider/closer viewpoints, the tree-bed finishing work, and the bridge view's overlap with the original bridge comparison.

## Paver-repair photo replacement

The wider bridge-approach comparison was replaced with the two newly supplied JPEGs: IMG_7973.jpg (Before) and IMG_7994(1).jpg (During repairs), titled Replacing broken and misaligned paver stones. The other six comparisons and their image files are unchanged. The photographs show different holes and are captioned accordingly.

Include file-library-ignore.json and the updated scripts folder when installing. The ignore list keeps the retired bridge-approach images out of the file listing and galleries even if older copies remain in your checkout after merging the update. It does not remove any files from your checkout.
