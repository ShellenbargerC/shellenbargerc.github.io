"""Index public portfolio files. Standard library only; never executes lab files."""
import json
import subprocess
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


def folder_created_at(root, relative):
    """First commit that added a file here; later file edits do not change it."""
    try:
        result = subprocess.run(
            ['git', 'log', '--reverse', '--diff-filter=A', '--format=%ct', '--',
             'content/' + relative], cwd=root, capture_output=True, text=True,
            timeout=15, check=True)
        timestamps = [int(line) for line in result.stdout.splitlines() if line.strip().isdigit()]
        return min(timestamps) if timestamps else None
    except (OSError, subprocess.SubprocessError):
        return None


def build(root=ROOT):
    content = root / 'content'
    metadata_path = root / 'courses.json'
    titles = json.loads(metadata_path.read_text(encoding='utf-8')) if metadata_path.exists() else {}
    folders = []
    for path in sorted(content.rglob('*'), key=lambda p: p.as_posix().lower()):
        relative = path.relative_to(content)
        if (path.is_dir() and not path.is_symlink()
                and relative.parts[0] in {'coursework', 'independent'}
                and not any(part.startswith('.') for part in relative.parts)):
            key = relative.as_posix()
            folders.append({'path': key, 'title': titles.get(key, path.name),
                            'createdAt': folder_created_at(root, key)})
    ignore_path = root / 'file-library-ignore.json'
    ignored = set(json.loads(ignore_path.read_text(encoding='utf-8'))) if ignore_path.exists() else set()
    records = []
    for path in sorted(content.rglob('*'), key=lambda p: p.as_posix().lower()):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(content)
        if relative.parts[0] not in {'coursework', 'independent'}:
            continue
        if any(part.startswith('.') for part in relative.parts) or path.name == 'Thumbs.db':
            continue
        if relative.as_posix() in ignored:
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
    pair_path = root / 'photo-pairs.json'
    photo_pairs = json.loads(pair_path.read_text(encoding='utf-8')) if pair_path.exists() else {}
    indexed_paths = {record['path'] for record in records}
    valid_pairs = {}
    for project, pairs in photo_pairs.items():
        for pair in pairs:
            valid = True
            for stage in ('before', 'after'):
                path = pair.get(stage, {}).get('path', '')
                if path not in indexed_paths or not path.startswith(project + '/'):
                    print(f'WARNING: skipping photo comparison {pair.get("title", "Untitled")!r}: missing or misplaced {stage} image {path!r}')
                    valid = False
            if valid:
                valid_pairs.setdefault(project, []).append(pair)
    alias_path = root / 'folder-aliases.json'
    aliases = json.loads(alias_path.read_text(encoding='utf-8')) if alias_path.exists() else {}
    (root / 'content-index.json').write_text(json.dumps({'files': records, 'folders': folders, 'photoPairs': valid_pairs, 'folderAliases': aliases}, ensure_ascii=False), encoding='utf-8')
    print(f'Indexed {len(records)} files')
    return records


if __name__ == '__main__':
    build()
