// Player progress persisted in localStorage. No backend.
const KEY = "csca-quest-progress-v1";

const DEFAULT = {
  xp: 0,
  lang: "en", // shared UI + question language
  realOnly: false, // play only real-exam questions
  streak: { count: 0, lastDay: null }, // lastDay = "YYYY-MM-DD"
  topics: {}, // topicKey -> { correct, total }
  badges: [], // earned badge ids
  bestScore: 0, // best mock-exam score
  practice: { seenIds: [] } // ids of questions already practiced — used to resume
};

export function load() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return { ...DEFAULT };
    return { ...DEFAULT, ...JSON.parse(raw) };
  } catch {
    return { ...DEFAULT };
  }
}

export function save(state) {
  try {
    localStorage.setItem(KEY, JSON.stringify(state));
  } catch {
    /* ignore quota errors */
  }
}

// "YYYY-MM-DD" for today in local time.
export function today() {
  const d = new Date();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${d.getFullYear()}-${m}-${day}`;
}

function daysBetween(a, b) {
  const da = new Date(a + "T00:00:00");
  const db = new Date(b + "T00:00:00");
  return Math.round((db - da) / 86400000);
}

// Call once per session when the player answers something — bumps the daily streak.
export function touchStreak(state) {
  const t = today();
  const last = state.streak.lastDay;
  if (last === t) return state; // already counted today
  let count = 1;
  if (last && daysBetween(last, t) === 1) count = state.streak.count + 1;
  return { ...state, streak: { count, lastDay: t } };
}

// Mark one question id as practiced so we can resume there next session.
export function markSeen(state, id) {
  const prev = state.practice || { seenIds: [] };
  if (!id || prev.seenIds.includes(id)) return state;
  return { ...state, practice: { ...prev, seenIds: [...prev.seenIds, id] } };
}

// Clear practice progress so the player can start the pool over.
export function resetSeen(state) {
  return { ...state, practice: { seenIds: [] } };
}

// Record one answered question into per-topic stats.
export function recordTopic(state, topic, isCorrect) {
  const cur = state.topics[topic] || { correct: 0, total: 0 };
  return {
    ...state,
    topics: {
      ...state.topics,
      [topic]: { correct: cur.correct + (isCorrect ? 1 : 0), total: cur.total + 1 }
    }
  };
}
