import re

with open('page5.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Pattern for span with position style: style="left:503px;top:5353px;..."
# or inside div / span
# Let's find all elements with left and top
items = []
pattern = re.compile(r'style="([^"]*left:([0-9.]+)px;top:([0-9.]+)px[^"]*)"[^>]*>(.*?)</span>', re.DOTALL)
for m in pattern.finditer(c):
    style, left, top, text = m.groups()
    text = re.sub(r'<[^>]+>', '', text).strip()
    if text:
        items.append((float(top), float(left), text))

# Also check without style attribute or other formats
print(f"Found {len(items)} items with left/top in span style.")

# Group by approximate line (top coordinate)
# Let's inspect unique tops
items.sort(key=lambda x: (x[0], x[1]))

# Group into lines where abs(top1 - top2) < 20 (or whatever the font-size scale is)
# Let's see some top values
for it in items[:25]:
    print(f"top: {it[0]}, left: {it[1]}, text: {it[2]}")
