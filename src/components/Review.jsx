import { UI, topicLabel } from "../lib/i18n.js";
import { weakTopics } from "../lib/game.js";

export default function Review({ progress, lang, onExit, onPracticeTopic }) {
  const t = UI[lang];
  const all = Object.entries(progress.topics)
    .map(([topic, s]) => ({ topic, ...s, accuracy: s.total ? s.correct / s.total : 0 }))
    .sort((a, b) => a.accuracy - b.accuracy);
  const weak = weakTopics(progress, 1);

  return (
    <div className="screen review-screen">
      <button className="btn ghost" onClick={onExit}>← {t.backHome}</button>
      <h2>🎯 {t.review}</h2>

      {all.length === 0 && <p className="empty">{t.noData}</p>}

      {weak.length > 0 && (
        <div className="card focus-card">
          <div className="focus-label">{t.weakest}</div>
          <div className="focus-topic">{topicLabel(weak[0].topic, lang)}</div>
          <div className="focus-acc">{Math.round(weak[0].accuracy * 100)}% {t.accuracy}</div>
          <button className="btn primary" onClick={() => onPracticeTopic(weak[0].topic)}>
            {t.practice} →
          </button>
        </div>
      )}

      <div className="topic-stats">
        {all.map((s) => {
          const pct = Math.round(s.accuracy * 100);
          const tone = pct >= 80 ? "good" : pct >= 50 ? "mid" : "low";
          return (
            <div key={s.topic} className="topic-stat" onClick={() => onPracticeTopic(s.topic)}>
              <div className="topic-stat-head">
                <span>{topicLabel(s.topic, lang)}</span>
                <span className="topic-pct">{pct}%</span>
              </div>
              <div className="acc-bar">
                <div className={`acc-fill acc-${tone}`} style={{ width: `${pct}%` }} />
              </div>
              <div className="topic-attempts">{s.correct}/{s.total} {t.attempts}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
