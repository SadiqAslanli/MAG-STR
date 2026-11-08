"use client";

import { useMemo, useState } from "react";

type BachelorSpecialty = {
  code: string | null;
  name: string;
  sourceText: string;
};

type UniversityMatch = {
  university: string;
  specialty: string;
  eligibleMasterProgramCode: string | null;
  eligibleMasterProgram: string | null;
  eligibleSpecializationSource: string;
  matchConfidence: number;
  paidScore?: number | null;
  paidScoreMax?: number | null;
  paidStatus?: string | null;
  freeScore?: number | null;
  freeScoreMax?: number | null;
  freeStatus?: string | null;
  hasAptitudeExam?: boolean;
  paidAptitudeScore?: number | null;
  freeAptitudeScore?: number | null;
};

export type FinderMapping = {
  sourcePage: number;
  bachelorSpecialties: BachelorSpecialty[];
  programNumber: number | null;
  minimumScore: number | null;
  universityMatches: UniversityMatch[];
};

type BachelorOption = {
  id: string;
  code: string | null;
  name: string;
};

type ResultSpecialty = {
  key: string;
  name: string;
  masterCode: string | null;
  masterName: string | null;
  minimumScore: number | null;
  sourcePage: number;
  paidScore: number | null;
  paidScoreMax?: number | null;
  paidStatus: string | null;
  freeScore: number | null;
  freeScoreMax?: number | null;
  freeStatus: string | null;
  hasAptitudeExam?: boolean;
  paidAptitudeScore?: number | null;
  freeAptitudeScore?: number | null;
  verdict?: "free" | "paid" | "insufficient" | "min_not_met";
  verdictDiff?: number | null;
};

type UniversityResult = {
  name: string;
  specialties: ResultSpecialty[];
};

type SearchMode = "eligibility" | "chance";
type FilterMode = "all" | "free" | "paid" | "insufficient";

const RUSSIAN_TO_AZ_DICT: Record<string, string> = {
  "учитель русского языка": "rus dili və ədəbiyyatı müəllimliyi",
  "преподаватель русского языка": "rus dili və ədəbiyyatı müəllimliyi",
  "русский язык и литература": "rus dili və ədəbiyyatı müəllimliyi",
  "русский язык": "rus dili",
  "русская филология": "filologiya rus dili",
  "учитель": "müəllimliyi",
  "преподаватель": "müəllimliyi",
  "переводчик": "tərcümə",
  "перевод": "tərcümə",
  "филология": "filologiya",
  "экономика": "iqtisadiyyat",
  "компьютерная инженерия": "kompüter mühəndisliyi",
  "компьютерные науки": "kompüter elmləri",
  "компьютер": "kompüter",
  "инженерия": "mühəndisliyi",
  "юриспруденция": "hüquqşünaslıq",
  "право": "hüquqşünaslıq",
  "международные отношения": "beynəlxalq münasibətlər",
  "финансы": "maliyyə",
  "менеджмент": "menecment",
  "маркетинг": "marketinq",
  "бухгалтерия": "mühasibat",
  "педагогика": "pedaqogika",
  "психология": "psixologiya",
  "журналистика": "jurnalistika",
  "туризм": "turizm",
  "дизайн": "dizayn",
  "архитектура": "memarlıq",
  "биология": "biologiya",
  "химия": "kimya",
  "физика": "fizika",
  "математика": "riyaziyyat",
  "история": "tarix",
  "география": "coğrafiya",
  "экология": "ekologiya",
};

function translateSearchQuery(input: string): string {
  let q = input.trim().toLowerCase();
  for (const [rus, az] of Object.entries(RUSSIAN_TO_AZ_DICT)) {
    if (q.includes(rus)) {
      q = q.replace(new RegExp(rus, "gi"), az);
    }
  }
  // Typos & phonetic variants like "rus ili" -> "rus dili", "muelim" -> "müəllim"
  q = q.replace(/\brus\s+ili\b/gi, "rus dili");
  q = q.replace(/muel+im/gi, "müəllim");
  return q;
}

function getQueryTokens(input: string): string[] {
  const translated = translateSearchQuery(input);
  return translated
    .toLocaleLowerCase("az")
    .replace(/və|va|ve/g, " ")
    .replace(/[^a-z0-9əıöüşçğ\s]/g, " ")
    .split(/\s+/)
    .filter(Boolean)
    .map((w) => normalize(w))
    .filter((w) => w.length > 1);
}

function normalize(value: string) {
  const translated = translateSearchQuery(value);
  return translated
    .toLocaleLowerCase("az")
    .replace(/və|va|ve/g, "ve")
    .replace(/ə/g, "e")
    .replace(/ı/g, "i")
    .replace(/ö/g, "o")
    .replace(/ü/g, "u")
    .replace(/ş/g, "s")
    .replace(/ç/g, "c")
    .replace(/ğ/g, "g")
    .replace(/[^a-z0-9]/g, "");
}

function editDistance(left: string, right: string) {
  const previous = Array.from({ length: right.length + 1 }, (_, index) => index);

  for (let row = 1; row <= left.length; row += 1) {
    let diagonal = previous[0];
    previous[0] = row;

    for (let column = 1; column <= right.length; column += 1) {
      const above = previous[column];
      previous[column] = Math.min(
        previous[column] + 1,
        previous[column - 1] + 1,
        diagonal + (left[row - 1] === right[column - 1] ? 0 : 1),
      );
      diagonal = above;
    }
  }

  return previous[right.length];
}

function similarity(left: string, right: string) {
  const normalizedLeft = normalize(left);
  const normalizedRight = normalize(right);

  if (!normalizedLeft || !normalizedRight) {
    return 0;
  }

  const distance = editDistance(normalizedLeft, normalizedRight);
  return 1 - distance / Math.max(normalizedLeft.length, normalizedRight.length);
}

function cleanBachelorName(name: string) {
  return name
    .replace(/^[\s*•·\-]+/, "")
    .replace(/\bD\s*M\s*-\s*2024\b/gi, "")
    .replace(/\bva\b/gi, "və")
    .replace(/\bvo\b/gi, "və")
    .replace(/mü\s*ə\s*llimliyi/gi, "müəllimliyi")
    .replace(/mü\s*ə\s*ndisliyi/gi, "mühəndisliyi")
    .replace(/mühə\s*ndisliyi/gi, "mühəndisliyi")
    .replace(/mühondis/gi, "mühəndis")
    .replace(/mühandis/gi, "mühəndis")
    .replace(/miihandis/gi, "mühəndis")
    .replace(/gə\s*miqay\s*ırma/gi, "gəmiqayırma")
    .replace(/gomiqayrrma/gi, "gəmiqayırma")
    .replace(/qurğ\s+u/gi, "qurğu")
    .replace(/nə\s+qliyyat/gi, "nəqliyyat")
    .replace(/sə\s+rrüfat/gi, "təsərrüfat")
    .replace(/\s+/g, " ")
    .trim();
}

function getUniversityResults(
  mappings: FinderMapping[],
  selected: BachelorOption,
  userScore: number | null,
  searchMode: SearchMode,
  filterMode: FilterMode,
): UniversityResult[] {
  const results = new Map<string, Map<string, ResultSpecialty>>();

  for (const mapping of mappings) {
    const applies = mapping.bachelorSpecialties.some((specialty) => {
      if (selected.code && specialty.code) {
        return (
          specialty.code === selected.code &&
          similarity(specialty.name, selected.name) >= 0.72
        );
      }

      return similarity(specialty.name, selected.name) >= 0.82;
    });

    if (!applies) {
      continue;
    }

    for (const match of mapping.universityMatches) {
      let university = results.get(match.university);
      if (!university) {
        university = new Map();
        results.set(match.university, university);
      }

      const key = [
        match.specialty,
        match.eligibleMasterProgramCode ?? "",
        mapping.programNumber ?? "",
      ].join("|");

      if (!university.has(key)) {
        let verdict: "free" | "paid" | "insufficient" | "min_not_met" | undefined;
        let verdictDiff: number | null = null;

        if (searchMode === "chance" && userScore !== null) {
          if (mapping.minimumScore && userScore < mapping.minimumScore) {
            verdict = "min_not_met";
            verdictDiff = mapping.minimumScore - userScore;
          } else if (match.freeScore !== null && match.freeScore !== undefined && userScore >= match.freeScore) {
            verdict = "free";
            verdictDiff = userScore - match.freeScore;
          } else if (match.paidScore !== null && match.paidScore !== undefined && userScore >= match.paidScore) {
            verdict = "paid";
            verdictDiff = match.freeScore ? match.freeScore - userScore : null;
          } else {
            verdict = "insufficient";
            const targetScore = match.paidScore ?? match.freeScore ?? mapping.minimumScore;
            verdictDiff = targetScore ? targetScore - userScore : null;
          }
        }

        university.set(key, {
          key,
          name: match.specialty,
          masterCode: match.eligibleMasterProgramCode,
          masterName: match.eligibleMasterProgram,
          minimumScore: mapping.minimumScore,
          sourcePage: mapping.sourcePage,
          paidScore: match.paidScore ?? null,
          paidScoreMax: match.paidScoreMax ?? null,
          paidStatus: match.paidStatus ?? null,
          freeScore: match.freeScore ?? null,
          freeScoreMax: match.freeScoreMax ?? null,
          freeStatus: match.freeStatus ?? null,
          hasAptitudeExam: match.hasAptitudeExam,
          paidAptitudeScore: match.paidAptitudeScore ?? null,
          freeAptitudeScore: match.freeAptitudeScore ?? null,
          verdict,
          verdictDiff,
        });
      }
    }
  }

  return [...results.entries()]
    .map(([name, specialtiesMap]) => {
      let specialties = [...specialtiesMap.values()];

      if (searchMode === "chance" && userScore !== null && filterMode !== "all") {
        specialties = specialties.filter((s) => {
          if (filterMode === "free") return s.verdict === "free";
          if (filterMode === "paid") return s.verdict === "paid";
          if (filterMode === "insufficient") return s.verdict === "insufficient" || s.verdict === "min_not_met";
          return true;
        });
      }

      return {
        name,
        specialties: specialties.sort((a, b) => a.name.localeCompare(b.name, "az")),
      };
    })
    .filter((u) => u.specialties.length > 0)
    .sort((a, b) => a.name.localeCompare(b.name, "az"));
}

function SearchIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <circle cx="10.8" cy="10.8" r="6.8" />
      <path d="m16 16 4.5 4.5" />
    </svg>
  );
}

function GraduationIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="m2.5 9 9.5-5 9.5 5-9.5 5-9.5-5Z" />
      <path d="M6.5 11.2v5.1c3.2 2.5 7.8 2.5 11 0v-5.1M21.5 9v6" />
    </svg>
  );
}

function ArrowIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M5 12h14M13 6l6 6-6 6" />
    </svg>
  );
}

function SparklesIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="m12 3 1.9 4.7L18.6 9.6l-4.7 1.9L12 16.2l-1.9-4.7L5.4 9.6l4.7-1.9L12 3Z" />
      <path d="M19 15l.9 2.1 2.1.9-2.1.9-.9 2.1-.9-2.1-2.1-.9 2.1-.9.9-2.1Z" />
      <path d="M5 16l.9 2.1 2.1.9-2.1.9-.9 2.1-.9-2.1-2.1-.9 2.1-.9.9-2.1Z" />
    </svg>
  );
}

function BookCheckIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z" />
      <path d="m9 10 2 2 4-4" />
    </svg>
  );
}

function CalculatorIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <rect x="4" y="2" width="16" height="20" rx="3" />
      <line x1="8" y1="6" x2="16" y2="6" />
      <line x1="8" y1="10" x2="10" y2="10" />
      <line x1="14" y1="10" x2="16" y2="10" />
      <line x1="8" y1="14" x2="10" y2="14" />
      <line x1="14" y1="14" x2="16" y2="14" />
      <line x1="8" y1="18" x2="16" y2="18" />
    </svg>
  );
}

export default function EligibilityFinder({
  mappings,
}: {
  mappings: FinderMapping[];
}) {
  const [searchMode, setSearchMode] = useState<SearchMode>("eligibility");
  const [query, setQuery] = useState("");
  const [scoreInput, setScoreInput] = useState<string>("");
  const [selected, setSelected] = useState<BachelorOption | null>(null);
  const [isOpen, setIsOpen] = useState(false);
  const [activeSuggestion, setActiveSuggestion] = useState(0);
  const [filterMode, setFilterMode] = useState<FilterMode>("all");

  const parsedUserScore = useMemo(() => {
    if (!scoreInput.trim()) return null;
    const num = parseFloat(scoreInput.replace(",", "."));
    return isNaN(num) ? null : Math.min(100, Math.max(0, num));
  }, [scoreInput]);

  const bachelorOptions = useMemo(() => {
    const options = new Map<string, BachelorOption>();

    for (const mapping of mappings) {
      for (const specialty of mapping.bachelorSpecialties) {
        // Discard meaningless fragments without code
        if (!specialty.code && (!specialty.name || specialty.name.length < 10 || /^(dili\)|üzrə|etmə|ı ı ı|sistemlər|hiyyə|ləri\b|lər\b)/.test(specialty.name))) {
          continue;
        }

        const name = cleanBachelorName(specialty.name);
        const id = specialty.code
          ? `code:${specialty.code}|name:${normalize(name)}`
          : `name:${normalize(name)}`;

        if (!name || name.length < 4) {
          continue;
        }

        const current = options.get(id);
        if (!current || name.length > current.name.length) {
          options.set(id, { id, code: specialty.code, name });
        }
      }
    }

    return [...options.values()].sort((a, b) =>
      a.name.localeCompare(b.name, "az"),
    );
  }, [mappings]);

  const suggestions = useMemo(() => {
    const normalizedQuery = normalize(query);
    if (!normalizedQuery || selected) {
      return [];
    }
    const queryTokens = getQueryTokens(query);

    return bachelorOptions
      .map((option) => {
        const normCode = normalize(option.code ?? "");
        const normName = normalize(option.name);
        const searchable = `${normCode}${normName}`;

        let score = 0;
        // Exact or prefix code match
        if (normCode && (normCode === normalizedQuery || normCode.startsWith(normalizedQuery))) {
          score += 60;
        }
        // Name starts with query
        if (normName.startsWith(normalizedQuery)) {
          score += 40;
        } else if (searchable.startsWith(normalizedQuery)) {
          score += 35;
        }
        // Substring match in name
        if (normName.includes(normalizedQuery)) {
          score += 25;
        } else if (searchable.includes(normalizedQuery)) {
          score += 20;
        }
        // Token match
        if (queryTokens.length > 0) {
          let matched = 0;
          for (const token of queryTokens) {
            if (normName.includes(token) || normCode.includes(token)) {
              matched++;
            }
          }
          if (matched === queryTokens.length) {
            score += 30;
          } else if (matched > 0) {
            score += matched * 6;
          }
        }

        // Fuzzy similarity fallback
        if (score === 0) {
          const sim = similarity(query, `${option.code ?? ""} ${option.name}`);
          if (sim >= 0.45) {
            score = sim * 10;
          }
        }

        return { option, score };
      })
      .filter(({ score }) => score > 0)
      .sort((a, b) => b.score - a.score || a.option.name.localeCompare(b.option.name, "az"))
      .slice(0, 10)
      .map(({ option }) => option);
  }, [bachelorOptions, query, selected]);

  const universityResults = useMemo(
    () => (selected ? getUniversityResults(mappings, selected, parsedUserScore, searchMode, filterMode) : []),
    [mappings, selected, parsedUserScore, searchMode, filterMode],
  );

  // Statistics for Chance mode
  const chanceStats = useMemo(() => {
    if (!selected || searchMode !== "chance" || parsedUserScore === null) {
      return { freeCount: 0, paidCount: 0, insufficientCount: 0, total: 0 };
    }
    const allResults = getUniversityResults(mappings, selected, parsedUserScore, searchMode, "all");
    let freeCount = 0;
    let paidCount = 0;
    let insufficientCount = 0;
    let total = 0;

    for (const uni of allResults) {
      for (const s of uni.specialties) {
        total++;
        if (s.verdict === "free") freeCount++;
        else if (s.verdict === "paid") paidCount++;
        else insufficientCount++;
      }
    }

    return { freeCount, paidCount, insufficientCount, total };
  }, [mappings, selected, parsedUserScore, searchMode]);

  function chooseOption(option: BachelorOption) {
    setSelected(option);
    setQuery(option.name);
    setIsOpen(false);
    setActiveSuggestion(0);
  }

  function handleInputChange(value: string) {
    setQuery(value);
    setSelected(null);
    setIsOpen(true);
    setActiveSuggestion(0);
  }

  function handleKeyDown(event: React.KeyboardEvent<HTMLInputElement>) {
    if (event.key === "Escape") {
      setIsOpen(false);
      return;
    }

    if (!suggestions.length) {
      return;
    }

    if (event.key === "ArrowDown") {
      event.preventDefault();
      setIsOpen(true);
      setActiveSuggestion((index) => (index + 1) % suggestions.length);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setActiveSuggestion(
        (index) => (index - 1 + suggestions.length) % suggestions.length,
      );
    } else if (event.key === "Enter") {
      event.preventDefault();
      chooseOption(suggestions[activeSuggestion]);
    }
  }

  function switchMode(mode: SearchMode) {
    setSearchMode(mode);
    setFilterMode("all");
    const axtarisEl = document.getElementById("axtaris");
    if (axtarisEl) {
      axtarisEl.scrollIntoView({ behavior: "smooth" });
    }
  }

  return (
    <main>
      <header className="site-header">
        <a className="brand" href="#" aria-label="Magistr seçim ana səhifə">
          <span className="brand-mark">
            <GraduationIcon />
          </span>
          <span className="brand-name">
            magistr<span>.seçim</span>
          </span>
        </a>
        <nav className="main-nav" aria-label="Əsas menyu">
          <a className="nav-active" href="#">
            Ana səhifə
          </a>
          <a href="#haqqinda">Haqqında</a>
        </nav>
        <button
          type="button"
          className="header-link"
          onClick={() => switchMode("chance")}
        >
          Şansını hesabla <ArrowIcon />
        </button>
      </header>

      <section className="hero">
        <div className="hero-inner">
          <div className="hero-copy">
            <div className="eyebrow">
              <span className="eyebrow-dot" />
              MAGİSTRATURA QƏBUL VƏ İXTİSAS SEÇİMİ 2025/2026
            </div>
            <h1>
              Gələcəyini dəqiq seç:
              <br />
              <span>ixtisasına və balına görə.</span>
            </h1>
            <p>
              DİM rəsmi uyğunluq cədvəli əsasında bakalavr ixtisasına uyğun magistr
              proqramlarını öyrən, topladığın bal ilə pulsuz (dövlət sifarişi) və
              ödənişli qəbul şansını dəqiq hesabla.
            </p>

            {/* 2 Primary Mode Buttons as requested */}
            <div className="hero-action-cards">
              <button
                type="button"
                className={`hero-action-btn ${searchMode === "eligibility" ? "hero-action-active" : ""}`}
                onClick={() => switchMode("eligibility")}
              >
                <div className="hero-action-icon">
                  <BookCheckIcon />
                </div>
                <div className="hero-action-text">
                  <strong>İxtisas uyğunluğu</strong>
                  <span>Bakalavr ixtisasına açıq olan magistr proqramlarını tap</span>
                </div>
                <span className="hero-action-badge">Bax</span>
              </button>

              <button
                type="button"
                className={`hero-action-btn hero-action-chance ${searchMode === "chance" ? "hero-action-active" : ""}`}
                onClick={() => switchMode("chance")}
              >
                <div className="hero-action-icon chance-icon-wrap">
                  <CalculatorIcon />
                </div>
                <div className="hero-action-text">
                  <strong>Balıma görə şans hesabla</strong>
                  <span>Balını və ixtisasını yaz, pulsuz/pullu düşməyini gör</span>
                </div>
                <span className="hero-action-badge chance-badge">Hesabla</span>
              </button>
            </div>

            <div className="hero-note">
              <span className="note-check">✓</span>
              DİM rəsmi jurnalı və keçid balları əsasında
            </div>
          </div>

          <div className="hero-art" aria-hidden="true">
            <div className="art-glow" />
            <div className="art-orbit orbit-one" />
            <div className="art-orbit orbit-two" />
            <div className="art-card art-card-back">
              <span className="art-small-line" />
              <span className="art-small-line short" />
              <span className="art-small-line" />
            </div>
            <div className="art-card art-card-main">
              <span className="art-icon">
                <SparklesIcon />
              </span>
              <div className="art-card-title">Pulsuz & Ödənişli</div>
              <div className="art-card-subtitle">Şansını dəqiq bil</div>
              <span className="art-progress">
                <i />
              </span>
              <div className="art-card-footer">
                <span>Dövlət sifarişi</span>
                <strong>✓ Pulsuz</strong>
              </div>
            </div>
            <div className="art-floating floating-top">+ şans hesablama</div>
            <div className="art-floating floating-bottom">
              <span>✓</span> Real ballar
            </div>
            <div className="art-dot dot-one" />
            <div className="art-dot dot-two" />
            <div className="art-dot dot-three" />
          </div>
        </div>
        <div className="hero-wave" />
      </section>

      <section className="finder-section" id="axtaris">
        <div className="section-heading">
          <span className="section-kicker">
            {searchMode === "chance" ? "ŞANS HESABLAYICI" : "UYĞUNLUQ AXTARIŞI"}
          </span>
          <h2>
            {searchMode === "chance"
              ? "Balını və ixtisasını daxil et"
              : "Bakalavr ixtisasını seç"}
          </h2>
          <p>
            {searchMode === "chance"
              ? "Topladığın balı yaz, sənə pulsuz və ya ödənişli düşən ixtisasları dərhal sıralayaq."
              : "Təhsil aldığın bakalavr ixtisasını seç, sənə açıq olan bütün magistr ixtisaslarını və universitetləri gör."}
          </p>

          <div className="mode-toggle-bar">
            <button
              type="button"
              className={`mode-toggle-pill ${searchMode === "eligibility" ? "pill-active" : ""}`}
              onClick={() => { setSearchMode("eligibility"); setFilterMode("all"); }}
            >
              <BookCheckIcon /> İxtisas uyğunluğu
            </button>
            <button
              type="button"
              className={`mode-toggle-pill ${searchMode === "chance" ? "pill-active" : ""}`}
              onClick={() => { setSearchMode("chance"); setFilterMode("all"); }}
            >
              <CalculatorIcon /> Balıma görə şans hesabla
            </button>
          </div>
        </div>

        <div className="search-panel">
          {searchMode === "chance" && (
            <div className="score-input-step">
              <div className="search-step">
                <span className="step-number">01</span>
                <div>
                  <label htmlFor="user-score-input">Topladığın imtahan balı</label>
                  <span className="field-hint">0 - 100 arası topladığın ümumi bal</span>
                </div>
              </div>
              <div className="score-input-wrapper">
                <input
                  id="user-score-input"
                  type="number"
                  min="0"
                  max="100"
                  step="0.5"
                  placeholder="Məsələn: 65.5"
                  value={scoreInput}
                  onChange={(e) => setScoreInput(e.target.value)}
                  className="score-number-input"
                />
                <div className="score-presets">
                  {[45, 50, 60, 70, 80].map((preset) => (
                    <button
                      key={preset}
                      type="button"
                      className={`preset-btn ${parsedUserScore === preset ? "preset-btn-active" : ""}`}
                      onClick={() => setScoreInput(String(preset))}
                    >
                      {preset} bal
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          <div className="bachelor-input-step">
            <div className="search-step">
              <span className="step-number">{searchMode === "chance" ? "02" : "01"}</span>
              <div>
                <label htmlFor="bachelor-search">Bakalavr ixtisasın</label>
                <span className="field-hint">
                  Təhsil aldığın ixtisasın adını və ya kodunu yaz
                </span>
              </div>
            </div>
            <div className="search-control">
              <div className="search-input-wrap">
                <SearchIcon />
                <input
                  id="bachelor-search"
                  type="text"
                  role="combobox"
                  aria-autocomplete="list"
                  aria-expanded={isOpen && suggestions.length > 0}
                  aria-controls="bachelor-suggestions"
                  placeholder="Məsələn, Kompüter mühəndisliyi və ya 050620"
                  value={query}
                  onChange={(event) => handleInputChange(event.target.value)}
                  onFocus={() => setIsOpen(true)}
                  onKeyDown={handleKeyDown}
                  autoComplete="off"
                />
                {selected ? (
                  <button
                    type="button"
                    className="clear-search"
                    aria-label="Seçilmiş ixtisası sil"
                    onClick={() => handleInputChange("")}
                  >
                    ×
                  </button>
                ) : null}
                {isOpen && suggestions.length > 0 ? (
                  <ul
                    className="suggestion-list"
                    id="bachelor-suggestions"
                    role="listbox"
                  >
                    {suggestions.map((option, index) => (
                      <li key={option.id} role="presentation">
                        <button
                          id={`suggestion-${index}`}
                          type="button"
                          role="option"
                          aria-selected={index === activeSuggestion}
                          className={
                            index === activeSuggestion ? "suggestion-active" : ""
                          }
                          onMouseDown={(event) => event.preventDefault()}
                          onClick={() => chooseOption(option)}
                        >
                          <span className="suggestion-icon">
                            <GraduationIcon />
                          </span>
                          <span className="suggestion-text">
                            <strong>{option.name}</strong>
                            {option.code ? <small>{option.code}</small> : null}
                          </span>
                          <ArrowIcon />
                        </button>
                      </li>
                    ))}
                  </ul>
                ) : null}
              </div>
              <span className="option-count">
                {bachelorOptions.length} bakalavr ixtisası mövcuddur
              </span>
            </div>
          </div>
        </div>

        {selected ? (
          <div className="results-section" aria-live="polite">
            <div className="results-heading">
              <div>
                <span className="section-kicker">
                  {searchMode === "chance" && parsedUserScore !== null
                    ? "SƏNİN BALINA UYĞUN NƏTİCƏLƏR"
                    : "SEÇİMİNƏ UYĞUN NƏTİCƏLƏR"}
                </span>
                <h2>
                  {searchMode === "chance" && parsedUserScore !== null
                    ? `Qəbul şansın (${parsedUserScore} bal ilə)`
                    : "Uyğun magistr ixtisasları"}
                </h2>
              </div>
              <div className="result-count">
                <strong>{universityResults.length}</strong>
                <span>universitet</span>
              </div>
            </div>

            <div className="selected-summary">
              <span className="summary-icon">
                <GraduationIcon />
              </span>
              <span>
                <small>Seçdiyin bakalavr ixtisası</small>
                <strong>{selected.name}</strong>
              </span>
              {selected.code ? (
                <span className="summary-code">{selected.code}</span>
              ) : null}
              {searchMode === "chance" && parsedUserScore !== null ? (
                <span className="summary-user-score">
                  Topladığın bal: <strong>{parsedUserScore}</strong>
                </span>
              ) : null}
            </div>

            {/* Chance Mode Statistics Banner & Filter Tabs */}
            {searchMode === "chance" && parsedUserScore !== null && (
              <div className="chance-analytics-card">
                <div className="chance-stats-grid">
                  <div className="stat-box stat-free">
                    <span className="stat-label">Dövlət sifarişi (Pulsuz)</span>
                    <strong className="stat-val">{chanceStats.freeCount}</strong>
                    <span className="stat-desc">ixtisasa pulsuz düşürsən</span>
                  </div>
                  <div className="stat-box stat-paid">
                    <span className="stat-label">Ödənişli əsaslarla</span>
                    <strong className="stat-val">{chanceStats.paidCount}</strong>
                    <span className="stat-desc">ixtisasa balın çatır</span>
                  </div>
                  <div className="stat-box stat-insufficient">
                    <span className="stat-label">Bal çatmayan</span>
                    <strong className="stat-val">{chanceStats.insufficientCount}</strong>
                    <span className="stat-desc">daha yüksək bal tələb edir</span>
                  </div>
                </div>

                <div className="chance-filter-tabs">
                  <button
                    type="button"
                    className={`filter-tab ${filterMode === "all" ? "filter-tab-active" : ""}`}
                    onClick={() => setFilterMode("all")}
                  >
                    Hamısı ({chanceStats.total})
                  </button>
                  <button
                    type="button"
                    className={`filter-tab tab-free ${filterMode === "free" ? "filter-tab-active" : ""}`}
                    onClick={() => setFilterMode("free")}
                  >
                    🟢 Pulsuz düşənlər ({chanceStats.freeCount})
                  </button>
                  <button
                    type="button"
                    className={`filter-tab tab-paid ${filterMode === "paid" ? "filter-tab-active" : ""}`}
                    onClick={() => setFilterMode("paid")}
                  >
                    🔵 Ödənişli düşənlər ({chanceStats.paidCount})
                  </button>
                  <button
                    type="button"
                    className={`filter-tab tab-insufficient ${filterMode === "insufficient" ? "filter-tab-active" : ""}`}
                    onClick={() => setFilterMode("insufficient")}
                  >
                    🔴 Bal çatmayanlar ({chanceStats.insufficientCount})
                  </button>
                </div>
              </div>
            )}

            {searchMode === "chance" && parsedUserScore === null && (
              <div className="score-prompt-warning">
                <span>⚠️</span>
                <div>
                  <strong>Balını daxil etməmisən</strong>
                  <p>Hansı ixtisaslara pulsuz və ya ödənişli düşdüyünü görmək üçün yuxarıdakı sahəyə balını yaz.</p>
                </div>
              </div>
            )}

            {universityResults.length > 0 ? (
              <div className="university-grid">
                {universityResults.map((university, index) => (
                  <article className="university-card" key={university.name}>
                    <div className="university-card-top">
                      <span className="university-index">
                        {String(index + 1).padStart(2, "0")}
                      </span>
                      <span className="university-badge">
                        {university.specialties.length} uyğun ixtisas
                      </span>
                    </div>
                    <h3>{university.name}</h3>
                    <div className="card-divider" />
                    <div className="specialty-list">
                      {university.specialties.map((specialty) => (
                        <div className="specialty-item" key={specialty.key}>
                          <span className={`specialty-check ${specialty.verdict ? `check-${specialty.verdict}` : ""}`}>
                            {specialty.verdict === "free" ? "★" : specialty.verdict === "insufficient" || specialty.verdict === "min_not_met" ? "✕" : "✓"}
                          </span>
                          <div className="specialty-body">
                            <div className="specialty-title-row">
                              <strong>{specialty.name}</strong>
                              {/* Verdict pill in chance mode */}
                              {specialty.verdict === "free" && (
                                <span className="verdict-pill verdict-free">
                                  Dövlət sifarişi (Pulsuz) düşürsən!
                                </span>
                              )}
                              {specialty.verdict === "paid" && (
                                <span className="verdict-pill verdict-paid">
                                  Ödənişli düşürsən
                                </span>
                              )}
                              {specialty.verdict === "insufficient" && (
                                <span className="verdict-pill verdict-insufficient">
                                  Bal çatmır
                                  {specialty.verdictDiff ? ` (${specialty.verdictDiff.toFixed(1)} bal fərq)` : ""}
                                </span>
                              )}
                              {specialty.verdict === "min_not_met" && (
                                <span className="verdict-pill verdict-min">
                                  Minimal bal ödənmir (min. {specialty.minimumScore})
                                </span>
                              )}
                            </div>
                            <span className="master-program">
                              {specialty.masterCode
                                ? `${specialty.masterCode} · `
                                : ""}
                              {specialty.masterName
                                ? cleanBachelorName(specialty.masterName)
                                : ""}
                            </span>
                          </div>
                          <div className="specialty-meta">
                            {/* Pulsuz keçid balı (dövlət sifarişi) - varsa göstərilir */}
                            {specialty.freeScore !== null && specialty.freeScore !== undefined ? (
                              <span
                                className={`score-badge score-free ${specialty.verdict === "free" ? "score-highlighted" : ""}`}
                                title="Dövlət sifarişi (pulsuz) keçid balı"
                              >
                                <span className="badge-tag">Pulsuz</span>
                                <span className="badge-val">
                                  {specialty.freeScoreMax && specialty.freeScoreMax !== specialty.freeScore
                                    ? `${specialty.freeScore}–${specialty.freeScoreMax}`
                                    : specialty.freeScore}
                                </span>
                                {specialty.freeAptitudeScore ? (
                                  <span className="badge-apt">(qab. {specialty.freeAptitudeScore})</span>
                                ) : null}
                              </span>
                            ) : null}

                            {/* Ödənişli keçid balı */}
                            {specialty.paidScore !== null && specialty.paidScore !== undefined ? (
                              <span
                                className={`score-badge score-paid ${specialty.verdict === "paid" ? "score-highlighted" : ""}`}
                                title="Ödənişli əsaslarla keçid balı"
                              >
                                <span className="badge-tag">Ödənişli</span>
                                <span className="badge-val">
                                  {specialty.paidScoreMax && specialty.paidScoreMax !== specialty.paidScore
                                    ? `${specialty.paidScore}–${specialty.paidScoreMax}`
                                    : specialty.paidScore}
                                </span>
                                {specialty.paidAptitudeScore ? (
                                  <span className="badge-apt">(qab. {specialty.paidAptitudeScore})</span>
                                ) : null}
                              </span>
                            ) : specialty.paidStatus === "no_places" ? (
                              <span
                                className="score-badge score-no-paid"
                                title="Ödənişli yer nəzərdə tutulmayıb"
                              >
                                Yalnız pulsuz
                              </span>
                            ) : null}

                            {/* Minimal qəbul balı tələbi */}
                            {specialty.minimumScore ? (
                              <span
                                className="minimum-score"
                                title="İmtahan üzrə tələb olunan minimal bal"
                              >
                                min. {specialty.minimumScore}
                              </span>
                            ) : null}
                          </div>
                        </div>
                      ))}
                    </div>
                  </article>
                ))}
              </div>
            ) : (
              <div className="empty-results">
                <span className="empty-icon">
                  <SearchIcon />
                </span>
                <h3>Meyarlara uyğun ixtisas tapılmadı</h3>
                <p>
                  {filterMode !== "all"
                    ? "Seçilmiş filtr üzrə nəticə yoxdur. Digər filtrləri və ya 'Hamısı' seçimini yoxla."
                    : "Bu bakalavr ixtisası üzrə seçim cədvəlində uyğunluq var, amma universitetlərin ixtisas siyahısı ilə üst-üstə düşən nəticə aşkarlanmadı. Başqa ixtisas kodu ilə yoxla."}
                </p>
              </div>
            )}
          </div>
        ) : (
          <div className="empty-prompt">
            <span className="prompt-icon">
              <SearchIcon />
            </span>
            <div>
              <strong>Nəticələrin burada görünəcək</strong>
              <p>
                {searchMode === "chance"
                  ? "Başlamaq üçün topladığın balı yaz və bakalavr ixtisasını seç."
                  : "Başlamaq üçün yuxarıdakı sahədən bakalavr ixtisasını seç."}
              </p>
            </div>
            <span className="prompt-arrow">
              <ArrowIcon />
            </span>
          </div>
        )}
      </section>

      {/* HAQQINDA BÖLMƏSİ (Rəsmi Qaydalar və Məlumat) */}
      <section className="about-section" id="haqqinda">
        <div className="about-inner">
          <div className="section-heading">
            <span className="section-kicker">MƏLUMAT VƏ QAYDALAR</span>
            <h2>Magistratura Seçimi Haqqında</h2>
            <p>
              Magistraturaya qəbul müsabiqəsində düzgün ixtisas seçimi etmək üçün
              bilməli olduğun əsas qaydalar.
            </p>
          </div>

          <div className="about-grid">
            <article className="about-card">
              <div className="about-card-icon">
                <BookCheckIcon />
              </div>
              <h3>1. İxtisas uyğunluğu nədir?</h3>
              <p>
                Bakalavriat səviyyəsində bitirdiyin ixtisasın DİM tərəfindən
                müəyyən edilmiş magistratura proqramlarına uyğunluğudur.
                Tələbə yalnız öz ixtisasına uyğun gələn magistr proqramlarını
                və ixtisaslaşmalarını seçə bilər.
              </p>
            </article>

            <article className="about-card">
              <div className="about-card-icon">
                <CalculatorIcon />
              </div>
              <h3>2. Minimal bal tələbi nədir?</h3>
              <p>
                Hər bir qəbul proqramı (məsələn, İqtisadiyyat, Kompüter elmləri,
                Mühəndislik və s.) üzrə müsabiqədə iştirak etmək üçün tələb olunan
                ən aşağı imtahan balıdır (adətən 30, 40 və ya 45 bal).
              </p>
            </article>

            <article className="about-card">
              <div className="about-card-icon">
                <SparklesIcon />
              </div>
              <h3>3. Pulsuz və Ödənişli keçid balı</h3>
              <p>
                <strong>Dövlət sifarişi (Pulsuz):</strong> Təhsil haqqını dövlət ödəyir. Ən yüksək nəticə göstərən tələbələr qəbul olur.
                <br />
                <strong>Ödənişli:</strong> Tələbə təhsil haqqını özü ödəyir, keçid balı adətən daha əlçatandır.
              </p>
            </article>

            <article className="about-card">
              <div className="about-card-icon">
                <GraduationIcon />
              </div>
              <h3>4. Qabiliyyət imtahanı tələbi</h3>
              <p>
                Jurnalistika, musiqi, rəssamlıq, dizayn, teatr və xoreoqrafiya
                kimi xüsusi istedad tələb edən ixtisaslarda test imtahanından
                əlavə qabiliyyət imtahanından məqbul nəticə (məs. 6.0 və ya 8.0)
                almaq zəruridir.
              </p>
            </article>
          </div>
        </div>
      </section>

      <footer className="site-footer">
        <a className="brand footer-brand" href="#">
          <span className="brand-mark">
            <GraduationIcon />
          </span>
          <span className="brand-name">
            magistr<span>.seçim</span>
          </span>
        </a>
        <p>Magistratura seçimini daha aydın və dəqiq et.</p>
        <span className="footer-source">Məlumatlar DİM 2025 rəsmi uyğunluq cədvəli və keçid balları əsasındadır</span>
      </footer>
    </main>
  );
}
