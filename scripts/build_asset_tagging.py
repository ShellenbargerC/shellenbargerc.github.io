"""Build an asset directory from the existing public HTML records; never run lab code."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote


class AssetRecord(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paragraph = None
        self.fields = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.paragraph = []

    def handle_data(self, data):
        if self.paragraph is not None:
            self.paragraph.append(data)

    def handle_endtag(self, tag):
        if tag == 'p' and self.paragraph is not None:
            key, sep, value = ''.join(self.paragraph).partition(':')
            if sep:
                self.fields[key.strip()] = value.strip()
            self.paragraph = None


def build_asset_tagging(root):
    docs = root / 'content/coursework/PythonEssentials/AssetTagging/docs'
    pages = sorted(docs.glob('*.html'), key=lambda p: p.stem)
    if not pages:
        raise ValueError('No asset HTML pages found in ' + str(docs))
    rows = []
    for page in pages:
        record = AssetRecord()
        record.feed(page.read_text(encoding='utf-8'))
        fields = record.fields
        url = quote(page.relative_to(root).as_posix(), safe='/')
        asset_id = escape(page.stem)
        values = [escape(fields.get(key, '—')) for key in ('Asset Name', 'Asset Type', 'Location', 'Owner')]
        rows.append(f'''<tr><th scope="row"><a href="{url}" target="_blank" rel="noopener">{asset_id}</a></th>
<td>{values[0]}</td><td>{values[1]}</td><td>{values[2]}</td><td>{values[3]}</td>
<td class="row-actions"><button type="button" data-preview="{url}" data-asset="{asset_id}">Preview</button>
<a class="button" href="{url}" target="_blank" rel="noopener">Open page ↗</a>
<button type="button" data-copy="{url}">Copy link</button></td></tr>''')
    first_url = quote(pages[0].relative_to(root).as_posix(), safe='/')
    template = (root / 'scripts/asset-tagging-template.html').read_text(encoding='utf-8')
    rendered = template.replace('<!-- ASSET_ROWS -->', '\n'.join(rows)).replace('<!-- ASSET_COUNT -->', str(len(pages)))
    rendered = rendered.replace('ASSET_FIRST_URL', first_url).replace('ASSET_FIRST_ID', escape(pages[0].stem))
    (root / 'asset-tagging.html').write_text(rendered, encoding='utf-8')
    print(f'Built Asset Tagging directory: {len(pages)} asset webpages')


if __name__ == '__main__':
    build_asset_tagging(Path(__file__).resolve().parents[1])
