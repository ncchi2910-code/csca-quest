import { useEffect, useMemo, useState } from "react";
import rawQuestions from "../data/questions.json";
import Header from "./components/Header.jsx";
import Home from "./components/Home.jsx";
import Practice from "./components/Practice.jsx";
import Exam from "./components/Exam.jsx";
import Review from "./components/Review.jsx";
import * as storage from "./lib/storage.js";
import { newlyEarned, badgeById } from "./lib/game.js";
import "./App.css";

export default function App() {
  const [progress, setProgress] = useState(() => storage.load());
  const [view, setView] = useState("home"); // home | practice | exam | review
  const [subject, setSubject] = useState("math");
  const [initialTopic, setInitialTopic] = useState("all");

  // Persist on every change.
  useEffect(() => storage.save(progress), [progress]);

  const lang = progress.lang;
  const toggleLang = () =>
    setProgress((p) => ({ ...p, lang: p.lang === "en" ? "zh" : "en" }));

  const pool = useMemo(
    () =>
      rawQuestions.filter(
        (q) => q.subject === subject && (!progress.realOnly || q.source !== "AI-generated")
      ),
    [subject, progress.realOnly]
  );

  // Apply a single practice answer; returns newly earned badge objects for toasts.
  function applyAnswer({ id, topic, isCorrect, xpGained, maxCombo }) {
    let earned = [];
    setProgress((p) => {
      let next = { ...p, xp: p.xp + xpGained };
      next = storage.recordTopic(next, topic, isCorrect);
      next = storage.markSeen(next, id);
      next = storage.touchStreak(next);
      const ids = newlyEarned(next, { maxCombo });
      if (ids.length) next = { ...next, badges: [...next.badges, ...ids] };
      earned = ids.map(badgeById);
      return next;
    });
    return { newBadges: earned };
  }

  // Apply a finished mock exam: per-topic stats, XP for correct, best score, badges.
  function applyExam(result) {
    setProgress((p) => {
      let next = { ...p };
      result.questions.forEach((q, i) => {
        const correct = result.answers[i] === q.answer;
        next = storage.recordTopic(next, q.topic, correct);
        if (correct) next = { ...next, xp: next.xp + 10 };
      });
      next = storage.touchStreak(next);
      next = { ...next, bestScore: Math.max(next.bestScore || 0, result.score) };
      const ids = newlyEarned(next, {});
      if (ids.length) next = { ...next, badges: [...next.badges, ...ids] };
      return next;
    });
  }

  function start(subj, mode) {
    setSubject(subj);
    setInitialTopic("all");
    setView(mode);
  }

  function practiceTopic(topic) {
    const found = rawQuestions.find((q) => q.topic === topic);
    if (found) setSubject(found.subject);
    setInitialTopic(topic);
    setView("practice");
  }

  const goHome = () => setView("home");

  return (
    <div className="app">
      <Header progress={progress} lang={lang} onToggleLang={toggleLang} onHome={goHome} />
      <main className="content">
        {view === "home" && (
          <Home
            progress={progress}
            lang={lang}
            questions={rawQuestions}
            onStart={start}
            onToggleRealOnly={() => setProgress((p) => ({ ...p, realOnly: !p.realOnly }))}
            onOpenReview={() => setView("review")}
          />
        )}
        {view === "practice" && (
          <Practice
            key={subject + initialTopic}
            pool={pool}
            initialTopic={initialTopic}
            lang={lang}
            seenIds={progress.practice?.seenIds || []}
            onToggleLang={toggleLang}
            applyAnswer={applyAnswer}
            onResetProgress={() => setProgress((p) => storage.resetSeen(p))}
            onExit={goHome}
          />
        )}
        {view === "exam" && (
          <Exam
            pool={pool}
            lang={lang}
            onToggleLang={toggleLang}
            applyExam={applyExam}
            onExit={goHome}
          />
        )}
        {view === "review" && (
          <Review
            progress={progress}
            lang={lang}
            onExit={goHome}
            onPracticeTopic={practiceTopic}
          />
        )}
      </main>
    </div>
  );
}
