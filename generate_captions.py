import csv
from pathlib import Path
from jinja2 import Environment

# Setup Jinja2 template engine
env = Environment()

# Load template
template_text = Path("template.txt").read_text(encoding="utf-8")
template = env.from_string(template_text)

# Load CSV
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Generate captions
captions = []
for row in rows:
    caption = template.render(**row)
    captions.append(caption)

# Save results
Path("captions.txt").write_text("\n\n---\n\n".join(captions), encoding="utf-8")
print("✅ Captions generated in captions.txt")
