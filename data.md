# Magistratura Səviyyəsi Üzrə İxtisaslaşma Seçimi Cədvəli (DİM)

> **Mənbə:** Dövlət İmtahan Mərkəzi (DİM) — Magistr xüsusi buraxılışı / Scribd Sənədi (`733759124/2-5341821482265756298`)  
> **Məlumat:** 126 uyğunluq bloku, 40-dan çox qəbul proqramı, bakalavriat və magistratura ixtisaslaşmaları, minimal bal tələbləri və universitet keçid balları.

## 1. Scribd Saytından Data Scraping Metodu (Necə Çəkilir?)

Scribd sənədləri standart veb səhifələrdən fərqli olaraq mətnləri birbaşa tək HTML teqi daxilində saxlamır. Məlumatı çəkmək üçün aşağıdakı arxitektura istifadə olunur:

1. **CDN / JSONP Arxitekturası:** Scribd sənədin hər səhifəsini `https://html.scribdassets.com/{doc_id}/pages/{page_num}-{hash}.jsonp` formatında saxlayır.
2. **Səhifə Linklərinin Çıxarılması:** Əsas sənəd səhifəsindən (`https://www.scribd.com/document/733759124/...`) HTML endirilir və içərisindəki bütün `html.scribdassets.com` jsonp ünvanları regex vasitəsilə aşkarlanır.
3. **JSONP-dən HTML-ə Keçid:** Hər bir JSONP faylı `window.pageN_callback(["<html content>"])` şəklində gəlir. Python vasitəsilə JSON hissəsi ayrılır və səhifənin HTML DOM-u əldə edilir.
4. **Koordinat Əsaslı Cədvəl Bərpası:** Hər bir mətn elementi (span) `top` (şaquli) və `left` (üfüqi) pikselləri ilə yerləşdirilib. 4 əsas sütun (Bakalavr ixtisası, Magistratura ixtisaslaşması, Proqram №, Minimal bal) X və Y koordinatlarına görə qruplaşdırılaraq tam cədvələ çevrilir.

```python
# Nümunə: Scribd JSONP səhifəsindən mətn və koordinatların çəkilməsi
import requests, re, json

url = 'https://html.scribdassets.com/eoh9xur0gchwezt/pages/5-c40328b208.jsonp'
res = requests.get(url)
match = re.search(r'callback\(\s*(\[.*\])\s*\);?', res.text, re.DOTALL)
if match:
    html_content = json.loads(match.group(1))[0]
    # Cədvəl elementlərinin koordinatlarla oxunması...
```

## 2. Ümumi Qeydlər və Tələblər

- **`*` İxtisaslar:** Əvvəlki illərin təsnifatına uyğun ixtisas kodları.
- **`**` İxtisaslar:** Cari bakalavriat təsnifatı üzrə ixtisaslar.
- **Minimal Bal:** Bakalavrın müvafiq proqram üzrə ixtisaslaşma seçiminə buraxılması üçün magistratura qəbul imtahanında (və ya qabiliyyət imtahanında) toplamalı olduğu ən aşağı bal həddidir.

## 3. İxtisaslaşma Seçimi və Uyğunluq Cədvəli

### Proqram № 1

#### Blok 1 (Minimal bal: `40`, Səhifə: 1)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050611` | Geologiya və geofizika mühəndisliyi |
| `050602` | Geologiya mühəndisliyi |
| `050604` | Geofizika mühəndisliyi |
| `T 010100` | Faydalı qazıntı yataqlarının axtarışı və geoloji plana alınması |
| `T 010200` | Faydalı qazıntı yataqlarının kəşfiyyatı və geologiyası |
| `T 010400` | Faydalı qazıntı yataqlarının axtarışı və kəşfiyyatının geofiziki üsulları (sahələr üzrə) |
| `T 010500` | Neft və qazın geologiyası |
| `TE 090200` | Geofizika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006010` Geologiya və geofizika mühəndisliyi**
  - Neft-qaz yataqlanmn axtar1S1 va ka$iyyatl
  - Neft-qaz-modan geologiyasl
  - Neft-qaz-modon geofizikasr
  - Faydall qanntl yataqlaruun hidrogeologiyasl Vö mühandis geologiyasl
  - Neft-qaz yataqlarmm axtarl#l va ka$iyyatrnrn geofiziki üsullarr

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz yataqlarının axtarışı və kəşfiyyatı | 40 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz-mədən geologiyası | 42 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz-mədən geofizikası | 43 | 40 |
| Bakı Dövlət Universiteti | Faydalı qazıntı yataqlarının hidrogeologiyası və mühəndis geologiyası | 43 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Faydalı qazıntı yataqlarının hidrogeologiyası və mühəndis geologiyası | None | 40 |
| Bakı Dövlət Universiteti | Neft-qaz yataqlarının axtarışı və kəşfiyyatının geofiziki üsulları | 41.5 | 41.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz yataqlarının axtarışı və kəşfiyyatının geofiziki üsulları | 42.5 | 40 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 1)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050603` | Hidrogeologiya mühəndisliyi |
| `TE 090400` | Hidrogeologiya və mühəndis geologiyası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006010` Geologiya və geofizika mühəndisliyi**
  - Neft-qaz yataqlarmm axtarl*l vo ka$iyyatl
  - Neft-qaz-modon geologiyasl
  - Neft-qaz-mödan geofizikasl
  - Faydall qanntl yataqlarrmn hidrogeologiyasl vo mühandis geologiyasr
  - Neft-qaz yataqlanmn axtarl#l va ka}fiyyatlnrn geofiziki üsullarl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz-mədən geologiyası | 42 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz-mədən geofizikası | 43 | 40 |
| Bakı Dövlət Universiteti | Faydalı qazıntı yataqlarının hidrogeologiyası və mühəndis geologiyası | 43 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Faydalı qazıntı yataqlarının hidrogeologiyası və mühəndis geologiyası | None | 40 |
| Bakı Dövlət Universiteti | Neft-qaz yataqlarının axtarışı və kəşfiyyatının geofiziki üsulları | 41.5 | 41.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz yataqlarının axtarışı və kəşfiyyatının geofiziki üsulları | 42.5 | 40 |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 1)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050603` | Hidrogeologiya mühəndisliyi |
| `TE 090400` | Hidrogeologiya və mühəndis geologiyası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005006` Geologiya**
  - Geokimya
  - Doniz Vö okean dibinin geologiyasl
  - Mineralogiya
  - Sedimentologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Dəniz və okean dibinin geologiyası | None | 45 |
| Bakı Dövlət Universiteti | Mineralogiya | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Sedimentologiya | 46.5 | 45 |

</details>

---

### Proqram № 2

#### Blok 1 (Minimal bal: `40`, Səhifə: 1)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050631` | Neft-qaz miihöndisliyi |
| `050606` | Neft-qaz mühəndisliyi |
| `T 020200` | Faydalı qazıntı yataqlarının yeraltı işlənməsi |
| `T 020500` | Neft-qaz yataqlarının işlənməsi və istismarı |
| `T 020700` | Neft və qaz quyularının qazılması |
| `TT 060100` | Neft-qaz və dag-mədən istehsalatının fiziki prosesləri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006034` Neft-qaz mühəndisliyi**
  - Doniz neft va qaz quyularmm qanlrnasl
  - Neft va qaz yataqlanmn i#lönmasi
  - Deniz neft-qaz Vö qaz-kondensat yataqlanrun islanmosi
  - Neft-qaz quyulannm istismarl
  - Yatagm qiymatlandirilmasi va idaro olunmasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft və qaz yataqlarının işlənməsi | 61 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Dəniz neft-qaz və qaz-kondensat yataqlarının işlənməsi | 60.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Dəniz neft-qaz və qaz-kondensat yataqlarının işlənməsi İngilis dilində | 63 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz quyularının istismarı | 60.5 | 40 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 1)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050607` | Neft-qaz qurğuları mühəndisliyi |
| `T 020600` | Qaz və neft kəmər və anbarlarının layihələndirilməsi, tikintisi və istismarı |
| `T 020800` | Daniz neft-qaz qurğuları |
| `T 370100` | Doniz neft-qaz hidrotexniki qurgularmm tikintisi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006034` Neft-qaz mühəndisliyi**
  - Doniz neft va qaz quyularmm qanlmasl
  - Neft va qaz yataqlannrn islanmasi
  - Doniz neft-qaz va qaz-kondensat yataqlarrnm islanmasi
  - Neft-qaz quyulanmn istisman
  - Yatagm qiymötlandirilmasi va idara olunmasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Dəniz neft və qaz quyularının qazılması | 60.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft və qaz yataqlarının işlənməsi | 61 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Dəniz neft-qaz və qaz-kondensat yataqlarının işlənməsi | 60.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz quyularının istismarı | 60.5 | 40 |

</details>

---

### Proqram № 3

#### Blok 1 (Minimal bal: `40`, Səhifə: 4)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 080700` | Gəmilarin avtomatla'dlrma və elektroenerii sistemlari |
| `T 120800` | Gəmilarin elektrik avadanh Ian və avtomatikast |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006008` Elektrik və elektronika mühəndisliyi**
  - Güc elektronikast
  - Gamilarin elektrik tochizatl sistemlori
  - Elektrik tochizatl sahalor üzra

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Güc elektronikası | 43 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Güc elektronikası | 43.5 | 40 |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmilərin elektrik təchizatı sistemləri | 50.5 | 50.5 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050602` | Aqromühəndislik |
| `050706` | Aqromühəndislik |
| `AT 060100` | Aqrar istehsalatın texnologiyası |
| `AT 060200` | Aqrar istehsalatın mexanikiləşdirilməsi |
| `AT 060300` | Aqrar istehsalatın elektrikiləşdirilməsi və avtomatlaşdırılması |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006002` Aqromühəndislik**
  - Aqrar istehsal saholorinin enerji tochizau

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsal sahələrinin enerji təchizatı (tədris Azərbaycan dilində) | 44 | 40 |

</details>

---

### Proqram № 4

#### Blok 1 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050104` | Pirotexniki və partlad |
| `XTB 050003` | Pirotexniki vasitalarin texnologiyasl |
| `XTB 050103` | Pirotexniki vasitalarin texnologiyast |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006009` Energetika mühəndisliyi**
  - Elektroenergetika
  - istilik energetikasa qurgulan
  - Barpaolunan enerji manbolari
  - Davamll elektroener etika sistemlori

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Elektroenergetika | 44 | 40 |
| Azərbaycan Texniki Universiteti | Elektroenergetika | 51 | 51 |
| Bakı Mühəndislik Universiteti | Elektroenergetika | 41.5 | 40 |
| Milli Aviasiya Akademiyası | Elektroenergetika | 46 | 40 |
| Naxçıvan Dövlət Universiteti | Elektroenergetika | 43 | 40 |
| Mingəçevir Dövlət Universiteti | Elektroenergetika | 42 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Elektroenergetika (tədris Azərbaycan dilində) | None | 40 |
| Azərbaycan Texniki Universiteti | Davamlı elektroenergetika sistemləri | 47.5 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstilik energetikası qurğuları | 40 | 40 |
| Azərbaycan Texniki Universiteti | İstilik energetikası qurğuları | 41.5 | 41 |
| Azərbaycan Texniki Universiteti | Bərpaolunan enerji mənbələri | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Davamlı elektroenergetika sistemləri | 47.5 | 45 |

</details>

---

### Proqram № 5

#### Blok 1 (Minimal bal: `40`, Səhifə: 2)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050622` | Maşın mühəndisliyi |
| `050628` | Mexanika mühəndisliyi |
| `050610` | Enerji maşınqayırması mühəndisliyi |
| `050612` | Maşın mühəndisliyi |
| `050625` | Texnoloji avadanhqlar m ühondisliyi |
| `050630` | Mexanika mühəndisliyi |
| `050645` | Poliqrafiya mühəndisliyi |
| `050646` | Təkrar emal və bərpa texnologiyaları (sahələr üzrə) |
| `T 060200` | Maşınqayırmada kompüter texnologiyası |
| `T 060300` | Tökmə istehsalının texnologiyası |
| `T 060400` | Texnoloii avadanhqlann layihalandirilmösi Vö istismarı |
| `T 060500` | Maşın və aparat hissələrinin bərpası və möhkəmliyinin artırılması texnologiyasl Vö avadanlığı |
| `T 060700` | Texnoloii komplekslarin |
| `T 060800` | Hidravlik maynlar, hidrointiqallar hidropnevmoavtomatika |
| `T 110100` | Texnoloji ma'lnlar və avadanhqlar (sahələr üzrə) |
| `T 110200` | Poliqrafiya masmlan Vö komplekslari |
| `T 110300` | Qaldmcl nəqliyyat və avadanhqlan |
| `T 110400` | Kimya müəssisələrinin avtomatlaşdırılmış istehsalatları |
| `TT 100100` | Maşınların möhkəmliyi və dinamikası |
| `TT 180100` | Tribotexnika |
| `200100` | Maddi istehsal vasitələrinin renovasiyası (sahələr üzrə) |
| `TT 230100` | Mexanikləşdirmə və avtomatlaşdırma (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Masmqayrrma texnologiyast
  - Maynqayrrmada kompüter texnologiyalan
  - Tökmo vo qaynaq istehsaluun mastn Vö avadanhqlan
  - Maynlarm tomir texnologiyast va
  - Texnoloji komplekslörin layiholondirilmosi
  - Yiiksak somaroli emal proseslarinin texnologiyasl va maynlan
  - hissölörinin yeyilmoyö davamllhgllun yüksöldilmosi Vö börpasl
  - texnologiyalan
- ** `7006026` Materiallar mühəndisliyi**
  - Materialsünasltq vo materiallar texnologiyast
  - Kompozit materiallar, mamulatlar vo konstruksiyalar
  - Maynqaytrmada materialsünashq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları | 44.5 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları İngilis dilində | 51.5 | 40 |
| Bakı Mühəndislik Universiteti | Tökmə və qaynaq istehsalının maşın və avadanlıqları | None | 40 |
| Azərbaycan Texniki Universiteti | Texnoloji komplekslərin layihələndirilməsi | 41 | 40 |
| Azərbaycan Texniki Universiteti | Yüksək səmərəli emal proseslərinin texnologiyası və maşınları | 40.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Kompozit materiallar, məmulatlar və konstruksiyalar | 44 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq | 47.5 | 40 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050643` | Coxi'l.non mallann texnologiyast mühəndisliyi |
| `T 280100` | Tabii liflarin istehsall texnologiyast və avadanhqlan |
| `T 280200` | Kimyavi liflar və onlann asastnda kompozisiya materiallan istehsalının texnologiyast və avadanhqlan |
| `T 280300` | Oyiricilik texnologiyast |
| `T 280400` | Toxuculuq texnologiyast |
| `T 280900` | Tiki* mamulatlannm konstruksiya edilmasi |
| `T 281100` | Gön-dari mamulatlanmn konstruksi a edilmasi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006026` Materiallar mühəndisliyi**
  - Materialsünashq va materiallar texnologiyast
  - Kom t materiallar, mamulatlar va konstruksiyalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Kompozit materiallar, məmulatlar və konstruksiyalar | 44 | 40 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050623` | Materiallar mühəndisliyi |
| `050601` | Materialşünaslıq mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006031` Metallurgiya mühəndisliyi**
  - Olvan va nadir metallann metallurgiyasl
  - Metallurji proseslarin vo materiallann fiziki-kimyovi todqiqat üsullan
  - Qaynaq istehsall metallurgiyasl, texnologiyast va avadanllgl
  - Metaliünashq vo metallann termiki emall
- ** `7006026` Materiallar mühəndisliyi**
  - Materialsünashq va materiallar texnologiyast
  - Masmqaytrmada materialsünashq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Əlvan və nadir metalların metallurgiyası | None | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Metallurji proseslərin və materialların fiziki-kimyəvi tədqiqat üsulları | None | 40 |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Azərbaycan Texniki Universiteti | Metalşünaslıq və metalların termiki emalı | 53.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq | 47.5 | 40 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050106` | Silah və silah sistemlari mühəndisliyi |
| `XTB 050001` | Silah və silah sistemlarinin istehsal texnologiyast |
| `-` | Xüsusi təyinatlı texnika və sistemlər |
| `XTB 050101` | Silah və silah sistemlarinin istehsal texnologiyast |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Masmqayrrma texnologiyast
  - Mastnqayarmada kompüter texnologiyalan
  - Tökmo vo qaynaq istehsahnm mastn va avadanhqlan
  - Masrnlann tomir texnologiyasl va servisi
  - Texnoloji komplekslarin layihölandirilmosi
  - Yüksok somoroli emal proseslorinin texnologiyasJ vo mastnlan
  - texnologiyalan
- ** `7006027` Mexanika mühəndisliyi**
  - Masmlann möhkomliyi vo dinamikast
- ** `7006026` Materiallar mühəndisliyi**
  - Materialsiinashq vo materiallar texnologiyast
  - Kompozit materiallar, mamulatlar vo konstruksiyalar
  - Mastn a rmada materialsünasli

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları | 44.5 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları İngilis dilində | 51.5 | 40 |
| Bakı Mühəndislik Universiteti | Tökmə və qaynaq istehsalının maşın və avadanlıqları | None | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Maşınların təmir texnologiyası və servisi | 53 | 53 |
| Bakı Mühəndislik Universiteti | Maşınların təmir texnologiyası və servisi | 51 | 51 |
| Azərbaycan Texniki Universiteti | Texnoloji komplekslərin layihələndirilməsi | 41 | 40 |
| Azərbaycan Texniki Universiteti | Yüksək səmərəli emal proseslərinin texnologiyası və maşınları | 40.5 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Maşınların möhkəmliyi və dinamikası | 46 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Kompozit materiallar, məmulatlar və konstruksiyalar | 44 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq | 47.5 | 40 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050101` | Harbi kompozisiya materiallarl mühəndisliyi |
| `XTB 050005` | Kompozisiya materiallarmdan müdafio toyinatll mamulatlann layihələndirilməsi və istehsall |
| `XTB 050105` | Kompozisiya materiallanndan müdafia toyinatll mamulatlann layihələndirilməsi və istehsall |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006026` Materiallar mühəndisliyi**
  - va materiallar texnologiyasr
  - Kompozit materiallar, momulatlar vo konstruksiyalar
  - Maynqayrrmada materia19ünashq
- ** `7006031` Metallurgiya mühəndisliyi**
  - Olvan vo nadir metallann metallurgiyasl
  - Metallurji proseslorin vo materiallarm fiziki-kimyavi todqiqat iisullan
  - Qaynaq istehsall metallurgiyasl, texnologiyasl vo avadan11É1
  - Metal$inashq vo metallartn termiki emali

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Kompozit materiallar, məmulatlar və konstruksiyalar | 44 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Əlvan və nadir metalların metallurgiyası | None | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Metallurji proseslərin və materialların fiziki-kimyəvi tədqiqat üsulları | None | 40 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Naxçıvan Dövlət Universiteti | Fiziki kimya | None | 45 |
| Sumqayıt Dövlət Universiteti | Fiziki kimya | 47 | 45 |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Azərbaycan Texniki Universiteti | Metalşünaslıq və metalların termiki emalı | 53.5 | 40 |

</details>

---

### Proqram № 6

#### Blok 1 (Minimal bal: `40`, Səhifə: 2)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050622` | Maşın mühəndisliyi |
| `050628` | Mexanika mühəndisliyi |
| `050610` | Enerji maşınqayırması mühəndisliyi |
| `050612` | Maşın mühəndisliyi |
| `050625` | Texnoloji avadanhqlar m ühondisliyi |
| `050630` | Mexanika mühəndisliyi |
| `050645` | Poliqrafiya mühəndisliyi |
| `050646` | Təkrar emal və bərpa texnologiyaları (sahələr üzrə) |
| `T 060200` | Maşınqayırmada kompüter texnologiyası |
| `T 060300` | Tökmə istehsalının texnologiyası |
| `T 060400` | Texnoloii avadanhqlann layihalandirilmösi Vö istismarı |
| `T 060500` | Maşın və aparat hissələrinin bərpası və möhkəmliyinin artırılması texnologiyasl Vö avadanlığı |
| `T 060700` | Texnoloii komplekslarin |
| `T 060800` | Hidravlik maynlar, hidrointiqallar hidropnevmoavtomatika |
| `T 110100` | Texnoloji ma'lnlar və avadanhqlar (sahələr üzrə) |
| `T 110200` | Poliqrafiya masmlan Vö komplekslari |
| `T 110300` | Qaldmcl nəqliyyat və avadanhqlan |
| `T 110400` | Kimya müəssisələrinin avtomatlaşdırılmış istehsalatları |
| `TT 100100` | Maşınların möhkəmliyi və dinamikası |
| `TT 180100` | Tribotexnika |
| `200100` | Maddi istehsal vasitələrinin renovasiyası (sahələr üzrə) |
| `TT 230100` | Mexanikləşdirmə və avtomatlaşdırma (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Neft-modon mayn vo avadanhqlan
  - Neft-kimya masrn Vö avadanhqlan
  - Texnoloji mayn vo avadanlaqlann istehsall, tamiri vo texniki xidmöt
  - texnologiyalarr
  - Poliqrafiya masrnlan
- ** `7006027` Mexanika mühəndisliyi**
  - Hidromexanika vo hidravlik
  - Maye vo qazlarm noqli avadanhqlan
  - Maynlann möhkomliy•i vo dinamikasl
  - Neft-modon texnikasuun dinamikast vo möhkomliyi
  - Qaldmo-noqliyyat, tikinti, yol maStn vo avadanhqlan
  - Tribologiya Vö tribotexnika
  - Liftlor va eskalatorlar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-kimya maşın və avadanlıqları | 40.5 | 40 |
| Bakı Musiqi Akademiyası | Musiqi texnologiyaları | 50 | 48 |
| Azərbaycan Texniki Universiteti | Poliqrafiya maşınları | 46 | 40 |
| Azərbaycan Texniki Universiteti | Hidromexanika və hidravlik maşınlar | None | 40 |
| Bakı Mühəndislik Universiteti | Hidromexanika və hidravlik maşınlar | 43 | 40 |
| Azərbaycan Texniki Universiteti | Maye və qazların nəqli avadanlıqları | 42.5 | 40 |
| Bakı Mühəndislik Universiteti | Maye və qazların nəqli avadanlıqları | 50 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Maşınların möhkəmliyi və dinamikası | 46 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-mədən texnikasının dinamikası və möhkəmliyi | 42.5 | 40 |
| Azərbaycan Texniki Universiteti | Qaldırıcı-nəqliyyat, tikinti, yol maşın və avadanlıqları | None | 40 |
| Bakı Mühəndislik Universiteti | Tribologiya və tribotexnika | None | 40 |
| Azərbaycan Texniki Universiteti | Liftlər və eskalatorlar | None | 40 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 2)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050622` | Maşın mühəndisliyi |
| `050628` | Mexanika mühəndisliyi |
| `050610` | Enerji maşınqayırması mühəndisliyi |
| `050612` | Maşın mühəndisliyi |
| `050625` | Texnoloji avadanhqlar m ühondisliyi |
| `050630` | Mexanika mühəndisliyi |
| `050645` | Poliqrafiya mühəndisliyi |
| `050646` | Təkrar emal və bərpa texnologiyaları (sahələr üzrə) |
| `T 060200` | Maşınqayırmada kompüter texnologiyası |
| `T 060300` | Tökmə istehsalının texnologiyası |
| `T 060400` | Texnoloii avadanhqlann layihalandirilmösi Vö istismarı |
| `T 060500` | Maşın və aparat hissələrinin bərpası və möhkəmliyinin artırılması texnologiyasl Vö avadanlığı |
| `T 060700` | Texnoloii komplekslarin |
| `T 060800` | Hidravlik maynlar, hidrointiqallar hidropnevmoavtomatika |
| `T 110100` | Texnoloji ma'lnlar və avadanhqlar (sahələr üzrə) |
| `T 110200` | Poliqrafiya masmlan Vö komplekslari |
| `T 110300` | Qaldmcl nəqliyyat və avadanhqlan |
| `T 110400` | Kimya müəssisələrinin avtomatlaşdırılmış istehsalatları |
| `TT 100100` | Maşınların möhkəmliyi və dinamikası |
| `TT 180100` | Tribotexnika |
| `200100` | Maddi istehsal vasitələrinin renovasiyası (sahələr üzrə) |
| `TT 230100` | Mexanikləşdirmə və avtomatlaşdırma (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006002` Aqromühəndislik**
  - Aqrar istehsal proseslarinin mexaniklasdirilmasi
  - Aqrar istehsalatda texniki tochizatm taskili va planla#drrtlmasl
  - A ar istehsahn va texnol
  - arin tahlükasizl•

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsal proseslərinin mexanikləşdirilməsi (tədris Azərbaycan dilində) | 44.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsalatda texniki təchizatın təşkili və planlaşdırılması (tədris Azərbaycan dilində) | 42.5 | 40 |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050632` | Nəqliyyat mühəndisliyi |
| `050622` | Yerüstü nəqliyyat vasitolarinin mühəndisliyi |
| `050623` | Nəqliyyatda daşımalarının və idarəetmənin təşkili mühəndisliyi (dəmiryol nəqliyyatı üzrə) |
| `T 100100` | Avtomobil və traktorlar |
| `T 100200` | Nəqliyyat vasitələrinin texniki istismarı |
| `T 100600` | Yol hərəkətinin təşkili |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (avtomobil nəqliyyatı üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006002` Aqromühəndislik**
  - Aqrar istehsal proseslarinin mexaniklö$dirilmosi
  - Aqrar istehsalatda texniki tochizatm taskili vo planlasdtnlmasr
  - A rar istehsalm va texnol •i roseslarin tahlükasizli

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsal proseslərinin mexanikləşdirilməsi (tədris Azərbaycan dilində) | 44.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsalatda texniki təchizatın təşkili və planlaşdırılması (tədris Azərbaycan dilində) | 42.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsalın və texnoloji proseslərin təhlükəsizliyi (tədris Azərbaycan dilində) | 51 | 40 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 4)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050636` | Radiotexnika və telekommunikasiya mühəndisliyi |
| `050624` | Cihazqayrma mühəndisliyi |
| `050627` | Elektronika, telekommunikasiya və radiotexnika mühəndisliyi |
| `T 130100` | Cihazqaprma |
| `T 130200` | Keyfiyyata nazarat və diaqnostika iisul və cihazlan |
| `T 130300` | Aviasiya cihazlan və ölçmə-hesablama komplekslari |
| `T 130900` | Kompüterli informasiya- ölçmə texnikası və texnologiyast |
| `T 131000` | Aerokosmik monitorinq |
| `T 131100` | Gömrük idxal-ixrac nazaratinin cihaz və sistemlari |
| `T 140100` | Elektron texnikasmm materiallan və komponentlari |
| `T 140200` | Elektron cihaz və qurğuları |
| `T 140300` | Sanaye elektronikasl |
| `T 140400` | Mikroelektronika və yanmkeqirici cihazlan |
| `T 140600` | Fiziki qurğuların elektronikasl və avtomatikast |
| `T 140800` | Introskopiyamn fiziki iisul və cihazlan |
| `T 350100` | Elektron hesablaytct vasitalarin konstruksiya edilmasi və texnologiyasl |
| `T 150100` | Radiotexnika |
| `T 150200` | Radiorabitö, radioverili'lari və televiziya |
| `T 150300` | Nəqliyyat radioavadanhqlannm texniki |
| `T 150400` | Mai'öt radioelektron aparatlan |
| `T 150500` | Radioelektron sistemlari |
| `T 150600` | Radioelektron mübariza vasitalari |
| `T 160100` | Rabita qovpqlan və kommutasiya sistemlari |
| `T 160200` | Elektron və post rabitosi |
| `T 160300` | Coxkanalll telekommunikasiya sistemlari |
| `T 160400` | Sabakalar, rabita sistemlari və informasiyanm paylanmast |
| `T 160500` | Hərəkətedon obyekti Olan rabita vasital |
| `T 160700` | Telekommunikasiya sistemlarinin informasiya təhlükəsizliyi |
| `T 290100` | Maipt radioelektron aparatlanna servis xidmati |
| `T 290200` | Məişət maşın və cihazlarının layihələndirilməsi və servis xidməti |
| `T 350200` | Radioelektronika vasitələrinin konstruksiyw, edilmasi və texnologiyas |
| `IT 150100` | Optik rabitə fizikası texnikası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqayrrma texnologiyast
  - K fi ata nazarat va dia nostika sistemlari sahalar iizra

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050624` | Cihazqayrrma mühəndisliyi |
| `050647` | Metrologiya, standartlaşdırma və sertifikasiya mühəndisliyi |
| `050648` | Biotibbi texnologiya mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqaytrma texnologiyast
  - Keyfiyyato nozarot vo diaqnostika sistemlori (saholor iizra)
  - Metrologiya va metroloji torninat

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050647` | Metrologiya, standartlaşdırma və sertifikasiya mühəndisliyi |
| `T 310100` | Standartla'drrma və sertifikasiya (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Metrologiya vo metroloji taminat
  - oto nazarot vo dia nostika sistemlari
  - saholor üzro

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050648` | Biotibbi texnologiya mühəndisliyi |
| `T 290300` | Biotexniki və tibbi aparat və sistemlarin qura#hnlmasr, texniki istismarı və servis xidmati |
| `T 360100` | Biotexniki və tibbi aparatlar və sistemlar |
| `T 360200` | Bioloii-tibbi praktikada mühəndis i'i |
| `T 360300` | Tibbi informasiya sistemləri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqaytrma texnologiyast
  - K fi oto nozarot Vö dia nostika sistemlari (saholor üzra)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050103` | Optotexnika mühəndisliyi |
| `XTB 050002` | Optotexnika |
| `XTB 050102` | Optotexnika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqaytrma texnologiyast
  - Ke Ota nazarot di nostika sistemlori üzrö)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |

</details>

---

#### Blok 9 (Minimal bal: `30`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050602` | Aqromühəndislik |
| `050706` | Aqromühəndislik |
| `AT 060100` | Aqrar istehsalatın texnologiyası |
| `AT 060200` | Aqrar istehsalatın mexanikiləşdirilməsi |
| `AT 060300` | Aqrar istehsalatın elektrikiləşdirilməsi və avtomatlaşdırılması |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006002` Aqromühəndislik**
  - Aqrar istehsal proseslorinin mexaniklö#dirilmosi
  - Aqrar istehsalatda texniki tochizahn tö*ili vo planlasdtrtlmast
  - Aqrar istehsahn va texnoloji proseslarin tohlükasizliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsal proseslərinin mexanikləşdirilməsi (tədris Azərbaycan dilində) | 44.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsalatda texniki təchizatın təşkili və planlaşdırılması (tədris Azərbaycan dilində) | 42.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsalın və texnoloji proseslərin təhlükəsizliyi (tədris Azərbaycan dilində) | 51 | 40 |

</details>

---

### Proqram № 7

#### Blok 1 (Minimal bal: `40`, Səhifə: 2)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Gəmiqayırma və gəmi təmiri mühəndisliyi |
| `050618` | Gəmiqayırma və gəmi təmiri mühəndisliyi |
| `T 080100` | Gəmiqaytrma və gəmi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006013` Gəmiqayırma və gəmi təmiri mühəndisliyi**
  - Gomiqaynrma
  - Gami tomiri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmiqayırma | 48.5 | 48.5 |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmi təmiri | 45.5 | 45.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050609` | Gəmi energetik qurğularının istismarı mühəndisliyi |
| `050619` | Gəmi energetik qurğularımn istismarı m iihandisliyi |
| `T 080200` | Gəmi energetik qurğuları Vö onlarm istismarı |
| `T 081300` | Gəmi ma'ln və mexanizmlari |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006008` Elektrik və elektronika mühəndisliyi**
  - Gamilarin elektrik tochizah sistemlari
  - Elektrik tachizatl (sahalar üzra)
- ** `7006012` Gəmi energetik qurğularının istismarı mühəndisliyi**
  - Gami energetik qurgularl va onlarm istisman

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmilərin elektrik təchizatı sistemləri | 50.5 | 50.5 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Sumqayıt Dövlət Universiteti | Elektrik təchizatı (sahələr üzrə) | 44 | 40 |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmi energetik qurğuları və onların istismarı | 46.5 | 40 |

</details>

---

### Proqram № 8

#### Blok 1 (Minimal bal: `40`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050632` | Nəqliyyat mühəndisliyi |
| `050621` | Dəmiryol nəqliyyatı və təsərrüfatı mühəndisliyi |
| `050623` | Nəqliyyatda daşımalarının və idarəetmənin təşkili mühəndisliyi (dəmiryol nəqliyyatı üzrə) |
| `T 090100` | Damir yolu və təsərrüfatı, onun istismarı |
| `T 090200` | Lokomotiv və vaqon təsərrüfatı |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (dəmiryol nəqliyyatı üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006035` Nəqliyyat mühəndisliyi**
  - Lokomotiv vo vaqon tosorrüfah
  - Damiryolu tasarrüfatl vo onun istisman
  - Yol-n li at hadisolörinin eks rtizasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Lokomotiv və vaqon təsərrüfatı | None | 40 |
| Azərbaycan Texniki Universiteti | Dəmiryolu təsərrüfatı və onun istismarı | 54.5 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Dəmiryolu təsərrüfatı və onun istismarı | None | 40 |
| Azərbaycan Texniki Universiteti | Yol-nəqliyyat hadisələrinin ekspertizası | None | 40 |

</details>

---

### Proqram № 9

#### Blok 1 (Minimal bal: `40`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050632` | Nəqliyyat mühəndisliyi |
| `050622` | Yerüstü nəqliyyat vasitolarinin mühəndisliyi |
| `050623` | Nəqliyyatda daşımalarının və idarəetmənin təşkili mühəndisliyi (dəmiryol nəqliyyatı üzrə) |
| `T 100100` | Avtomobil və traktorlar |
| `T 100200` | Nəqliyyat vasitələrinin texniki istismarı |
| `T 100600` | Yol hərəkətinin təşkili |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (avtomobil nəqliyyatı üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006035` Nəqliyyat mühəndisliyi**
  - Elektrik va hibrid noqliyyat vasitölori
  - Avtomobil texnikasl vo istisman
  - Yol harakotinin to*ili vo tohlükosizliyi
  - Noqliyyat omaliyyatlarrnm intellektual idaro edilmosi
  - Yol-n li at hadisalorinin eks rtizasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Elektrik və hibrid nəqliyyat vasitələri | 43.5 | 40 |
| Azərbaycan Texniki Universiteti | Avtomobil texnikası və istismarı | None | 40 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Naxçıvan Dövlət Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 58.5 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Yol hərəkətinin təşkili və təhlükəsizliyi | 51.5 | 40 |
| Mingəçevir Dövlət Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat əməliyyatlarının intellektual idarə edilməsi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Yol-nəqliyyat hadisələrinin ekspertizası | None | 40 |

</details>

---

### Proqram № 10

#### Blok 1 (Minimal bal: `40`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050632` | Nəqliyyat mühəndisliyi |
| `050621` | Dəmiryol nəqliyyatı və təsərrüfatı mühəndisliyi |
| `050623` | Nəqliyyatda daşımalarının və idarəetmənin təşkili mühəndisliyi (dəmiryol nəqliyyatı üzrə) |
| `T 090100` | Damir yolu və təsərrüfatı, onun istismarı |
| `T 090200` | Lokomotiv və vaqon təsərrüfatı |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (dəmiryol nəqliyyatı üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006024` Logistika və nəqliyyat texnologiyaları mühəndisliyi**
  - Noqliyyatda da9malar va menecment (naqliyyat növlari üzra)
  - Noqliyyat logistikasl
  - Beynolxalq daymalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Bakı Mühəndislik Universiteti | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 55.5 | 51.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 57 | 44.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Nəqliyyat logistikası | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyat logistikası | 55.5 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nəqliyyat logistikası | 56 | 56 |
| Milli Aviasiya Akademiyası | Nəqliyyat logistikası | 62 | 62 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası | None | 44 |
| Azərbaycan Texniki Universiteti | Beynəlxalq daşımalar | 61 | 61 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050632` | Nəqliyyat mühəndisliyi |
| `050622` | Yerüstü nəqliyyat vasitolarinin mühəndisliyi |
| `050623` | Nəqliyyatda daşımalarının və idarəetmənin təşkili mühəndisliyi (dəmiryol nəqliyyatı üzrə) |
| `T 100100` | Avtomobil və traktorlar |
| `T 100200` | Nəqliyyat vasitələrinin texniki istismarı |
| `T 100600` | Yol hərəkətinin təşkili |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (avtomobil nəqliyyatı üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006024` Logistika və nəqliyyat texnologiyaları mühəndisliyi**
  - Naqliyyatda dastmalar va menecment (naqliyyat növlari üzra)
  - Naqliyyat logistikasl
  - Sahar naqliyyat pbakasi vo naqliyyat xidmatinin ta*ili
  - Noqliyyat xidmatlori üqün böhran va risklarin idara edilmosi
  - B ölxal d lmalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Bakı Mühəndislik Universiteti | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 55.5 | 51.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 57 | 44.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Nəqliyyat logistikası | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyat logistikası | 55.5 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nəqliyyat logistikası | 56 | 56 |
| Milli Aviasiya Akademiyası | Nəqliyyat logistikası | 62 | 62 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası | None | 44 |
| Azərbaycan Texniki Universiteti | Şəhər nəqliyyat şəbəkəsi və nəqliyyat xidmətinin təşkili | 59 | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | None | 44 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050613` | Hava nəqliyyatının hərəkətinin təşkili |
| `050613` | Avianəqliyyat istehsalatının təşkili mühəndisliyi |
| `050658` | Logistika və nəqliyyat texnologiyaları mühəndisliyi |
| `T 072400` | Avianəqliyyat istehsalatının təşkili |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (hava nəqliyyatı üzrə) |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (su nəqliyyatı üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006024` Logistika və nəqliyyat texnologiyaları mühəndisliyi**
  - Noqliyyatda dasrmalar va menecment (noqliyyat növlori üzrö)
  - N oqliyyat logistikasr
  - Noqliyyat xidmötlari üqün böhran Vö risklorin idara edilmosi
  - Be alxal d unalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Bakı Mühəndislik Universiteti | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 55.5 | 51.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 57 | 44.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Nəqliyyat logistikası | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyat logistikası | 55.5 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nəqliyyat logistikası | 56 | 56 |
| Milli Aviasiya Akademiyası | Nəqliyyat logistikası | 62 | 62 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası | None | 44 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | None | 44 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050402` | Biznesin idarə edilməsi |
| `050407` | Marketinq |
| `050408` | Menecment |
| `050638` | Sanaye mühəndisliyi |
| `050638` | (B040S Sanayenin təşkili idara olunmasl |
| `050407` | Menecment |
| `050408` | Marketinq |
| `050409` | Biznesin idarə edilməsi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006024` Logistika və nəqliyyat texnologiyaları mühəndisliyi**
  - Naqliyyatda dasrmalar Vö menecment (naqliyyat növlari üzra)
  - Naqliyyat logistikasl
  - Sohor noqliyyat 9bokasi vo noqliyyat xidmotinin to*ili
  - Noqliyyat xidmatlari iiqiin böhran vo risklorin idara edilmosi
  - Beynalxalq da#lmalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Bakı Mühəndislik Universiteti | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 55.5 | 51.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 57 | 44.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Nəqliyyat logistikası | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyat logistikası | 55.5 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nəqliyyat logistikası | 56 | 56 |
| Milli Aviasiya Akademiyası | Nəqliyyat logistikası | 62 | 62 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası | None | 44 |
| Azərbaycan Texniki Universiteti | Şəhər nəqliyyat şəbəkəsi və nəqliyyat xidmətinin təşkili | 59 | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | None | 44 |
| Azərbaycan Texniki Universiteti | Beynəlxalq daşımalar | 61 | 61 |

</details>

---

### Proqram № 11

#### Blok 1 (Minimal bal: `40`, Səhifə: 4)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050636` | Radiotexnika və telekommunikasiya mühəndisliyi |
| `050624` | Cihazqayrma mühəndisliyi |
| `050627` | Elektronika, telekommunikasiya və radiotexnika mühəndisliyi |
| `T 130100` | Cihazqaprma |
| `T 130200` | Keyfiyyata nazarat və diaqnostika iisul və cihazlan |
| `T 130300` | Aviasiya cihazlan və ölçmə-hesablama komplekslari |
| `T 130900` | Kompüterli informasiya- ölçmə texnikası və texnologiyast |
| `T 131000` | Aerokosmik monitorinq |
| `T 131100` | Gömrük idxal-ixrac nazaratinin cihaz və sistemlari |
| `T 140100` | Elektron texnikasmm materiallan və komponentlari |
| `T 140200` | Elektron cihaz və qurğuları |
| `T 140300` | Sanaye elektronikasl |
| `T 140400` | Mikroelektronika və yanmkeqirici cihazlan |
| `T 140600` | Fiziki qurğuların elektronikasl və avtomatikast |
| `T 140800` | Introskopiyamn fiziki iisul və cihazlan |
| `T 350100` | Elektron hesablaytct vasitalarin konstruksiya edilmasi və texnologiyasl |
| `T 150100` | Radiotexnika |
| `T 150200` | Radiorabitö, radioverili'lari və televiziya |
| `T 150300` | Nəqliyyat radioavadanhqlannm texniki |
| `T 150400` | Mai'öt radioelektron aparatlan |
| `T 150500` | Radioelektron sistemlari |
| `T 150600` | Radioelektron mübariza vasitalari |
| `T 160100` | Rabita qovpqlan və kommutasiya sistemlari |
| `T 160200` | Elektron və post rabitosi |
| `T 160300` | Coxkanalll telekommunikasiya sistemlari |
| `T 160400` | Sabakalar, rabita sistemlari və informasiyanm paylanmast |
| `T 160500` | Hərəkətedon obyekti Olan rabita vasital |
| `T 160700` | Telekommunikasiya sistemlarinin informasiya təhlükəsizliyi |
| `T 290100` | Maipt radioelektron aparatlanna servis xidmati |
| `T 290200` | Məişət maşın və cihazlarının layihələndirilməsi və servis xidməti |
| `T 350200` | Radioelektronika vasitələrinin konstruksiyw, edilmasi və texnologiyas |
| `IT 150100` | Optik rabitə fizikası texnikası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqaynrma texnologiyast
  - Optik-elektron cihazlar va sistemlar
  - Metrologiya va metroloji taminat
  - intellektual öl€mo va idaroetmo sistemlari cihazlan
  - Keyfiyyota nozarat vo diaqnostika sistemlori (saholar üzra)
  - Biotexniki va tibbi aparatlar va sistemlar
  - Aerokosmik cihazlar va informasiya-ölqma sistemlari
- ** `7006039` Radiotexnika və telekommunikasiya mühəndisliyi**
  - Radiorabita, radioverilislar vo televiziya
  - Radiotexnika
  - Rabito qovsaqlan vo kommutasiya sistemlari
  - Coxkanalll telekommunikasiya sistemlari
  - Sabakalar, rabito sistemlari va informasiyamn paylanmast
  - Optik rabito texnologiyalan
  - Aerokosmik telekommunikasiya sistemlari
  - Aviasiya radioelektron avadanhqlan
  - Mobil rabito sistemlari

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Milli Aviasiya Akademiyası | Optik-elektron cihazlar və sistemlər | 59.5 | 59.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| Azərbaycan Texniki Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 51 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Milli Aviasiya Akademiyası | Aerokosmik cihazlar və informasiya- ölçmə sistemləri | 54.5 | 54.5 |
| Milli Aviasiya Akademiyası | Aerokosmik informasiya sistemləri | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Radiorabitə, radioverilişlər və televiziya | 49 | 49 |
| Azərbaycan Texniki Universiteti | Radiotexnika | 50 | 50 |
| *... və daha 11 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050624` | Cihazqayrrma mühəndisliyi |
| `050647` | Metrologiya, standartlaşdırma və sertifikasiya mühəndisliyi |
| `050648` | Biotibbi texnologiya mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqayrrma texnologiyast
  - Optik-elektron cihazlar va sistemlar
  - Metrologiya Vö metroloji taminat
  - intellektual öl€mo vo idaroetmo sistemlari cihazlan
  - Keyfiyyato nazarat vo diaqnostika sistemlari (sahalor üzro)
  - Biotexniki vo tibbi aparatlar va sistemlar
  - Aerokosmik cihazlar vo informasi a-ölcma sistemlari

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Milli Aviasiya Akademiyası | Optik-elektron cihazlar və sistemlər | 59.5 | 59.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| Azərbaycan Texniki Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 51 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Milli Aviasiya Akademiyası | Aerokosmik cihazlar və informasiya- ölçmə sistemləri | 54.5 | 54.5 |
| Milli Aviasiya Akademiyası | Aerokosmik informasiya sistemləri | 63.5 | 63.5 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `050634` | Proseslarin avtomatlasdtnlmast mühəndisliyi |
| `050628` | Proseslarin avtomatla'drnlmas |
| `050628` | Mühəndisliyi |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `T 090300` | Dəmiryol nəqliyyatmda avtomatika, telemexanika və rabita |
| `T 170100` | Texniki sistemlordo idaraetma və informatika |
| `T 170200` | Texnoloji proseslarin və istehsalatların avtomatla'drnlmasr (sahələr üzrə) |
| `T 170300` | Robotlar və robototexniki sistemlar |
| `T 170400` | Energetika sistemlarinin avtomatik idara edilmasi |
| `T 170900` | Ususlara avtomatla'dtnlnus nazarat sistemlarinin istismarı |
| `T 171000` | Avtomatlaşdırılmış sistemlərin informasiya təhlükəsizliyinin kompleks təminatı |
| `T 180700` | Avtomatla'drrma və informasiya texnikası (Tempus proqranu) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqaytrma texnologiyasr
  - Optik-elektron cihazlar va sistemlar
  - Metrologiya va metroloji taminat
  - intellektual öl€ma va sistemlari cihazlan
  - Keyfiyyata nazarat vo diaqnostika sistemlari (sahalar üzra)
  - Biotexniki vo tibbi aparatlar vo sistemlar
  - Aerokosmik cihazlar vo informasiya-öl€rno sistemlari
- ** `7006039` Radiotexnika və telekommunikasiya mühəndisliyi**
  - Radiorabita, radioverili}lor televiziya
  - Radiotexnika
  - Rabito qovsaqlan va kommutasiya sistemlari
  - Coxkanalli telekommunikasiya sistemlari
  - Sobokolor, rabito sistemlori vo informasiyanm paylanmast
  - Optik rabitö texnologiyalan
  - Aerokosmik telekommunikasiya sistemlori
  - Aviasiya radioelektron avadanhqlan
  - Mobil rabita sistemlari

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Milli Aviasiya Akademiyası | Optik-elektron cihazlar və sistemlər | 59.5 | 59.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| Azərbaycan Texniki Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 51 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Milli Aviasiya Akademiyası | Aerokosmik cihazlar və informasiya- ölçmə sistemləri | 54.5 | 54.5 |
| Milli Aviasiya Akademiyası | Aerokosmik informasiya sistemləri | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Radiorabitə, radioverilişlər və televiziya | 49 | 49 |
| Azərbaycan Texniki Universiteti | Radiotexnika | 50 | 50 |
| Azərbaycan Texniki Universiteti | Rabitə qovşaqları və kommutasiya sistemləri | 52 | 52 |
| *... və daha 11 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050647` | Metrologiya, standartlaşdırma və sertifikasiya mühəndisliyi |
| `T 310100` | Standartla'drrma və sertifikasiya (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Metrologiya vo metroloji törninat
  - K fi Ota nozarot vo di nostika sistemlari
  - saholor üzro

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050648` | Biotibbi texnologiya mühəndisliyi |
| `T 290300` | Biotexniki və tibbi aparat və sistemlarin qura#hnlmasr, texniki istismarı və servis xidmati |
| `T 360100` | Biotexniki və tibbi aparatlar və sistemlar |
| `T 360200` | Bioloii-tibbi praktikada mühəndis i'i |
| `T 360300` | Tibbi informasiya sistemləri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Cihazqayurma texnologiyast
  - Optik-elektron cihazlar va sistemlar
  - Metrologiya vo metroloji taminat
  - intellektual ölqmo vo idaraetmo sistemlori cihazlan
  - Keyfiyyatö nazarat Vö diaqnostika sistemlori (saholar üzra)
  - Biotexniki va tibbi aparatlar vo sistemlor
  - Aerokosmik cihazlar vo informasiya-ölcmo sistemlori
- ** `7006039` Radiotexnika və telekommunikasiya mühəndisliyi**
  - Radiorabita, radioverilislor va televiziya
  - Radiotexnika
  - Rabito qov#aqlan va kommutasiya sistemlari
  - Coxkanalh telekommunikasiya sistemlari
  - Sobokolor, rabito sistemlori vo informasiyanm paylanrnasl
  - Optik rabito texnologiyalan
  - Aerokosmik telekommunikasiya sistemlari
  - Aviasiya radioelektron avadanbqlan
  - Mobil rabito sistemlori

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Milli Aviasiya Akademiyası | Optik-elektron cihazlar və sistemlər | 59.5 | 59.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| Azərbaycan Texniki Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 51 | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Milli Aviasiya Akademiyası | Aerokosmik cihazlar və informasiya- ölçmə sistemləri | 54.5 | 54.5 |
| Milli Aviasiya Akademiyası | Aerokosmik informasiya sistemləri | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Radiorabitə, radioverilişlər və televiziya | 49 | 49 |
| Azərbaycan Texniki Universiteti | Radiotexnika | 50 | 50 |
| *... və daha 11 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050614` | Aviasiya texnikası avadanltqlanmn istismarı mühəndisliyi |
| `T 070300` | Ugan aparatlann və onlann müharriklarinin texniki istismarı |
| `T 071000` | Aviasiya elektrosistemlarinin və pilotaj- naviqasiya komplekslarinin texniki istismarı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Optik-elektron cihazlar vo sistemlor
  - Aerokosmik cihazlar Vö informasiya-ölqrna sistemlari

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Optik-elektron cihazlar və sistemlər | 59.5 | 59.5 |
| Milli Aviasiya Akademiyası | Aerokosmik cihazlar və informasiya- ölçmə sistemləri | 54.5 | 54.5 |
| Milli Aviasiya Akademiyası | Aerokosmik informasiya sistemləri | 63.5 | 63.5 |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050601` | Aerokosmik mühəndislik |
| `050652` | Kosmik texnologiyalar mühəndisliyi |
| `050653` | Kosmik texnika mühəndisliyi |
| `050654` | Kosmik idaraetmo sistemləri mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006004` Çap mühəndisliyi**
  - Aerokosmik cihazlar vo informasiya-ölqmo sistemlari
  - Optik-elektron cihazlar vo sistemlar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Aerokosmik cihazlar və informasiya- ölçmə sistemləri | 54.5 | 54.5 |
| Milli Aviasiya Akademiyası | Aerokosmik informasiya sistemləri | 63.5 | 63.5 |
| Milli Aviasiya Akademiyası | Optik-elektron cihazlar və sistemlər | 59.5 | 59.5 |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050102` | Harbi rabita vasitolari mühəndisliyi |
| `XTB 050004` | Coxkanalll radiorele və troposfer rabitasinin yerüstü aparatlanmn hazrrlanmasr, istismarı və təmiri |
| `XTB 050104` | Coxkanalh radiorele və troposfer rabitasinin yerüstü aparatlanmn haztrlanmasi, istismarı və təmiri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006039` Radiotexnika və telekommunikasiya mühəndisliyi**
  - Radiorabito, vo televiziya
  - Radiotexnika
  - Rabito qovsaqlan va kommutasiya sistemlori
  - Coxkanalh telekommunikasiya sistemlari
  - Sabakalar, rabito sistemlori vo informasiyanm paylanmast
  - Optik rabito texnologiyalan
  - Aerokosmik telekommunikasiya sistemlari
  - AViasiYa radioelektron avadanbqlan
  - Mobil rabito sistemlari

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Radiotexnika | 50 | 50 |
| Azərbaycan Texniki Universiteti | Rabitə qovşaqları və kommutasiya sistemləri | 52 | 52 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Rabitə qovşaqları və kommutasiya sistemləri | None | 40 |
| Azərbaycan Texniki Universiteti | Çoxkanalh telekommunikasiya sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Texniki Universiteti | Şəbəkələr, rabitə sistemləri və informasiyanın paylanması | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Şəbəkələr, rabitə sistemləri və informasiyanın paylanması | 52.5 | 52.5 |
| Azərbaycan Texniki Universiteti | Optik rabitə texnologiyaları | 55 | 55 |
| Milli Aviasiya Akademiyası | Aerokosmik telekommunikasiyaasistemləri | 52 | 52 |
| Milli Aviasiya Akademiyası | Aerokosmik informasiya sistemləri | 63.5 | 63.5 |
| Milli Aviasiya Akademiyası | Aviasiya radioelektron avadanlıqları | 52 | 52 |
| Bakı Mühəndislik Universiteti | Mobil rabitə sistemləri | 48.5 | 48.5 |

</details>

---

### Proqram № 13

#### Blok 1 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `050634` | Proseslarin avtomatlasdtnlmast mühəndisliyi |
| `050628` | Proseslarin avtomatla'drnlmas |
| `050628` | Mühəndisliyi |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `T 090300` | Dəmiryol nəqliyyatmda avtomatika, telemexanika və rabita |
| `T 170100` | Texniki sistemlordo idaraetma və informatika |
| `T 170200` | Texnoloji proseslarin və istehsalatların avtomatla'drnlmasr (sahələr üzrə) |
| `T 170300` | Robotlar və robototexniki sistemlar |
| `T 170400` | Energetika sistemlarinin avtomatik idara edilmasi |
| `T 170900` | Ususlara avtomatla'dtnlnus nazarat sistemlarinin istismarı |
| `T 171000` | Avtomatlaşdırılmış sistemlərin informasiya təhlükəsizliyinin kompleks təminatı |
| `T 180700` | Avtomatla'drrma və informasiya texnikası (Tempus proqranu) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006038` Proseslərin avtomatlaşdırılması mühəndisliyi**
  - Texniki sistemlordö idaraetma
  - Texnoloji proseslorin avtomatlasdrnlmasl va idaro edilmasi (sahalar
  - üzra)
  - Mexatronika
  - Robotlar vo robototexniki sistemlor

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texniki sistemlərdə idarəetmə | 52.5 | 40 |
| Azərbaycan Texniki Universiteti | Texniki sistemlərdə idarəetmə | 59 | 59 |
| Bakı Mühəndislik Universiteti | Texniki sistemlərdə idarəetmə | None | 40 |
| Azərbaycan Texniki Universiteti | Mexatronika | 63 | 63 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Robotlar və robototexniki sistemlər | 62.5 | 62.5 |
| Azərbaycan Texniki Universiteti | Robotlar və robototexniki sistemlər | 64 | 64 |
| Azərbaycan Texniki Universiteti | Robotlar və robototexniki sistemlər İngilis dilində | 68 | 68 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050509` | Kompüter elmləri |
| `050615` | Informasiya tohlükosizliyi |
| `050616` | Informasiya texnologiyaları Kompüter mühəndisliyi |
| `050509` | Kompüter elmləri |
| `050631` | Kompüter mühəndisliyi |
| `050632` | İnformasiya texnologiyaları və sistemləri mühəndisliyi |
| `050655` | İnformasiya texnologiyaları |
| `050656` | Sistem mühəndisliyi |
| `T 180100` | Hesablama ma'tnlan, komplekslari, sistemlari və pbokolari |
| `T 180200` | Avtomatlaşdırılmış layihələndirmə sistemləri (sahələr üzrə) |
| `T 180300` | İnformasiya işlənməsinin və idarəetmənin sistemləri |
| `T 180500` | Malumatlann mühafizasinin texnologiyast və təşkili |
| `T 180600` | Kompüter təhlükəsizliyi |
| `160100` | İnformasiya sistemləri (tətbiq sahələri üzrə) |
| `TE 100100` | Tatbiqi riyaziyyat |
| `TE 100200` | Informatika |
| `XTB 50106` | Informasiya təhlükəsizliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006028` Mexatronika və robototexnika mühəndisliyi**
  - Mexatronika
  - Robotlar va robototexniki sistemlar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Mexatronika | 63 | 63 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Robotlar və robototexniki sistemlər | 62.5 | 62.5 |
| Azərbaycan Texniki Universiteti | Robotlar və robototexniki sistemlər | 64 | 64 |
| Azərbaycan Texniki Universiteti | Robotlar və robototexniki sistemlər İngilis dilində | 68 | 68 |

</details>

---

### Proqram № 14

#### Blok 1 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `050634` | Proseslarin avtomatlasdtnlmast mühəndisliyi |
| `050628` | Proseslarin avtomatla'drnlmas |
| `050628` | Mühəndisliyi |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `T 090300` | Dəmiryol nəqliyyatmda avtomatika, telemexanika və rabita |
| `T 170100` | Texniki sistemlordo idaraetma və informatika |
| `T 170200` | Texnoloji proseslarin və istehsalatların avtomatla'drnlmasr (sahələr üzrə) |
| `T 170300` | Robotlar və robototexniki sistemlar |
| `T 170400` | Energetika sistemlarinin avtomatik idara edilmasi |
| `T 170900` | Ususlara avtomatla'dtnlnus nazarat sistemlarinin istismarı |
| `T 171000` | Avtomatlaşdırılmış sistemlərin informasiya təhlükəsizliyinin kompleks təminatı |
| `T 180700` | Avtomatla'drrma və informasiya texnikası (Tempus proqranu) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006022` Kompüter mühəndisliyi**
  - Dinamiki arxitekturah multiprosessor sistem vo pbakalari
  - Kompüter sisternlori va sobakölori
  - Biliklorin alda edilmosi sistemlori
  - Kompüter texnikasrntn layihalondirilmasi texnologiyast
  - Bulud va pbokö infrastrukturlan
  - Daxilo qura#hnlnus sistemlar
  - Kompüter görmosi vo obrazlann tarunmast
- ** `7006016` İnformasiya texnologiyaları**
  - idaroetmodo informasiya sistemlari
  - informasiya i#lonmosinin vo idaraetmonin avtomatla#lrnlnus
  - sistemlori
  - Aerokosmik informasiya sistemlari
  - Telekommunikasiya sistemlorinda informasiya texnologiyalan
  - iqtisadiyyatda intellektual texnologiyalar
  - Roqamsal transformasiya
  - Logistikada informasiya texnologiyalan
  - Ma911
  - masi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Kooperasiya Universiteti | Dinamiki arxitekturalı multiprosessor sistem və şəbəkələri (tədris Azərbaycan dilində) | 59 | 59 |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası | 65 | 65 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası Türk dilində | 64 | 64 |
| Azərbaycan Texniki Universiteti | Bulud və şəbəkə infrastrukturları | 69 | 69 |
| Bakı Mühəndislik Universiteti | Bulud və şəbəkə infrastrukturları | 62 | 62 |
| Milli Aviasiya Akademiyası | Kompüter görməsi və obrazların tanınması | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 68.5 | 68.5 |
| Azərbaycan Texniki Universiteti | İdarəetmədə informasiya sistemləri | 72 | 72 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmədə informasiya sistemləri | 78 | 78 |
| Bakı Mühəndislik Universiteti | İdarəetmədə informasiya sistemləri | 63 | 63 |
| Naxçıvan Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 61.5 | 61.5 |
| Sumqayıt Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 61.5 | 61.5 |
| Lənkəran Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 52 | 52 |
| *... və daha 18 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050509` | Kompüter elmləri |
| `050615` | Informasiya tohlükosizliyi |
| `050616` | Informasiya texnologiyaları Kompüter mühəndisliyi |
| `050509` | Kompüter elmləri |
| `050631` | Kompüter mühəndisliyi |
| `050632` | İnformasiya texnologiyaları və sistemləri mühəndisliyi |
| `050655` | İnformasiya texnologiyaları |
| `050656` | Sistem mühəndisliyi |
| `T 180100` | Hesablama ma'tnlan, komplekslari, sistemlari və pbokolari |
| `T 180200` | Avtomatlaşdırılmış layihələndirmə sistemləri (sahələr üzrə) |
| `T 180300` | İnformasiya işlənməsinin və idarəetmənin sistemləri |
| `T 180500` | Malumatlann mühafizasinin texnologiyast və təşkili |
| `T 180600` | Kompüter təhlükəsizliyi |
| `160100` | İnformasiya sistemləri (tətbiq sahələri üzrə) |
| `TE 100100` | Tatbiqi riyaziyyat |
| `TE 100200` | Informatika |
| `XTB 50106` | Informasiya təhlükəsizliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006022` Kompüter mühəndisliyi**
  - Dinamiki arxitekturah multiprosessor sistem va pbakölori
  - Kompüter sistemlori vo pbakölori
  - Biliklarin aldo edilmasi sistemlori
  - Kompüter texnikasnun layihölondirilmasi texnologiyasl
  - Bulud pbökö infrastrukturlarl
  - Daxila qurasdrrllmli sistemlar
  - Kompüter görmosi va obrazlann tamnmasl
- ** `7006016` İnformasiya texnologiyaları**
  - idaraetmoda informasiya sistemlari
  - Informasiya islonmosinin vo idaroetmanin
  - sistemlori
  - Aerokosmik informasiya sistemlori
  - Telekommunikasiya sistemlorindo informasiya texnologiyalan
  - iqtisadiyyatda intellektual texnologiyalar
  - Roqomsal transformasiya
  - Logistikada informasiya texnologiyalart
  - öyranmosi
  - iqtisadiyyatda intellektual texnologiyalar
- ** `7006017` İnformasiya təhlükəsizliyi**
  - informasiya mühafizasi va töhlükasizliyi
  - Kibertohlükasizlik
  - Kompüter Vö Söbökö töhlükasizliyi
  - informasiya sistemlarinin tahlükasizliyi (sahalar üzra)
  - idaroetmo sistemlarinin proqram torninatrrun tohlükosizliyi
  - Tötbiqi kriptoqrafiya
  - Telekommunikasiya sistemlarinin informasiya töhlükosizliyi
  - Sonaye idaroetmo sistemlarinin töhlükasizliyi
- ** `7006005` Data elmləri**
  - Verilanlarin tahlili

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Kooperasiya Universiteti | Dinamiki arxitekturalı multiprosessor sistem və şəbəkələri (tədris Azərbaycan dilində) | 59 | 59 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Kompüter sistemləri və şəbəkələri | 64.5 | 64.5 |
| Azərbaycan Texniki Universiteti | Kompüter sistemləri və şəbəkələri | 67 | 67 |
| Bakı Mühəndislik Universiteti | Kompüter sistemləri və şəbəkələri | 64.5 | 64.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Kompüter sistemləri və şəbəkələri | 51 | 51 |
| Sumqayıt Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 61.5 | 61.5 |
| Lənkəran Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 52 | 52 |
| “Azərbaycan” Universiteti | Kompüter sistemləri və şəbəkələri | 62 | 62 |
| Qərbi Kaspi Universiteti | Kompüter sistemləri və şəbəkələri | 62 | 62 |
| “Odlar Yurdu” Universiteti | Kompüter sistemləri və şəbəkələri | 60.5 | 60.5 |
| Azərbaycan Kooperasiya Universiteti | Kompüter sistemləri və şəbəkələri (tədris Azərbaycan dilində) | 60.5 | 60.5 |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası | 65 | 65 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası Türk dilində | 64 | 64 |
| *... və daha 52 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050509` | Kompüter elmləri |
| `050615` | Informasiya tohlükosizliyi |
| `050616` | Informasiya texnologiyaları Kompüter mühəndisliyi |
| `050509` | Kompüter elmləri |
| `050631` | Kompüter mühəndisliyi |
| `050632` | İnformasiya texnologiyaları və sistemləri mühəndisliyi |
| `050655` | İnformasiya texnologiyaları |
| `050656` | Sistem mühəndisliyi |
| `T 180100` | Hesablama ma'tnlan, komplekslari, sistemlari və pbokolari |
| `T 180200` | Avtomatlaşdırılmış layihələndirmə sistemləri (sahələr üzrə) |
| `T 180300` | İnformasiya işlənməsinin və idarəetmənin sistemləri |
| `T 180500` | Malumatlann mühafizasinin texnologiyast və təşkili |
| `T 180600` | Kompüter təhlükəsizliyi |
| `160100` | İnformasiya sistemləri (tətbiq sahələri üzrə) |
| `TE 100100` | Tatbiqi riyaziyyat |
| `TE 100200` | Informatika |
| `XTB 50106` | Informasiya təhlükəsizliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005009` Kompüter elmləri**
  - intellektual sistemlor
  - Kompüter mode110#iirmasi
  - Riyazi modellö#dirmo
  - Tatbiqi riyaziyyat
  - iqtisadiyyatda optimal idaroetmanin riyazi üsullarl
  - Kompüter riyaziyyatl
  - Raqamsal dövlöt
  - Süni intellekt
  - Yüksok mohsuldarhqll hesablama sistemlori
  - Os alarm interneti va kiberfiziki sistemlar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | İntellektual sistemlər | 70.5 | 70.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İntellektual sistemlər | 73.5 | 73.5 |
| Gəncə Dövlət Universiteti | İntellektual sistemlər | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi | 65.5 | 65.5 |
| Naxçıvan Dövlət Universiteti | Kompüter modelləşdirməsi | 55 | 55 |
| Gəncə Dövlət Universiteti | Kompüter modelləşdirməsi | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Riyazi modelləşdirmə | 64 | 64 |
| Azərbaycan Texniki Universiteti | Riyazi modelləşdirmə | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Tətbiqi riyaziyyat | 66 | 66 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tətbiqi riyaziyyat | 63.5 | 63.5 |
| Bakı Dövlət Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 67 | 67 |
| Azərbaycan Texniki Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 64 | 64 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 73 | 73 |
| Azərbaycan Respublikası Prezidenti yanında Dövlət İdarəçilik Akademiyası | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 73 | 73 |
| Azərbaycan Texniki Universiteti | Kompüter riyaziyyatı | 65 | 65 |
| *... və daha 11 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `TT 210100` | Kompüter riyaziyyati |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006022` Kompüter mühəndisliyi**
  - Dinamiki arxitekturall multiprosessor sistem vo
  - Kompüter sistemlori va pbakölori
  - Biliklorin oldo edilmasi sistemlari
  - Kompüter texnikasrmn layiholondirilmosi texnologiyast
  - Bulud va 9baka infrastrukturlan
  - Daxilo sistemlar
  - Kompüter görmosi Vö obrazlann tarunmast
- ** `7006016` İnformasiya texnologiyaları**
  - idaraetmada informasiya sistemlori
  - informasiya islanmosinin va idaroetmanin avtomatlasdtnlrms
  - sistemlori
  - Aerokosmik informasiya sistemlari
  - Telekommunikasiya sistemlorindo informasiya texnologiyalan
  - iqtisadiyyatda intellektual texnologiyalar
  - Roqamsal transformasiya
  - Logistikada informasiya texnologiyalan
  - Ma'tn öyronmasi
- ** `7006005` Data elmləri**
  - Verilanlarin tohlili

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Kooperasiya Universiteti | Dinamiki arxitekturalı multiprosessor sistem və şəbəkələri (tədris Azərbaycan dilində) | 59 | 59 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Kompüter sistemləri və şəbəkələri | 64.5 | 64.5 |
| Azərbaycan Texniki Universiteti | Kompüter sistemləri və şəbəkələri | 67 | 67 |
| Bakı Mühəndislik Universiteti | Kompüter sistemləri və şəbəkələri | 64.5 | 64.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Kompüter sistemləri və şəbəkələri | 51 | 51 |
| Sumqayıt Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 61.5 | 61.5 |
| Lənkəran Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 52 | 52 |
| “Azərbaycan” Universiteti | Kompüter sistemləri və şəbəkələri | 62 | 62 |
| Qərbi Kaspi Universiteti | Kompüter sistemləri və şəbəkələri | 62 | 62 |
| “Odlar Yurdu” Universiteti | Kompüter sistemləri və şəbəkələri | 60.5 | 60.5 |
| Azərbaycan Kooperasiya Universiteti | Kompüter sistemləri və şəbəkələri (tədris Azərbaycan dilində) | 60.5 | 60.5 |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası | 65 | 65 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası Türk dilində | 64 | 64 |
| *... və daha 32 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `45`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `TT 210100` | Kompüter riyaziyyati |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005009` Kompüter elmləri**
  - intellektual sistemlar
  - Kompüter modellasdirmasi
  - Riyazi mode110#lirmo
  - Tatbiqi riyaziyyat
  - iqtisadiyyatda optimal idaroetmonin riyazi üsullan
  - Kompüter riyaziyyatl
  - Raqamsal dövlöt
  - Siini intellekt
  - Yüksok mahsuldarhqll hesablama sistemlari
  - O+'alarm interneti va kiberfiziki sistemlor

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | İntellektual sistemlər | 70.5 | 70.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İntellektual sistemlər | 73.5 | 73.5 |
| Gəncə Dövlət Universiteti | İntellektual sistemlər | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi | 65.5 | 65.5 |
| Naxçıvan Dövlət Universiteti | Kompüter modelləşdirməsi | 55 | 55 |
| Gəncə Dövlət Universiteti | Kompüter modelləşdirməsi | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Tətbiqi riyaziyyat | 66 | 66 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tətbiqi riyaziyyat | 63.5 | 63.5 |
| Bakı Dövlət Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 67 | 67 |
| Azərbaycan Texniki Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 64 | 64 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 73 | 73 |
| Azərbaycan Respublikası Prezidenti yanında Dövlət İdarəçilik Akademiyası | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 73 | 73 |
| Azərbaycan Texniki Universiteti | Kompüter riyaziyyatı | 65 | 65 |
| Azərbaycan Texniki Universiteti | Rəqəmsal dövlət | 71 | 71 |
| Azərbaycan Respublikası Prezidenti yanında Dövlət İdarəçilik Akademiyası | Rəqəmsal dövlət | 77 | 77 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 15

#### Blok 1 (Minimal bal: `40`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050626` | Memarhq |
| `050637` | Şəhərsalma |
| `050633` | Memarhq |
| `050659` | Şəhərsalma |
| `T 190100` | Memarhq |
| `T 190200` | Memarhq mühitinin dizaynl |
| `T 190300` | Memarhq abidalörinin barpasr Vö yenidan qurulmasr |
| `T 190400` | Bag-park və landsaft quruculugu |
| `T 190500` | Aharsalma |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006030` Memarlıq**
  - Bina va qurgulann memarhÉ1
  - Memarhq mühitinin dizayru
  - Landsaft memar11É1
  - Memarhq abidalarinin mühafizasi va barpasl
- ** `7006041` Şəhərsalma**
  - Sahar planlasdmlmasl
  - Dayamqll Pharsalma vo regionlann planla#irrrlmasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq mühitinin dizaynı | 43.5 | 43.5 |
| Bakı Mühəndislik Universiteti | Memarlıq mühitinin dizaynı | 49 | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Landşaft memarlığı | 40 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası | 46 | 40 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Memarlıq abidələrinin mühafizəsi və bərpası | 51.5 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 55.5 | 55.5 |
| Naxçıvan Dövlət Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 58 | 58 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050710` | Yerquruluşu və daşınmaz əmlakın kadastrı |
| `050705` | Yer, torpaq və şəhər kadastrı |
| `AT 050100` | Yer quruluşu və torpaq müfəttişliyi |
| `AT 050200` | Torpaq kadastrı |
| `AT 050300` | Şəhər kadastrı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006041` Şəhərsalma**
  - Sohor planlasdtrtlmast
  - Dayaruqh saharsalma Vö regionlann planla#irnlrnast

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Şəhər planlaşdırılması | 51 | 51 |
| Bakı Mühəndislik Universiteti | Şəhər planlaşdırılması | 45 | 40 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050402` | Biznesin idarə edilməsi |
| `050403` | Davamlı inkişafın idarə edilməsi |
| `050404` | Dövlət və bələdiyyə idarəetməsi |
| `050405` | Iqtisadiyyat |
| `05041B` | Menecment |
| `050617` | Inpat mühəndisliyi |
| `050637` | Şəhərsalma |
| `050404` | Iqtisadiyyat |
| `0504 IO` | Dövlət və bələdiyyə idarəetməsi |
| `050710` | Yerquruluşu və daşınmaz əmlakın kadastrı |
| `050407` | Menecment |
| `050409` | Biznesin idarə edilməsi |
| `050412` | Davamlı inkişafın idarə edilməsi |
| `050634` | Intaat mühəndisliyi |
| `050659` | Şəhərsalma |
| `T 190100` | Memarl' |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006041` Şəhərsalma**
  - Sohar planlasdmlmasa
  - Dayaruqll Pharsalma Vö regionlartn planlasdlrllmasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 55.5 | 55.5 |
| Naxçıvan Dövlət Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 58 | 58 |

</details>

---

### Proqram № 16

#### Blok 1 (Minimal bal: `40`, Səhifə: 1)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050607` | Neft-qaz qurğuları mühəndisliyi |
| `T 020600` | Qaz və neft kəmər və anbarlarının layihələndirilməsi, tikintisi və istismarı |
| `T 020800` | Daniz neft-qaz qurğuları |
| `T 370100` | Doniz neft-qaz hidrotexniki qurgularmm tikintisi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006018` İnşaat mühəndisliyi**
  - Bina va qurgulann tikintisinin töikili Vö texnologiyasl
  - Qurgular nazariyyasi
  - Doniz hidrotexniki qurgulann tikintisi
  - Osaslar va özüllar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Bina və qurğuların tikintisinin təşkili və texnologiyası | 56.5 | 56.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Dəniz hidrotexniki qurğuların tikintisi | 53.5 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Əsaslar və özüllər | 53.5 | 47.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050617` | Insaat mühəndisliyi |
| `050625` | Meliorasiya mühəndisliyi |
| `050634` | Insaat mühəndisliyi |
| `050637` | Meliorasiya və su təsərrüfatı tikintisi mühəndisliyi |
| `T 200100` | Sanaye və mülki tikinti |
| `T 200200` | Hidrotexniki tikinti |
| `T 200300` | Sahar bölödiyyo tikintisi və təsərrüfatı |
| `T 200400` | Meliorasiya mühəndis sistemlərinin tikintisi |
| `050619` | Kommunikasiya sistemlari mühəndisliyi |
| `050635` | Mühəndis sistemlərinin və qurğularınrn tikintisi mühəndisliyi |
| `T 210100` | İstilik-qaz təchizatı və ventilyasiya |
| `T 210200` | Su təchizatı və suayırma |
| `T 210300` | Xiisusi mühəndis sistemləri və qurğularınm tikintisi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006018` İnşaat mühəndisliyi**
  - Sonaye Vö mülki tikinti
  - Dasmmaz ornlakrn ekspertizasl
  - Bina va qurgulann tikintisinin ta*ili va texnologiyasl
  - Qurgular nazoriyyosi
  - Doniz hidrotexniki qurgularrn tikintisi
  - Osaslar va özüllor
- ** `7006021` Kommunikasiya sistemləri mühəndisliyi**
  - Sahar infrastrukturunda agrlll texnologiyalar
  - Su tochizah vo su tomizlomo texnologiyalart
  - Bina vo qurgulartn mikroiqlimini tamin edan sistemlor
- ** `7006029` Meliorasiya mühəndisliyi**
  - Meliorasiya sistemlari
  - Hidrotexniki qurgular
  - Suvarma sistemlari
- ** `7006038` Proseslərin avtomatlaşdırılması mühəndisliyi**
  - Texniki sistemlorda idaroetma
  - Texnoloji proseslorin avtomatla#dlnlmasl vo idaro edilmosi (sahölor
  - üzra)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Sənaye və mülki tikinti | 60.5 | 60.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Daşınmaz əmlakın ekspertizası | 55.5 | 55.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Bina və qurğuların tikintisinin təşkili və texnologiyası | 56.5 | 56.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Dəniz hidrotexniki qurğuların tikintisi | 53.5 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Hidrotexniki qurğular | 52 | 52 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Əsaslar və özüllər | 53.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Şəhər infrastrukturunda ağıllı texnologiyalar | None | 44.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su təchizatı və su təmizləmə texnologiyaları | None | 43 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Bina və qurğuların mikroiqlimini təmin edən sistemlər | None | 44.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya sistemləri | 52 | 52 |
| Naxçıvan Dövlət Universiteti | Meliorasiya sistemləri | 49 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Meliorasiya sistemləri (tədris Azərbaycan dilində) | 40 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Hidrotexniki qurğular | 52 | 52 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Dəniz hidrotexniki qurğuların tikintisi | 53.5 | 40 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050617` | Insaat mühəndisliyi |
| `050625` | Meliorasiya mühəndisliyi |
| `050634` | Insaat mühəndisliyi |
| `050637` | Meliorasiya və su təsərrüfatı tikintisi mühəndisliyi |
| `T 200100` | Sanaye və mülki tikinti |
| `T 200200` | Hidrotexniki tikinti |
| `T 200300` | Sahar bölödiyyo tikintisi və təsərrüfatı |
| `T 200400` | Meliorasiya mühəndis sistemlərinin tikintisi |
| `050619` | Kommunikasiya sistemlari mühəndisliyi |
| `050635` | Mühəndis sistemlərinin və qurğularınrn tikintisi mühəndisliyi |
| `T 210100` | İstilik-qaz təchizatı və ventilyasiya |
| `T 210200` | Su təchizatı və suayırma |
| `T 210300` | Xiisusi mühəndis sistemləri və qurğularınm tikintisi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006040` Sənaye mühəndisliyi**
  - materiallarl sanayesi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnşaat materialları sənayesi | 56 | 56 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050633` | Nəqliyyat tikintisi mühəndisliyi |
| `050636` | Nəqliyyat tikintisi mühəndisliyi |
| `T 220100` | Damir yolu tikintisi və tasarrüfati |
| `T 220200` | Avtomobil yollarr və aerodromlarm tikintisi |
| `T 220300` | Körpülor Vö nəqliyyat tunellarinin tikintisi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006036` Nəqliyyat tikintisi mühəndisliyi**
  - Avtomobil yollarl vo aerodromlar
  - Körpülor va naqliyyat qurgulan

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Avtomobil yolları və aerodromlar | 40 | 40 |
| Bakı Mühəndislik Universiteti | Avtomobil yolları və aerodromlar | None | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Körpülər və nəqliyyat qurğuları | 44 | 40 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050623` | Materiallar mühəndisliyi |
| `050638` | Tikinti materiallan Vö mamulatlanmn texnologiyasr mühəndisliyi |
| `050639` | Mea materiallanmn və agac emalmm texnologiyasr mühəndisliyi |
| `T 230100` | Tikinti materiallart, mamulatlan və konstruksiyalan is tehsall |
| `T 230400` | Catinariyan qeyri-metal və silikat materiallar texnologiyasr |
| `T 260300` | Agac email texnologiyasl |
| `T 281400` | Gini-saxsl və mamulatlarr texnologiyasr |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006026` Materiallar mühəndisliyi**
  - iryaat materialsiinas11É1

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnşaat materialşünaslığı | 52.5 | 52.5 |
| Bakı Dövlət Universiteti | Radiasiya materialşünaslığı | 58.5 | 58.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnşaat materialları sənayesi | 56 | 56 |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050623` | Materiallar mühəndisliyi |
| `050601` | Materialşünaslıq mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006026` Materiallar mühəndisliyi**
  - insaat materialsünasll*l

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnşaat materialşünaslığı | 52.5 | 52.5 |

</details>

---

### Proqram № 17

#### Blok 1 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050612` | Geomatika və geodeziya mühəndisliyi |
| `050640` | Geodeziya Vö xaritogilik mühəndisliyi |
| `T 240100` | Tatbiqi geodeziya |
| `T 240400` | Xaritoölik |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006011` Geomatika və geodeziya mühəndisliyi**
  - Totbiqi geodeziya
  - Geoma tika
  - Kartoqrafiya vo geoinformatika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tətbiqi geodeziya | 47 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tətbiqi geodeziya | 44 | 40 |
| Bakı Dövlət Universiteti | Geomatika | 44 | 40 |
| Bakı Dövlət Universiteti | Kartoqrafiya və geoinformatika | 53 | 53 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050612` | Geomatika və geodeziya mühəndisliyi |
| `050640` | Geodeziya Vö xaritogilik mühəndisliyi |
| `T 240100` | Tatbiqi geodeziya |
| `T 240400` | Xaritoölik |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7007009` Yerquruluşu və daşınmaz əmlakın kadastrı**
  - Yerqurulusu landsaft planlasdlrllmasl
  - Da'lnrnaz amlakrn kadastrt vo reyestri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Yerquruluşu və landşaft planlaşdırılması | 43.5 | 43.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Yerquruluşu və landşaft planlaşdırılması (tədris Azərbaycan dilində) | 37.5 | 37.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Daşınmaz əmlakın kadastrı və reyestri | 41.5 | 41.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Daşınmaz əmlakın kadastrı və reyestri (tədris Azərbaycan dilində) | 38 | 38 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050710` | Yerquruluşu və daşınmaz əmlakın kadastrı |
| `050705` | Yer, torpaq və şəhər kadastrı |
| `AT 050100` | Yer quruluşu və torpaq müfəttişliyi |
| `AT 050200` | Torpaq kadastrı |
| `AT 050300` | Şəhər kadastrı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006011` Geomatika və geodeziya mühəndisliyi**
  - Tatbiqi geodeziya
  - Geoma tika
  - Kartoqrafiya vo geoinformatika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tətbiqi geodeziya | 47 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tətbiqi geodeziya | 44 | 40 |
| Bakı Dövlət Universiteti | Geomatika | 44 | 40 |
| Bakı Dövlət Universiteti | Kartoqrafiya və geoinformatika | 53 | 53 |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050710` | Yerquruluşu və daşınmaz əmlakın kadastrı |
| `050705` | Yer, torpaq və şəhər kadastrı |
| `AT 050100` | Yer quruluşu və torpaq müfəttişliyi |
| `AT 050200` | Torpaq kadastrı |
| `AT 050300` | Şəhər kadastrı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7007009` Yerquruluşu və daşınmaz əmlakın kadastrı**
  - Yerqurultiiu vo landsaft planlasdtnlmasl
  - Da9nmaz amlakm kadastrr va reyestri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Yerquruluşu və landşaft planlaşdırılması | 43.5 | 43.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Yerquruluşu və landşaft planlaşdırılması (tədris Azərbaycan dilində) | 37.5 | 37.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Daşınmaz əmlakın kadastrı və reyestri | 41.5 | 41.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Daşınmaz əmlakın kadastrı və reyestri (tədris Azərbaycan dilində) | 38 | 38 |

</details>

---

### Proqram № 18

#### Blok 1 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050618` | Kimya |
| `050641` | Kimya mühəndisliyi |
| `T 250100` | Üzvi maddalorin kimyovi texnologiyasr |
| `T 250200` | Qeyri-üzvi maddolorin kimyavi texnologiyasl |
| `T 250300` | Elektrokimyavi istehsal texnologiyast |
| `T 250400` | Neft-qaz və alternativ enerji texnologiyasr |
| `T 250500` | Yüksakmolekullu birl"malarin kimyavi texnologiyasr |
| `T 250600` | Plastik kütla və elastomerlarin kimyovi texnologiyasr |
| `T 251700` | Kimyavi istehsalatların |
| `T 251700` | Sas proseslari və kimyavi kibernetikasr |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006020` Kimya mühəndisliyi**
  - Neft-kimya sintezinin texnologiyasl
  - Osas üzvi sintezin kimyast vo texnologiyast
  - Qeyri-üzvi maddalarin istehsal texnologiyast
  - Neft email texnologiyast
  - Karbohidrogen qazlann emall texnologiyasl
  - Polimerlarin kimyavi texnologiyasl
  - Kimya texnologiyasnun proses va aparatlan
  - Neft vo qaz texnologiyasr
  - Kimya mühondisliyinda y•a91 texnologiyalar
  - Polimer osasll kom ozit materiallarrn email texnolo i asl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-kimya sintezinin texnologiyası | 57.5 | 40 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| Sumqayıt Dövlət Universiteti | Neft kimyası | 51 | 51 |
| Bakı Mühəndislik Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | 59 | 54.5 |
| Sumqayıt Dövlət Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qeyri-üzvi maddələrin istehsal texnologiyası | 55.5 | 53.5 |
| Bakı Dövlət Universiteti | Neft emalı texnologiyası | 66.5 | 66.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft emalı texnologiyası | 68.5 | 68.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Karbohidrogen qazların emalı texnologiyası | 56 | 56 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Polimerlərin kimyəvi texnologiyası | 56.5 | 40 |
| Sumqayıt Dövlət Universiteti | Polimerlərin kimyəvi texnologiyası | 64 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Kimya texnologiyasının proses və aparatları | 61 | 61 |
| Bakı Dövlət Universiteti | Neft emalı texnologiyası | 66.5 | 66.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft emalı texnologiyası | 68.5 | 68.5 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar | 57.5 | 57.5 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 19

#### Blok 1 (Minimal bal: `40`, Səhifə: 4)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050636` | Radiotexnika və telekommunikasiya mühəndisliyi |
| `050624` | Cihazqayrma mühəndisliyi |
| `050627` | Elektronika, telekommunikasiya və radiotexnika mühəndisliyi |
| `T 130100` | Cihazqaprma |
| `T 130200` | Keyfiyyata nazarat və diaqnostika iisul və cihazlan |
| `T 130300` | Aviasiya cihazlan və ölçmə-hesablama komplekslari |
| `T 130900` | Kompüterli informasiya- ölçmə texnikası və texnologiyast |
| `T 131000` | Aerokosmik monitorinq |
| `T 131100` | Gömrük idxal-ixrac nazaratinin cihaz və sistemlari |
| `T 140100` | Elektron texnikasmm materiallan və komponentlari |
| `T 140200` | Elektron cihaz və qurğuları |
| `T 140300` | Sanaye elektronikasl |
| `T 140400` | Mikroelektronika və yanmkeqirici cihazlan |
| `T 140600` | Fiziki qurğuların elektronikasl və avtomatikast |
| `T 140800` | Introskopiyamn fiziki iisul və cihazlan |
| `T 350100` | Elektron hesablaytct vasitalarin konstruksiya edilmasi və texnologiyasl |
| `T 150100` | Radiotexnika |
| `T 150200` | Radiorabitö, radioverili'lari və televiziya |
| `T 150300` | Nəqliyyat radioavadanhqlannm texniki |
| `T 150400` | Mai'öt radioelektron aparatlan |
| `T 150500` | Radioelektron sistemlari |
| `T 150600` | Radioelektron mübariza vasitalari |
| `T 160100` | Rabita qovpqlan və kommutasiya sistemlari |
| `T 160200` | Elektron və post rabitosi |
| `T 160300` | Coxkanalll telekommunikasiya sistemlari |
| `T 160400` | Sabakalar, rabita sistemlari və informasiyanm paylanmast |
| `T 160500` | Hərəkətedon obyekti Olan rabita vasital |
| `T 160700` | Telekommunikasiya sistemlarinin informasiya təhlükəsizliyi |
| `T 290100` | Maipt radioelektron aparatlanna servis xidmati |
| `T 290200` | Məişət maşın və cihazlarının layihələndirilməsi və servis xidməti |
| `T 350200` | Radioelektronika vasitələrinin konstruksiyw, edilmasi və texnologiyas |
| `IT 150100` | Optik rabitə fizikası texnikası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006007` Ekologiya mühəndisliyi**
  - Aerokosmik monitorinq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050618` | Kimya |
| `050641` | Kimya mühəndisliyi |
| `T 250100` | Üzvi maddalorin kimyovi texnologiyasr |
| `T 250200` | Qeyri-üzvi maddolorin kimyavi texnologiyasl |
| `T 250300` | Elektrokimyavi istehsal texnologiyast |
| `T 250400` | Neft-qaz və alternativ enerji texnologiyasr |
| `T 250500` | Yüksakmolekullu birl"malarin kimyavi texnologiyasr |
| `T 250600` | Plastik kütla və elastomerlarin kimyovi texnologiyasr |
| `T 251700` | Kimyavi istehsalatların |
| `T 251700` | Sas proseslari və kimyavi kibernetikasr |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006007` Ekologiya mühəndisliyi**
  - Otraf mühitin mühafizasi vo tobii ehtiyatlardan samaroli istifada Olunrnasi
  - Otraf mühit va neft sanayesi
  - Tullantllann emal texnologiyalart (sahölor üzra)
  - Otraf mühitin idara olunmast
  - Sana eda ekol •i texnol i alar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 59.5 | 41.5 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| *... və daha 6 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050618` | Kimya |
| `050641` | Kimya mühəndisliyi |
| `T 250100` | Üzvi maddalorin kimyovi texnologiyasr |
| `T 250200` | Qeyri-üzvi maddolorin kimyavi texnologiyasl |
| `T 250300` | Elektrokimyavi istehsal texnologiyast |
| `T 250400` | Neft-qaz və alternativ enerji texnologiyasr |
| `T 250500` | Yüksakmolekullu birl"malarin kimyavi texnologiyasr |
| `T 250600` | Plastik kütla və elastomerlarin kimyovi texnologiyasr |
| `T 251700` | Kimyavi istehsalatların |
| `T 251700` | Sas proseslari və kimyavi kibernetikasr |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005004` Ekologiya**
  - Otraf mühitin mühafiza vo barpa metodlart
  - Ekoloji kimya
  - Ekol •i monitorin vo atraf mühitin modell
  - irilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 45 |
| Azərbaycan Tibb Universiteti | Toksikoloji kimya | 75.5 | 75.5 |
| Naxçıvan Dövlət Universiteti | Toksikoloji kimya | 47.5 | 40 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Azərbaycan Dövlət İqtisad Universiteti | Ekoloji monitorinq və ətraf mühitin modelləşdirilməsi | 65.5 | 65.5 |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Meşəçilik |
| `050708` | Meşəçilik |
| `T 260100` | Mep mühəndisliyi |
| `T 260200` | Mesa və mep-park təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7007007` Meşəçilik**
  - Mep priologiyast vo mühafizosi
  - Ümumi mep€ilik va me91arin idaro olunmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Lənkəran Dövlət Universiteti | Meşə priologiyası və mühafizəsi | None | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ümumi meşəçilik və meşələrin idarə olunması (tədris Azərbaycan dilində) | 41.5 | 41.5 |
| Lənkəran Dövlət Universiteti | Ümumi meşəçilik və meşələrin idarə olunması | 41 | 30 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Meşəçilik |
| `050708` | Meşəçilik |
| `T 260100` | Mep mühəndisliyi |
| `T 260200` | Mesa və mep-park təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006007` Ekologiya mühəndisliyi**
  - Meliorasiya, rekultivasiya vo torpaq mühafizosi
  - Otraf mühitin mühafizosi vo tobii ehtiyatlardan samaroli istifadö olunmasr
  - Su ehtiyatlanmn idara olunmasl Vö mühafizasi
  - Otraf mühitin idara olunmast
  - alar
  - Sana edo ekol •i texnol

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 59.5 | 41.5 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Su ehtiyatlarının idarə olunması və mühafizəsi | None | 40.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi İngilis dilində | 58.5 | 54 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `45`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Meşəçilik |
| `050708` | Meşəçilik |
| `T 260100` | Mep mühəndisliyi |
| `T 260200` | Mesa və mep-park təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005004` Ekologiya**
  - Otraf mühitin mühafiza vo barpa metodlart
  - Aqroekologiya
  - Biom üxtalifliyin qorunmasr
  - Bioekologiya
  - Ekolo'i monitorin va atraf mühitin

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Bakı Dövlət Universiteti | Antropologiya | 61 | 59 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050504` | Ekologiya |
| `050606` | Ekologiya mühəndisliyi |
| `050510` | Ekologiya |
| `050649` | Ekologiya mühəndisliyi |
| `ET 010100` | Ekologiya |
| `ET 010200` | Təbiətdən istifadə |
| `ET 010300` | Bioekologiya |
| `ET 010800` | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006007` Ekologiya mühəndisliyi**
  - Meliorasiya, rekultivasiya vo torpaq mühafizosi
  - Otraf mühitin mühafizasi vo tobii ehtiyatlardan samoroli istifado
  - olunmast
  - Otraf rnühit vo neft sanayesi
  - Aerokosmik monitorinq
  - Tullantllann emal texnologiyalan (saholor üzro)
  - Su ehtiyatlarlnln idara olunrnasl vo mühafizasi
  - Otraf mühitin idara olunmast
  - Sanayeda ekoloji texnologiyalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 59.5 | 41.5 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 59.5 | 46 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `45`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050504` | Ekologiya |
| `050606` | Ekologiya mühəndisliyi |
| `050510` | Ekologiya |
| `050649` | Ekologiya mühəndisliyi |
| `ET 010100` | Ekologiya |
| `ET 010200` | Təbiətdən istifadə |
| `ET 010300` | Bioekologiya |
| `ET 010800` | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005004` Ekologiya**
  - Otraf mühitin mühafizo vo borpa metodlan
  - Aqroekologiya
  - Biomüxtolifliyin qorunmasl
  - Bioekologiya
  - Ekoloji kimya
  - Ekoloji monitorinq vo atraf mühitin

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Bakı Dövlət Universiteti | Antropologiya | 61 | 59 |
| *... və daha 14 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `ET 010500` | Aqroekologiya |
| `ET 010600` | Meliorasiya və torpaq mühafizəsi |
| `ET 010700` | Su ehtiyatlarının mühafizəsi və kompleks istifadəsi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006007` Ekologiya mühəndisliyi**
  - Meliorasiya, rekultivasiya vo torpaq mühafiz.asi
  - Otraf mühitin mühafizosi vo tobii ehtiyatlardan somoroli istifado
  - olunmast
  - Aerokosmik monitorinq
  - Su ehtiyatlarrrun idara olunmast vo mühafizasi
  - Otraf mühitin idara olunmasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 59.5 | 41.5 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Su ehtiyatlarının idarə olunması və mühafizəsi | None | 40.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Ətraf mühitin idarə edilməsi | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin idarə edilməsi (tədris Azərbaycan dilində) | None | 45 |

</details>

---

#### Blok 10 (Minimal bal: `45`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `ET 010500` | Aqroekologiya |
| `ET 010600` | Meliorasiya və torpaq mühafizəsi |
| `ET 010700` | Su ehtiyatlarının mühafizəsi və kompleks istifadəsi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005004` Ekologiya**
  - Otraf mühitin mühafiza vo barpa metodlan
  - Aqroekologiya
  - Biomüxtalifliyin qorunmast
  - Bioekologiya
  - Ekoloji kimya
  - Ekoloji monitorinq vo atraf mühitin modellosdirilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Bakı Dövlət Universiteti | Antropologiya | 61 | 59 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 11 (Minimal bal: `40`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050701` | Aqronomluq |
| `050702` | Bağçılıq və tərəvəzçilik |
| `050705` | Bitki mühafizəsi |
| `050709` | Torpaqşünaslıq və aqrokimya |
| `050701` | Torpaqşünaslıq və aqrokimya |
| `050702` | Aqronomluq |
| `050710` | Bitki miihafizasi |
| `050711` | Bağçılıq və tərəvəzçilik |
| `AT 020100` | Aqronomluq |
| `AT 020200` | Meyvə-tərəvəzçilik və üzümçülük |
| `AT 020300` | Bitkilərin mühafizəsi |
| `AT 020400` | İpəkçilik |
| `AT 020500` | Aqrar təsərrüfat bitkilərinin seleksiyası və genetikası |
| `TE 080100` | Torpaq'iinashq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006007` Ekologiya mühəndisliyi**
  - Meliorasiya, rekultivasiya vo torpaq mühafizosi
  - Otraf miihitin mühafizosi Vö tobii ehtiyatlardan samaroli istifada
  - Aerokosmik monitorinq
  - Su ehtiyatlannm idara olunmast va mühafizasi
  - Otraf mühitin idaro olunmast

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 59.5 | 41.5 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Su ehtiyatlarının idarə olunması və mühafizəsi | None | 40.5 |

</details>

---

#### Blok 12 (Minimal bal: `45`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050701` | Aqronomluq |
| `050702` | Bağçılıq və tərəvəzçilik |
| `050705` | Bitki mühafizəsi |
| `050709` | Torpaqşünaslıq və aqrokimya |
| `050701` | Torpaqşünaslıq və aqrokimya |
| `050702` | Aqronomluq |
| `050710` | Bitki miihafizasi |
| `050711` | Bağçılıq və tərəvəzçilik |
| `AT 020100` | Aqronomluq |
| `AT 020200` | Meyvə-tərəvəzçilik və üzümçülük |
| `AT 020300` | Bitkilərin mühafizəsi |
| `AT 020400` | İpəkçilik |
| `AT 020500` | Aqrar təsərrüfat bitkilərinin seleksiyası və genetikası |
| `TE 080100` | Torpaq'iinashq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005004` Ekologiya**
  - Otraf mühitin mühafiza va barpa metodlan
  - Aqroekologiya
  - Biomüxtolifliyin qorunmast
  - Bioekologiya
  - Ekoloji monitorinq vo Otraf mühitin modella#lirilmosi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Bakı Dövlət Universiteti | Antropologiya | 61 | 59 |
| *... və daha 11 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 13 (Minimal bal: `45`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050703` | Balıqçılıq |
| `050707` | Bahq€iltq və bahq€lltq təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005004` Ekologiya**
  - Otraf mühitin mühafizo vo borpa metodlan
  - Aqroekologiya
  - Biomüxtalifliyin qorunmasl
  - Bioekologiya
  - Ekoloji kimya
  - Ekoloji monitorinq va atraf mühitin mode110#dirilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Bakı Dövlət Universiteti | Antropologiya | 61 | 59 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 14 (Minimal bal: `45`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050708` | Su bioehtiyatlan və akvakultura |
| `050709` | Su bioehtiyatları və akvabitkilər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005004` Ekologiya**
  - Otraf mühitin mühafiza va borpa metodlan
  - Aqroekologiya
  - Biomüxtolifliyin qorunmast
  - Bioekologiya
  - Ekoloji kimya
  - Ekoloji monitorinq vo •traf mühitin modellasdirilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Ətraf mühitin mühafizə və bərpa metodları (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Bakı Dövlət Universiteti | Antropologiya | 61 | 59 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 20

#### Blok 1 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050644` | Istehlak mallanmn ekspertizast və marketinqi |
| `T 320100` | Istehlak mallanmn keyfiyyat ekspertizast |
| `T 320200` | Orzaq mahsullanmn amtöö$ünasll |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006023` Qida mühəndisliyi**
  - Qida tohlükosizliyi vo risklorin idaro edilmosi
  - Qida istehsalltun idara edilmosi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 43.5 | 43.5 |
| Azərbaycan Turizm və Menecment Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 51.5 | 51.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Qida təhlükəsizliyi və risklərin idarə edilməsi | 51 | 51 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Qida təhlükəsizliyi və risklərin idarə edilməsi | 44 | 40 |
| Lənkəran Dövlət Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 40 | 40 |
| Azərbaycan Kooperasiya Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi (tədris Azərbaycan dilində) | 51 | 51 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Qida istehsalının idarə edilməsi | 42.5 | 42.5 |
| Lənkəran Dövlət Universiteti | Qida istehsalının idarə edilməsi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Qida istehsalının idarə edilməsi (tədris Azərbaycan dilində) | 50 | 50 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `ii 030400` | Gömrük ekspertizasi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006023` Qida mühəndisliyi**
  - Qida tahlükasizliyi va risklarin idaro edilmasi
  - Qida istehsahmn idaro edilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 43.5 | 43.5 |
| Azərbaycan Turizm və Menecment Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 51.5 | 51.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Qida təhlükəsizliyi və risklərin idarə edilməsi | 51 | 51 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Qida təhlükəsizliyi və risklərin idarə edilməsi | 44 | 40 |
| Lənkəran Dövlət Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 40 | 40 |
| Azərbaycan Kooperasiya Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi (tədris Azərbaycan dilində) | 51 | 51 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Qida istehsalının idarə edilməsi | 42.5 | 42.5 |
| Lənkəran Dövlət Universiteti | Qida istehsalının idarə edilməsi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Qida istehsalının idarə edilməsi (tədris Azərbaycan dilində) | 50 | 50 |

</details>

---

### Proqram № 22

#### Blok 1 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050809` | Turizm balodçuluğu |
| `050810` | Turizm işinin təşkili |
| `050810` | Turizm və hotelçilik |
| `T 300100` | Turizm və sosial mədəni servis xidmati |
| `T 300200` | Turist, sanatoriya-kurort komplekslarinin servis və tibb xidmatinin t0'kili |
| `T 300300` | Turist və sanatoriya-kurort komplekslarind. tabii və qeyri- ananavi vasital |
| `T 300300` | Rla "jsial-ba isi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7008004` Turizm və hotelçilik**
  - Beynolxalq turizm
  - Hotelqilik
  - Turizm i'i
  - Turizm vo sosial-modoni servis

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Beynəlxalq turizm | 57 | 57 |
| Azərbaycan Turizm və Menecment Universiteti | Beynəlxalq turizm | 52 | 45.5 |
| Gəncə Dövlət Universiteti | Beynəlxalq turizm | 54 | 44 |
| Qərbi Kaspi Universiteti | Beynəlxalq turizm | 51.5 | 44 |
| Azərbaycan Kooperasiya Universiteti | Beynəlxalq turizm (tədris Azərbaycan dilində) | 63 | 43 |
| Azərbaycan Turizm və Menecment Universiteti | Hotelçilik | 51.5 | 46 |
| Gəncə Dövlət Universiteti | Hotelçilik | None | 43 |
| Lənkəran Dövlət Universiteti | Hotelçilik | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Hotelçilik (tədris Azərbaycan dilində) | None | 41.5 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Turizm və sosial-mədəni servis | 53.5 | 44 |
| *... və daha 3 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050806` | Nəqliyyatda servis (nəqliyyat növləri üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7008004` Turizm və hotelçilik**
  - Beynolxalq turizm
  - Turizm i$
  - Turizm va sosial-madani servis

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Beynəlxalq turizm | 57 | 57 |
| Azərbaycan Turizm və Menecment Universiteti | Beynəlxalq turizm | 52 | 45.5 |
| Gəncə Dövlət Universiteti | Beynəlxalq turizm | 54 | 44 |
| Qərbi Kaspi Universiteti | Beynəlxalq turizm | 51.5 | 44 |
| Azərbaycan Kooperasiya Universiteti | Beynəlxalq turizm (tədris Azərbaycan dilində) | 63 | 43 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Turizm və sosial-mədəni servis | 53.5 | 44 |
| Naxçıvan Dövlət Universiteti | Turizm və sosial-mədəni servis | 57 | 42 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Turizm və sosial-mədəni servis | 54.5 | 40 |
| Lənkəran Dövlət Universiteti | Turizm və sosial-mədəni servis | 53 | 40 |

</details>

---

### Proqram № 23

#### Blok 1 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050624` | Cihazqayrrma mühəndisliyi |
| `050647` | Metrologiya, standartlaşdırma və sertifikasiya mühəndisliyi |
| `050648` | Biotibbi texnologiya mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Standartla$dtrrna vo sertifikatla#dtrma

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Standartlaşdırma və sertifikatlaşdırma | 53.5 | 53.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050635` | Qida mühəndisliyi |
| `050707` | Sarıbulaq |
| `050642` | Qida mahsullan mühəndisliyi |
| `T 270100` | Taxil və taxtl mahsullanmn saxlanmast və email texnologiyast |
| `T 270200` | Cörak, makaron, unlu qannadi mamulatlanmn və qi da konsentratlanmn texnologiyast |
| `T 270300` | Sakar və pkarli mahsullar texnologiyast |
| `T 270400` | Sarabgliq və qtcqtrma istehsalatlmn texnologiyast |
| `T 270500` | Subtropik və tamb mahsullar texnologiyast |
| `T 270700` | Konserv və qida konsentratlan texnologiyast |
| `T 270800` | Ot və at mahsullan texnologiyasl |
| `T 270900` | Balaq və bahq mahsullan texnologiyast |
| `T 271000` | Süd və Süd mahsullan texnologiyasl |
| `T 271100` | Mahsullan texnologiyasl |
| `T 271200` | Bitkisilik mahsullanmn saxlarulmast və emall texnologiyast |
| `T 271300` | Mep qida mahsullanrun və darman bitkilarinin saxlamlmasl. email texnologiyast və arntaa'iinasl |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Standartla#dlrma Vö sertifikatla#åjrma

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Standartlaşdırma və sertifikatlaşdırma | 53.5 | 53.5 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050643` | Coxi'l.non mallann texnologiyast mühəndisliyi |
| `T 280100` | Tabii liflarin istehsall texnologiyast və avadanhqlan |
| `T 280200` | Kimyavi liflar və onlann asastnda kompozisiya materiallan istehsalının texnologiyast və avadanhqlan |
| `T 280300` | Oyiricilik texnologiyast |
| `T 280400` | Toxuculuq texnologiyast |
| `T 280900` | Tiki* mamulatlannm konstruksiya edilmasi |
| `T 281100` | Gön-dari mamulatlanmn konstruksi a edilmasi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Standartlasdlrma va sertifikatla#irrma

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Standartlaşdırma və sertifikatlaşdırma | 53.5 | 53.5 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050647` | Metrologiya, standartlaşdırma və sertifikasiya mühəndisliyi |
| `T 310100` | Standartla'drrma və sertifikasiya (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Standartl Irma Vö sertifikatla Irma

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Standartlaşdırma və sertifikatlaşdırma | 53.5 | 53.5 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050644` | Istehlak mallanmn ekspertizast və marketinqi |
| `T 320100` | Istehlak mallanmn keyfiyyat ekspertizast |
| `T 320200` | Orzaq mahsullanmn amtöö$ünasll |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Standartlasdrrma vo sertifikatlasdrrma

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Standartlaşdırma və sertifikatlaşdırma | 53.5 | 53.5 |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050644` | Istehlak mallanmn ekspertizas |
| `050644` | Və marketinqi |
| `T 320100` | Istehlak mallanmn keyfiyyat ekspertizast |
| `T 320300` | Qeyri-arzaq mallanmn amtoo ünash |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006025` Maşın mühəndisliyi**
  - Standartla#ålrrna va sertifikatla*drrma

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Standartlaşdırma və sertifikatlaşdırma | 53.5 | 53.5 |

</details>

---

### Proqram № 24

#### Blok 1 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050614` | Həyat fəaliyyətinin təhlükəsizliyi mühəndisliyi |
| `050651` | Fövqəladə hallar və həyat fəaliyyətinin təhlükəsizliyi mühəndisliyi |
| `T 340100` | Hayat faaliyyotinin təhlükəsizliyi (in'aatda) |
| `T 340200` | Otraf mühitin mühəndis mühafizasi (sahələr üzrə) |
| `T 340300` | Otraf miihitin və radiasi a tahlükasizli |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006015` Həyat fəaliyyətinin təhlükəsizliyi mühəndisliyi**
  - Fövqolado hallarda texnoloji proseslarin tahlükasizliyi
  - Fövqalada hallartn idara olunmast
  - Sonaye müossisolorindo hoyat foaliyyatinin tahlükosizliyi
  - Nüvo elmlorindo radiasiya va tohlükosizlik

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Fövqəladə Hallar Nazirliyinin Akademiyası | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 68.5 | None |
| Azərbaycan Memarlıq və İnşaat Universiteti | Fövqəladə halların idarə olunması | 51 | 42 |
| Fövqəladə Hallar Nazirliyinin Akademiyası | Fövqəladə halların idarə olunması | 75 | None |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nüvə elmlərində radiasiya və təhlükəsizlik | None | 40 |

</details>

---

### Proqram № 25

#### Blok 1 (Minimal bal: `40`, Səhifə: 2)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050603` | Aviasiya təhlükəsizliyi |
| `050617` | Hava nəqliyyatmda texnoloji proseslarin və istehsalatrn təhlükəsizliyi mühəndisliyi |
| `T 072200` | Aviasiya təhlükəsizliyinin |
| `T 072300` | Qaza-xilasetma və axtans islörinin toskili |
| `T 340500` | Istehsalatların və texnoloji proseslarin töhlükasizliyi (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006003` Aviasiya təhlükəsizliyi mühəndisliyi**
  - Aviasi a tohlükasizli • idaraolunmast

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Aviasiya təhlükəsizliyinin idarə olunması | 62.5 | 48.5 |

</details>

---

### Proqram № 26

#### Blok 1 (Minimal bal: `45`, Səhifə: 2)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050603` | Aviasiya təhlükəsizliyi |
| `050617` | Hava nəqliyyatmda texnoloji proseslarin və istehsalatrn təhlükəsizliyi mühəndisliyi |
| `T 072200` | Aviasiya təhlükəsizliyinin |
| `T 072300` | Qaza-xilasetma və axtans islörinin toskili |
| `T 340500` | Istehsalatların və texnoloji proseslarin töhlükasizliyi (sahələr üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7004008` Menecment**
  - Mülki aviasiyamn menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Mülki aviasiyanın menecmenti | 80 | 49.5 |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 3)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050613` | Hava nəqliyyatının hərəkətinin təşkili |
| `050613` | Avianəqliyyat istehsalatının təşkili mühəndisliyi |
| `050658` | Logistika və nəqliyyat texnologiyaları mühəndisliyi |
| `T 072400` | Avianəqliyyat istehsalatının təşkili |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (hava nəqliyyatı üzrə) |
| `T 100500` | Nəqliyyatda daşımalarının və idarəetmənin təşkili (su nəqliyyatı üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7004008` Menecment**
  - Mülki aviasiyarun menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Mülki aviasiyanın menecmenti | 80 | 49.5 |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050809` | Turizm balodçuluğu |
| `050810` | Turizm işinin təşkili |
| `050810` | Turizm və hotelçilik |
| `T 300100` | Turizm və sosial mədəni servis xidmati |
| `T 300200` | Turist, sanatoriya-kurort komplekslarinin servis və tibb xidmatinin t0'kili |
| `T 300300` | Turist və sanatoriya-kurort komplekslarind. tabii və qeyri- ananavi vasital |
| `T 300300` | Rla "jsial-ba isi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7004008` Menecment**
  - Turizm menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Turizm menecmenti | None | 45 |
| “Odlar Yurdu” Universiteti | Turizm menecmenti | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Risk menecmenti | 74.5 | 60 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Teatr menecmenti | None | 45 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman menecmenti | None | 45 |

</details>

---

#### Blok 4 (Minimal bal: `45`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050639` | Mühəndisliyi |
| `050616` | Mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7004008` Menecment**
  - Mülki aviasiyamn menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Mülki aviasiyanın menecmenti | 80 | 49.5 |

</details>

---

#### Blok 5 (Minimal bal: `45`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050808` | Tibbi biologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7004008` Menecment**
  - Sohi a menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman menecmenti | None | 45 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil menecmenti (tədris Azərbaycan dilində) | 73.5 | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Təhsil menecmenti | None | 45 |
| Azərbaycan Dillər Universiteti | Təhsil menecmenti | 75 | 75 |
| Bakı Slavyan Universiteti | Təhsil menecmenti | 73 | 61 |
| Sumqayıt Dövlət Universiteti | Təhsil menecmenti | None | 52.5 |
| “Azərbaycan” Universiteti | Təhsil menecmenti | 74.5 | 52.5 |
| “Odlar Yurdu” Universiteti | Təhsil menecmenti | None | 51 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Musiqi menecmenti | None | 48 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Tibb Universiteti | Səhiyyə menecmenti | 73 | 45 |
| “Odlar Yurdu” Universiteti | Səhiyyə menecmenti | None | 45 |

</details>

---

#### Blok 6 (Minimal bal: `45`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050401` | Beynalxalq ticarat və logistika |
| `050403` | Davamlı inkişafın idarə edilməsi |
| `050405` | Iqtisadiyyat |
| `050406` | Maliyya |
| `050407` | Marketing |
| `050408` | Menecment |
| `050409` | Mühasibat |
| `050410` | Statistika |
| `050402` | Mühasibat ugotu və audit |
| `050403` | Maliyya |
| `050404` | Iqtisadiyyat |
| `050406` | Statistika |
| `050407` | Menecment |
| `050408` | Marketin q |
| `050410` | Dövlat və baladiyya idaroetmosi |
| `050411` | Kommersiya |
| `050412` | Davamlı inkişafın idarə edilməsi |
| `010100` | Beynəlxalq iqtisadi münasibətlər |
| `010100` | Beynəlxalq iqtisadi münasibətlər (türk proqramı) |
| `010200` | Mühasibat auditi |
| `010300` | Maliyyə və kredit |
| `ii 010800` | Statistika |
| `040200` | Beynəlxalq ticarət |
| `ii 030300` | Gömrük işinin təşkili |
| `010400` | İqtisadiyyatın tənzimlənməsi |
| `010500` | Əmək haqqının iqtisadiyyatı və sosiologiyası |
| `010600` | Təbiətdən istifadənin iqtisadiyyatı |
| `010700` | Təhsil, elm və sosial |
| `010700` | mədəni sahənin iqtisadiyyatı |
| `010900` | Iqtisadi kibernetika |
| `ii 011000` | Qiymat və qiymatin amala galmasi |
| `ii 012000` | İqtisadi nəzəriyyə |
| `ii 012100` | Vergilər və vergitutma |
| `012200` | Sığorta işinin təşkili |
| `ii 012300` | İqtisadi siyasət |
| `012500` | Milli hesablar sistemi |
| `ii 012600` | İqtisadi resursların idarə olunması |
| `ii 012700` | Qiymətləndirmə |
| `012800` | Qiymətli kağızlar bazarı |
| `020100` | İstehsalat və xidmət sahəl |
| `ii 020200` | Menecment (bank üzrə) |
| `ii 020200` | Menecment (sahələr üzrə) |
| `ii 020400` | Biznesin təşkili və idarə edilməsi |
| `030200` | Təhsilin təşkili və idarə olunması |
| `030400` | Gömrük ekspertizası |
| `ii 030600` | İqtisadiyyatın hüquqi tənzimlənməsi |
| `030700` | Vergi işinin təşkili və idarə edilməsi |
| `030800` | Mühəndisliyi |
| `ii 030900` | İnzibati idarəetmə |
| `ii 040100` | Kommersiya (sahələr üzrə) |
| `ii 040300` | Birja fəaliyyəti və fond bazarı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** **
  - qtisadiyyat
  - iqtisadi nazariyyo
  - iqtisadi-riyazi modella'dirma
  - iqtisadiyyatln tanzimlanmasi
  - Mülkiyyot obyektl•rinin qiymatlondirilmasi
  - Aqrar iqtisadiyyat
  - Tohsilin iqtisadiyyatl
  - Turizmin iqtisadiyyatl
  - Ekonometriya
  - iqtisadi Siyasat
  - Davran1S iqtisadiyyau
  - Beynalxalq iq tisadiyyat
  - Dövlat iqtisadiyyah
  - Xidmat sahalarinin iqtisadiyyatl
  - iqtisadi tohlükasizlik
  - Ümumi iqtisadiyyat
- ** `7004009` Mühasibat**
  - idaroetmo miihasibatl•gl
  - Maliyya rnühasibatllgl
  - Audit
- ** `7004006` Maliyyə**
  - Bank isi
  - Sigorta va risklorin idara edilmosi
  - Maliyya nazaroti va audit
  - Maliyya menecmenti
  - Maliyyo bazarlan
  - Vergi vo vergitutma
  - Korporativ maliyyo
  - Dövlat maliyyasi
  - investisiyalann idara edilmosi
- ** `7006040` Sənaye mühəndisliyi**
  - Texnologiyalar vo amaliyyatlann idara edilmosi
  - ilyaat materiallan sanayesi
- ** `7005012` Statistika**
  - Totbiqi statistika
  - iqtisadiyyatda statistik analiz
- ** `7004008` Menecment**
  - Strateji menecment
  - innovasiya menecmenti
  - Layiha menecmenti
  - idrnan menecmenti
  - Kand tasorrüiati vo qida sistemlorinin menecmenti
  - Tahsil menecmenti
  - Risk menecmenti
  - insan resurslan menecmenti
  - Korporativ menecment
  - istehsal va amaliyyat menecmenti
  - Turizm menecmen ti
  - Musiqi menecmenti
  - Teatr menecmenti
  - Muza•y vo qalereya menecmenti
  - Kino vo tele.'iziya menecmenti
  - Sahiyya menecmenti
  - Qlobal menecment va Siyasot
  - Oczaqlrq menecmenti
  - Mulki aviasiyanm menecmenti
  - Oqli miilkiyyatin idara edilmasi
- ** `7004002` Biznesin idarə edilməsi**
  - Biznesin tehkili
  - Elektron kommersiya
  - Bimes analitikasa
  - Beynalxalq biznesin idara edilmasi
  - Dayamqll biznes va ESK (ESC,) idarasiliyi
  - Biznesda suni intellekt
  - Enerji biznesi
- ** `7004004` Dövlət və bələdiyyə**
  - Dövlat qullugunun ta*ili vo idaro edilmasi
  - Regional idarm•tmo
  - Dövlat pnxvarnlaruun vo layihalorin idara edilmasi
  - Dövlat idaroetmasi
- ** `7002002` Davamlı inkişaf**
  - Davamli inki9fda insan potensiali va yüksak idarm•tma standartlan
  - Davamll inki*lida vo mavi transformasiya Siyasoti
- ** `7004001` Beynəlxalq ticarət və logistika**
  - Gömrük isi
  - Beynolxalq logistika
  - Beynalxalq ticarat siyasati
  - Logistika vo tochizat zancirinin idaro olunmast
  - 70041M Marketinq
  - Strateii marketinq
  - Roqornsal marketinq
  - Beynolxalq marketinq
  - Aqromarketinq
  - Marketinq tadqiqatlan bazann proqnozla#dinlmasi
  - Xidmat sahalarinin marketinqi
  - Brendin idaro olunmasa
  - In idara olunmast

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Aqrar iqtisadiyyat | 64.5 | 64.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar iqtisadiyyat (tədris Azərbaycan dilində) | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Aqrar iqtisadiyyat (tədris Azərbaycan dilində) | None | 45 |
| Lənkəran Dövlət Universiteti | Ümumi iqtisadiyyat | None | 45 |
| Azərbaycan Kooperasiya Universiteti | Dövlət iqtisadiyyatı (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Turizmin iqtisadiyyatı | 64 | 45.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Turizmin iqtisadiyyatı | 65.5 | 65.5 |
| Azərbaycan Turizm və Menecment Universiteti | Turizmin iqtisadiyyatı | 64 | 46.5 |
| “Azərbaycan” Universiteti | Turizmin iqtisadiyyatı | None | 45 |
| Bakı Avrasiya Universiteti | Turizmin iqtisadiyyatı | None | 45 |
| Bakı Biznes Universiteti | Turizmin iqtisadiyyatı | None | 45 |
| Azərbaycan Əmək və Sosial Münasibətlər Akademiyası | Turizmin iqtisadiyyatı | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Təhsilin iqtisadiyyatı | 64 | 55 |
| Azərbaycan Dövlət İqtisad Universiteti | Davranış iqtisadiyyatı | 65.5 | 65.5 |
| Azərbaycan Kooperasiya Universiteti | Turizmin iqtisadiyyatı (tədris Azərbaycan dilində) | None | 45 |
| *... və daha 420 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `45`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `ii 030400` | Gömrük ekspertizasi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7004001` Beynəlxalq ticarət və logistika**
  - Gömrük i

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Gömrük işi | None | 45 |
| Dövlət Gömrük Komitəsinin Akademiyası | Gömrük işi | 73 | 56.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Gömrük işi | 81.5 | 45 |

</details>

---

#### Blok 8 (Minimal bal: `45`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050638` | Sanaye mühəndisliyi |
| `050657` | Sanaye mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006040` Sənaye mühəndisliyi**
  - Texnolo ivalar va omali atlann idara edilmosi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnologiyalar və əməliyyatların idarə edilməsi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Texnologiyalar və əməliyyatların idarə edilməsi | 60 | 60 |

</details>

---

### Proqram № 27

#### Blok 1 (Minimal bal: `45`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050114` | Riyaziyyat müəllimliyi |
| `050106` | Riyaziyyat müəllimliyi |
| `050115` | Riyaziyyat və informatika müəllimliyi |
| `050105` | Riyaziyyat və informatika müəllimliyi |
| `050108` | Informatika müəllimliyi |
| `050116` | İnformatika müəllimliyi |
| `050110` | Kimya və biologiya müəllimliyi |
| `050112` | Kimya və biologiya müəllimliyi |
| `050116` | Tarix müəllimliyi |
| `050113` | Tarix müəllimliyi |
| `050117` | Tarix və coğrafiya müəllimliyi |
| `050114` | Tarix və coğrafiya müəllimliyi |
| `050115` | Coğrafiya müəllimliyi |
| `050105` | Fizika müəllimliyi |
| `050104` | Fizika müəllimliyi |
| `050109` | Kimya müəllimliyi |
| `050111` | Kimya müəllimliyi |
| `050102` | Biologiya müəllimliyi |
| `OSOIIO` | Biologiya müəllimliyi |
| `050101` | Azərbaycan dili və ədəbiyyatı müəllimliyi |
| `050101` | Azərbaycan dili və ədəbiyyatı müəllimliyi |
| `050107` | İbtidai sinif müəllimliyi |
| `050111` | Korreksiyaedici talim |
| `050112` | Maktabaqador təhsil |
| `050118` | İbtidai sinif müəllimliyi |
| `050119` | Korreksiyaedici təlim |
| `050120` | Məktəbəqədər təlim və tərbiyə |
| `050104` | Dil və ədəbiyyat müəllimliyi (dillər üzrə) |
| `050121` | Xarici dil müəllimliyi (dillar üzrə) |
| `050107` | Fiziki tərbiyə və gənclərarası hazırlıq (qızlar üçün fiziki tərbiyə) müəllimliyi |
| `050120` | Texnologiya müəllimliyi |
| `M 010600` | Peşə təlimi |
| `050113` | Musiqi müəllimliyi |
| `050109` | Musiqi müəllimliyi |
| `050118` | Təhsildə sosial-psixoloji xidmət |
| `050119` | Tasviri incasanat müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7004008` Menecment**
  - Tahsil menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil menecmenti (tədris Azərbaycan dilində) | 73.5 | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Təhsil menecmenti | None | 45 |
| Azərbaycan Dillər Universiteti | Təhsil menecmenti | 75 | 75 |
| Bakı Slavyan Universiteti | Təhsil menecmenti | 73 | 61 |
| Sumqayıt Dövlət Universiteti | Təhsil menecmenti | None | 52.5 |
| “Azərbaycan” Universiteti | Təhsil menecmenti | 74.5 | 52.5 |
| “Odlar Yurdu” Universiteti | Təhsil menecmenti | None | 51 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Teatr menecmenti | None | 45 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050114` | Riyaziyyat müəllimliyi |
| `050106` | Riyaziyyat müəllimliyi |
| `050115` | Riyaziyyat və informatika müəllimliyi |
| `050105` | Riyaziyyat və informatika müəllimliyi |
| `050108` | Informatika müəllimliyi |
| `050116` | İnformatika müəllimliyi |
| `050110` | Kimya və biologiya müəllimliyi |
| `050112` | Kimya və biologiya müəllimliyi |
| `050116` | Tarix müəllimliyi |
| `050113` | Tarix müəllimliyi |
| `050117` | Tarix və coğrafiya müəllimliyi |
| `050114` | Tarix və coğrafiya müəllimliyi |
| `050115` | Coğrafiya müəllimliyi |
| `050105` | Fizika müəllimliyi |
| `050104` | Fizika müəllimliyi |
| `050109` | Kimya müəllimliyi |
| `050111` | Kimya müəllimliyi |
| `050102` | Biologiya müəllimliyi |
| `OSOIIO` | Biologiya müəllimliyi |
| `050101` | Azərbaycan dili və ədəbiyyatı müəllimliyi |
| `050101` | Azərbaycan dili və ədəbiyyatı müəllimliyi |
| `050107` | İbtidai sinif müəllimliyi |
| `050111` | Korreksiyaedici talim |
| `050112` | Maktabaqador təhsil |
| `050118` | İbtidai sinif müəllimliyi |
| `050119` | Korreksiyaedici təlim |
| `050120` | Məktəbəqədər təlim və tərbiyə |
| `050104` | Dil və ədəbiyyat müəllimliyi (dillər üzrə) |
| `050121` | Xarici dil müəllimliyi (dillar üzrə) |
| `050107` | Fiziki tərbiyə və gənclərarası hazırlıq (qızlar üçün fiziki tərbiyə) müəllimliyi |
| `050120` | Texnologiya müəllimliyi |
| `M 010600` | Peşə təlimi |
| `050113` | Musiqi müəllimliyi |
| `050109` | Musiqi müəllimliyi |
| `050118` | Təhsildə sosial-psixoloji xidmət |
| `050119` | Tasviri incasanat müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7001001` Pedaqogika**
  - Texnologiyamn tadrisi
  - Tahsil nazariyyasi va tarixi
  - Tahsilda monitorinq vo qiymatlandirmo
  - Tolim va tadrisin t*ili

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Pedaqoji Universiteti | Texnologiyanın tədrisi | None | 48.5 |
| Naxçıvan Dövlət Universiteti | Texnologiyanın tədrisi | None | 45.5 |
| Gəncə Dövlət Universiteti | Texnologiyanın tədrisi | None | 44 |
| Lənkəran Dövlət Universiteti | Texnologiyanın tədrisi | None | 41 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 55.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 51.5 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |
| Bakı Dövlət Universiteti | Təhsildə monitorinq və qiymətləndirmə | 64.5 | 64.5 |
| *... və daha 9 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 28

#### Blok 1 (Minimal bal: `45`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `TT 210100` | Kompüter riyaziyyati |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005011` Riyaziyyat**
  - Riyazi analiz
  - Funksional analiz
  - Diferensial tonliklor
  - Hondoso vo topologiya
  - Cobr va ododlor nozariyyasi
  - Hesablama riyaziyyah vo mode110#Iirmo
  - Ehtimal nazoriyyosi va riyazi statistika
  - Omaliyyatlar todqiqi
  - Optimalla#hrma va optimal idaraetrno
  - Hesablama diaqnostikast
  - Riyazi fizika
  - Diskret sistemlar
  - Aktuar riyaziyyat
  - informatikarun riyazi osaslan
  - Stoxastik modelle&dirmo
  - Dinamik sistemlor vo idaroetmo nozoriyyosi
- ** `7005009` Kompüter elmləri**
  - intellektual sistemlor
  - Kompüter modellasdirmosi
  - Riyazi
  - Tatbiqi riyaziyyat
  - iqtisadiyyatda optimal idaraetmonin riyazi üsullan
  - Kompüter riyaziyyatl
  - Roqamsal dövlat
  - Süni intellekt
  - Yüksak mahsuldarhqli hesablama sistemlori
  - alarm interneti vo kiberfiziki sistemlar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Riyazi analiz | 72 | 72 |
| Naxçıvan Dövlət Universiteti | Riyazi analiz | 53 | 53 |
| Gəncə Dövlət Universiteti | Riyazi analiz | 48.5 | 48.5 |
| Sumqayıt Dövlət Universiteti | Riyazi analiz | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Riyazi analiz İngilis dilində | 69.5 | 69.5 |
| Bakı Dövlət Universiteti | Funksional analiz | 63.5 | 63.5 |
| Bakı Dövlət Universiteti | Diferensial tənliklər | 69 | 69 |
| Gəncə Dövlət Universiteti | Diferensial tənliklər | 52 | 45 |
| Sumqayıt Dövlət Universiteti | Diferensial tənliklər | 53.5 | 53.5 |
| Bakı Dövlət Universiteti | Həndəsə və topologiya | 72.5 | 72.5 |
| Naxçıvan Dövlət Universiteti | Həndəsə və topologiya | 50.5 | 50.5 |
| Gəncə Dövlət Universiteti | Həndəsə və topologiya | 46.5 | 45 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 66 | 66 |
| Gəncə Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 53 | 53 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| *... və daha 35 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 29

#### Blok 1 (Minimal bal: `40`, Səhifə: 1)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050624` | Mədən mühəndisliyi |
| `050605` | Dag-mədən mühəndisliyi |
| `T 020400` | Açıq-dağ mədən işləri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006032` Mədən mühəndisliyi**
  - Faydall qazmtl yataqlaruun i*lonmasi
  - Faydall qanntllann zonginlö}dirilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Faydalı qazıntıların zənginləşdirilməsi | None | 40 |

</details>

---

### Proqram № 31

#### Blok 1 (Minimal bal: `40`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | İnformasiya texnologiyaları |
| `050632` | Informasiya texnologiyalart və sistemlari mühəndisli |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006033` Mühəndislik fizikası**
  - Fiziki elektronika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Fiziki elektronika | 58 | 58 |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050630` | Mühəndis fizikasj |
| `TT 090100` | Materiallar fizikas, |
| `TT 120100` | Fiziki elektronika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005005` Fizika**
  - Nazari va riyazi fizika
  - Bork cisimlor fizikast
  - Yanmkecirici Cihazlar texnologiyalar
  - Bork cisim elektronikast
  - Optoelektronika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Nəzəri və riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bərk cisimlər fizikası | 64 | 64 |
| Bakı Dövlət Universiteti | Yarımkeçirici cihazlar və texnologiyalar | 59 | 45 |
| Naxçıvan Dövlət Universiteti | Yarımkeçirici cihazlar və texnologiyalar | None | 45 |
| Gəncə Dövlət Universiteti | Yarımkeçirici cihazlar və texnologiyalar | 45 | 45 |
| Bakı Dövlət Universiteti | Yarımkeçirici cihazlar və texnologiyalar İngilis dilində | 69 | 45 |
| Bakı Dövlət Universiteti | Bərk cisim elektronikası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Optoelektronika | 61.5 | 61.5 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050630` | Mühəndis fizikasj |
| `TT 090100` | Materiallar fizikas, |
| `TT 120100` | Fiziki elektronika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006033` Mühəndislik fizikası**
  - Fiziki elektronika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Fiziki elektronika | 58 | 58 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050103` | Optotexnika mühəndisliyi |
| `XTB 050002` | Optotexnika |
| `XTB 050102` | Optotexnika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006033` Mühəndislik fizikası**
  - Fiziki elektronika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Fiziki elektronika | 58 | 58 |

</details>

---

### Proqram № 32

#### Blok 1 (Minimal bal: `45`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050618` | Kimya |
| `050641` | Kimya mühəndisliyi |
| `T 250100` | Üzvi maddalorin kimyovi texnologiyasr |
| `T 250200` | Qeyri-üzvi maddolorin kimyavi texnologiyasl |
| `T 250300` | Elektrokimyavi istehsal texnologiyast |
| `T 250400` | Neft-qaz və alternativ enerji texnologiyasr |
| `T 250500` | Yüksakmolekullu birl"malarin kimyavi texnologiyasr |
| `T 250600` | Plastik kütla və elastomerlarin kimyovi texnologiyasr |
| `T 251700` | Kimyavi istehsalatların |
| `T 251700` | Sas proseslari və kimyavi kibernetikasr |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005008` Kimya**
  - Kimyovi kinetika va kataliz
  - Kompozit materiallar kimyasl
  - Qeyri-üzvi kimya
  - Üzvi kimya
  - Fiziki kimya
  - Kolloid kimya
  - Analitik kimya
  - Elektrokimya
  - Tabii vo fizioloji foal maddalor kimyast
  - Neft kimyast
  - Nanomateriallar kimyasl
  - Kimyovi ekspertiza
  - Materiallar kimyasl
  - Polimer kim asr

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 52 | 52 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Materiallar kimyası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 51 | 51 |
| Naxçıvan Dövlət Universiteti | Qeyri-üzvi kimya | 46.5 | 46.5 |
| Gəncə Dövlət Universiteti | Qeyri-üzvi kimya | 51 | 45 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Gəncə Dövlət Universiteti | Üzvi kimya | 52 | 45 |
| Sumqayıt Dövlət Universiteti | Üzvi kimya | 48 | 45.5 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Gəncə Dövlət Universiteti | Üzvi kimya | 52 | 45 |
| Sumqayıt Dövlət Universiteti | Üzvi kimya | 48 | 45.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 51 | 51 |
| Naxçıvan Dövlət Universiteti | Qeyri-üzvi kimya | 46.5 | 46.5 |
| Gəncə Dövlət Universiteti | Qeyri-üzvi kimya | 51 | 45 |
| *... və daha 22 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 33

#### Blok 1 (Minimal bal: `45`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050808` | Tibbi biologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005001` Biologiya**
  - Molekulyar biologiya
  - Biokimya
  - insan vo heyvan fiziologiyasl
  - Mikologiya
  - Mikrobiologiya
  - Biofizika
  - Entomologiya
  - Bioloji monito

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Qərbi Kaspi Universiteti | Molekulyar biologiya | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Biokimya | 71.5 | 71.5 |
| Azərbaycan Tibb Universiteti | Biokimya | 48.5 | 48.5 |
| Gəncə Dövlət Universiteti | Biokimya | 65 | 65 |
| Bakı Dövlət Universiteti | İnsan və heyvan fiziologiyası | 71 | 71 |
| Gəncə Dövlət Universiteti | İnsan və heyvan fiziologiyası | 51 | 51 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050703` | Balıqçılıq |
| `050707` | Bahq€iltq və bahq€lltq təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005001` Biologiya**
  - Mikrobiologiya
  - Biofizika
  - Onurgalilar zoologiyasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Bakı Dövlət Universiteti | Biofizika | 56 | 56 |
| Bakı Dövlət Universiteti | Onurğalılar zoologiyası | 68.5 | 68.5 |
| Gəncə Dövlət Universiteti | Onurğalılar zoologiyası | None | 45 |
| Bakı Dövlət Universiteti | Onurğasızlar zoologiyası | 65.5 | 65.5 |
| Naxçıvan Dövlət Universiteti | Onurğasızlar zoologiyası | 45 | 45 |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050708` | Su bioehtiyatlan və akvakultura |
| `050709` | Su bioehtiyatları və akvabitkilər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005001` Biologiya**
  - Bitki fiziologiyast
  - Botanika
  - Onurgastzlar zoologiyast
  - Onurgalilar zoologiyasa
  - Biofizik9
  - Entomologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bitki fiziologiyası | 67 | 67 |
| Gəncə Dövlət Universiteti | Bitki fiziologiyası | 47 | 45 |
| Bakı Dövlət Universiteti | Botanika | 46.5 | 45 |
| Naxçıvan Dövlət Universiteti | Botanika | 47 | 45 |
| Gəncə Dövlət Universiteti | Botanika | 49.5 | 49.5 |
| Bakı Dövlət Universiteti | Onurğasızlar zoologiyası | 65.5 | 65.5 |
| Naxçıvan Dövlət Universiteti | Onurğasızlar zoologiyası | 45 | 45 |
| Bakı Dövlət Universiteti | Onurğalılar zoologiyası | 68.5 | 68.5 |
| Gəncə Dövlət Universiteti | Onurğalılar zoologiyası | None | 45 |
| Bakı Dövlət Universiteti | Onurğalılar zoologiyası | 68.5 | 68.5 |
| Gəncə Dövlət Universiteti | Onurğalılar zoologiyası | None | 45 |
| Bakı Dövlət Universiteti | Onurğasızlar zoologiyası | 65.5 | 65.5 |
| Naxçıvan Dövlət Universiteti | Onurğasızlar zoologiyası | 45 | 45 |
| Bakı Dövlət Universiteti | Biofizika | 56 | 56 |
| Bakı Dövlət Universiteti | Entomologiya | 62.5 | 62.5 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 35

#### Blok 1 (Minimal bal: `30`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Meşəçilik |
| `050708` | Meşəçilik |
| `T 260100` | Mep mühəndisliyi |
| `T 260200` | Mesa və mep-park təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7007001` Aqronomluq**
  - Ümumi okinqilik
  - Ekoloji akinqilik
  - Texniki bitkilarin becorma texnologiyast
  - Taxil Vö paxlah bitkilarin becarma texnologiyasl
  - Kond tosorrüfatl bitkilorinin biotexnologiyasl
  - Kand tosorrüfatl bitkilorinin seleksiyasi va toxumqulugu
  - Kond tosorrüfati bitkilarinin genetikast
- ** `7007002` Bağçılıq və tərəvəzçilik**
  - Meyvo bitkilorinin becorma texnologiyasr
  - Torovoz, bostan bitkilorinin vo kartofun becarmo texnologiyasl
  - Üzüm bitkisinin becarma texnologiyast
- ** `7007005` Bitki mühafizəsi**
  - Bitki mühafizosi vo karantin
  - Bitki saglarn11É1 vo fitosanitar xidmat
  - Fito tolo i a

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ümumi əkinçilik (tədris Azərbaycan dilində) | 46 | 46 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ekoloji əkinçilik (tədris Azərbaycan dilində) | 40.5 | 40.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Texniki bitkilərin becənnə texnologiyası (tədris Azərbaycan dilində) | 33 | 33 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Taxıl və paxlalı bitkilərin becərmə texnologiyası (tədris Azərbaycan dilində) | 31 | 31 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu (tədris Azərbaycan dilində) | 39 | 39 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu | 33.5 | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin genetikası (tədris Azərbaycan dilində) | 39.5 | 39.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Meyvə bitkilərinin becərmə texnologiyası (tədris Azərbaycan dilində) | None | 44.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Üzüm bitkisinin becərmə texnologiyası (tədris Azərbaycan dilində) | None | 32.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Tərəvəz, bostan bitkilərinin və kartofun becərmə texnologiyası (tədris Azərbaycan dilində) | None | 37 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Üzüm bitkisinin becərmə texnologiyası (tədris Azərbaycan dilində) | None | 32.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Meyvə bitkilərinin becərmə texnologiyası (tədris Azərbaycan dilində) | None | 44.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Bitki mühafizəsi və karantin (tədris Azərbaycan dilində) | None | 30 |
| *... və daha 1 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `ET 010500` | Aqroekologiya |
| `ET 010600` | Meliorasiya və torpaq mühafizəsi |
| `ET 010700` | Su ehtiyatlarının mühafizəsi və kompleks istifadəsi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7007008` Torpaqşünaslıq və aqrokimya**
  - Torpaq#inashq
  - Aqrokimya vo torpaq münbitliyinin idaro olunmasr
  - Aqrokimyavi xidmot vo keyfiyyat:in qiymotlandirilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Torpaqşünaslıq | 51 | 51 |
| Naxçıvan Dövlət Universiteti | Torpaqşünaslıq | 43.5 | 30 |
| Lənkəran Dövlət Universiteti | Torpaqşünaslıq | 40.5 | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Torpaqşünaslıq (tədris Azərbaycan dilində) | 38 | 30 |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Lənkəran Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 44 | 44 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimya və torpaq münbitliyinin idarə olunması (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimyəvi xidmət və keyfiyyətin qiymətləndirilməsi (tədris Azərbaycan dilində) | 38 | 30 |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050701` | Aqronomluq |
| `050702` | Bağçılıq və tərəvəzçilik |
| `050705` | Bitki mühafizəsi |
| `050709` | Torpaqşünaslıq və aqrokimya |
| `050701` | Torpaqşünaslıq və aqrokimya |
| `050702` | Aqronomluq |
| `050710` | Bitki miihafizasi |
| `050711` | Bağçılıq və tərəvəzçilik |
| `AT 020100` | Aqronomluq |
| `AT 020200` | Meyvə-tərəvəzçilik və üzümçülük |
| `AT 020300` | Bitkilərin mühafizəsi |
| `AT 020400` | İpəkçilik |
| `AT 020500` | Aqrar təsərrüfat bitkilərinin seleksiyası və genetikası |
| `TE 080100` | Torpaq'iinashq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7007008` Torpaqşünaslıq və aqrokimya**
  - Torpaq#inashq
  - Aqrokimya vo torpaq münbitliyinin idaro olunmast
  - Aqrokimyovi xidmot va keyfiyyotin qiymotlandirilmosi
- ** `7007001` Aqronomluq**
  - Ümumi okincilik
  - Ekoloji akinqilik
  - Texniki bitkilarin becarma texnologiyast
  - Taxil vo paxlali bitkilorin becormo texnologiyast
  - Kand tasorrüfah bitkilarinin biotexnologiyasl
  - Kond tasarrüfah bitkilarinin seleksiyast va toxumqulugu
  - Kand tosorrüfah bitkilorinin genetikast
- ** `7007002` Bağçılıq və tərəvəzçilik**
  - Meyvo bitkilarinin becormo texnologiyast
  - Tarovoz, bostan bitkilorinin vo kartofun becorma texnologiyast
  - Üzüm bitkisinin becarmo texnologiyast
- ** `7007005` Bitki mühafizəsi**
  - Bitki mühafizosi va karantin
  - Bitki saklarnlngt va fitosanitar xidmat
  - Fitopatologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Torpaqşünaslıq | 51 | 51 |
| Naxçıvan Dövlət Universiteti | Torpaqşünaslıq | 43.5 | 30 |
| Lənkəran Dövlət Universiteti | Torpaqşünaslıq | 40.5 | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Torpaqşünaslıq (tədris Azərbaycan dilində) | 38 | 30 |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Lənkəran Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 44 | 44 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimya və torpaq münbitliyinin idarə olunması (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimyəvi xidmət və keyfiyyətin qiymətləndirilməsi (tədris Azərbaycan dilində) | 38 | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ümumi əkinçilik (tədris Azərbaycan dilində) | 46 | 46 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ekoloji əkinçilik (tədris Azərbaycan dilində) | 40.5 | 40.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Texniki bitkilərin becənnə texnologiyası (tədris Azərbaycan dilində) | 33 | 33 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Taxıl və paxlalı bitkilərin becərmə texnologiyası (tədris Azərbaycan dilində) | 31 | 31 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu (tədris Azərbaycan dilində) | 39 | 39 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 36

#### Blok 1 (Minimal bal: `30`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050704` | Baytarlıq təbabəti |
| `050711` | Zoomühəndislik |
| `050703` | Zootexniklik |
| `050704` | Baytarlıq |
| `AT 030100` | Zootexniklik |
| `AT 040100` | Baytarlıq |
| `AT 040200` | Baytarlıq əczaçılığı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7007010` Zoomühəndislik**
  - Kond tasarrüfatl heyvanlanrun yetisdirilmosi, genetikast vo seleksiyasr
  - Anoltq vo baramaqhq mohsullan istehsahnda innovativ
  - texnologiyalar
  - Heyvandarhq mahsullart istehsahnm texnologiyasl
- ** `7007004` Baytarlıq təbabəti**
  - Heyvanlann yoluxmayan daxili xostaliklari
  - Baytarhq tobabotindo mamahq-ginekologiya vo süni mayalanma
  - Baytarhq carrahiyyosi
  - Baytarhq sanitariya-ekspertizasl
  - Baytarhq tobaböti oczaqltgt
  - Baytarhq epidemiologiyasl
  - Heyvanlann yoluxucu xastaliklari va profilaktikasl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı heyvanlarının yetişdirilməsi, genetikası və seleksiyası (tədris Azərbaycan dilində) | 33.5 | 33.5 |
| Bakı Musiqi Akademiyası | Musiqi texnologiyaları | 50 | 48 |
| Azərbaycan Texniki Universiteti | Optik rabitə texnologiyaları | 55 | 55 |
| Bakı Dövlət Universiteti | Nanofizika və nanotexnologiyalar | 68.5 | 68.5 |
| Naxçıvan Dövlət Universiteti | Nanofizika və nanotexnologiyalar | 51.5 | 51.5 |
| Azərbaycan Texniki Universiteti | Sənayedə ekoloji texnologiyalar | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 59.5 | 46 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 41 |
| Gəncə Dövlət Universiteti | Tullantıların emal texnologiyaları (dağ-mədən sənayesi) | None | 42.5 |
| Azərbaycan Texniki Universiteti | Logistikada informasiya texnologiyaları | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Yarımkeçirici cihazlar və texnologiyalar | 59 | 45 |
| Naxçıvan Dövlət Universiteti | Yarımkeçirici cihazlar və texnologiyalar | None | 45 |
| Gəncə Dövlət Universiteti | Yarımkeçirici cihazlar və texnologiyalar | 45 | 45 |
| *... və daha 27 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 48

#### Blok 1 (Minimal bal: `50`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050808` | Tibbi biologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7002013` Psixologiya**
  - Sosial psixologiya
  - Klinik (tibbi) psixologiya
  - inki9af psixologiyast
  - Tatbi i ixol i a

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 50 |
| Qərbi Kaspi Universiteti | Sosial psixologiya | 78 | 50 |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| Azərbaycan Dillər Universiteti | Təhsil psixologiyası | None | 50 |
| Bakı Slavyan Universiteti | Təhsil psixologiyası | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil psixologiyası | None | 50 |
| Sumqayıt Dövlət Universiteti | Təhsil psixologiyası | None | 50 |
| “Azərbaycan” Universiteti | Təhsil psixologiyası | None | 50 |
| “Odlar Yurdu” Universiteti | Təhsil psixologiyası | None | 50 |
| “Odlar Yurdu” Universiteti | Ailə psixologiyası | None | 53.5 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 57.5 |
| Azərbaycan Tibb Universiteti | Klinik (tibbi) psixologiya | 69 | 61.5 |
| Qərbi Kaspi Universiteti | Klinik (tibbi) psixologiya | 68 | 64.5 |
| Xəzər Universiteti | Klinik (tibbi) psixologiya | 70 | 70 |
| *... və daha 5 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 52

#### Blok 1 (Minimal bal: `30`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050703` | Balıqçılıq |
| `050707` | Bahq€iltq və bahq€lltq təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** **
  - 7007003
  - Bahqqltq tosorrüfatl isi
  - Sanaye ixtiologiyasj

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Sənaye ixtiologiyası (tədris Azərbaycan dilində) | 40 | 40 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050708` | Su bioehtiyatlan və akvakultura |
| `050709` | Su bioehtiyatları və akvabitkilər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7005013` Su bioehtiyatları və akvakultura**
  - Akvabioresurlar
- ** `7007003` Balıqçılıq**
  - Baltqqltq tosorrüfatl isi
  - Sanaye ixtiologiyast

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Akvabioresurlar | 56.5 | 56.5 |
| Qərbi Kaspi Universiteti | Akvabioresurlar | 47.5 | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Sənaye ixtiologiyası (tədris Azərbaycan dilində) | 40 | 40 |

</details>

---

### Proqram № 57

#### Blok 1 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050811` | Nəqliyyat servisi (avtomobil nəqliyyatı üzrə) |
| `T 290600` | Texnoloii və nəqliyyat və avadanltqlanmn texniki istismarı və servis xidmati (saholor üzrə) |
| `T 290700` | Nəqliyyat vasitələrinin təmiri və servis xidmati |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7008002` Nəqliyyatda servis**
  - Avtomobil naqliyyatlnda servis texnologiyalan
  - Sornisindastrna xidmatlarinin taskili vo tahlükosizliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Avtomobil nəqliyyatında servis texnologiyaları | 43.5 | 43.5 |
| Bakı Mühəndislik Universiteti | Sərnişindaşıma xidmətlərinin təşkili və təhlükəsizliyi | 43.5 | 43.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050809` | Turizm balodçuluğu |
| `050810` | Turizm işinin təşkili |
| `050810` | Turizm və hotelçilik |
| `T 300100` | Turizm və sosial mədəni servis xidmati |
| `T 300200` | Turist, sanatoriya-kurort komplekslarinin servis və tibb xidmatinin t0'kili |
| `T 300300` | Turist və sanatoriya-kurort komplekslarind. tabii və qeyri- ananavi vasital |
| `T 300300` | Rla "jsial-ba isi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7008002` Nəqliyyatda servis**
  - Avtomobil naqliyyatmda servis texnologiyalan
  - Sornisin da$tna xidmatlarinin taskili va tahlükasizli

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Avtomobil nəqliyyatında servis texnologiyaları | 43.5 | 43.5 |
| Bakı Mühəndislik Universiteti | Sərnişindaşıma xidmətlərinin təşkili və təhlükəsizliyi | 43.5 | 43.5 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050806` | Nəqliyyatda servis (nəqliyyat növləri üzrə) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7008002` Nəqliyyatda servis**
  - Avtomobil noqliyyatmda servis texnologiyalan
  - Sarnisin da$ma xidmatlarinin t kili va tohlükosizli

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Avtomobil nəqliyyatında servis texnologiyaları | 43.5 | 43.5 |
| Bakı Mühəndislik Universiteti | Sərnişindaşıma xidmətlərinin təşkili və təhlükəsizliyi | 43.5 | 43.5 |

</details>

---

### Proqram № 58

#### Blok 1 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050613` | Hava nəqliyyatının hərəkətinin təşkili |
| `050615` | Hava noqliyyaUmn harakotinin idaro olunmast mühəndisliyi |
| `T 100700` | Hava nəqliyyatlrun istismarı və horakotinin idara edilmasi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006014` Hava nəqliyyatının hərəkətinin təşkili**
  - Hava noqliyyatl horokötinin idara olunmasl
  - Aeronaviqasiya taminatl

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Hava nəqliyyatı hərəkətinin idarə olunması İngilis dilində | None | 40 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050639` | Uçuş mühəndisliyi |
| `050616` | Uçuş mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006043` Uçuş mühəndisliyi**
  - Hava gomilorinin istismart
  - töhlükasizliyinin tominati vo idarö edilmosi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Hava gəmilərinin uçuş istismarı İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Uçuşların təhlükəsizliyinin təminatı və idarə edilməsi İngilis dilində | None | 40 |

</details>

---

### Proqram № 60

#### Blok 1 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050614` | Aviasiya texnikası avadanltqlanmn istismarı mühəndisliyi |
| `T 070300` | Ugan aparatlann və onlann müharriklarinin texniki istismarı |
| `T 071000` | Aviasiya elektrosistemlarinin və pilotaj- naviqasiya komplekslarinin texniki istismarı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006001` Aerokosmik mühəndislik**
  - Us-us aparatlan vo güc qurgulan
  - Aerokosmik elektron sistemlor
  - Peyklor va kosmik sistemlar
  - Us-us yararljgrrun saxlarulmast vo idara edilmosi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Uçuş aparatları və güc qurğuları | 52.5 | 52.5 |
| Milli Aviasiya Akademiyası | Aerokosmik elektron sistemlər | 48 | 48 |
| Milli Aviasiya Akademiyası | Aerokosmik elektronika | None | 40 |
| Milli Aviasiya Akademiyası | Peyklər və kosmik sistemlər | 47.5 | 47.5 |
| Milli Aviasiya Akademiyası | Uçuş yararlığının saxlanılması və idarə edilməsi | 48.5 | 48.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050601` | Aerokosmik mühəndislik |
| `050652` | Kosmik texnologiyalar mühəndisliyi |
| `050653` | Kosmik texnika mühəndisliyi |
| `050654` | Kosmik idaraetmo sistemləri mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006001` Aerokosmik mühəndislik**
  - Us-us aparatlan vo güc qurgulan
  - Aerokosmik elektron sistemlar
  - Peyklor vo kosmik sistemlor
  - yararllgtmn saxlantlmasl vo idara edilmasi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Uçuş aparatları və güc qurğuları | 52.5 | 52.5 |
| Milli Aviasiya Akademiyası | Aerokosmik elektron sistemlər | 48 | 48 |
| Milli Aviasiya Akademiyası | Aerokosmik elektronika | None | 40 |
| Milli Aviasiya Akademiyası | Peyklər və kosmik sistemlər | 47.5 | 47.5 |
| Milli Aviasiya Akademiyası | Uçuş yararlığının saxlanılması və idarə edilməsi | 48.5 | 48.5 |

</details>

---

### Proqram № 61

#### Blok 1 (Minimal bal: `30`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050106` | Silah və silah sistemlari mühəndisliyi |
| `XTB 050001` | Silah və silah sistemlarinin istehsal texnologiyast |
| `-` | Xüsusi təyinatlı texnika və sistemlər |
| `XTB 050101` | Silah və silah sistemlarinin istehsal texnologiyast |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7010006` Silah sistemləri mühəndisliyi**
  - Atto artilleriya va raket silahlannm istehsal texnologiyast
  - Xüsusi ta
  - th dron u a ratlanntn istehsal texnolo ast

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Atıcı artilleriya və raket silahlarının istehsal texnologiyası | 39 | None |

</details>

---

### Proqram № 63

#### Blok 1 (Minimal bal: `30`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050104` | Pirotexniki və partlad |
| `XTB 050003` | Pirotexniki vasitalarin texnologiyasl |
| `XTB 050103` | Pirotexniki vasitalarin texnologiyast |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006020` Kimya mühəndisliyi**
  - Osas iizvi sintezin kimyasl va texnologiyasl
  - Qeyri-üzvi maddalorin istehsal texnologiyast
  - Kim a texnolo astnm roses va a ratlan

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Mühəndislik Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | 59 | 54.5 |
| Sumqayıt Dövlət Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qeyri-üzvi maddələrin istehsal texnologiyası | 55.5 | 53.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Kimya texnologiyasının proses və aparatları | 61 | 61 |

</details>

---

### Proqram № 64

#### Blok 1 (Minimal bal: `30`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050102` | Harbi rabita vasitolari mühəndisliyi |
| `XTB 050004` | Coxkanalll radiorele və troposfer rabitasinin yerüstü aparatlanmn hazrrlanmasr, istismarı və təmiri |
| `XTB 050104` | Coxkanalh radiorele və troposfer rabitasinin yerüstü aparatlanmn haztrlanmasi, istismarı və təmiri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7010003` Xüsusi rabitə vasitələri mühəndisliyi**
  - Radioelektron mübarizo vasitalori
  - Xüsusi ta •nath radiorabita sistemlori

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Radioelektron mübarizə vasitələri | 45 | 30 |
| Azərbaycan Texniki Universiteti | Xüsusi təyinatlı radiorabitə sistemləri | 41 | 30 |

</details>

---

### Proqram № 69

#### Blok 1 (Minimal bal: `30`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050509` | Kompüter elmləri |
| `050615` | Informasiya tohlükosizliyi |
| `050616` | Informasiya texnologiyaları Kompüter mühəndisliyi |
| `050509` | Kompüter elmləri |
| `050631` | Kompüter mühəndisliyi |
| `050632` | İnformasiya texnologiyaları və sistemləri mühəndisliyi |
| `050655` | İnformasiya texnologiyaları |
| `050656` | Sistem mühəndisliyi |
| `T 180100` | Hesablama ma'tnlan, komplekslari, sistemlari və pbokolari |
| `T 180200` | Avtomatlaşdırılmış layihələndirmə sistemləri (sahələr üzrə) |
| `T 180300` | İnformasiya işlənməsinin və idarəetmənin sistemləri |
| `T 180500` | Malumatlann mühafizasinin texnologiyast və təşkili |
| `T 180600` | Kompüter təhlükəsizliyi |
| `160100` | İnformasiya sistemləri (tətbiq sahələri üzrə) |
| `TE 100100` | Tatbiqi riyaziyyat |
| `TE 100200` | Informatika |
| `XTB 50106` | Informasiya təhlükəsizliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7003015` Rejissorluq**
  - Animasi a r •issoru*

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Animasiya rejissoru | None | 30 |

</details>

---

### Proqram № 70

#### Blok 1 (Minimal bal: `30`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050509` | Kompüter elmləri |
| `050615` | Informasiya tohlükosizliyi |
| `050616` | Informasiya texnologiyaları Kompüter mühəndisliyi |
| `050509` | Kompüter elmləri |
| `050631` | Kompüter mühəndisliyi |
| `050632` | İnformasiya texnologiyaları və sistemləri mühəndisliyi |
| `050655` | İnformasiya texnologiyaları |
| `050656` | Sistem mühəndisliyi |
| `T 180100` | Hesablama ma'tnlan, komplekslari, sistemlari və pbokolari |
| `T 180200` | Avtomatlaşdırılmış layihələndirmə sistemləri (sahələr üzrə) |
| `T 180300` | İnformasiya işlənməsinin və idarəetmənin sistemləri |
| `T 180500` | Malumatlann mühafizasinin texnologiyast və təşkili |
| `T 180600` | Kompüter təhlükəsizliyi |
| `160100` | İnformasiya sistemləri (tətbiq sahələri üzrə) |
| `TE 100100` | Tatbiqi riyaziyyat |
| `TE 100200` | Informatika |
| `XTB 50106` | Informasiya təhlükəsizliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7003010` Qrafika**
  - Animasiya rossanu*
  - Kitab tortibah vo illüstrasiyasl*
  - Poster afikasi*

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Animasiya rəssamı | None | 30 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Qrafika (dəzgah qrafikası, kitab tərtibatı və illüstrasiyası, poster qrafikası, animasiya rəssamı) | 37 | 30 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Qrafika (dəzgah qrafikası, kitab tərtibatı və illüstrasiyası, poster qrafikası, animasiya rəssamı) | 37 | 30 |

</details>

---

### Proqram № 71

#### Blok 1 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050640` | Yangm tahlükosizliyi mühəndisliyi |
| `050650` | Yanğın təhlükəsizliyi mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006044` Yanğın təhlükəsizliyi mühəndisliyi**
  - Yangm tohlükasizliyinin idaro olunmast

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Fövqəladə Hallar Nazirliyinin Akademiyası | Yanğın təhlükəsizliyinin idarə olunması | None | None |
| Milli Aviasiya Akademiyası | Aviasiya təhlükəsizliyinin idarə olunması | 62.5 | 48.5 |

</details>

---

### Ümumi / Digər Proqramlar

#### Blok 1 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `050634` | Proseslarin avtomatlasdtnlmast mühəndisliyi |
| `050628` | Proseslarin avtomatla'drnlmas |
| `050628` | Mühəndisliyi |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `T 090300` | Dəmiryol nəqliyyatmda avtomatika, telemexanika və rabita |
| `T 170100` | Texniki sistemlordo idaraetma və informatika |
| `T 170200` | Texnoloji proseslarin və istehsalatların avtomatla'drnlmasr (sahələr üzrə) |
| `T 170300` | Robotlar və robototexniki sistemlar |
| `T 170400` | Energetika sistemlarinin avtomatik idara edilmasi |
| `T 170900` | Ususlara avtomatla'dtnlnus nazarat sistemlarinin istismarı |
| `T 171000` | Avtomatlaşdırılmış sistemlərin informasiya təhlükəsizliyinin kompleks təminatı |
| `T 180700` | Avtomatla'drrma və informasiya texnikası (Tempus proqranu) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `7006033` Mühəndislik fizikası**
  - Fiziki elektronika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Fiziki elektronika | 58 | 58 |

</details>

---
