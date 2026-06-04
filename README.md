# CSCA Quest 🎓

A fun, bilingual (English ↔ 中文) web game to help prepare for the **CSCA**
(China Scholastic Competency Assessment). Practice mode, timed mock exams,
XP / levels / streaks / badges, and per-topic weak-spot tracking — all stored
locally in the browser (no backend).

## Tech stack
- **Vite + React** (JavaScript)
- **KaTeX** for math formulas (stored as LaTeX inside `$...$`)
- **localStorage** for progress (XP, level, streak, per-topic accuracy)
- Designed for both phone and desktop

## Run locally
```bash
npm install
npm run dev      # http://localhost:5173
npm run build    # production build into dist/
npm run preview  # preview the production build
```

## Question bank — `data/questions.json`
Each question is bilingual (EN + ZH) with 4 distinct options, a 0-based
`answer` index, and a **step-by-step** `explanation` (numbered lines split by
`\n`). See `scripts/` for how the real-exam bank was generated.

Current contents (83 questions):
- **Math — 47** from the real CSCA January 2026 paper (`source: "CSCA_Jan_2026"`),
  extracted from `materials/toan/CSCA_Jan_en.pdf` + `CSCA_Jan_cn.pdf`,
  cross-checked EN↔CN, every answer re-solved independently.
  Topics: coordinate-geometry, trigonometry, sequence, function, inequality,
  set, logarithm, vector, complex, probability.
- **Chinese — 36** humanities-track vocabulary flashcards
  (`source: "大文科 (Humanities Chinese)"`, `topic: "vocab"`).

Physics & Chemistry are wired into the UI as "Coming soon" — drop new PDFs into
`materials/<subject>/` to extend later. **Do not invent Physics/Chemistry data.**

### Question schema
```json
{
  "id": "math-jan2026-q03",
  "subject": "math",              // math | physics | chemistry | chinese
  "topic": "inequality",
  "source": "CSCA_Jan_2026",      // "AI-generated" for practice-only items
  "points": 2,
  "difficulty": "medium",          // easy | medium | hard
  "question":    { "en": "...", "zh": "..." },
  "options":     { "en": ["A","B","C","D"], "zh": ["A","B","C","D"] },
  "answer": 0,
  "explanation": { "en": "1. ...\n2. ...", "zh": "1. ...\n2. ..." }
}
```

## Adding more practice questions
Real-exam questions (`source` ≠ `"AI-generated"`) are the trusted core and must
not be edited or removed. To add extra practice items later, ask Claude Code to
write them with `source: "AI-generated"` and ids like `math-gen-0001`; the game
flags them as "Practice" and the home screen has a **"Real exam questions only"**
toggle to hide them.

## Regenerating the real-exam bank
```bash
python3 scripts/build_jan2026.py       > /tmp/jan.json
python3 scripts/build_chinese_vocab.py > /tmp/vocab.json
# data/questions.json = jan + vocab (+ any AI-generated items appended)
```
The Python generators use raw strings so `json.dump` emits correct LaTeX escaping.
