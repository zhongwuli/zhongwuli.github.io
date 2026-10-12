#!/usr/bin/env python3
"""Convert published raster photos to WebP and rewrite published references.
Private source and original files are never changed.
"""
from pathlib import Path
from urllib.parse import quote
import subprocess

root = Path("_site")
images = root / "assets" / "img"
originals = sorted(
    (p for p in images.rglob("*") if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png"}),
    key=lambda p: str(p),
)
# Preserve source extensions in WebP filenames (e.g. image.PNG.webp), so
# similarly named files with different original extensions cannot collide.
replacements = {}
for original in originals:
    output = original.with_name(original.name + ".webp")
    subprocess.run(
        ["convert", str(original), "-strip", "-quality", "84", str(output)],
        check=True,
    )
    if not output.is_file() or output.stat().st_size == 0:
        raise RuntimeError(f"WebP conversion failed: {original}")
    old = original.relative_to(root).as_posix()
    new = output.relative_to(root).as_posix()
    replacements[old] = new
    # URLs produced by Jekyll escape spaces and other non-ASCII characters.
    replacements[quote(old, safe="/")] = quote(new, safe="/")

text_extensions = {".html", ".htm", ".css", ".js", ".json", ".xml", ".svg", ".txt", ".webmanifest"}
changed = 0
for document in root.rglob("*"):
    if not document.is_file() or document.suffix.lower() not in text_extensions:
        continue
    try:
        original_text = document.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    new_text = original_text
    for old, new in replacements.items():
        new_text = new_text.replace(old, new)
    if new_text != original_text:
        document.write_text(new_text, encoding="utf-8")
        changed += 1

# Ensure references no longer point to soon-to-be-deleted assets.
for document in root.rglob("*"):
    if not document.is_file() or document.suffix.lower() not in text_extensions:
        continue
    try:
        content = document.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for old in replacements:
        if old in content.replace(old + '.webp', ''):
            raise RuntimeError(f"Old raster reference remains: {document}: {old}")

for original in originals:
    original.unlink()

print(f"Converted {len(originals)} PNG/JPG files to WebP, updated {changed} website documents.")
