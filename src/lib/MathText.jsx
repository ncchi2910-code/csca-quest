import katex from "katex";

// Renders a string that mixes plain text with inline math delimited by $...$.
// e.g. "Solve $x^2 - 1 = 0$ for x" -> text + KaTeX + text.
export default function MathText({ children, className }) {
  const text = children == null ? "" : String(children);
  const parts = splitMath(text);
  return (
    <span className={className}>
      {parts.map((p, i) =>
        p.math ? (
          <span
            key={i}
            dangerouslySetInnerHTML={{ __html: renderMath(p.value) }}
          />
        ) : (
          <span key={i}>{p.value}</span>
        )
      )}
    </span>
  );
}

function splitMath(text) {
  const parts = [];
  const re = /\$([^$]+)\$/g;
  let last = 0;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) parts.push({ math: false, value: text.slice(last, m.index) });
    parts.push({ math: true, value: m[1] });
    last = re.lastIndex;
  }
  if (last < text.length) parts.push({ math: false, value: text.slice(last) });
  if (parts.length === 0) parts.push({ math: false, value: text });
  return parts;
}

function renderMath(tex) {
  try {
    return katex.renderToString(tex, { throwOnError: false, displayMode: false });
  } catch {
    return tex;
  }
}
