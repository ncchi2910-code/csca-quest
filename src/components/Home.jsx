import { useState } from "react";
import { UI, subjectLabel } from "../lib/i18n.js";
import { BADGES } from "../lib/game.js";

const SUBJECTS = [
  { key: "math", emoji: "📐", active: true },
  { key: "chinese", emoji: "🀄", active: true },
  { key: "physics", emoji: "⚛️", active: false },
  { key: "chemistry", emoji: "🧪", active: false }
];

export default function Home({ progress, lang, questions, onStart, onToggleRealOnly, onOpenReview }) {
  const t = UI[lang];
  const [subject, setSubject] = useState(null);

  const countFor = (subj) =>
    questions.filter((q) => q.subject === subj && (!progress.realOnly || q.source !== "AI-generated")).length;

  return (
    <div className="home">
      <div className="hero">
        <h1>{t.appName}</h1>
        <p>{t.tagline}</p>
      </div>

      <section>
        <h2>{t.chooseSubject}</h2>
        <div className="grid subjects">
          {SUBJECTS.map((s) => {
            const n = countFor(s.key);
            const disabled = !s.active || n === 0;
            return (
              <button
                key={s.key}
                className={`tile subject-tile ${subject === s.key ? "tile-active" : ""} ${disabled ? "tile-disabled" : ""}`}
                onClick={() => !disabled && setSubject(s.key)}
                disabled={disabled}
              >
                <span className="tile-emoji">{s.emoji}</span>
                <span className="tile-title">{subjectLabel(s.key, lang)}</span>
                <span className="tile-sub">
                  {s.active ? `${n} ${t.questionsCount}` : t.comingSoon}
                </span>
              </button>
            );
          })}
        </div>
      </section>

      {subject && (
        <section className="modes-section">
          <h2>{t.chooseMode}</h2>
          <label className="real-only">
            <input
              type="checkbox"
              checked={progress.realOnly}
              onChange={onToggleRealOnly}
            />
            {t.realOnly}
          </label>
          <div className="grid modes">
            <button className="tile mode-tile" onClick={() => onStart(subject, "practice")}>
              <span className="tile-emoji">📚</span>
              <span className="tile-title">{t.practice}</span>
              <span className="tile-sub">{t.practiceDesc}</span>
            </button>
            <button className="tile mode-tile" onClick={() => onStart(subject, "exam")}>
              <span className="tile-emoji">⏱️</span>
              <span className="tile-title">{t.exam}</span>
              <span className="tile-sub">{t.examDesc}</span>
            </button>
            <button className="tile mode-tile" onClick={onOpenReview}>
              <span className="tile-emoji">🎯</span>
              <span className="tile-title">{t.review}</span>
              <span className="tile-sub">{t.reviewDesc}</span>
            </button>
          </div>
        </section>
      )}

      <section className="badges-section">
        <h2>🏆 {lang === "en" ? "Badges" : "徽章"}</h2>
        <div className="badge-row">
          {BADGES.map((b) => {
            const earned = progress.badges.includes(b.id);
            return (
              <div key={b.id} className={`badge ${earned ? "badge-on" : "badge-off"}`} title={b[lang]}>
                <span className="badge-emoji">{b.emoji}</span>
                <span className="badge-name">{b[lang]}</span>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}
