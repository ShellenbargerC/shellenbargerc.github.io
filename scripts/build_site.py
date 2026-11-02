"""Build exactly the public static site. Run from any working directory."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import shutil
from build_content import build, ROOT

PAGES = ('index.html', 'projects.html', 'files.html', 'about.html', 'labs.html')
REQUIRED = (*PAGES, 'assets/js/avalanche-feature.js',
            'assets/js/markdown-preview.js', 'assets/vendor/marked/marked.umd.js')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ('href', 'src') and value:
                self.links.append(value)


def validate_site(destination):
    for page in PAGES:
        links = Links()
        links.feed((destination / page).read_text(encoding='utf-8'))
        for href in links.links:
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            target = destination / unquote(url.path).lstrip('/')
            if not target.is_file():
                raise ValueError(f'{page} links to missing public file: {href}')
    index = json.loads((destination / 'content-index.json').read_text(encoding='utf-8'))
    for record in index['files']:
        if not (destination / record['url']).is_file():
            raise ValueError(f'Indexed file was not staged: {record["url"]}')
    folder_paths = {folder['path'] for folder in index['folders']}
    for page in PAGES:
        links = Links()
        links.feed((destination / page).read_text(encoding='utf-8'))
        from urllib.parse import parse_qs
        for href in links.links:
            url = urlsplit(href)
            if url.path != 'files.html':
                continue
            folder = parse_qs(url.query).get('folder', [None])[0]
            if folder and folder not in folder_paths:
                raise ValueError(f'{page} links to missing library folder: {folder}')
    print(f'Validated {len(PAGES)} pages and {len(index["files"])} indexed public files.')


def main():
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit('Missing required site files: ' + ', '.join(missing)
                         + '. Copy the complete replacement into the repository root.')
    records = build()
    destination = ROOT / '_site'
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir()
    for name in (*PAGES, 'content-index.json', '.nojekyll'):
        shutil.copy2(ROOT / name, destination / name)
    shutil.copytree(ROOT / 'assets', destination / 'assets')
    # Stage only indexed content. Ignored files and project metadata stay out.
    for record in records:
        target = destination / record['url']
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / record['url'], target)
    validate_site(destination)
    print('Ready to publish: _site/')


if __name__ == '__main__':
    main()
