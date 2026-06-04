import MathText from "../lib/MathText.jsx";
import { UI, topicLabel } from "../lib/i18n.js";

const LETTERS = ["A", "B", "C", "D", "E", "F"];

// Presentational question card. Parent owns selection/reveal state.
export default function QuestionCard({
  question,
  lang,
  index,
  total,
  selected,
  revealed,
  onSelect,
  onToggleLang
}) {
  const t = UI[lang];
  const q = question;
  const isReal = q.source !== "AI-generated";

  return (
    <div className="card question-card">
      <div className="q-top">
        <div className="q-meta">
          <span className="q-counter">
            {lang === "zh" ? `${t.question} ${index + 1} ${t.of} ${total} ${t.question === "第" ? "题" : ""}` : `${t.question} ${index + 1} ${t.of} ${total}`}
          </span>
          <span className="chip topic-chip">{topicLabel(q.topic, lang)}</span>
          <span className={`chip ${isReal ? "real-chip" : "ai-chip"}`}>
            {isReal ? t.examTag : t.aiTag}
          </span>
        </div>
        <button className="lang-toggle" onClick={onToggleLang} title="EN / 中文">
          {lang === "en" ? "中文" : "EN"}
        </button>
      </div>

      <div className="q-text">
        <MathText>{q.question[lang]}</MathText>
      </div>

      <div className="options">
        {q.options[lang].map((opt, i) => {
          let cls = "option";
          if (revealed) {
            if (i === q.answer) cls += " opt-correct";
            else if (i === selected) cls += " opt-wrong";
          } else if (i === selected) {
            cls += " opt-selected";
          }
          return (
            <button
              key={i}
              className={cls}
              onClick={() => onSelect(i)}
              disabled={revealed}
            >
              <span className="opt-letter">{LETTERS[i]}</span>
              <span className="opt-body">
                <MathText>{opt}</MathText>
              </span>
              {revealed && i === q.answer && <span className="opt-mark">✓</span>}
              {revealed && i === selected && i !== q.answer && (
                <span className="opt-mark">✗</span>
              )}
            </button>
          );
        })}
      </div>

      {revealed && (
        <div className={`feedback ${selected === q.answer ? "fb-correct" : "fb-wrong"}`}>
          <div className="fb-head">
            {selected === q.answer ? `✅ ${t.correct}` : `❌ ${t.wrong}`}
          </div>
          <div className="fb-exp">
            <span className="exp-title">{t.explanation}:</span>
            <MathText className="exp-body">{q.explanation[lang]}</MathText>
          </div>
        </div>
      )}
    </div>
  );
}
