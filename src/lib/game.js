// XP / level curve, combo multipliers and badges.

export const XP_PER_CORRECT = 10;

// Level N requires this much cumulative XP. Smooth-ish quadratic curve.
export function levelFromXp(xp) {
  // xp needed to reach level L (L>=1) = 50 * (L-1) * L  -> 0,100,300,600,1000...
  let level = 1;
  while (xpForLevel(level + 1) <= xp) level++;
  return level;
}

export function xpForLevel(level) {
  return 50 * (level - 1) * level;
}

// Progress within the current level, 0..1, plus raw numbers for display.
export function levelProgress(xp) {
  const level = levelFromXp(xp);
  const cur = xpForLevel(level);
  const next = xpForLevel(level + 1);
  const into = xp - cur;
  const span = next - cur;
  return { level, into, span, ratio: span > 0 ? into / span : 0, next };
}

// Combo multiplier grows with consecutive correct answers.
export function comboMultiplier(streak) {
  if (streak >= 8) return 3;
  if (streak >= 5) return 2;
  if (streak >= 3) return 1.5;
  return 1;
}

// Badge definitions. `check` receives the live progress + a context object.
export const BADGES = [
  { id: "first-correct", emoji: "🌱", en: "First Step", zh: "第一步", check: (s) => totalAnswered(s) >= 1 },
  { id: "ten-correct", emoji: "⭐", en: "Rising Star", zh: "初露锋芒", check: (s) => totalCorrect(s) >= 10 },
  { id: "fifty-correct", emoji: "🌟", en: "Sharp Mind", zh: "头脑敏捷", check: (s) => totalCorrect(s) >= 50 },
  { id: "level-5", emoji: "🏅", en: "Level 5", zh: "五级达人", check: (s) => levelFromXp(s.xp) >= 5 },
  { id: "level-10", emoji: "🏆", en: "Level 10", zh: "十级大师", check: (s) => levelFromXp(s.xp) >= 10 },
  { id: "streak-3", emoji: "🔥", en: "3-Day Streak", zh: "三天连续", check: (s) => s.streak.count >= 3 },
  { id: "streak-7", emoji: "🚀", en: "Week Warrior", zh: "一周不断", check: (s) => s.streak.count >= 7 },
  { id: "combo-5", emoji: "⚡", en: "On Fire", zh: "连击高手", check: (s, ctx) => (ctx.maxCombo || 0) >= 5 },
  { id: "exam-80", emoji: "🎯", en: "High Scorer", zh: "高分选手", check: (s) => s.bestScore >= 80 },
  { id: "exam-100", emoji: "👑", en: "Perfect Exam", zh: "满分王者", check: (s) => s.bestScore >= 100 }
];

export function totalCorrect(s) {
  return Object.values(s.topics).reduce((a, t) => a + t.correct, 0);
}
export function totalAnswered(s) {
  return Object.values(s.topics).reduce((a, t) => a + t.total, 0);
}

// Returns the list of newly-earned badge ids given current state + context.
export function newlyEarned(state, ctx = {}) {
  return BADGES.filter((b) => !state.badges.includes(b.id) && b.check(state, ctx)).map((b) => b.id);
}

export function badgeById(id) {
  return BADGES.find((b) => b.id === id);
}

// Weak-topic ranking: lowest accuracy first (min attempts to count).
export function weakTopics(state, minAttempts = 2) {
  return Object.entries(state.topics)
    .filter(([, t]) => t.total >= minAttempts)
    .map(([topic, t]) => ({ topic, ...t, accuracy: t.correct / t.total }))
    .sort((a, b) => a.accuracy - b.accuracy);
}
