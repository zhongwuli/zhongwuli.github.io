#!/usr/bin/env python3
"""Optimize generated website images using Pillow, rewrite public URLs to WebP.

All operations are confined to _site/. Originals in the private repo are untouched.
"""
from pathlib import Path
from urllib.parse import quote
from PIL import Image, ImageOps

root = Path("_site")
images = root / "assets" / "img"
max_size = (1600, 1600)
replacements = {}

if images.exists():
    raster = sorted((p for p in images.rglob("*")
                     if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}),
                    key=str)
else:
    raster = []

converted = []
for source in raster:
    original_format = source.suffix.lower()
    is_webp = original_format == ".webp"
    destination = source if is_webp else source.with_name(source.name + ".webp")
    # Keep static asset names and relative paths unchanged apart from adding .webp.
    with Image.open(source) as raw:
        image = ImageOps.exif_transpose(raw)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "A" in image.getbands() or "transparency" in image.info else "RGB")
        image.save(destination, format="WEBP", quality=84, method=5)
    if not destination.exists() or destination.stat().st_size == 0:
        raise RuntimeError(f"WebP conversion failed: {source}")
    if not is_webp:
        old = source.relative_to(root).as_posix()
        new = destination.relative_to(root).as_posix()
        replacements[old] = new
        replacements[quote(old, safe="/")] = quote(new, safe="/")
        converted.append(source)

text_extensions = {".html", ".htm", ".css", ".js", ".json", ".xml", ".svg", ".txt", ".webmanifest"}
changed = 0
for document in root.rglob("*"):
    if not document.is_file() or document.suffix.lower() not in text_extensions:
        continue
    try:
        original_text = document.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    updated = original_text
    for old, new in replacements.items():
        updated = updated.replace(old, new)
    if updated != original_text:
        document.write_text(updated, encoding="utf-8")
        changed += 1

for document in root.rglob("*"):
    if not document.is_file() or document.suffix.lower() not in text_extensions:
        continue
    try:
        text = document.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for old in replacements:
        if old in text.replace(old + ".webp", ""):
            raise RuntimeError(f"Unconverted raster reference in {document}: {old}")

for source in converted:
    source.unlink()

print(f"Optimized {len(raster)} images; converted {len(converted)} PNG/JPG to WebP; updated {changed} documents.")
