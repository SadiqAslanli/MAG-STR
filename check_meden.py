import json

with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)

print("=== 'meden' olan hər şey ===")
found = False
for m in db['mappings']:
    for b in m.get('bachelorSpecialties', []):
        name = b.get('name', '')
        if 'məd' in name.lower() or 'meden' in name.lower() or 'mədən' in name.lower():
            found = True
            print(f"  Bachelor: {name} (code: {b.get('code')})")
            print(f"  -> Page {m.get('sourcePage')}, Program #{m.get('programNumber')}")

if not found:
    print("  >>> 'mədən' heç bir bachelor ixtisasında TAPILMADI <<<")

print()
print("=== data.json-da 'meden' olan ixtisaslar ===")
with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

unis = data if isinstance(data, list) else data.get('universities', [])
for uni in unis:
    for sp in uni.get('specialties', []):
        name = sp.get('name', '')
        if 'mədən' in name.lower() or 'maşın' in name.lower():
            if 'mədən' in name.lower():
                print(f"  {uni.get('name')}: {name}")

print()
print("=== magistr_uygunluq.json-da 050611 kodu ===")
for m in db['mappings']:
    for b in m.get('bachelorSpecialties', []):
        code = b.get('code', '') or ''
        if '0506' in code or 'dag' in b.get('name','').lower() or 'dağ' in b.get('name','').lower():
            print(f"  Code: {code}, Name: {b.get('name')}")

