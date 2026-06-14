import { useMemo, useState } from "react";
import QuestionCard from "./QuestionCard.jsx";
import { UI, topicLabel } from "../lib/i18n.js";
import { comboMultiplier, XP_PER_CORRECT } from "../lib/game.js";

export default function Practice({ pool, initialTopic = "all", lang, seenIds = [], onToggleLang, applyAnswer, onResetProgress, onExit }) {
  const t = UI[lang];
  const topics = useMemo(() => [...new Set(pool.map((q) => q.topic))], [pool]);

  const [topic, setTopic] = useState(
    initialTopic !== "all" && topics.includes(initialTopic) ? initialTopic : "all"
  );
  const questions = useMemo(
    () => pool.filter((q) => topic === "all" || q.topic === topic),
    [pool, topic]
  );

  // Set of question ids already practiced (from saved progress).
  const seenSet = useMemo(() => new Set(seenIds), [seenIds]);
  // First question the player hasn't answered yet — that's where we resume.
  const firstUnseen = (list) => {
    const i = list.findIndex((q) => !seenSet.has(q.id));
    return i === -1 ? 0 : i;
  };
  const answeredCount = questions.filter((q) => seenSet.has(q.id)).length;
  const allDone = questions.length > 0 && answeredCount >= questions.length;

  // Resume at the first unanswered question instead of always starting at 0.
  const [idx, setIdx] = useState(() => firstUnseen(questions));
  const [resumed] = useState(() => firstUnseen(questions) > 0);
  const [selected, setSelected] = useState(null);
  const [revealed, setRevealed] = useState(false);
  const [combo, setCombo] = useState(0);
  const [toast, setToast] = useState(null); // { xp, mult } | { badge }

  const q = questions[idx];

  function pick(i) {
    if (revealed) return;
    setSelected(i);
    setRevealed(true);
    const correct = i === q.answer;
    const nextCombo = correct ? combo + 1 : 0;
    setCombo(nextCombo);
    const mult = correct ? comboMultiplier(nextCombo) : 1;
    const xp = correct ? Math.round(XP_PER_CORRECT * mult) : 0;
    const res = applyAnswer({ id: q.id, topic: q.topic, isCorrect: correct, xpGained: xp, maxCombo: nextCombo });
    if (correct) setToast({ xp, mult, badges: res.newBadges });
    else setToast({ xp: 0, badges: res.newBadges });
  }

  function next() {
    setToast(null);
    if (idx + 1 < questions.length) {
      setIdx(idx + 1);
    } else {
      setIdx(0); // loop the pool
    }
    setSelected(null);
    setRevealed(false);
  }

  function changeTopic(tp) {
    setTopic(tp);
    const list = pool.filter((qq) => tp === "all" || qq.topic === tp);
    setIdx(firstUnseen(list)); // resume within the newly selected topic too
    setSelected(null);
    setRevealed(false);
    setToast(null);
  }

  function restart() {
    onResetProgress?.();
    setIdx(0);
    setSelected(null);
    setRevealed(false);
    setToast(null);
  }

  if (!q) {
    return (
      <div className="screen">
        <button className="btn ghost" onClick={onExit}>← {t.backHome}</button>
        <p className="empty">{t.noQuestions}</p>
      </div>
    );
  }

  return (
    <div className="screen practice">
      <div className="toolbar">
        <button className="btn ghost" onClick={onExit}>← {t.backHome}</button>
        <div className="topic-filter">
          <span className="filter-label">{t.filterTopic}:</span>
          <select value={topic} onChange={(e) => changeTopic(e.target.value)}>
            <option value="all">{t.allTopics}</option>
            {topics.map((tp) => (
              <option key={tp} value={tp}>{topicLabel(tp, lang)}</option>
            ))}
          </select>
        </div>
        {combo >= 2 && <div className="combo-chip">⚡ {t.combo} ×{comboMultiplier(combo)}</div>}
      </div>

      <div className="practice-progress">
        <span className="pp-count">{t.practiceProgress}: {answeredCount} / {questions.length}</span>
        <div className="pp-bar">
          <div className="pp-fill" style={{ width: `${questions.length ? (answeredCount / questions.length) * 100 : 0}%` }} />
        </div>
        {answeredCount > 0 && (
          <button className="btn ghost small" onClick={restart}>↻ {t.restart}</button>
        )}
      </div>

      {resumed && !allDone && <div className="resume-note">⏯ {t.resumeNote}</div>}
      {allDone && <div className="resume-note done">{t.allDone}</div>}

      <QuestionCard
        question={q}
        lang={lang}
        index={idx}
        total={questions.length}
        selected={selected}
        revealed={revealed}
        onSelect={pick}
        onToggleLang={onToggleLang}
      />

      {toast && (
        <div className="toast-area">
          {toast.xp > 0 && (
            <div className="xp-toast">
              +{toast.xp} {t.xp} {toast.mult > 1 ? `(×${toast.mult})` : ""}
            </div>
          )}
          {toast.badges && toast.badges.map((b) => (
            <div key={b.id} className="badge-toast">{b.emoji} {t.newBadge} {b[lang]}</div>
          ))}
        </div>
      )}

      {revealed && (
        <button className="btn primary big" onClick={next}>
          {t.next} →
        </button>
      )}
    </div>
  );
}
