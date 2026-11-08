import re

with open('page5.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect all tags inside text_layer
# Often scribd has: <div class="..." style="font-size:..."><span class=... style="left:...;top:...">text</span></div>
# Let's parse all divs and spans with their style
# A regex to capture: style="...top:(\d+)px;left:(\d+)px..." or style="...left:(\d+)px;top:(\d+)px..."
elements = []
for m in re.finditer(r'<span[^>]*style="([^"]*)"[^>]*>(.*?)</span>', html, re.DOTALL):
    style = m.group(1)
    raw_text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    if not raw_text:
        continue
    top_m = re.search(r'top:([0-9.]+)px', style)
    left_m = re.search(r'left:([0-9.]+)px', style)
    if top_m and left_m:
        top = float(top_m.group(1))
        left = float(left_m.group(1))
        elements.append({'top': top, 'left': left, 'text': raw_text})

print(f"Total positioned spans: {len(elements)}")

# Let's cluster spans that are on the same line (top within ~10-15px)
# and sort by left
elements.sort(key=lambda e: (e['top'], e['left']))

lines = []
curr_line = []
curr_top = None

for e in elements:
    if curr_top is None:
        curr_top = e['top']
        curr_line = [e]
    elif abs(e['top'] - curr_top) <= 15:
        curr_line.append(e)
    else:
        # line finished
        curr_line.sort(key=lambda x: x['left'])
        # merge text
        lines.append((curr_top, curr_line))
        curr_top = e['top']
        curr_line = [e]

if curr_line:
    curr_line.sort(key=lambda x: x['left'])
    lines.append((curr_top, curr_line))

print(f"Total lines reconstructed: {len(lines)}")
for top, line in lines[10:35]:
    # see what left coordinates exist
    line_str = " | ".join([f"[{item['left']:.0f}] {item['text']}" for item in line])
    print(f"y={top:.0f}: {line_str}")
