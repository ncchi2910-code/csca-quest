import { UI } from "../lib/i18n.js";
import { levelProgress } from "../lib/game.js";

export default function Header({ progress, lang, onToggleLang, onHome }) {
  const t = UI[lang];
  const lp = levelProgress(progress.xp);
  return (
    <header className="app-header">
      <button className="brand" onClick={onHome}>
        <span className="brand-mark">🎓</span>
        <span className="brand-name">{t.appName}</span>
      </button>

      <div className="header-stats">
        <div className="stat level-stat" title={t.level}>
          <span className="stat-badge">Lv {lp.level}</span>
          <div className="xp-bar" aria-label={`${t.xp}`}>
            <div className="xp-fill" style={{ width: `${Math.round(lp.ratio * 100)}%` }} />
            <span className="xp-text">{lp.into} / {lp.span} {t.xp}</span>
          </div>
        </div>
        <div className="stat streak-stat" title={t.streak}>
          🔥 <strong>{progress.streak.count}</strong>
          <span className="stat-label">{t.days}</span>
        </div>
        <button className="lang-toggle header-lang" onClick={onToggleLang}>
          {lang === "en" ? "中文" : "EN"}
        </button>
      </div>
    </header>
  );
}
