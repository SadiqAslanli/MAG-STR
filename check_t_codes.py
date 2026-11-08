import json

with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)

t_codes = set()
for m in db['mappings']:
    for b in m.get('bachelorSpecialties', []):
        c = b.get('code') or ''
        if c.startswith('T '):
            t_codes.add((c, b.get('name'), m.get('programNumber'), m.get('sourcePage')))

for c in sorted(list(t_codes)):
    if any(k in c[1].lower() for k in ['qaz', 'neft', 'geologiya', 'yataq', 'qazıntı', 'faydalı', 'dağ', 'mədən']):
        print(c)

