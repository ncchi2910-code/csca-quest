import { UI } from "../lib/i18n.js";
import QuestionCard from "./QuestionCard.jsx";

export default function Results({ result, lang, onToggleLang, onExit }) {
  const t = UI[lang];
  const { questions, answers, score } = result;

  let msg = t.tryAgain;
  if (score === 100) msg = t.perfect;
  else if (score >= 80) msg = t.great;
  else if (score >= 60) msg = t.good;

  const wrong = questions
    .map((q, i) => ({ q, i }))
    .filter(({ q, i }) => answers[i] !== q.answer);

  return (
    <div className="screen results">
      <div className="card score-card">
        <div className="score-ring" style={{ "--p": score }}>
          <div className="score-num">{score}</div>
          <div className="score-max">/ 100</div>
        </div>
        <h2>{t.yourScore}</h2>
        <p className="score-msg">{msg}</p>
        <div className="score-detail">
          {answers.filter((a, i) => a === questions[i].answer).length} / {questions.length} {t.correct.replace("!", "")}
        </div>
        <button className="btn primary big" onClick={onExit}>{t.backHome}</button>
      </div>

      {wrong.length > 0 && (
        <div className="review-list">
          <h3>📝 {t.reviewMistakes} ({wrong.length})</h3>
          {wrong.map(({ q, i }) => (
            <QuestionCard
              key={q.id}
              question={q}
              lang={lang}
              index={i}
              total={questions.length}
              selected={answers[i]}
              revealed={true}
              onSelect={() => {}}
              onToggleLang={onToggleLang}
            />
          ))}
        </div>
      )}
    </div>
  );
}
