import json
with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)
for m in db['mappings']:
    for b in m.get('bachelorSpecialties', []):
        name = b.get('name','')
        if 'rus' in name.lower() and 'dil' in name.lower():
            print('CODE:', b.get('code'), 'NAME:', name)
            print('  -> master:', m.get('masterProgram', {}).get('name',''))
            unis = m.get('universityMatches',[])
            print('  -> uni matches:', [u['specialty'] for u in unis[:8]])
            print()

