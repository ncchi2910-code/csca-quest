import { useEffect, useMemo, useRef, useState } from "react";
import QuestionCard from "./QuestionCard.jsx";
import Results from "./Results.jsx";
import { UI } from "../lib/i18n.js";

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function fmt(sec) {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${m}:${String(s).padStart(2, "0")}`;
}

export default function Exam({ pool, lang, onToggleLang, applyExam, onExit }) {
  const t = UI[lang];
  const [phase, setPhase] = useState("setup"); // setup | run | done
  const [count, setCount] = useState(Math.min(20, pool.length));
  const [minutes, setMinutes] = useState(30);

  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]); // index per question or null
  const [idx, setIdx] = useState(0);
  const [secs, setSecs] = useState(0);
  const [result, setResult] = useState(null);
  const timerRef = useRef(null);

  const maxCount = pool.length;
  const countOptions = [5, 10, 20, 30, 40].filter((n) => n <= maxCount);
  if (!countOptions.includes(maxCount)) countOptions.push(maxCount);

  function start() {
    const qs = shuffle(pool).slice(0, count);
    setQuestions(qs);
    setAnswers(new Array(qs.length).fill(null));
    setIdx(0);
    setSecs(minutes * 60);
    setPhase("run");
  }

  useEffect(() => {
    if (phase !== "run") return;
    timerRef.current = setInterval(() => {
      setSecs((s) => {
        if (s <= 1) {
          clearInterval(timerRef.current);
          finish();
          return 0;
        }
        return s - 1;
      });
    }, 1000);
    return () => clearInterval(timerRef.current);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [phase]);

  function choose(i) {
    setAnswers((a) => {
      const n = [...a];
      n[idx] = i;
      return n;
    });
  }

  function finish() {
    clearInterval(timerRef.current);
    let earned = 0;
    let possible = 0;
    const perTopic = {};
    questions.forEach((q, i) => {
      const pts = q.points || 1;
      possible += pts;
      const correct = answers[i] === q.answer;
      if (correct) earned += pts;
      perTopic[q.topic] = perTopic[q.topic] || { correct: 0, total: 0 };
      perTopic[q.topic].total++;
      if (correct) perTopic[q.topic].correct++;
    });
    const score = possible > 0 ? Math.round((earned / possible) * 100) : 0;
    const res = { questions, answers, score, perTopic };
    applyExam(res);
    setResult(res);
    setPhase("done");
  }

  const answeredCount = useMemo(() => answers.filter((a) => a !== null).length, [answers]);

  if (phase === "setup") {
    return (
      <div className="screen exam-setup">
        <button className="btn ghost" onClick={onExit}>← {t.backHome}</button>
        <div className="card setup-card">
          <h2>⏱️ {t.exam}</h2>
          <div className="setup-row">
            <label>{t.numQuestions}</label>
            <div className="pill-group">
              {countOptions.map((n) => (
                <button key={n} className={`pill ${count === n ? "pill-on" : ""}`} onClick={() => setCount(n)}>{n}</button>
              ))}
            </div>
          </div>
          <div className="setup-row">
            <label>{t.minutes}</label>
            <div className="pill-group">
              {[10, 20, 30, 45, 60].map((n) => (
                <button key={n} className={`pill ${minutes === n ? "pill-on" : ""}`} onClick={() => setMinutes(n)}>{n}</button>
              ))}
            </div>
          </div>
          <button className="btn primary big" onClick={start} disabled={maxCount === 0}>
            {t.startExam}
          </button>
          {maxCount === 0 && <p className="empty">{t.noQuestions}</p>}
        </div>
      </div>
    );
  }

  if (phase === "done") {
    return <Results result={result} lang={lang} onToggleLang={onToggleLang} onExit={onExit} />;
  }

  const q = questions[idx];
  const low = secs <= 30;
  return (
    <div className="screen exam-run">
      <div className="exam-bar">
        <button className="btn ghost" onClick={onExit}>✕</button>
        <div className={`timer ${low ? "timer-low" : ""}`}>⏱️ {t.timeLeft}: {fmt(secs)}</div>
        <div className="answered">{answeredCount}/{questions.length}</div>
      </div>

      <div className="q-progress">
        <div className="q-progress-fill" style={{ width: `${((idx + 1) / questions.length) * 100}%` }} />
      </div>

      <QuestionCard
        question={q}
        lang={lang}
        index={idx}
        total={questions.length}
        selected={answers[idx]}
        revealed={false}
        onSelect={choose}
        onToggleLang={onToggleLang}
      />

      <div className="exam-nav">
        <button className="btn ghost" onClick={() => setIdx((i) => Math.max(0, i - 1))} disabled={idx === 0}>
          ← {t.back}
        </button>
        {idx + 1 < questions.length ? (
          <button className="btn primary" onClick={() => setIdx((i) => i + 1)}>{t.next} →</button>
        ) : (
          <button className="btn success" onClick={finish}>{t.finish} ✓</button>
        )}
      </div>

      <div className="dots">
        {questions.map((_, i) => (
          <button
            key={i}
            className={`dot ${answers[i] !== null ? "dot-done" : ""} ${i === idx ? "dot-cur" : ""}`}
            onClick={() => setIdx(i)}
          >
            {i + 1}
          </button>
        ))}
      </div>
    </div>
  );
}
