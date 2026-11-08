import requests
import re
import json
import time
from concurrent.futures import ThreadPoolExecutor

t0 = time.time()
print("1. Scribd-dən səhifələrin endirilməsi...")

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=3)
session.mount('https://', adapter)

url = 'https://www.scribd.com/document/733759124/2-5341821482265756298'
r = session.get(url, timeout=15)
urls = re.findall(r'https?://html\.scribdassets\.com/[^\s"\'<>]+\.jsonp', r.text)

def get_p(u):
    m = re.search(r'/pages/(\d+)-', u)
    return int(m.group(1)) if m else 9999

unique_urls = sorted(list(set(urls)), key=get_p)
target_urls = [(get_p(u), u) for u in unique_urls if 5 <= get_p(u) <= 52]

page_htmls = {}
def fetch_p(item):
    p_num, u = item
    try:
        res = session.get(u, timeout=15)
        m = re.search(r'callback\(\s*(\[.*\])\s*\);?', res.text, re.DOTALL)
        if m:
            data = json.loads(m.group(1))
            return p_num, data[0]
    except Exception:
        pass
    return p_num, None

with ThreadPoolExecutor(max_workers=10) as executor:
    for p_num, html in executor.map(fetch_p, target_urls):
        if html:
            page_htmls[p_num] = html

# Retry any missing
missing = [p for p, _ in target_urls if p not in page_htmls]
for p, u in target_urls:
    if p in missing:
        _, html = fetch_p((p, u))
        if html:
            page_htmls[p] = html

print(f"Endirildi: {len(page_htmls)} / {len(target_urls)} səhifə ({time.time()-t0:.2f}s).")

print("2. Cədvəl bloklarının koordinatlarla çıxarılması və sətirlərin birləşdirilməsi...")

pattern = re.compile(r'style="([^"]*left:([0-9.]+)px;top:([0-9.]+)px[^"]*)"[^>]*>(.*?)</span>', re.DOTALL)

def clean_letters(text):
    t = text
    t = re.sub(r'([a-zA-Z0-9])\s+([əƏıIİöÖüÜşŞçÇğĞ])', r'\1\2', t)
    t = re.sub(r'([əƏıIİöÖüÜşŞçÇğĞ])\s+([a-zA-Z0-9])', r'\1\2', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def merge_spans(spans, y_threshold=26):
    if not spans:
        return []
    spans = sorted(spans, key=lambda s: (s['top'], s['left']))
    lines = []
    curr = []
    for s in spans:
        if not curr:
            curr = [s]
        else:
            avg_top = sum(x['top'] for x in curr) / len(curr)
            if abs(s['top'] - avg_top) <= y_threshold:
                curr.append(s)
            else:
                curr.sort(key=lambda x: x['left'])
                lines.append(curr)
                curr = [s]
    if curr:
        curr.sort(key=lambda x: x['left'])
        lines.append(curr)
        
    res = []
    for line in lines:
        lt = ""
        prev_r = None
        for it in line:
            tx = it['text']
            lt += (" " if prev_r and it['left'] - prev_r > 20 else "") + tx
            prev_r = it['left'] + len(tx) * 11
        cl = clean_letters(lt)
        if cl and len(cl) > 1 and not cl.startswith('D M -'):
            res.append(cl)
    return res

all_blocks = []

for p_num in range(5, 53):
    if p_num not in page_htmls:
        continue
    html = page_htmls[p_num]
    elements = []
    for match in pattern.finditer(html):
        style, left_s, top_s, text = match.groups()
        cl = re.sub(r'<[^>]+>', '', text).strip()
        if cl:
            elements.append({'top': float(top_s), 'left': float(left_s), 'text': cl})
            
    elems = [e for e in elements if 680 <= e['top'] <= 5900]
    prog_elems = [e for e in elems if e['left'] >= 3450]
    
    prog_rows = []
    for e in prog_elems:
        txt = e['text'].strip()
        nums = re.findall(r'\b\d+\b', txt)
        if nums:
            prog_rows.append({'top': e['top'], 'text': txt, 'nums': [int(n) for n in nums]})
            
    prog_rows.sort(key=lambda x: x['top'])
    clustered_progs = []
    curr_c = []
    for pr in prog_rows:
        if not curr_c:
            curr_c = [pr]
        elif abs(pr['top'] - curr_c[0]['top']) <= 45:
            curr_c.append(pr)
        else:
            clustered_progs.append(curr_c)
            curr_c = [pr]
    if curr_c:
        clustered_progs.append(curr_c)
        
    markers = []
    for c in clustered_progs:
        all_nums = []
        for item in c:
            all_nums.extend(item['nums'])
        if not all_nums:
            continue
        avg_top = sum(item['top'] for item in c) / len(c)
        prog_num = None
        min_score = None
        if len(all_nums) >= 2:
            prog_num = all_nums[0]
            min_score = all_nums[1]
        elif len(all_nums) == 1:
            val = all_nums[0]
            if val in [30, 35, 40, 45, 50, 55, 60]:
                min_score = val
            elif 1 <= val <= 75:
                prog_num = val
                min_score = 40
        markers.append({'top': avg_top, 'prog': prog_num, 'score': min_score})
        
    if not markers:
        b_lines = merge_spans([e for e in elems if e['left'] < 1350])
        m_lines = merge_spans([e for e in elems if 1350 <= e['left'] < 3450])
        if b_lines or m_lines:
            all_blocks.append({'page': p_num, 'program': None, 'min_score': None, 'bachelor_lines': b_lines, 'master_lines': m_lines})
    else:
        for idx, m in enumerate(markers):
            s_top = m['top'] - 120 if idx == 0 else (markers[idx-1]['top'] + m['top']) / 2
            s_bot = 6000 if idx == len(markers) - 1 else (m['top'] + markers[idx+1]['top']) / 2
            b_lines = merge_spans([e for e in elems if s_top <= e['top'] < s_bot and e['left'] < 1350])
            m_lines = merge_spans([e for e in elems if s_top <= e['top'] < s_bot and 1350 <= e['left'] < 3450])
            if b_lines or m_lines:
                all_blocks.append({'page': p_num, 'program': m['prog'], 'min_score': m['score'], 'bachelor_lines': b_lines, 'master_lines': m_lines})

print(f"Cəmi çıxarılan blok: {len(all_blocks)}")

print("3. İxtisas adlarının və çoxsətirli adların dəqiq birləşdirilməsi...")

code_start_regex = re.compile(r'^(?:\*{1,2}\s*)?([A-Z]{1,2}\s+\d{6}|\d{6})\b', re.IGNORECASE)

def merge_bachelor_specialties(lines):
    specs = []
    curr_code = None
    curr_parts = []
    curr_source = []
    
    for l in lines:
        clean_l = l.strip().replace('D M - 2024', '').strip()
        if not clean_l or clean_l in ['ı', 'ə', 'ğ', 'və']:
            continue
            
        m = code_start_regex.match(clean_l)
        if m:
            if curr_code or curr_parts:
                full_name = " ".join(curr_parts).strip().lstrip('*-• ')
                if full_name:
                    specs.append({'code': curr_code, 'name': full_name, 'sourceText': " ".join(curr_source)})
                curr_parts = []
                curr_source = []
            curr_code = m.group(1).strip()
            rest = clean_l[m.end():].strip().lstrip('*-• ')
            curr_source.append(clean_l)
            if rest:
                curr_parts.append(rest)
        else:
            curr_source.append(clean_l)
            curr_parts.append(clean_l)
            
    if curr_code or curr_parts:
        full_name = " ".join(curr_parts).strip().lstrip('*-• ')
        if full_name:
            specs.append({'code': curr_code, 'name': full_name, 'sourceText': " ".join(curr_source)})
            
    # Clean up names:
    cleaned_specs = []
    for s in specs:
        name = s['name']
        name = re.sub(r'\s+', ' ', name)
        # Fix common words:
        name = name.replace('mü əllimliyi', 'müəllimliyi')
        name = name.replace('mü əndisliyi', 'mühəndisliyi')
        name = name.replace('mühandisliyi', 'mühəndisliyi')
        name = name.replace('mühəndislik', 'mühəndisliyi')
        name = name.replace('G əmiqay ı rma', 'Gəmiqayırma')
        name = name.replace('g əmi', 'gəmi')
        name = name.replace('t əmiri', 'təmiri')
        # If name is just "mühəndisliyi" without prefix and code is None, skip
        if len(name) < 4:
            continue
        cleaned_specs.append({'code': s['code'], 'name': name, 'sourceText': s['sourceText']})
    return cleaned_specs

def parse_master_programs(lines):
    m_specs = []
    curr_code = None
    curr_name = None
    curr_lines = []
    for l in lines:
        clean_l = l.strip()
        if not clean_l:
            continue
        m_code_m = re.match(r'(\d{6,7})\s*(.*)', clean_l)
        if m_code_m:
            if curr_code or curr_lines or curr_name:
                m_specs.append({'code': curr_code, 'name': curr_name or "Magistratura ixtisaslaşması", 'specializations': curr_lines})
            curr_code = m_code_m.group(1)
            curr_name = m_code_m.group(2).strip()
            curr_lines = []
        else:
            spec = clean_l.lstrip('-*• ').strip()
            if len(spec) > 2:
                curr_lines.append(spec)
    if curr_code or curr_lines or curr_name:
        m_specs.append({'code': curr_code, 'name': curr_name or "Magistratura ixtisaslaşması", 'specializations': curr_lines})
    return m_specs

print("4. Universitetlər və keçid balları ilə eşləşdirmə...")

with open('data.json', 'r', encoding='utf-8') as f:
    data_json = json.load(f)

def normalize(text):
    if not text:
        return ""
    t = text.lower()
    t = t.replace('və', 'va').replace('ə', 'e').replace('ı', 'i').replace('i̇', 'i')
    t = t.replace('ö', 'o').replace('ü', 'u').replace('ş', 's').replace('ç', 'c').replace('ğ', 'g')
    t = re.sub(r'[^a-z0-9]', '', t)
    return t

def get_bigrams(s):
    if len(s) < 2:
        return set()
    return set(s[i:i+2] for i in range(len(s)-1))

uni_catalog = []
for uni in data_json.get('universities', []):
    u_name = uni.get('name')
    for spec in uni.get('specialties', []):
        s_name = spec.get('name')
        norm_s = normalize(s_name)
        if not norm_s:
            continue
        uni_catalog.append({
            'university': u_name,
            'specialty': s_name,
            'norm': norm_s,
            'bigrams': get_bigrams(norm_s),
            'paidScore': spec.get('paidScore'),
            'paidScoreMax': spec.get('paidScoreMax'),
            'paidStatus': spec.get('paidStatus'),
            'freeScore': spec.get('freeScore'),
            'freeScoreMax': spec.get('freeScoreMax'),
            'freeStatus': spec.get('freeStatus'),
            'hasAptitudeExam': spec.get('hasAptitudeExam', False),
            'paidAptitudeScore': spec.get('paidAptitudeScore'),
            'freeAptitudeScore': spec.get('freeAptitudeScore'),
        })

final_mappings = []

for b in all_blocks:
    page = b.get('page')
    prog = b.get('program')
    score = b.get('min_score') or (40 if prog else None)
    
    b_specs = merge_bachelor_specialties(b.get('bachelor_lines', []))
    m_specs = parse_master_programs(b.get('master_lines', []))
    
    uni_matches = []
    seen = set()
    
    targets = []
    for mp in m_specs:
        mc = mp.get('code')
        mn = mp.get('name')
        if mn and len(mn) > 3:
            targets.append((mc, mn, mn))
        for sp in mp.get('specializations', []):
            if len(sp) > 3:
                targets.append((mc, mn, sp))
                
    for mc, mn, ts in targets:
        nt = normalize(ts)
        if not nt or len(nt) < 4:
            continue
        bg_t = get_bigrams(nt)
        if not bg_t:
            continue
            
        for u in uni_catalog:
            key = (u['university'], u['specialty'])
            if key in seen:
                continue
            nu = u['norm']
            sim = 0.0
            if nt == nu:
                sim = 1.0
            elif nt in nu or nu in nt:
                sim = 0.88
            else:
                ov = len(bg_t & u['bigrams'])
                tot = len(bg_t) + len(u['bigrams'])
                if tot > 0:
                    sim = (2.0 * ov) / tot
            if sim >= 0.76:
                seen.add(key)
                uni_matches.append({
                    'university': u['university'],
                    'specialty': u['specialty'],
                    'eligibleMasterProgramCode': mc,
                    'eligibleMasterProgram': mn,
                    'eligibleSpecializationSource': ts,
                    'matchConfidence': round(sim, 2),
                    'paidScore': u['paidScore'],
                    'paidScoreMax': u['paidScoreMax'],
                    'paidStatus': u['paidStatus'],
                    'freeScore': u['freeScore'],
                    'freeScoreMax': u['freeScoreMax'],
                    'freeStatus': u['freeStatus'],
                    'hasAptitudeExam': u['hasAptitudeExam'],
                    'paidAptitudeScore': u['paidAptitudeScore'],
                    'freeAptitudeScore': u['freeAptitudeScore'],
                })
                
    if b_specs or uni_matches:
        final_mappings.append({
            'sourcePage': page,
            'programNumber': prog,
            'minimumScore': score,
            'bachelorSpecialties': b_specs,
            'eligibleMasterPrograms': [
                {
                    'code': mp.get('code'),
                    'name': mp.get('name'),
                    'specializationsText': "\n".join(mp.get('specializations', []))
                }
                for mp in m_specs
            ],
            'universityMatches': uni_matches
        })

print(f"5. Baza yaddaşa yazılır (Cəmi mapping: {len(final_mappings)})...")

final_dataset = {
    'title': 'DİM Magistratura səviyyəsi üzrə İxtisaslaşma Seçimi Cədvəli (Tam Rəsmi Baza)',
    'source': 'https://www.scribd.com/document/733759124/2-5341821482265756298',
    'pageCount': 48,
    'mappingsCount': len(final_mappings),
    'mappings': final_mappings
}

with open('magistr_uygunluq.json', 'w', encoding='utf-8') as f:
    json.dump(final_dataset, f, ensure_ascii=False, indent=2)

print(f"UĞURLA TAMAMLANDI! {time.time()-t0:.2f} saniyə.")

