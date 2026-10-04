"""Write every ```mermaid block in the repo's Markdown files to OUT_DIR as .mmd files."""
import pathlib
import re
import sys

out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "mermaid-out")
out.mkdir(parents=True, exist_ok=True)
count = 0
for md in sorted(pathlib.Path(".").rglob("*.md")):
    if any(part.startswith(".") or part in ("node_modules", "private") for part in md.parts):
        continue
    text = md.read_text(encoding="utf-8")
    for i, block in enumerate(re.findall(r"```mermaid\n(.*?)```", text, re.S), 1):
        name = f"{md.as_posix().replace('/', '__')}__{i:02d}.mmd"
        (out / name).write_text(block, encoding="utf-8")
        count += 1
print(f"Extracted {count} Mermaid diagrams to {out}")
