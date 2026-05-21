<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Audit Sistem Informasi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg: #f7f5f0;
    --surface: #ffffff;
    --surface2: #f0ede6;
    --border: #e0dbd0;
    --border2: #ccc6b8;
    --text: #1a1916;
    --text2: #5a5650;
    --text3: #8a8580;
    --accent: #2d5a3d;
    --accent-light: #e8f0ea;
    --accent-mid: #4a8c61;
    --empty-bg: #f7f5f0;
    --empty-border: #e0dbd0;
    --empty-text: #b0aa9e;
    --header-bg: #1a2e22;
  }
  body {
    font-family: 'Outfit', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    font-size: 15px;
    line-height: 1.6;
  }
  header {
    background: var(--header-bg);
    padding: 2.5rem 2rem 2rem;
    position: relative;
    overflow: hidden;
  }
  header::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 220px; height: 220px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.06);
  }
  header::after {
    content: '';
    position: absolute;
    bottom: -60px; right: 60px;
    width: 140px; height: 140px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.04);
  }
  .header-inner {
    max-width: 860px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
  }
  .header-top-row {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
  }
  .header-switcher {
    display: inline-flex;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px;
    padding: 3px;
    gap: 2px;
    flex-shrink: 0;
    margin-top: 2px;
  }
  .header-switcher button {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.04em;
    padding: 4px 12px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    background: transparent;
    color: rgba(255,255,255,0.4);
    transition: all 0.2s;
  }
  .header-switcher button.active {
    background: rgba(255,255,255,0.12);
    color: rgba(255,255,255,0.9);
  }
  .header-switcher button:not(.active):hover {
    color: rgba(255,255,255,0.65);
    background: rgba(255,255,255,0.06);
  }
  .header-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    color: rgba(255,255,255,0.4);
    text-transform: uppercase;
    margin-bottom: 0.5rem;
  }
  header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(1.8rem, 4vw, 2.6rem);
    color: #ffffff;
    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 0.4rem;
  }
  header h1 em { font-style: italic; color: rgba(255,255,255,0.6); }
  .header-meta { font-size: 13px; color: rgba(255,255,255,0.45); margin-top: 0.3rem; }
  .header-actions {
    margin-top: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }
  .rps-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.15);
    color: rgba(255,255,255,0.85);
    padding: 7px 14px;
    border-radius: 6px;
    text-decoration: none;
    font-size: 13px;
    font-family: 'Outfit', sans-serif;
    transition: background 0.2s, border-color 0.2s;
  }
  .rps-btn:hover { background: rgba(255,255,255,0.18); border-color: rgba(255,255,255,0.25); }
  .rps-btn svg { width: 14px; height: 14px; opacity: 0.8; }

  main {
    max-width: 860px;
    margin: 0 auto;
    padding: 1.5rem 2rem 4rem;
  }
  .week-list { display: flex; flex-direction: column; gap: 2px; margin-top: 0.5rem; }
  .week-row {
    display: grid;
    grid-template-columns: 46px 1fr;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    transition: border-color 0.15s, box-shadow 0.15s;
  }
  .week-row:hover { border-color: var(--border2); box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
  .week-row.exam-row { background: var(--header-bg); border-color: transparent; }
  .week-num {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding-top: 13px;
    background: var(--surface2);
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    color: var(--text3);
    border-right: 1px solid var(--border);
    flex-shrink: 0;
  }
  .exam-row .week-num {
    background: rgba(255,255,255,0.06);
    border-right-color: rgba(255,255,255,0.08);
    color: rgba(255,255,255,0.5);
    padding-top: 0;
    align-items: center;
  }
  .week-body { padding: 12px 16px; }
  .week-topic { font-weight: 500; font-size: 14px; color: var(--text); }
  .exam-row .week-topic {
    color: #fff;
    font-family: 'DM Serif Display', serif;
    font-weight: 400;
    font-style: italic;
    font-size: 14px;
  }
  .week-details {
    display: grid;
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid var(--border);
    gap: 10px;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  }
  .detail-col { display: flex; flex-direction: column; gap: 4px; }
  .detail-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text3);
    margin-bottom: 2px;
  }
  .detail-link {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 13px;
    color: var(--accent);
    text-decoration: none;
    line-height: 1.5;
  }
  .detail-link:hover { text-decoration: underline; color: var(--accent-mid); }
  .detail-link svg { width: 12px; height: 12px; flex-shrink: 0; opacity: 0.6; }
  .detail-text { font-size: 13px; color: var(--text2); font-style: italic; }
  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text3);
    padding: 1.5rem 0 0.5rem;
  }
  @media (max-width: 600px) {
    header, .switcher-wrap, main { padding-left: 1rem; padding-right: 1rem; }
    .week-details { grid-template-columns: 1fr; }
    header h1 { font-size: 1.6rem; }
  }
</style>
</head>
<body>

<header>
  <div class="header-inner">
    <div class="header-top-row">
      <div>
        <div class="header-label">Politeknik Keuangan Negara STAN</div>
        <h1>Audit <em>Sistem</em> Informasi</h1>
      </div>
      <div class="header-switcher">
        <button id="btn-genap2026" class="active" onclick="switchSemester('genap2026')">Genap 2026</button>
        <button id="btn-ganjil2025" onclick="switchSemester('ganjil2025')">Ganjil 2025</button>
      </div>
    </div>
    <div class="header-meta">Teuku Raja Irfan Radarma &nbsp;&middot;&nbsp; <span id="header-semester">Genap 2026</span></div>
    <div class="header-actions">
      <a href="https://github.com/irfanradarma/Audit-SI/raw/main/ASP%20STR_2514926D_Audit%20Sistem%20Informasi.pdf" target="_blank" class="rps-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 15V3m0 12l-4-4m4 4l4-4M2 17l.621 2.485A2 2 0 0 0 4.561 21h14.877a2 2 0 0 0 1.94-1.515L22 17"/></svg>
        Unduh RPS
      </a>
    </div>
  </div>
</header>


<main>
  <div id="content-genap2026"></div>
  <div id="content-ganjil2025" style="display:none"></div>
</main>

<script>
const iconLink = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>`;
const iconFile = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`;
const iconVideo = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>`;

function link(href, text, icon) {
  icon = icon || iconLink;
  return `<a href="${href}" target="_blank" class="detail-link">${icon} ${text}</a>`;
}

function buildCols(w) {
  if (w.exam) return '';
  const cols = [
    { label: 'Bahan Ajar', items: w.slides || [] },
    { label: 'Praktikum', items: w.praktikum || [] },
    { label: 'Lain-Lain', items: w.lain || [] }
  ].filter(c => c.items.length > 0);
  if (!cols.length) return '';
  return `<div class="week-details">${cols.map(c =>
    `<div class="detail-col"><div class="detail-label">${c.label}</div>${c.items.join('')}</div>`
  ).join('')}</div>`;
}

const dataGanjil2025 = [
  { num:1, topic:"IT Governance",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/01%20-%20IT%20Governance%20Concept.pptx","01 – IT Governance: Concept",iconFile)],
    praktikum:[],
    lain:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/COBIT_2019_Framework_Introduction.pdf","COBIT 2019 Framework by ISACA",iconFile)]
  },
  { num:2, topic:"IT Governance Audit",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/02%20-%20IT%20Governance%20Audit.pptx","02 – IT Governance Audit",iconFile)],
    praktikum:[],
    lain:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/COBIT_2019_Framework_Governance.pdf","COBIT 2019 Governance & Management Objectives",iconFile)]
  },
  { num:3, topic:"IS Acquisition, Development & Implementation I",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/03%20-%20IS%20Acquisition%20%26%20Development.pptx","03 – IS Acquisition & Development",iconFile)],
    praktikum:[link("https://irfanradarma.github.io/Audit-SI/mind-map-audit5.html","Mind Map App 7 Audit-5"),link("https://irfanradarma.github.io/Audit-SI/mind-map-sisfo2.html","Mind Map App 7 Sisfo-2")],
    lain:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/CISA%20Review%20Manual%2027th%20Edition-2019.pdf","CISA Review Manual",iconFile)]
  },
  { num:4, topic:"IS Acquisition, Development & Implementation II",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/04%20-%20IS%20Implementation.pptx","04 – IS Implementation",iconFile)],
    praktikum:[`<span class="detail-text">Quiz via LMS</span>`],
    lain:[link("https://irfanradarma.github.io/Audit-SI/exercise.html","Try Out")]
  },
  { num:5, topic:"IS Operations & Business Resilience",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/05%20-%20IS%20Operations%20and%20Business%20Resilience.pptx","05 – IS Operations and Business Resilience",iconFile)],
    praktikum:[], lain:[]
  },
  { num:6, topic:"Protection of Information Assets: Part A",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/06%20-%20Information%20Asset%20Security%20and%20Control.pptx","06 – Information Asset Security and Control",iconFile)],
    praktikum:[], lain:[]
  },
  { num:7, topic:"Protection of Information Assets: Part B",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/07%20-%20Security%20Event%20Management.pptx","07 – Security Event Management",iconFile)],
    praktikum:[`<span class="detail-text">Quiz via LMS</span>`],
    lain:[link("https://irfanradarma.github.io/Audit-SI/try-out.html","Try Out Domain 1–5"),link("https://forms.gle/JNBbpYAWQXh7wtPH6","Tugas VII – Lessons Learned")]
  },
  { num:8, exam:"UTS — Ujian Tengah Semester" },
  { num:9, topic:"Basic of Data Analysis",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/09%20-%20Basic%20Data%20Analysis.pptx","09 – Basic Data Analysis",iconFile)],
    praktikum:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/Data%20Impor.zip","Impor Data",iconFile),link("https://github.com/irfanradarma/PTIK-STAN/raw/main/Slides/06/spotify_data_light.xlsx","Data Spotify",iconFile)],
    lain:[link("https://www.youtube.com/watch?v=Kwn8GJyNv64","Tutorial Pivot Table",iconVideo),link("https://www.youtube.com/watch?v=bhfRlU_bNmw","Tutorial SUM / SUMIF / SUMIFS",iconVideo),link("https://www.youtube.com/watch?v=OekP7P-Xw4I","Tutorial CONSOLIDATE",iconVideo),link("https://www.youtube.com/watch?v=JNZqRYkgZ4c","Tutorial Filtering Data",iconVideo),link("https://www.youtube.com/watch?v=UV-SPoVkDaU","Tutorial Advanced Filters",iconVideo),link("https://www.youtube.com/watch?v=LKbRkIIVG60","Tutorial Vlookup",iconVideo)]
  },
  { num:10, topic:"Risk and Control",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/10%20-%20Risiko%20dan%20Pengendalian.pptx","10 – Risiko dan Pengendalian",iconFile)],
    praktikum:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/Week%2010%20Practice.xlsx","Week 10 Practice",iconFile),`<span class="detail-text">Tugas VIII – Simulasi ToE</span>`,link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/Assignment%20of%20Week%2010.xlsx","Sales Data",iconFile),link("https://forms.gle/UomXmnZEnLGkxyWz9","Submission Form")],
    lain:[link("https://drive.google.com/drive/folders/1KWQqTYpNElnZxWfQIZvHP4nMVipOfils","Praktik Pengujian AppCon MYOB"),link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/Fun%20Excel%20II.xlsx","Fun Excel Comp II Data",iconFile)]
  },
  { num:11, topic:"Parallel Simulation",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/11%20-%20Simulasi%20Sejajar.pptx","11 – Simulasi Sejajar",iconFile)],
    praktikum:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/payroll-jan1-5.zip","Payroll Jan 1–5",iconFile),link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/payroll-jan6-7.zip","Payroll Jan 6–7",iconFile),link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/payroll-2025.csv","Payroll 2025",iconFile)],
    lain:[]
  },
  { num:12, topic:"Sampling and Statistical Approach",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/12.%20Sampling%20dan%20Pendekatan%20Statistik.pptx","12 – Sampling dan Pendekatan Statistik",iconFile)],
    praktikum:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/week12%20-%20Latihan%20Anomaly.xlsx","Data latihan anomali",iconFile)],
    lain:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/Tugas%20Week%2012.pptx","Instruksi Tugas Week 12",iconFile),link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/12%20-%20data%20absensi.csv","Data Absensi",iconFile),link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/12%20-%20audit_log_wifi_kampus.csv","Data Log Jaringan",iconFile),link("https://forms.gle/BfQk7hNuQbunQDDm7","Submit Tugas")]
  },
  { num:13, topic:"Substantive Testing: Sales Cycle",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/13.%20Asersi%20Siklus%20Penjualan.pptx","13 – Audit Siklus Penjualan",iconFile)],
    praktikum:[`<span class="detail-text">Kuis via LMS</span>`],
    lain:[]
  },
  { num:14, topic:"Substantive Testing: Expenditure Cycle",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/14.%20Asersi%20Siklus%20Pengeluaran.pptx","14 – Audit Siklus Pembelian",iconFile)],
    praktikum:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Externals/14%20-%20Latihan%20Data%20Pembelian.xls","Data Pembelian",iconFile)],
    lain:[]
  },
  { num:15, topic:"Audit Report",
    slides:[link("https://github.com/irfanradarma/Audit-SI/raw/main/Slides/15.%20Laporan%20Audit.pptx","15 – (Bukan) Laporan Audit",iconFile)],
    praktikum:[],
    lain:[link("https://www.youtube.com/watch?v=zcp2Ku5T8h8","Hyperlink Excel Tutorial",iconVideo)]
  },
  { num:16, exam:"UAS — Ujian Akhir Semester" }
];

const dataGenap2026 = dataGanjil2025.map(w =>
  w.exam ? { ...w } : { num: w.num, topic: w.topic, slides: [], praktikum: [], lain: [] }
);

function renderList(data, containerId) {
  const container = document.getElementById(containerId);
  const pre  = data.slice(0, 7);
  const exam1 = data[7];
  const post = data.slice(8, 15);
  const exam2 = data[15];

  function weekHTML(w) {
    if (w.exam) {
      return `<div class="week-row exam-row">
        <div class="week-num">${w.num}</div>
        <div class="week-body"><div class="week-topic">${w.exam}</div></div>
      </div>`;
    }
    const cols = buildCols(w);
    return `<div class="week-row">
      <div class="week-num">${w.num}</div>
      <div class="week-body">
        <div class="week-topic">${w.topic}</div>
        ${cols}
      </div>
    </div>`;
  }

  let html = '';
  html += `<div class="section-label">Pra-UTS</div><div class="week-list">`;
  pre.forEach(w => html += weekHTML(w));
  html += weekHTML(exam1);
  html += `</div><div class="section-label">Pasca-UTS</div><div class="week-list">`;
  post.forEach(w => html += weekHTML(w));
  html += weekHTML(exam2);
  html += `</div>`;
  container.innerHTML = html;
}

function switchSemester(code) {
  document.getElementById('content-genap2026').style.display = code === 'genap2026' ? '' : 'none';
  document.getElementById('content-ganjil2025').style.display = code === 'ganjil2025' ? '' : 'none';
  document.getElementById('btn-genap2026').className = code === 'genap2026' ? 'active' : '';
  document.getElementById('btn-ganjil2025').className = code === 'ganjil2025' ? 'active' : '';
  const label = code === 'genap2026' ? 'Genap 2026' : 'Ganjil 2025';
  document.getElementById('header-semester').textContent = label;
}

renderList(dataGenap2026, 'content-genap2026');
renderList(dataGanjil2025, 'content-ganjil2025');
</script>
</body>
</html>