import json
import re

with open('data.json', 'r', encoding='utf-8') as f:
    dj = json.load(f)

with open('magistr_uygunluq.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print(f"Total mappings to process: {len(db['mappings'])}")

LANG_MAP = {
    'rus': ['rus', 'rus dili', 'rus ədəbiyyatı'],
    'ingilis': ['ingilis', 'ingiltərə', 'amerika', 'avropa'],
    'alman': ['alman'],
    'fransız': ['fransız'],
    'ispan': ['ispan'],
    'italyan': ['italyan'],
    'ərəb': ['ərəb', 'rəb'],
    'fars': ['fars'],
    'türk': ['türk', 'türk xalqları'],
    'çin': ['çin'],
    'yapon': ['yapon'],
    'koreya': ['koreya'],
    'urdu': ['urdu'],
    'azərbaycan': ['azərbaycan dili', 'azərbaycan ədəbiyyatı', 'azərbaycan'],
    'polyak': ['polyak'],
    'ukrayna': ['ukrayna'],
    'çex': ['çex'],
    'bolqar': ['bolqar'],
    'gürcü': ['gürcü'],
    'dünya': ['dünya'],
}

def detect_langs(text):
    if not text:
        return set()
    t = text.lower()
    found = set()
    for lang, kws in LANG_MAP.items():
        for kw in kws:
            if re.search(r'\b' + re.escape(kw), t):
                found.add(lang)
                break
    return found

def normalize(text):
    if not text:
        return ""
    t = text.lower()
    t = t.replace('və', 'va').replace('ə', 'e').replace('ı', 'i').replace('i̇', 'i')
    t = t.replace('ö', 'o').replace('ü', 'u').replace('ş', 's').replace('ç', 'c').replace('ğ', 'g')
    t = re.sub(r'[^a-z0-9]', '', t)
    return t

def strip_fillers(text):
    t = text
    fillers = [
        r'metodikas[ıi]\s+v[əe]\s+metodologiyas[ıi]',
        r'metodikas[ıi]',
        r'metodologiyas[ıi]',
        r'sah[əe]l[əe]r\s+[uü]zr[əe]',
        r'[uü]zr[əe]',
        r't[əe]drisi',
        r'istiqam[əe]ti',
    ]
    for fil in fillers:
        t = re.sub(fil, ' ', t, flags=re.IGNORECASE)
    t = re.sub(r'\s+', ' ', t).strip(' ,;-()')
    return t

def get_bigrams(s):
    if len(s) < 2:
        return set()
    return set(s[i:i+2] for i in range(len(s)-1))

uni_catalog = []
for uni in dj.get('universities', []):
    u_name = uni.get('name')
    for spec in uni.get('specialties', []):
        s_name = spec.get('name')
        norm_s = normalize(s_name)
        norm_stripped = normalize(strip_fillers(s_name))
        
        uni_catalog.append({
            'university': u_name,
            'specialty': s_name,
            'norm': norm_s,
            'norm_stripped': norm_stripped,
            'bigrams': get_bigrams(norm_s),
            'bigrams_stripped': get_bigrams(norm_stripped),
            'langs': detect_langs(s_name),
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

# Comprehensive junk list:
STRICT_JUNK = {
    'leri', 'riyyesi', 'nezeriyyesi', 'sistemler', 'sistemleri', 'techizati',
    'edilmesi', 'olunmasi', 'idareolunmasi', 'tehlukesizliyi', 'sivetarixi', 'neti',
    'debiyyati', 'rcume', 'tsunasliq', 'uzre', 'dirme', 'etme', 'tler', 'ruzre',
    'biyyat', 'tarixi', 'metodlari', 'sahesi', 'saheleri', 'istiqameti', 'xidmeti',
    'kompleksleri', 'komplekslerin', 'materiallari', 'istehsali', 'qurgulari',
    'muhendisliyi', 'ixtisasi', 'tedrisi', 'metodikasi', 'metodologiyasi',
    'biyyatsunasli', 'muellimliyi', 'biyyatmuellimliyi', 'ii', 'iii', 'iiii',
    'menecment', 'biznes', 'iqtisadiyyat', 'huquq', 'senaye', 'riyye',
    'magistraturaixtisaslasmasi', 'rinidareolunmasi', 'ninidareolunmasi',
    'ninidareolunmas', 'rinidareolunmas', 'idareolunmas',
    'lerinintarixi', 'srlerintarixi', 'srleritarixi', 'liistifadeolunmasi',
    'rvediplomatiya', 'iqtisadiyyatinmesi', 'intellektualsistemler',
    'biologiya', 'psixologiya', 'sosiologiya', 'fizika', 'kimya', 'riyaziyyat',
    'tarix', 'ekologiya', 'cografiya', 'felsefe', 'filologiya', 'pedaqogika',
    'marketinq', 'maliyye', 'dizayn', 'antropologiya', 'arxeologiya',
    'informasiyasistemleri', 'kitabxana'
}

def clean_spec_name(s):
    s = re.sub(r'D\s*M\s*-\s*2024', '', s, flags=re.IGNORECASE)
    s = re.sub(r'\bD\s*M\b', '', s)
    s = s.replace('mü ə llimliyi', 'müəllimliyi')
    s = s.replace('mü ə ndisliyi', 'mühəndisliyi')
    s = s.replace('tə drisi', 'tədrisi')
    s = s.replace('ş ünasl q', 'şünaslıq')
    s = s.replace('şünasl q', 'şünaslıq')
    s = s.replace('ş ünaslıq', 'şünaslıq')
    s = s.replace('biyyat', 'ədəbiyyat')
    s = s.replace('dəbiyyat', 'ədəbiyyat')
    s = s.replace('rcümə', 'tərcümə')
    s = re.sub(r'\s+', ' ', s).strip(' -*•')
    return s

def merge_spec_lines(lines):
    cleaned = []
    for l in lines:
        cl = clean_spec_name(l)
        if not cl or cl in ['ı', 'ə', 'ı ı', 'ı ı ı', 'D M', 'və']:
            continue
        cleaned.append(cl)
        
    merged = []
    for cl in cleaned:
        if not merged:
            merged.append(cl)
            continue
            
        prev = merged[-1]
        is_continuation = False
        if prev.endswith(('və', 'üzrə', 'üzrə)', '(', 'və ya', 'ilə', 'üzrə )', '-')):
            is_continuation = True
        elif prev.endswith('dili') and cl.startswith('və'):
            is_continuation = True
        elif cl.startswith(('ədəbiyyatı)', 'dili)', 'intiqalı', 'sistemləri', 'texnikası', 'texnologiyası', 'fizikası', 'istehsalatı', 'mühəndisliyi')):
            is_continuation = True
        elif len(cl) < 14 and not cl.startswith(('060', '050', 'T ', 'İxtisas')):
            is_continuation = True
            
        if is_continuation:
            merged[-1] = f"{prev} {cl}".strip()
        else:
            merged.append(cl)
            
    return merged

total_matches_built = 0

for m in db['mappings']:
    b_text = " ".join([b.get('name', '') for b in m.get('bachelorSpecialties', [])])
    b_langs = detect_langs(b_text)
    
    raw_targets = []
    for emp in m.get('eligibleMasterPrograms', []):
        mc = emp.get('code')
        mn = emp.get('name') or ''
        raw_specs = [l.strip() for l in (emp.get('specializationsText') or '').split('\n') if l.strip()]
        merged_specs = merge_spec_lines(raw_specs)
        emp['specializationsText'] = "\n".join(merged_specs)
        
        # Only add specific specializations that are NOT in STRICT_JUNK and length >= 8
        for sp in merged_specs:
            norm = normalize(sp)
            if norm not in STRICT_JUNK and len(norm) >= 8:
                raw_targets.append((mc, mn, sp))
                
    uni_matches = []
    seen = set()
    
    for mc, mn, ts in raw_targets:
        clean_ts = clean_spec_name(ts)
        norm_ts = normalize(clean_ts)
        norm_ts_stripped = normalize(strip_fillers(clean_ts))
        
        if len(norm_ts) < 8 or norm_ts in STRICT_JUNK:
            continue
            
        bg_ts = get_bigrams(norm_ts)
        bg_ts_stripped = get_bigrams(norm_ts_stripped)
        
        target_langs = detect_langs(clean_ts)
        effective_langs = target_langs or b_langs
        
        for u in uni_catalog:
            key = (u['university'], u['specialty'])
            if key in seen:
                continue
                
            u_langs = u['langs']
            
            # LANGUAGE GATE:
            if u_langs:
                if not (effective_langs & u_langs):
                    continue
            else:
                if target_langs:
                    continue
                    
            sim = 0.0
            if norm_ts == u['norm'] or (norm_ts_stripped and norm_ts_stripped == u['norm_stripped']):
                sim = 1.0
            else:
                if bg_ts_stripped and u['bigrams_stripped']:
                    ov = len(bg_ts_stripped & u['bigrams_stripped'])
                    tot = len(bg_ts_stripped) + len(u['bigrams_stripped'])
                    if tot > 0:
                        sim = max(sim, (2.0 * ov) / tot)
                if bg_ts and u['bigrams']:
                    ov = len(bg_ts & u['bigrams'])
                    tot = len(bg_ts) + len(u['bigrams'])
                    if tot > 0:
                        sim = max(sim, (2.0 * ov) / tot)
                        
            if sim < 0.78 and len(norm_ts_stripped) >= 16 and len(u['norm_stripped']) >= 16:
                if norm_ts_stripped in u['norm_stripped'] or u['norm_stripped'] in norm_ts_stripped:
                    sim = max(sim, 0.85)

            # Suffix topic protection (prevent "Dinin sosiologiyası" matching "Siyasətin sosiologiyası")
            for suffix in ['sosiologiya', 'tarix', 'psixologiya', 'huquq', 'iqtisadiyyat', 'senaye', 'menecment', 'sistem']:
                rx = re.compile(rf'({suffix}[a-z0-9]*)$')
                m_ts = rx.search(norm_ts)
                m_u = rx.search(u['norm'])
                if m_ts and m_u:
                    prefix_ts = norm_ts[:m_ts.start()]
                    prefix_u = u['norm'][:m_u.start()]
                    if prefix_ts and prefix_u:
                        bg_p_ts = get_bigrams(prefix_ts)
                        bg_p_u = get_bigrams(prefix_u)
                        p_sim = (2.0 * len(bg_p_ts & bg_p_u)) / (len(bg_p_ts) + len(bg_p_u)) if (len(bg_p_ts) + len(bg_p_u)) > 0 else 0
                        if p_sim < 0.6 and prefix_ts not in prefix_u and prefix_u not in prefix_ts:
                            sim = 0.0
                            break
                    
            # Require higher confidence (>= 0.78)
            if sim >= 0.78:
                seen.add(key)
                uni_matches.append({
                    'university': u['university'],
                    'specialty': u['specialty'],
                    'eligibleMasterProgramCode': mc,
                    'eligibleMasterProgram': mn,
                    'eligibleSpecializationSource': clean_ts,
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
                
    m['universityMatches'] = uni_matches
    total_matches_built += len(uni_matches)

print(f"Total clean university matches across all mappings: {total_matches_built}")

with open('magistr_uygunluq.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Saved updated magistr_uygunluq.json successfully.")
