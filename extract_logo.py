#!/usr/bin/env python3
"""Extract the bottom-right barycentric triangle from the subdivision SVG as a logo."""

import re
import xml.etree.ElementTree as ET

INPUT_FILE = "Barycentric_subdivision.svg"
OUTPUT_FILE = "profile/logo.svg"
FILL_COLOR = "#00FFCE"
PADDING = 2.0

# Triangle vertices (resolved from PolyCollection_4 with y-offset 842.04)
VERTICES = [
    (205.68, 788.64838),
    (590.64, 788.64838),
    (398.16, 455.26324),
]

# Bounding box
min_x = min(v[0] for v in VERTICES)
max_x = max(v[0] for v in VERTICES)
min_y = min(v[1] for v in VERTICES)
max_y = max(v[1] for v in VERTICES)

# Translation to move triangle near origin
tx = -(min_x - PADDING)
ty = -(min_y - PADDING)

vb_w = (max_x - min_x) + 2 * PADDING
vb_h = (max_y - min_y) + 2 * PADDING

# Parse source SVG
ns = {"svg": "http://www.w3.org/2000/svg"}
tree = ET.parse(INPUT_FILE)
root = tree.getroot()

# Find LineCollection_4
line_collection = None
for g in root.iter("{http://www.w3.org/2000/svg}g"):
    if g.get("id") == "LineCollection_4":
        line_collection = g
        break

if line_collection is None:
    raise RuntimeError("Could not find LineCollection_4 in SVG")


def translate_path(d: str) -> str:
    """Translate M/L coordinates in a path d attribute."""
    def replace_coord(m):
        cmd = m.group(1)
        x = float(m.group(2)) + tx
        y = float(m.group(3)) + ty
        return f"{cmd} {x:.4f} {y:.4f}"
    return re.sub(r"([ML])\s+([\d.]+)\s+([\d.]+)", replace_coord, d)


# Extract and group paths by stroke-width
paths_by_weight = {}
total_paths = 0

for path_elem in line_collection.findall("{http://www.w3.org/2000/svg}path"):
    d = path_elem.get("d")
    style = path_elem.get("style", "")

    sw_match = re.search(r"stroke-width:([\d.]+)", style)
    sw = float(sw_match.group(1)) if sw_match else 1.0

    new_d = translate_path(d)
    paths_by_weight.setdefault(sw, []).append(new_d)
    total_paths += 1

# Build filled triangle path
tv = [(v[0] + tx, v[1] + ty) for v in VERTICES]
fill_d = (
    f"M {tv[0][0]:.4f} {tv[0][1]:.4f} "
    f"L {tv[1][0]:.4f} {tv[1][1]:.4f} "
    f"L {tv[2][0]:.4f} {tv[2][1]:.4f} Z"
)

# Build output SVG
lines = []
lines.append('<?xml version="1.0" encoding="UTF-8"?>')
lines.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'viewBox="0 0 {vb_w:.4f} {vb_h:.4f}" '
    f'width="{vb_w:.4f}" height="{vb_h:.4f}">'
)
lines.append("  <style>path{stroke-linecap:butt;stroke-linejoin:round;}</style>")
lines.append(f'  <path d="{fill_d}" fill="{FILL_COLOR}" stroke="none"/>')

for sw in sorted(paths_by_weight.keys()):
    group = paths_by_weight[sw]
    lines.append(f'  <g class="sw-{sw}">')
    for d in group:
        lines.append(f'    <path d="{d}" fill="none" stroke="#000" stroke-width="{sw}"/>')
    lines.append("  </g>")

lines.append("</svg>")

svg_output = "\n".join(lines)

with open(OUTPUT_FILE, "w") as f:
    f.write(svg_output)

print(f"Wrote {OUTPUT_FILE}: {vb_w:.1f}x{vb_h:.1f} viewBox, {total_paths} paths")
