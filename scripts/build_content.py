"""Index public portfolio files. Standard library only; never executes lab files."""
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content'
TEXT = {'.py', '.txt', '.md', '.json', '.csv', '.tsv', '.yaml', '.yml', '.xml', '.html', '.css', '.js', '.ts', '.sql', '.sh', '.ps1', '.log', '.ini', '.cfg'}
IMAGES = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.avif'}
PREVIEW_LIMIT = 512_000


def docx_text(path):
    with zipfile.ZipFile(path) as archive:
        member = archive.getinfo('word/document.xml')
        if member.file_size > 4_000_000:
            return 'Document is too large to preview. Download the original file.'
        document = ET.fromstring(archive.read(member))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    return '\n'.join(''.join(p.itertext()) for p in document.findall('.//w:p', ns))[:PREVIEW_LIMIT]


def build(root=ROOT):
    content = root / 'content'
    records = []
    for path in sorted(content.rglob('*'), key=lambda p: p.as_posix().lower()):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(content)
        if relative.parts[0] not in {'coursework', 'independent'}:
            continue
        if any(part.startswith('.') for part in relative.parts) or path.name == 'Thumbs.db':
            continue
        extension = path.suffix.lower()
        size = path.stat().st_size
        kind = 'download'
        preview = None
        truncated = False
        if extension in TEXT or not extension:
            sample = path.open('rb')
            with sample:
                raw = sample.read(PREVIEW_LIMIT + 1)
            try:
                if b'\x00' not in raw:
                    preview = raw[:PREVIEW_LIMIT].decode('utf-8-sig', errors='replace')
                    truncated = size > PREVIEW_LIMIT
                    kind = 'text'
            except UnicodeError:
                pass
        elif extension in IMAGES:
            kind = 'image'
        elif extension == '.pdf':
            kind = 'pdf'
        elif extension == '.docx':
            kind = 'document'
            try:
                preview = docx_text(path)
            except (zipfile.BadZipFile, KeyError, ET.ParseError, OSError, RuntimeError):
                preview = 'Preview unavailable. Download the original document.'
        records.append({'path': relative.as_posix(), 'url': 'content/' + relative.as_posix(),
                        'name': path.name, 'category': relative.parts[0], 'kind': kind,
                        'size': size, 'preview': preview, 'truncated': truncated})
    (root / 'content-index.json').write_text(json.dumps({'files': records}, ensure_ascii=False), encoding='utf-8')
    print(f'Indexed {len(records)} files')
    return records


if __name__ == '__main__':
    build()
