#!/usr/bin/env python3
"""
Builds the CSCA January 2026 real-exam question bank (math, 47 solvable items;
Q7 is blank/figure-only in the source and is omitted).

Source: materials/toan/CSCA_Jan_en.pdf + CSCA_Jan_cn.pdf (same paper, EN+CN),
cross-checked against rendered pages to fix OCR of math symbols. Every answer
was re-solved independently; explanations are step-by-step (EN + ZH).

Run:  python3 scripts/build_jan2026.py
Writes the list to stdout as JSON (used to assemble data/questions.json).
Uses raw strings so json.dump emits correct LaTeX escaping.
"""
import json

# Each q: id_num, topic, difficulty, points, qen, qzh, [opts_en], [opts_zh], answer, exp_en, exp_zh
Q = []
def add(n, topic, diff, pts, qen, qzh, oen, ozh, ans, een, ezh):
    Q.append({
        "id": f"math-jan2026-q{n:02d}",
        "subject": "math", "topic": topic, "source": "CSCA_Jan_2026",
        "points": pts, "difficulty": diff,
        "question": {"en": qen, "zh": qzh},
        "options": {"en": oen, "zh": ozh},
        "answer": ans,
        "explanation": {"en": een, "zh": ezh},
    })

add(1, "set", "easy", 2,
    r"Let $A = \{6, 7, 8, 9, 10\}$ be a set and $\Phi$ the empty set. Which statement is correct?",
    r"设集合 $A = \{6, 7, 8, 9, 10\}$，$\Phi$ 表示空集。则下列说法正确的是？",
    [r"$9 \in A$", r"$\{6\} \in A$", r"$6 \subseteq A$", r"$\Phi \in A$"],
    [r"$9 \in A$", r"$\{6\} \in A$", r"$6 \subseteq A$", r"$\Phi \in A$"],
    0,
    "1. $\\in$ links an element to a set; $\\subseteq$ links a set to a set.\n2. $9$ is one of the listed elements, so $9 \\in A$ is true — answer (A).\n3. $\\{6\\}$ is a set, so it should use $\\subseteq$, not $\\in$ (B is wrong).\n4. $6$ is an element, so it should use $\\in$, not $\\subseteq$ (C is wrong); and $\\Phi$ is not an element of $A$ (D is wrong).",
    "1. $\\in$ 连接元素与集合；$\\subseteq$ 连接集合与集合。\n2. $9$ 是所列元素之一，故 $9 \\in A$ 成立，选 (A)。\n3. $\\{6\\}$ 是集合，应用 $\\subseteq$ 而非 $\\in$（B 错）。\n4. $6$ 是元素，应用 $\\in$ 而非 $\\subseteq$（C 错）；$\\Phi$ 不是 $A$ 的元素（D 错）。")

add(2, "set", "easy", 2,
    r"Let $A = \{x \mid -2 \le x \le 2\}$ and $B = \{x \mid x > 0\}$. Then $A \cup B =$",
    r"设集合 $A = \{x \mid -2 \le x \le 2\}$，$B = \{x \mid x > 0\}$。则 $A \cup B =$",
    [r"$\{x \mid x \le -2\}$", r"$\{x \mid 0 < x \le 2\}$", r"$\{x \mid x \ge -2\}$", r"$\{x \mid -2 \le x < 0\}$"],
    [r"$\{x \mid x \le -2\}$", r"$\{x \mid 0 < x \le 2\}$", r"$\{x \mid x \ge -2\}$", r"$\{x \mid -2 \le x < 0\}$"],
    2,
    "1. The union $A \\cup B$ contains every $x$ that is in $A$ OR in $B$.\n2. $A = [-2, 2]$ and $B = (0, +\\infty)$.\n3. Together they cover everything from $-2$ rightward: $[-2, +\\infty)$.\n4. So $A \\cup B = \\{x \\mid x \\ge -2\\}$ — answer (C).\nTip: union widens the set; intersection (option B) would narrow it.",
    "1. 并集 $A \\cup B$ 包含所有属于 $A$ 或属于 $B$ 的 $x$。\n2. $A = [-2, 2]$，$B = (0, +\\infty)$。\n3. 两者合并覆盖从 $-2$ 向右的全部：$[-2, +\\infty)$。\n4. 故 $A \\cup B = \\{x \\mid x \\ge -2\\}$，选 (C)。\n提示：并集变大，交集（选项 B）才变小。")

add(3, "inequality", "medium", 2,
    r"The solution set of the inequality $x^2 - x - 2 > 0$ is",
    r"不等式 $x^2 - x - 2 > 0$ 的解集是",
    [r"$\{x \mid x < -1 \text{ or } x > 2\}$", r"$\{x \mid -1 < x < 2\}$", r"$\{x \mid x < -2 \text{ or } x > -1\}$", r"$\{x \mid -2 < x < 1\}$"],
    [r"$\{x \mid x < -1 \text{ 或 } x > 2\}$", r"$\{x \mid -1 < x < 2\}$", r"$\{x \mid x < -2 \text{ 或 } x > -1\}$", r"$\{x \mid -2 < x < 1\}$"],
    0,
    "1. Factor the quadratic: $x^2 - x - 2 = (x-2)(x+1)$.\n2. Find the roots: $x = 2$ and $x = -1$.\n3. The parabola opens upward, so $(x-2)(x+1) > 0$ holds OUTSIDE the roots.\n4. Therefore $x < -1$ or $x > 2$ — answer (A).\nTip: '$> 0$' on an upward parabola means the two outer intervals; '$< 0$' would mean the middle interval $(-1, 2)$, the trap in option (B).",
    "1. 因式分解：$x^2 - x - 2 = (x-2)(x+1)$。\n2. 求根：$x = 2$ 和 $x = -1$。\n3. 抛物线开口向上，所以 $(x-2)(x+1) > 0$ 在两根之外成立。\n4. 因此 $x < -1$ 或 $x > 2$，选 (A)。\n提示：开口向上时 '$> 0$' 取两侧外区间；'$< 0$' 才取中间区间 $(-1, 2)$，这正是选项 (B) 的陷阱。")

add(4, "sequence", "easy", 2,
    r"An arithmetic sequence $\{a_n\}$ has first term $a_1 = 2$ and common difference $d = 3$. Then $a_{100} =$",
    r"等差数列 $\{a_n\}$ 首项 $a_1 = 2$，公差 $d = 3$。则 $a_{100} =$",
    [r"$299$", r"$302$", r"$305$", r"$298$"],
    [r"$299$", r"$302$", r"$305$", r"$298$"],
    0,
    "1. Formula for an arithmetic sequence: $a_n = a_1 + (n-1)d$.\n2. Substitute $a_1 = 2$, $d = 3$, $n = 100$: $a_{100} = 2 + (100-1)\\times 3$.\n3. Compute: $2 + 99 \\times 3 = 2 + 297 = 299$ — answer (A).\nTip: a common mistake is using $n$ instead of $(n-1)$, giving $2 + 100\\times3 = 302$, the trap in option (B).",
    "1. 等差数列通项公式：$a_n = a_1 + (n-1)d$。\n2. 代入 $a_1 = 2$，$d = 3$，$n = 100$：$a_{100} = 2 + (100-1)\\times 3$。\n3. 计算：$2 + 99 \\times 3 = 2 + 297 = 299$，选 (A)。\n提示：常见错误是用 $n$ 代替 $(n-1)$，得到 $2 + 100\\times3 = 302$，即选项 (B) 的陷阱。")

add(5, "function", "medium", 2,
    r"The domain of the function $f(x) = \dfrac{1}{x} + \sqrt{1 - x}$ is",
    r"函数 $f(x) = \dfrac{1}{x} + \sqrt{1 - x}$ 的定义域是",
    [r"$(-\infty, 1]$", r"$(-\infty, 0) \cup (0, 1)$", r"$(-\infty, 0) \cup (0, 1]$", r"$[1, +\infty)$"],
    [r"$(-\infty, 1]$", r"$(-\infty, 0) \cup (0, 1)$", r"$(-\infty, 0) \cup (0, 1]$", r"$[1, +\infty)$"],
    2,
    "1. Collect every restriction on $x$.\n2. From $\\dfrac{1}{x}$: the denominator cannot be $0$, so $x \\ne 0$.\n3. From $\\sqrt{1-x}$: the radicand must be $\\ge 0$, so $1 - x \\ge 0 \\Rightarrow x \\le 1$.\n4. Combine: $x \\le 1$ but $x \\ne 0$, i.e. $(-\\infty, 0) \\cup (0, 1]$ — answer (C).\nTip: $x = 1$ is allowed because $\\sqrt{0} = 0$; only option (C) both includes $1$ and excludes $0$.",
    "1. 收集 $x$ 的所有限制。\n2. 由 $\\dfrac{1}{x}$：分母不为 $0$，故 $x \\ne 0$。\n3. 由 $\\sqrt{1-x}$：被开方数 $\\ge 0$，故 $1 - x \\ge 0 \\Rightarrow x \\le 1$。\n4. 综合：$x \\le 1$ 且 $x \\ne 0$，即 $(-\\infty, 0) \\cup (0, 1]$，选 (C)。\n提示：$x = 1$ 可取，因为 $\\sqrt{0}=0$；只有 (C) 既含 $1$ 又去掉 $0$。")

add(6, "coordinate-geometry", "easy", 2,
    r"Point $P(1, 2)$ is reflected about the $x$-axis to point $Q$. The coordinates of $Q$ are",
    r"在直角坐标系中，点 $P(1, 2)$ 关于 $x$ 轴对称得到点 $Q$，则 $Q$ 的坐标为",
    [r"$(2, 1)$", r"$(1, -2)$", r"$(-1, 2)$", r"$(-1, -2)$"],
    [r"$(2, 1)$", r"$(1, -2)$", r"$(-1, 2)$", r"$(-1, -2)$"],
    1,
    "1. Reflection about the $x$-axis keeps $x$ the same and negates $y$: $(x, y) \\to (x, -y)$.\n2. Apply to $P(1, 2)$: $x$ stays $1$, $y$ becomes $-2$.\n3. So $Q = (1, -2)$ — answer (B).\nTip: reflecting about the $y$-axis instead would give $(-1, 2)$, the trap in option (C).",
    "1. 关于 $x$ 轴对称：横坐标不变，纵坐标取相反数，即 $(x, y) \\to (x, -y)$。\n2. 代入 $P(1, 2)$：$x$ 仍为 $1$，$y$ 变为 $-2$。\n3. 故 $Q = (1, -2)$，选 (B)。\n提示：若关于 $y$ 轴对称则为 $(-1, 2)$，即选项 (C) 的陷阱。")

add(8, "function", "easy", 2,
    r"For the function $f(x) = x^4 + 3$, which statement is correct?",
    r"关于函数 $f(x) = x^4 + 3$，下列说法正确的是",
    ["The function is odd", "None of the above", "The function is neither odd nor even", "The function is even"],
    ["该函数是奇函数", "以上都不是", "该函数既非奇函数也非偶函数", "该函数是偶函数"],
    3,
    "1. Test parity by computing $f(-x)$.\n2. $f(-x) = (-x)^4 + 3 = x^4 + 3$ because the exponent $4$ is even.\n3. Since $f(-x) = f(x)$, the function is even — answer (D).\nTip: 'even' means symmetric about the $y$-axis; an odd function would need $f(-x) = -f(x)$, which fails here.",
    "1. 通过计算 $f(-x)$ 判断奇偶性。\n2. $f(-x) = (-x)^4 + 3 = x^4 + 3$，因为指数 $4$ 为偶数。\n3. 由 $f(-x) = f(x)$ 知该函数为偶函数，选 (D)。\n提示：偶函数关于 $y$ 轴对称；奇函数需满足 $f(-x) = -f(x)$，此处不成立。")

add(9, "function", "medium", 2,
    r"The inverse function of $y = x^3 + 3,\ x \in \mathbb{R}$ is",
    r"函数 $y = x^3 + 3,\ x \in \mathbb{R}$ 的反函数是",
    [r"$y = \sqrt[3]{x - 3},\ x \in \mathbb{R}$", r"$y = \sqrt[3]{x} + 3,\ x \ge -3$", r"$y = \sqrt[3]{x} + 3,\ x \in \mathbb{R}$", r"$y = \sqrt[3]{x} - 3,\ x \ge 3$"],
    [r"$y = \sqrt[3]{x - 3},\ x \in \mathbb{R}$", r"$y = \sqrt[3]{x} + 3,\ x \ge -3$", r"$y = \sqrt[3]{x} + 3,\ x \in \mathbb{R}$", r"$y = \sqrt[3]{x} - 3,\ x \ge 3$"],
    0,
    "1. To find an inverse, swap the roles of $x$ and $y$: $x = y^3 + 3$.\n2. Solve for $y$: $y^3 = x - 3$, so $y = \\sqrt[3]{x - 3}$.\n3. The cube root is defined for all reals, so the domain is $x \\in \\mathbb{R}$ — answer (A).\nTip: note $\\sqrt[3]{x-3}$ (subtract first, then root), NOT $\\sqrt[3]{x} - 3$; that wrong grouping is the trap in (D).",
    "1. 求反函数：交换 $x$ 与 $y$，得 $x = y^3 + 3$。\n2. 解出 $y$：$y^3 = x - 3$，故 $y = \\sqrt[3]{x - 3}$。\n3. 立方根对所有实数都有定义，故定义域为 $x \\in \\mathbb{R}$，选 (A)。\n提示：应是 $\\sqrt[3]{x-3}$（先减再开方），不是 $\\sqrt[3]{x} - 3$；后者是选项 (D) 的陷阱。")

add(10, "coordinate-geometry", "easy", 2,
    r"Which of the following points is in the third quadrant?",
    r"下列哪个点位于第三象限？",
    [r"$(-1, 2)$", r"$(-1, -2)$", r"$(1, 2)$", r"$(1, -2)$"],
    [r"$(-1, 2)$", r"$(-1, -2)$", r"$(1, 2)$", r"$(1, -2)$"],
    1,
    "1. Recall the sign of each quadrant: I $(+,+)$, II $(-,+)$, III $(-,-)$, IV $(+,-)$.\n2. The third quadrant needs BOTH coordinates negative.\n3. Check options: $(-1,-2)$ has both negative — answer (B).\n4. The others: $(-1,2)$ is II, $(1,2)$ is I, $(1,-2)$ is IV.",
    "1. 记住各象限符号：第一 $(+,+)$，第二 $(-,+)$，第三 $(-,-)$，第四 $(+,-)$。\n2. 第三象限要求横纵坐标都为负。\n3. 检查选项：$(-1,-2)$ 两者都为负，选 (B)。\n4. 其余：$(-1,2)$ 在第二象限，$(1,2)$ 在第一象限，$(1,-2)$ 在第四象限。")

add(11, "function", "easy", 2,
    r"Given $y = |x|$, which conclusion is correct?",
    r"已知 $y = |x|$，下列结论正确的是",
    ["When $x < 0$, the function is increasing", "When $x > 0$, the function is increasing", r"For $x \in \mathbb{R}$, the function is decreasing", r"For $x \in \mathbb{R}$, the function is increasing"],
    ["当 $x < 0$ 时，函数是增函数", "当 $x > 0$ 时，函数是增函数", "当 $x \\in \\mathbb{R}$ 时，函数是减函数", "当 $x \\in \\mathbb{R}$ 时，函数是增函数"],
    1,
    "1. Split $y = |x|$ by sign: for $x \\ge 0$, $|x| = x$; for $x < 0$, $|x| = -x$.\n2. On $x > 0$ the piece $y = x$ rises as $x$ grows, so it is increasing — answer (B).\n3. On $x < 0$ the piece $y = -x$ falls, so it is decreasing there (A is wrong).\n4. Over all of $\\mathbb{R}$ it is neither only-increasing nor only-decreasing (C and D are wrong).",
    "1. 按符号分段：当 $x \\ge 0$ 时 $|x| = x$；当 $x < 0$ 时 $|x| = -x$。\n2. 在 $x > 0$ 上 $y = x$ 随 $x$ 增大而上升，为增函数，选 (B)。\n3. 在 $x < 0$ 上 $y = -x$ 下降，为减函数（A 错）。\n4. 在整个 $\\mathbb{R}$ 上既非单调增也非单调减（C、D 错）。")

add(12, "inequality", "medium", 2,
    r"The solution set of the rational inequality $\dfrac{2x+1}{x-2} \le 0$ is",
    r"分式不等式 $\dfrac{2x+1}{x-2} \le 0$ 的解集是",
    [r"$\left[-\frac{1}{2},\ 2\right)$", r"$\left(-\infty,\ -\frac{1}{2}\right] \cup (2,\ +\infty)$", r"$\left[-\frac{1}{2},\ 2\right]$", r"$\left(-\infty,\ -\frac{1}{2}\right]$"],
    [r"$\left[-\frac{1}{2},\ 2\right)$", r"$\left(-\infty,\ -\frac{1}{2}\right] \cup (2,\ +\infty)$", r"$\left[-\frac{1}{2},\ 2\right]$", r"$\left(-\infty,\ -\frac{1}{2}\right]$"],
    0,
    "1. A fraction is $\\le 0$ when numerator and denominator have opposite signs (or the numerator is $0$).\n2. Critical points: numerator $2x+1 = 0 \\Rightarrow x = -\\frac12$; denominator $x - 2 = 0 \\Rightarrow x = 2$.\n3. Test a value between them, e.g. $x = 0$: $\\dfrac{1}{-2} < 0$ ✓, so the interval $\\left(-\\frac12, 2\\right)$ works.\n4. Include $x = -\\frac12$ (fraction $= 0$, allowed) but exclude $x = 2$ (undefined): $\\left[-\\frac12, 2\\right)$ — answer (A).",
    "1. 分式 $\\le 0$ 当分子分母异号（或分子为 $0$）。\n2. 关键点：分子 $2x+1 = 0 \\Rightarrow x = -\\frac12$；分母 $x - 2 = 0 \\Rightarrow x = 2$。\n3. 取中间值如 $x = 0$ 检验：$\\dfrac{1}{-2} < 0$ ✓，故区间 $\\left(-\\frac12, 2\\right)$ 成立。\n4. 含 $x = -\\frac12$（分式 $= 0$，可取），不含 $x = 2$（无定义）：$\\left[-\\frac12, 2\\right)$，选 (A)。")

add(13, "sequence", "easy", 2,
    r"Given $a = 2 - \sqrt{3}$ and $b = 2 + \sqrt{3}$, the arithmetic mean of $a$ and $b$ is",
    r"已知 $a = 2 - \sqrt{3}$，$b = 2 + \sqrt{3}$，则 $a$ 与 $b$ 的等差中项是",
    [r"$1$", r"$2$", r"$\pm 1$", r"$-1$"],
    [r"$1$", r"$2$", r"$\pm 1$", r"$-1$"],
    1,
    "1. The arithmetic mean of two numbers is $\\dfrac{a+b}{2}$.\n2. Add: $a + b = (2 - \\sqrt3) + (2 + \\sqrt3) = 4$ (the $\\sqrt3$ terms cancel).\n3. Divide by $2$: $\\dfrac{4}{2} = 2$ — answer (B).\nTip: the arithmetic mean is a single value, so option (C) $\\pm 1$ can be ruled out immediately.",
    "1. 两数的等差中项为 $\\dfrac{a+b}{2}$。\n2. 相加：$a + b = (2 - \\sqrt3) + (2 + \\sqrt3) = 4$（$\\sqrt3$ 抵消）。\n3. 除以 $2$：$\\dfrac{4}{2} = 2$，选 (B)。\n提示：等差中项是唯一值，故选项 (C) $\\pm 1$ 可直接排除。")

add(14, "coordinate-geometry", "easy", 2,
    r"If line $l$ passes through $A(-2, 3)$ and $B(3, 1)$, then the slope of $l$ is",
    r"若直线 $l$ 经过点 $A(-2, 3)$ 和 $B(3, 1)$，则 $l$ 的斜率为",
    [r"$\frac{2}{5}$", r"$\frac{5}{2}$", r"$-\frac{5}{2}$", r"$-\frac{2}{5}$"],
    [r"$\frac{2}{5}$", r"$\frac{5}{2}$", r"$-\frac{5}{2}$", r"$-\frac{2}{5}$"],
    3,
    "1. Slope formula: $k = \\dfrac{y_2 - y_1}{x_2 - x_1}$.\n2. Take $A(-2,3)$ as point 1 and $B(3,1)$ as point 2: $k = \\dfrac{1 - 3}{3 - (-2)}$.\n3. Simplify: $k = \\dfrac{-2}{5} = -\\dfrac{2}{5}$ — answer (D).\nTip: keep the point order consistent in numerator and denominator; flipping only one of them flips the sign.",
    "1. 斜率公式：$k = \\dfrac{y_2 - y_1}{x_2 - x_1}$。\n2. 取 $A(-2,3)$ 为点 1，$B(3,1)$ 为点 2：$k = \\dfrac{1 - 3}{3 - (-2)}$。\n3. 化简：$k = \\dfrac{-2}{5} = -\\dfrac{2}{5}$，选 (D)。\n提示：分子分母要按相同的点顺序，只颠倒其中一个会算错符号。")

add(15, "trigonometry", "medium", 2,
    r"If the terminal side of angle $\alpha$ passes through $P(1, 3)$, then $\sin\alpha =$",
    r"若角 $\alpha$ 的终边经过点 $P(1, 3)$，则 $\sin\alpha =$",
    [r"$3$", r"$\frac{3\sqrt{10}}{10}$", r"$\frac{1}{3}$", r"$\frac{\sqrt{10}}{10}$"],
    [r"$3$", r"$\frac{3\sqrt{10}}{10}$", r"$\frac{1}{3}$", r"$\frac{\sqrt{10}}{10}$"],
    1,
    "1. For a point $(x, y)$ on the terminal side, $\\sin\\alpha = \\dfrac{y}{r}$ where $r = \\sqrt{x^2 + y^2}$.\n2. Here $x = 1$, $y = 3$, so $r = \\sqrt{1 + 9} = \\sqrt{10}$.\n3. Thus $\\sin\\alpha = \\dfrac{3}{\\sqrt{10}}$.\n4. Rationalize: $\\dfrac{3}{\\sqrt{10}} = \\dfrac{3\\sqrt{10}}{10}$ — answer (B).",
    "1. 终边上点 $(x, y)$ 满足 $\\sin\\alpha = \\dfrac{y}{r}$，其中 $r = \\sqrt{x^2 + y^2}$。\n2. 此处 $x = 1$，$y = 3$，故 $r = \\sqrt{1 + 9} = \\sqrt{10}$。\n3. 于是 $\\sin\\alpha = \\dfrac{3}{\\sqrt{10}}$。\n4. 分母有理化：$\\dfrac{3}{\\sqrt{10}} = \\dfrac{3\\sqrt{10}}{10}$，选 (B)。")

add(16, "sequence", "easy", 2,
    r"Among the four sequences, how many are arithmetic? (1) $7, 13, 19, 25$; (2) $2, 4, 7, 11$; (3) $-1, -3, -5, -7$; (4) $2, 4, 8, 16$",
    r"在下列四个数列中，等差数列的个数是：(1) $7, 13, 19, 25$；(2) $2, 4, 7, 11$；(3) $-1, -3, -5, -7$；(4) $2, 4, 8, 16$",
    [r"$1$", r"$2$", r"$3$", r"$4$"],
    [r"$1$", r"$2$", r"$3$", r"$4$"],
    1,
    "1. A sequence is arithmetic when consecutive differences are constant.\n2. (1): $13-7=6,\\ 19-13=6,\\ 25-19=6$ — constant $6$, arithmetic ✓.\n3. (2): $4-2=2,\\ 7-4=3$ — not constant, NOT arithmetic.\n4. (3): differences all $-2$ — arithmetic ✓. (4): $2,4,8,16$ doubles each time — geometric, not arithmetic.\n5. So exactly $2$ are arithmetic — answer (B).",
    "1. 相邻两项之差为常数的数列才是等差数列。\n2. (1)：$13-7=6,\\ 19-13=6,\\ 25-19=6$，公差恒为 $6$，是等差 ✓。\n3. (2)：$4-2=2,\\ 7-4=3$，差不恒定，不是等差。\n4. (3)：差均为 $-2$，是等差 ✓。(4)：$2,4,8,16$ 每次翻倍，是等比，不是等差。\n5. 故恰有 $2$ 个为等差数列，选 (B)。")

add(17, "coordinate-geometry", "easy", 2,
    r"The distance from $A(3, -2)$ to $B(-5, -1)$ is $|AB| =$",
    r"平面上点 $A(3, -2)$ 到点 $B(-5, -1)$ 的距离 $|AB| =$",
    [r"$65$", r"$\sqrt{65}$", r"$13$", r"$\sqrt{13}$"],
    [r"$65$", r"$\sqrt{65}$", r"$13$", r"$\sqrt{13}$"],
    1,
    "1. Distance formula: $|AB| = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.\n2. $x_2 - x_1 = -5 - 3 = -8$ and $y_2 - y_1 = -1 - (-2) = 1$.\n3. Square and add: $(-8)^2 + 1^2 = 64 + 1 = 65$.\n4. Take the square root: $|AB| = \\sqrt{65}$ — answer (B).\nTip: don't forget the root — $65$ (option A) is the squared distance, not the distance.",
    "1. 距离公式：$|AB| = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$。\n2. $x_2 - x_1 = -5 - 3 = -8$，$y_2 - y_1 = -1 - (-2) = 1$。\n3. 平方相加：$(-8)^2 + 1^2 = 64 + 1 = 65$。\n4. 开方：$|AB| = \\sqrt{65}$，选 (B)。\n提示：别忘了开方——$65$（选项 A）是距离的平方，不是距离本身。")

add(18, "coordinate-geometry", "easy", 2,
    r"If line $l$ has inclination angle $45^\circ$ and passes through $(0, 2)$, then its equation is",
    r"若直线 $l$ 的倾斜角为 $45^\circ$，且经过点 $(0, 2)$，则 $l$ 的方程为",
    [r"$y = 2x - 2$", r"$y = x + 2$", r"$y = 2x + 2$", r"$y = x - 2$"],
    [r"$y = 2x - 2$", r"$y = x + 2$", r"$y = 2x + 2$", r"$y = x - 2$"],
    1,
    "1. Slope $=$ tangent of the inclination angle: $k = \\tan 45^\\circ = 1$.\n2. The point $(0, 2)$ is on the $y$-axis, so the $y$-intercept is $2$.\n3. Use slope-intercept form $y = kx + b$: $y = 1\\cdot x + 2 = x + 2$ — answer (B).\nTip: options with slope $2$ confuse the angle ($45^\\circ$) with a slope of $2$; $\\tan 45^\\circ = 1$, not $2$.",
    "1. 斜率等于倾斜角的正切：$k = \\tan 45^\\circ = 1$。\n2. 点 $(0, 2)$ 在 $y$ 轴上，故 $y$ 轴截距为 $2$。\n3. 用斜截式 $y = kx + b$：$y = 1\\cdot x + 2 = x + 2$，选 (B)。\n提示：斜率为 $2$ 的选项把角度 $45^\\circ$ 误当成斜率 $2$；$\\tan 45^\\circ = 1$，不是 $2$。")

add(19, "coordinate-geometry", "medium", 2,
    r"If the circle is $x^2 + y^2 - 4x - 3 = 0$, its center and radius are",
    r"若圆的方程为 $x^2 + y^2 - 4x - 3 = 0$，则其圆心和半径分别为",
    [r"$(0, 2)$ and $\sqrt{7}$", r"$(0, 2)$ and $7$", r"$(2, 0)$ and $\sqrt{7}$", r"$(2, 0)$ and $7$"],
    [r"$(0, 2)$ 和 $\sqrt{7}$", r"$(0, 2)$ 和 $7$", r"$(2, 0)$ 和 $\sqrt{7}$", r"$(2, 0)$ 和 $7$"],
    2,
    "1. Group and complete the square in $x$: $x^2 - 4x = (x-2)^2 - 4$.\n2. Rewrite the equation: $(x-2)^2 - 4 + y^2 - 3 = 0$, i.e. $(x-2)^2 + y^2 = 7$.\n3. Compare with $(x-a)^2 + (y-b)^2 = r^2$: center $(2, 0)$, $r^2 = 7$.\n4. So radius $r = \\sqrt{7}$ — answer (C).\nTip: the radius is $\\sqrt{7}$, not $7$; $7$ is $r^2$ (trap in option D).",
    "1. 对 $x$ 配方：$x^2 - 4x = (x-2)^2 - 4$。\n2. 改写方程：$(x-2)^2 - 4 + y^2 - 3 = 0$，即 $(x-2)^2 + y^2 = 7$。\n3. 与 $(x-a)^2 + (y-b)^2 = r^2$ 比较：圆心 $(2, 0)$，$r^2 = 7$。\n4. 故半径 $r = \\sqrt{7}$，选 (C)。\n提示：半径是 $\\sqrt{7}$ 而非 $7$；$7$ 是 $r^2$（选项 D 的陷阱）。")

add(20, "trigonometry", "medium", 2,
    r"Given $\sin\alpha = \frac{4}{5}$ and $\alpha$ in the second quadrant, which statement is correct?",
    r"已知 $\sin\alpha = \frac{4}{5}$，且角 $\alpha$ 属于第二象限，则下列说法正确的是",
    [r"$\cos\alpha = \frac{3}{5}$", r"$\cos\alpha = -\frac{3}{5}$", r"$\tan\alpha = \frac{3}{4}$", r"$\tan\alpha = \frac{4}{3}$"],
    [r"$\cos\alpha = \frac{3}{5}$", r"$\cos\alpha = -\frac{3}{5}$", r"$\tan\alpha = \frac{3}{4}$", r"$\tan\alpha = \frac{4}{3}$"],
    1,
    "1. Use the identity $\\sin^2\\alpha + \\cos^2\\alpha = 1$ to find $|\\cos\\alpha|$.\n2. $\\cos^2\\alpha = 1 - \\left(\\frac45\\right)^2 = 1 - \\frac{16}{25} = \\frac{9}{25}$, so $|\\cos\\alpha| = \\frac35$.\n3. In the second quadrant cosine is NEGATIVE, so $\\cos\\alpha = -\\frac35$ — answer (B).\n4. Then $\\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha} = \\dfrac{4/5}{-3/5} = -\\dfrac43$, so the positive tangents in (C)/(D) are wrong.",
    "1. 用恒等式 $\\sin^2\\alpha + \\cos^2\\alpha = 1$ 求 $|\\cos\\alpha|$。\n2. $\\cos^2\\alpha = 1 - \\left(\\frac45\\right)^2 = \\frac{9}{25}$，故 $|\\cos\\alpha| = \\frac35$。\n3. 第二象限余弦为负，故 $\\cos\\alpha = -\\frac35$，选 (B)。\n4. 此时 $\\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha} = \\dfrac{4/5}{-3/5} = -\\dfrac43$，故 (C)、(D) 的正值是错的。")

add(21, "sequence", "easy", 2,
    r"In an arithmetic sequence $\{a_n\}$, $a_2 = 1$ and $a_4 = 5$. The first term $a_1$ and common difference $d$ are",
    r"在等差数列 $\{a_n\}$ 中，$a_2 = 1$ 且 $a_4 = 5$，则首项 $a_1$ 和公差 $d$ 分别为",
    [r"$-1,\ 2$", r"$1,\ -2$", r"$-1,\ -2$", r"$1,\ 2$"],
    [r"$-1,\ 2$", r"$1,\ -2$", r"$-1,\ -2$", r"$1,\ 2$"],
    0,
    "1. From $a_2$ to $a_4$ there are two steps of $d$: $a_4 = a_2 + 2d$.\n2. So $5 = 1 + 2d \\Rightarrow 2d = 4 \\Rightarrow d = 2$.\n3. Back up one step: $a_1 = a_2 - d = 1 - 2 = -1$.\n4. Thus $a_1 = -1,\\ d = 2$ — answer (A).",
    "1. 从 $a_2$ 到 $a_4$ 经过两个公差：$a_4 = a_2 + 2d$。\n2. 故 $5 = 1 + 2d \\Rightarrow 2d = 4 \\Rightarrow d = 2$。\n3. 倒推一项：$a_1 = a_2 - d = 1 - 2 = -1$。\n4. 因此 $a_1 = -1,\\ d = 2$，选 (A)。")

add(22, "inequality", "medium", 2,
    r"Let $a, b, c$ be real numbers. Which statement is correct?",
    r"设 $a, b, c$ 为三个实数。下列说法正确的是",
    ["If $a > b$, then $ac > bc$", "If $a > b$, then $a + c > b + c$", "If $ac > bc$, then $a > b$", "If $a > b$, then $a^2 > b^2$"],
    ["若 $a > b$，则 $ac > bc$", "若 $a > b$，则 $a + c > b + c$", "若 $ac > bc$，则 $a > b$", "若 $a > b$，则 $a^2 > b^2$"],
    1,
    "1. Adding the same number to both sides never changes the inequality, so $a > b \\Rightarrow a + c > b + c$ — answer (B).\n2. (A) fails if $c \\le 0$: e.g. $a=2, b=1, c=-1$ gives $-2 > -1$? No.\n3. (C) fails if $c < 0$: dividing by a negative flips the sign.\n4. (D) fails with negatives: $a=1, b=-2$ has $a>b$ but $a^2=1 < 4=b^2$.",
    "1. 两边同加一个数不改变不等号，故 $a > b \\Rightarrow a + c > b + c$，选 (B)。\n2. (A) 当 $c \\le 0$ 时不成立：如 $a=2, b=1, c=-1$ 得 $-2 > -1$？不成立。\n3. (C) 当 $c < 0$ 时不成立：除以负数要变号。\n4. (D) 含负数时不成立：$a=1, b=-2$ 满足 $a>b$，但 $a^2=1 < 4=b^2$。")

add(23, "function", "medium", 2,
    r"About the exponential function $y = a^x$ ($a > 0,\ a \ne 1$), which statement is incorrect?",
    r"关于指数函数 $y = a^x$（$a > 0$ 且 $a \ne 1$），下列说法错误的是",
    [r"The range is $(0, +\infty)$", "The graph passes through $(0, 1)$", "The function is increasing on its domain", r"The domain is $\mathbb{R}$"],
    [r"值域为 $(0, +\infty)$", "图像经过点 $(0, 1)$", "在定义域上是增函数", r"定义域为 $\mathbb{R}$"],
    2,
    "1. The question asks which statement is INCORRECT.\n2. (A) range $(0, +\\infty)$ — true for every base.\n3. (B) passes through $(0,1)$ since $a^0 = 1$ — true. (D) domain $\\mathbb{R}$ — true.\n4. (C) 'increasing' holds only when $a > 1$; if $0 < a < 1$ the function is decreasing, so the blanket claim is INCORRECT — answer (C).",
    "1. 题目问哪一项是错误的。\n2. (A) 值域 $(0, +\\infty)$ —— 对任意底数都成立。\n3. (B) 过 $(0,1)$，因为 $a^0 = 1$ —— 成立。(D) 定义域 $\\mathbb{R}$ —— 成立。\n4. (C) 仅当 $a > 1$ 时为增函数；当 $0 < a < 1$ 时为减函数，故笼统说‘增函数’是错误的，选 (C)。")

add(24, "trigonometry", "medium", 2,
    r"If $\sin\alpha = \frac{3}{5}$ and $\alpha$ is in the first quadrant, then $\sin 2\alpha =$",
    r"若 $\sin\alpha = \frac{3}{5}$，且 $\alpha$ 属于第一象限，则 $\sin 2\alpha =$",
    [r"$\frac{12}{25}$", r"$\frac{24}{25}$", r"$\frac{18}{25}$", r"$\frac{7}{25}$"],
    [r"$\frac{12}{25}$", r"$\frac{24}{25}$", r"$\frac{18}{25}$", r"$\frac{7}{25}$"],
    1,
    "1. Double-angle formula: $\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha$.\n2. Find $\\cos\\alpha$: in the first quadrant it is positive, $\\cos\\alpha = \\sqrt{1 - \\frac{9}{25}} = \\frac45$.\n3. Substitute: $\\sin 2\\alpha = 2 \\cdot \\frac35 \\cdot \\frac45 = \\frac{24}{25}$ — answer (B).\nTip: don't forget the factor of $2$; $\\frac35\\cdot\\frac45 = \\frac{12}{25}$ alone is the trap in (A).",
    "1. 二倍角公式：$\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha$。\n2. 求 $\\cos\\alpha$：第一象限为正，$\\cos\\alpha = \\sqrt{1 - \\frac{9}{25}} = \\frac45$。\n3. 代入：$\\sin 2\\alpha = 2 \\cdot \\frac35 \\cdot \\frac45 = \\frac{24}{25}$，选 (B)。\n提示：别漏掉系数 $2$；只算 $\\frac35\\cdot\\frac45 = \\frac{12}{25}$ 是选项 (A) 的陷阱。")

add(25, "coordinate-geometry", "medium", 2,
    r"The intersection of $l_1: 3x - y + 8 = 0$ and $l_2: x + 2y - 9 = 0$ is",
    r"直线 $l_1: 3x - y + 8 = 0$ 和 $l_2: x + 2y - 9 = 0$ 的交点坐标为",
    [r"$(-5, 1)$", r"$(1, -5)$", r"$(5, -1)$", r"$(-1, 5)$"],
    [r"$(-5, 1)$", r"$(1, -5)$", r"$(5, -1)$", r"$(-1, 5)$"],
    3,
    "1. Solve the system. From $l_1$: $y = 3x + 8$.\n2. Substitute into $l_2$: $x + 2(3x + 8) - 9 = 0$.\n3. Simplify: $x + 6x + 16 - 9 = 0 \\Rightarrow 7x + 7 = 0 \\Rightarrow x = -1$.\n4. Back-substitute: $y = 3(-1) + 8 = 5$. Intersection $(-1, 5)$ — answer (D).\nTip: always plug your answer back into BOTH equations to confirm.",
    "1. 解方程组。由 $l_1$：$y = 3x + 8$。\n2. 代入 $l_2$：$x + 2(3x + 8) - 9 = 0$。\n3. 化简：$x + 6x + 16 - 9 = 0 \\Rightarrow 7x + 7 = 0 \\Rightarrow x = -1$。\n4. 回代：$y = 3(-1) + 8 = 5$。交点 $(-1, 5)$，选 (D)。\n提示：把答案代回两条方程验证。")

add(26, "coordinate-geometry", "hard", 2,
    r"Given the hyperbola $\dfrac{x^2}{64} - \dfrac{y^2}{16} = 1$, which statement is correct?",
    r"已知双曲线方程为 $\dfrac{x^2}{64} - \dfrac{y^2}{16} = 1$，下列说法正确的是",
    [r"The focal distance is $8\sqrt{5}$", "The real semi-axis has length $4$", r"The eccentricity is $\sqrt{5}$", "The imaginary semi-axis has length $8$"],
    [r"焦距为 $8\sqrt{5}$", "实半轴长为 $4$", r"离心率为 $\sqrt{5}$", "虚半轴长为 $8$"],
    0,
    "1. Read $a^2 = 64,\\ b^2 = 16$, so $a = 8$ (real semi-axis) and $b = 4$ (imaginary semi-axis).\n2. For a hyperbola $c^2 = a^2 + b^2 = 64 + 16 = 80$, so $c = \\sqrt{80} = 4\\sqrt5$.\n3. Focal distance $= 2c = 8\\sqrt5$ — answer (A).\n4. Check others: real semi-axis is $8$ not $4$ (B wrong); eccentricity $e = \\frac{c}{a} = \\frac{4\\sqrt5}{8} = \\frac{\\sqrt5}{2}$ not $\\sqrt5$ (C wrong); imaginary semi-axis is $4$ not $8$ (D wrong).",
    "1. 读出 $a^2 = 64,\\ b^2 = 16$，故 $a = 8$（实半轴）、$b = 4$（虚半轴）。\n2. 双曲线中 $c^2 = a^2 + b^2 = 64 + 16 = 80$，故 $c = \\sqrt{80} = 4\\sqrt5$。\n3. 焦距 $= 2c = 8\\sqrt5$，选 (A)。\n4. 验证其余：实半轴为 $8$ 非 $4$（B 错）；离心率 $e = \\frac{c}{a} = \\frac{\\sqrt5}{2}$ 非 $\\sqrt5$（C 错）；虚半轴为 $4$ 非 $8$（D 错）。")

add(27, "inequality", "medium", 2,
    r"Which of the following inequalities is correct?",
    r"下列不等式正确的是",
    [r"$2.1^{-2} > 1.2^{-2}$", r"$0.75^{-0.2} > 0.75^{-0.4}$", r"$3^{2.25} > 3^{3}$", r"$2.1^{\frac{2}{3}} > 1.2^{\frac{2}{3}}$"],
    [r"$2.1^{-2} > 1.2^{-2}$", r"$0.75^{-0.2} > 0.75^{-0.4}$", r"$3^{2.25} > 3^{3}$", r"$2.1^{\frac{2}{3}} > 1.2^{\frac{2}{3}}$"],
    3,
    "1. (D): the power function $t^{2/3}$ is increasing for $t > 0$, and $2.1 > 1.2$, so $2.1^{2/3} > 1.2^{2/3}$ — TRUE, answer (D).\n2. (A): with negative exponent $-2$, larger base gives SMALLER value, so $2.1^{-2} < 1.2^{-2}$ — false.\n3. (B): base $0.75 < 1$, so $0.75^x$ decreases in $x$; since $-0.2 > -0.4$, $0.75^{-0.2} < 0.75^{-0.4}$ — false.\n4. (C): $3^x$ increases, and $2.25 < 3$, so $3^{2.25} < 3^3$ — false.",
    "1. (D)：幂函数 $t^{2/3}$ 在 $t > 0$ 时递增，且 $2.1 > 1.2$，故 $2.1^{2/3} > 1.2^{2/3}$ —— 成立，选 (D)。\n2. (A)：指数为负 $-2$ 时，底越大值越小，故 $2.1^{-2} < 1.2^{-2}$ —— 错。\n3. (B)：底 $0.75 < 1$，$0.75^x$ 随 $x$ 递减；因 $-0.2 > -0.4$，故 $0.75^{-0.2} < 0.75^{-0.4}$ —— 错。\n4. (C)：$3^x$ 递增，且 $2.25 < 3$，故 $3^{2.25} < 3^3$ —— 错。")

add(28, "coordinate-geometry", "easy", 2,
    r"A circle has center $(-3, 2)$ and radius $4$. Its equation is",
    r"圆心在 $(-3, 2)$ 且半径为 $4$ 的圆的方程是",
    [r"$(x+3)^2 + (y-2)^2 = 4$", r"$(x-3)^2 + (y+2)^2 = 4$", r"$(x-3)^2 + (y+2)^2 = 16$", r"$(x+3)^2 + (y-2)^2 = 16$"],
    [r"$(x+3)^2 + (y-2)^2 = 4$", r"$(x-3)^2 + (y+2)^2 = 4$", r"$(x-3)^2 + (y+2)^2 = 16$", r"$(x+3)^2 + (y-2)^2 = 16$"],
    3,
    "1. Standard circle: $(x-a)^2 + (y-b)^2 = r^2$ with center $(a, b)$.\n2. Center $(-3, 2)$ means $a = -3, b = 2$, giving $(x-(-3))^2 + (y-2)^2 = (x+3)^2 + (y-2)^2$.\n3. Radius $4$ means $r^2 = 16$.\n4. So the equation is $(x+3)^2 + (y-2)^2 = 16$ — answer (D).\nTip: the sign inside flips relative to the center; and use $r^2 = 16$, not $r = 4$.",
    "1. 圆的标准式：$(x-a)^2 + (y-b)^2 = r^2$，圆心 $(a, b)$。\n2. 圆心 $(-3, 2)$ 即 $a = -3, b = 2$，得 $(x+3)^2 + (y-2)^2$。\n3. 半径 $4$ 即 $r^2 = 16$。\n4. 故方程为 $(x+3)^2 + (y-2)^2 = 16$，选 (D)。\n提示：括号内符号与圆心坐标相反；右边用 $r^2 = 16$，不是 $4$。")

add(29, "logarithm", "medium", 2,
    r"Let $a > 0$ and $b > 0$. Which statement is incorrect?",
    r"设 $a > 0$ 且 $b > 0$。则下列说法错误的是",
    [r"$\ln(a^b) = b\ln a$", r"$\log_a b = \dfrac{\ln a}{\ln b}\ (a \ne 1, b \ne 1)$", r"$\ln\dfrac{a}{b} = \ln a - \ln b$", r"$\ln(ab) = \ln a + \ln b$"],
    [r"$\ln(a^b) = b\ln a$", r"$\log_a b = \dfrac{\ln a}{\ln b}\ (a \ne 1, b \ne 1)$", r"$\ln\dfrac{a}{b} = \ln a - \ln b$", r"$\ln(ab) = \ln a + \ln b$"],
    1,
    "1. The question asks which one is INCORRECT.\n2. (A) power rule $\\ln(a^b) = b\\ln a$ — correct. (C) quotient rule and (D) product rule — both correct.\n3. (B) the change-of-base formula is $\\log_a b = \\dfrac{\\ln b}{\\ln a}$ (target on top), NOT $\\dfrac{\\ln a}{\\ln b}$.\n4. So (B) is incorrect — answer (B).\nTip: remember 'new base on the bottom': $\\log_a b = \\frac{\\ln b}{\\ln a}$.",
    "1. 题目问哪一项是错误的。\n2. (A) 幂法则 $\\ln(a^b) = b\\ln a$ —— 正确。(C) 商法则、(D) 积法则 —— 都正确。\n3. (B) 换底公式应为 $\\log_a b = \\dfrac{\\ln b}{\\ln a}$（真数在上），而非 $\\dfrac{\\ln a}{\\ln b}$。\n4. 故 (B) 错误，选 (B)。\n提示：记住‘新底在分母’：$\\log_a b = \\frac{\\ln b}{\\ln a}$。")

add(30, "trigonometry", "easy", 2,
    r"For $y = \sin x$, which statement is incorrect?",
    r"给定正弦函数 $y = \sin x$，下列说法错误的是",
    ["The maximum and minimum are $1$ and $-1$", "The function is periodic", "The function is even", r"The domain is $\mathbb{R}$"],
    ["最大值和最小值分别为 $1$ 和 $-1$", "该函数是周期函数", "该函数是偶函数", r"定义域为 $\mathbb{R}$"],
    2,
    "1. The question asks which one is INCORRECT.\n2. (A) $\\sin x$ ranges in $[-1, 1]$ — correct. (B) period $2\\pi$ — correct. (D) defined for all reals — correct.\n3. (C) $\\sin(-x) = -\\sin x$, so sine is an ODD function, not even — INCORRECT, answer (C).\nTip: sine is odd (symmetric about the origin); cosine is the even one.",
    "1. 题目问哪一项是错误的。\n2. (A) $\\sin x$ 取值于 $[-1, 1]$ —— 正确。(B) 周期 $2\\pi$ —— 正确。(D) 对所有实数有定义 —— 正确。\n3. (C) $\\sin(-x) = -\\sin x$，正弦为奇函数而非偶函数 —— 错误，选 (C)。\n提示：正弦是奇函数（关于原点对称）；偶函数是余弦。")

add(31, "coordinate-geometry", "medium", 2,
    r"Let $F$ be the focus of the parabola $y^2 = 4x$. A point $P$ on it has $x$-coordinate $4$. Then $|PF| =$",
    r"设抛物线 $y^2 = 4x$ 的焦点为 $F$。若点 $P$ 在抛物线上，且 $P$ 的横坐标为 $4$，则 $|PF| =$",
    [r"$2$", r"$3$", r"$4$", r"$5$"],
    [r"$2$", r"$3$", r"$4$", r"$5$"],
    3,
    "1. Compare $y^2 = 4x$ with $y^2 = 4cx$: $4c = 4 \\Rightarrow c = 1$, so the directrix is $x = -1$.\n2. The focal distance equals the distance to the directrix: $|PF| = x_P + 1$.\n3. With $x_P = 4$: $|PF| = 4 + 1 = 5$ — answer (D).\nTip: the focal-radius shortcut $|PF| = x_P + c$ avoids computing $P$'s $y$-coordinate.",
    "1. 将 $y^2 = 4x$ 与 $y^2 = 4cx$ 比较：$4c = 4 \\Rightarrow c = 1$，准线为 $x = -1$。\n2. 焦半径等于到准线的距离：$|PF| = x_P + 1$。\n3. 代入 $x_P = 4$：$|PF| = 4 + 1 = 5$，选 (D)。\n提示：焦半径公式 $|PF| = x_P + c$ 可省去求 $P$ 的纵坐标。")

add(32, "coordinate-geometry", "hard", 2,
    r"Lines $l_1: ax + (a-1)y + 3 = 0$ and $l_2: 2x + ay - 1 = 0$ satisfy $l_1 \perp l_2$. Then $a =$",
    r"已知两条直线 $l_1: ax + (a-1)y + 3 = 0$ 和 $l_2: 2x + ay - 1 = 0$。若 $l_1 \perp l_2$，则 $a =$",
    [r"$-1$", r"$-1$ or $1$", r"$1$", r"$0$ or $-1$"],
    [r"$-1$", r"$-1$ 或 $1$", r"$1$", r"$0$ 或 $-1$"],
    3,
    "1. For lines $A_1x + B_1y + C_1 = 0$ and $A_2x + B_2y + C_2 = 0$, perpendicular means $A_1A_2 + B_1B_2 = 0$.\n2. Here $A_1 = a, B_1 = a-1, A_2 = 2, B_2 = a$: $a\\cdot 2 + (a-1)\\cdot a = 0$.\n3. Expand: $2a + a^2 - a = a^2 + a = 0 \\Rightarrow a(a+1) = 0$.\n4. So $a = 0$ or $a = -1$ — answer (D).\nTip: this $A_1A_2 + B_1B_2 = 0$ test also works when a line is vertical, unlike the slope method.",
    "1. 对直线 $A_1x + B_1y + C_1 = 0$ 与 $A_2x + B_2y + C_2 = 0$，垂直条件为 $A_1A_2 + B_1B_2 = 0$。\n2. 此处 $A_1 = a, B_1 = a-1, A_2 = 2, B_2 = a$：$a\\cdot 2 + (a-1)\\cdot a = 0$。\n3. 展开：$2a + a^2 - a = a^2 + a = 0 \\Rightarrow a(a+1) = 0$。\n4. 故 $a = 0$ 或 $a = -1$，选 (D)。\n提示：$A_1A_2 + B_1B_2 = 0$ 这一判据在直线竖直时仍适用，优于斜率法。")

add(33, "coordinate-geometry", "easy", 2,
    r"The distance between $P(-1, 2)$ and $Q(3, 1)$ is",
    r"点 $P(-1, 2)$ 和 $Q(3, 1)$ 之间的距离是",
    [r"$\sqrt{5}$", r"$\sqrt{17}$", r"$\sqrt{13}$", r"$5$"],
    [r"$\sqrt{5}$", r"$\sqrt{17}$", r"$\sqrt{13}$", r"$5$"],
    1,
    "1. Distance formula: $\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.\n2. $x_2 - x_1 = 3 - (-1) = 4$ and $y_2 - y_1 = 1 - 2 = -1$.\n3. $\\sqrt{4^2 + (-1)^2} = \\sqrt{16 + 1} = \\sqrt{17}$ — answer (B).",
    "1. 距离公式：$\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$。\n2. $x_2 - x_1 = 3 - (-1) = 4$，$y_2 - y_1 = 1 - 2 = -1$。\n3. $\\sqrt{4^2 + (-1)^2} = \\sqrt{16 + 1} = \\sqrt{17}$，选 (B)。")

add(34, "trigonometry", "hard", 2,
    r"Let $\cos\alpha = -\dfrac{\sqrt5}{5}$ and $\alpha \in \left(\dfrac{\pi}{2}, \pi\right)$. Then $\sin\left(\dfrac{\pi}{6} + \alpha\right) =$",
    r"设 $\cos\alpha = -\dfrac{\sqrt5}{5}$，且 $\alpha \in \left(\dfrac{\pi}{2}, \pi\right)$。则 $\sin\left(\dfrac{\pi}{6} + \alpha\right) =$",
    [r"$\dfrac{2\sqrt5 - \sqrt{15}}{10}$", r"$\dfrac{2\sqrt{15} + \sqrt5}{10}$", r"$\dfrac{2\sqrt{15} - \sqrt5}{10}$", r"$\dfrac{2\sqrt5 + \sqrt{15}}{10}$"],
    [r"$\dfrac{2\sqrt5 - \sqrt{15}}{10}$", r"$\dfrac{2\sqrt{15} + \sqrt5}{10}$", r"$\dfrac{2\sqrt{15} - \sqrt5}{10}$", r"$\dfrac{2\sqrt5 + \sqrt{15}}{10}$"],
    2,
    "1. Find $\\sin\\alpha$: in QII it is positive, $\\sin\\alpha = \\sqrt{1 - \\frac{1}{5}} = \\sqrt{\\frac45} = \\frac{2\\sqrt5}{5}$.\n2. Expand: $\\sin\\!\\left(\\frac{\\pi}{6}+\\alpha\\right) = \\sin\\frac{\\pi}{6}\\cos\\alpha + \\cos\\frac{\\pi}{6}\\sin\\alpha = \\frac12\\cos\\alpha + \\frac{\\sqrt3}{2}\\sin\\alpha$.\n3. Substitute: $\\frac12\\!\\left(-\\frac{\\sqrt5}{5}\\right) + \\frac{\\sqrt3}{2}\\cdot\\frac{2\\sqrt5}{5} = -\\frac{\\sqrt5}{10} + \\frac{2\\sqrt{15}}{10}$.\n4. Combine: $\\dfrac{2\\sqrt{15} - \\sqrt5}{10}$ — answer (C).",
    "1. 求 $\\sin\\alpha$：第二象限为正，$\\sin\\alpha = \\sqrt{1 - \\frac{1}{5}} = \\sqrt{\\frac45} = \\frac{2\\sqrt5}{5}$。\n2. 展开：$\\sin\\!\\left(\\frac{\\pi}{6}+\\alpha\\right) = \\sin\\frac{\\pi}{6}\\cos\\alpha + \\cos\\frac{\\pi}{6}\\sin\\alpha = \\frac12\\cos\\alpha + \\frac{\\sqrt3}{2}\\sin\\alpha$。\n3. 代入：$\\frac12\\!\\left(-\\frac{\\sqrt5}{5}\\right) + \\frac{\\sqrt3}{2}\\cdot\\frac{2\\sqrt5}{5} = -\\frac{\\sqrt5}{10} + \\frac{2\\sqrt{15}}{10}$。\n4. 合并：$\\dfrac{2\\sqrt{15} - \\sqrt5}{10}$，选 (C)。")

add(35, "function", "hard", 2,
    r"Which pair represents the same function?",
    r"下列哪一对是同一函数？",
    [r"$y = (\sqrt{x})^2$ and $y = x^2$", r"$y = \dfrac{x^4 - 1}{x^2 + 1}$ and $y = x^2 - 1$", r"$y = 1$ and $y = x^0$", r"$y = x$ and $y = \sqrt{x^2}$"],
    [r"$y = (\sqrt{x})^2$ 和 $y = x^2$", r"$y = \dfrac{x^4 - 1}{x^2 + 1}$ 和 $y = x^2 - 1$", r"$y = 1$ 和 $y = x^0$", r"$y = x$ 和 $y = \sqrt{x^2}$"],
    1,
    "1. Two functions are the SAME only if they have the same rule AND the same domain.\n2. (B): $\\dfrac{x^4-1}{x^2+1} = \\dfrac{(x^2-1)(x^2+1)}{x^2+1} = x^2 - 1$, and the denominator $x^2+1$ is never $0$, so the domain is all of $\\mathbb{R}$ — same as $y = x^2 - 1$. Answer (B).\n3. (A): $(\\sqrt{x})^2$ needs $x \\ge 0$, but $x^2$ allows all reals — domains differ.\n4. (C): $x^0$ is undefined at $x = 0$ — domains differ. (D): $\\sqrt{x^2} = |x| \\ne x$ — rules differ.",
    "1. 两函数相同当且仅当对应法则相同且定义域相同。\n2. (B)：$\\dfrac{x^4-1}{x^2+1} = \\dfrac{(x^2-1)(x^2+1)}{x^2+1} = x^2 - 1$，且分母 $x^2+1$ 恒不为 $0$，定义域为全体实数 —— 与 $y = x^2 - 1$ 相同，选 (B)。\n3. (A)：$(\\sqrt{x})^2$ 要求 $x \\ge 0$，而 $x^2$ 对所有实数都有定义 —— 定义域不同。\n4. (C)：$x^0$ 在 $x = 0$ 无定义 —— 定义域不同。(D)：$\\sqrt{x^2} = |x| \\ne x$ —— 法则不同。")

add(36, "trigonometry", "hard", 2,
    r"Let $\sin\alpha = -\dfrac{12}{13}$ and $\alpha \in \left(\pi, \dfrac{3\pi}{2}\right)$. Then $\cos\dfrac{\alpha}{2} =$",
    r"设 $\sin\alpha = -\dfrac{12}{13}$，且 $\alpha \in \left(\pi, \dfrac{3\pi}{2}\right)$。则 $\cos\dfrac{\alpha}{2} =$",
    [r"$\dfrac{3\sqrt{13}}{13}$", r"$-\dfrac{3\sqrt{13}}{13}$", r"$-\dfrac{2\sqrt{13}}{13}$", r"$\dfrac{2\sqrt{13}}{13}$"],
    [r"$\dfrac{3\sqrt{13}}{13}$", r"$-\dfrac{3\sqrt{13}}{13}$", r"$-\dfrac{2\sqrt{13}}{13}$", r"$\dfrac{2\sqrt{13}}{13}$"],
    2,
    "1. $\\alpha$ is in QIII, so $\\cos\\alpha = -\\sqrt{1 - \\frac{144}{169}} = -\\frac{5}{13}$.\n2. Locate $\\frac{\\alpha}{2}$: from $\\pi < \\alpha < \\frac{3\\pi}{2}$ we get $\\frac{\\pi}{2} < \\frac{\\alpha}{2} < \\frac{3\\pi}{4}$ (QII), so $\\cos\\frac{\\alpha}{2} < 0$.\n3. Half-angle: $\\cos\\frac{\\alpha}{2} = -\\sqrt{\\dfrac{1+\\cos\\alpha}{2}} = -\\sqrt{\\dfrac{1 - 5/13}{2}} = -\\sqrt{\\dfrac{4}{13}}$.\n4. So $\\cos\\frac{\\alpha}{2} = -\\dfrac{2}{\\sqrt{13}} = -\\dfrac{2\\sqrt{13}}{13}$ — answer (C).\nTip: the sign of a half-angle comes from which quadrant $\\frac{\\alpha}{2}$ lands in, not from $\\alpha$.",
    "1. $\\alpha$ 在第三象限，故 $\\cos\\alpha = -\\sqrt{1 - \\frac{144}{169}} = -\\frac{5}{13}$。\n2. 定位 $\\frac{\\alpha}{2}$：由 $\\pi < \\alpha < \\frac{3\\pi}{2}$ 得 $\\frac{\\pi}{2} < \\frac{\\alpha}{2} < \\frac{3\\pi}{4}$（第二象限），故 $\\cos\\frac{\\alpha}{2} < 0$。\n3. 半角公式：$\\cos\\frac{\\alpha}{2} = -\\sqrt{\\dfrac{1+\\cos\\alpha}{2}} = -\\sqrt{\\dfrac{1 - 5/13}{2}} = -\\sqrt{\\dfrac{4}{13}}$。\n4. 故 $\\cos\\frac{\\alpha}{2} = -\\dfrac{2}{\\sqrt{13}} = -\\dfrac{2\\sqrt{13}}{13}$，选 (C)。\n提示：半角的符号由 $\\frac{\\alpha}{2}$ 落在哪个象限决定，而非由 $\\alpha$ 决定。")

add(37, "trigonometry", "hard", 2,
    r"Suppose $\cos\alpha = -\dfrac{1}{2}$ and $\alpha \in \left(\dfrac{\pi}{2}, \pi\right)$. Then $\sin\dfrac{\alpha}{2} =$",
    r"设 $\cos\alpha = -\dfrac{1}{2}$，且 $\alpha \in \left(\dfrac{\pi}{2}, \pi\right)$。则 $\sin\dfrac{\alpha}{2} =$",
    [r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
    [r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
    1,
    "1. Locate $\\frac{\\alpha}{2}$: from $\\frac{\\pi}{2} < \\alpha < \\pi$ we get $\\frac{\\pi}{4} < \\frac{\\alpha}{2} < \\frac{\\pi}{2}$ (QI), so $\\sin\\frac{\\alpha}{2} > 0$.\n2. Half-angle: $\\sin\\frac{\\alpha}{2} = \\sqrt{\\dfrac{1-\\cos\\alpha}{2}}$.\n3. Substitute $\\cos\\alpha = -\\frac12$: $\\sqrt{\\dfrac{1 - (-1/2)}{2}} = \\sqrt{\\dfrac{3/2}{2}} = \\sqrt{\\dfrac34}$.\n4. So $\\sin\\frac{\\alpha}{2} = \\dfrac{\\sqrt3}{2}$ — answer (B).",
    "1. 定位 $\\frac{\\alpha}{2}$：由 $\\frac{\\pi}{2} < \\alpha < \\pi$ 得 $\\frac{\\pi}{4} < \\frac{\\alpha}{2} < \\frac{\\pi}{2}$（第一象限），故 $\\sin\\frac{\\alpha}{2} > 0$。\n2. 半角公式：$\\sin\\frac{\\alpha}{2} = \\sqrt{\\dfrac{1-\\cos\\alpha}{2}}$。\n3. 代入 $\\cos\\alpha = -\\frac12$：$\\sqrt{\\dfrac{1 - (-1/2)}{2}} = \\sqrt{\\dfrac{3/2}{2}} = \\sqrt{\\dfrac34}$。\n4. 故 $\\sin\\frac{\\alpha}{2} = \\dfrac{\\sqrt3}{2}$，选 (B)。")

add(38, "trigonometry", "medium", 2,
    r"Which identity is correct?",
    r"下列说法正确的是",
    [r"$\sin(\pi + \alpha) = \sin\alpha$", r"$\cos(\pi + \alpha) = \cos\alpha$", r"$\sin(-\alpha) = \sin\alpha$", r"$\cos(-\alpha) = \cos\alpha$"],
    [r"$\sin(\pi + \alpha) = \sin\alpha$", r"$\cos(\pi + \alpha) = \cos\alpha$", r"$\sin(-\alpha) = \sin\alpha$", r"$\cos(-\alpha) = \cos\alpha$"],
    3,
    "1. Use the standard reduction/parity identities.\n2. (D): cosine is even, so $\\cos(-\\alpha) = \\cos\\alpha$ — TRUE, answer (D).\n3. (A): $\\sin(\\pi + \\alpha) = -\\sin\\alpha$ — false. (B): $\\cos(\\pi + \\alpha) = -\\cos\\alpha$ — false.\n4. (C): $\\sin(-\\alpha) = -\\sin\\alpha$ (sine is odd) — false.",
    "1. 使用诱导公式与奇偶性。\n2. (D)：余弦为偶函数，$\\cos(-\\alpha) = \\cos\\alpha$ —— 成立，选 (D)。\n3. (A)：$\\sin(\\pi + \\alpha) = -\\sin\\alpha$ —— 错。(B)：$\\cos(\\pi + \\alpha) = -\\cos\\alpha$ —— 错。\n4. (C)：$\\sin(-\\alpha) = -\\sin\\alpha$（正弦为奇函数）—— 错。")

add(39, "trigonometry", "medium", 2,
    r"About $y = \tan x$, which statement is correct?",
    r"关于正切函数 $y = \tan x$，下列说法正确的是",
    [r"The range is $[-1, 1]$", r"The domain is $\mathbb{R}$", "The function is even", r"The smallest positive period is $\pi$"],
    [r"值域为 $[-1, 1]$", r"定义域为 $\mathbb{R}$", "该函数是偶函数", r"最小正周期是 $\pi$"],
    3,
    "1. (D): $\\tan x$ repeats every $\\pi$, so its smallest positive period is $\\pi$ — TRUE, answer (D).\n2. (A): the range of tangent is all of $\\mathbb{R}$, not $[-1, 1]$ — false.\n3. (B): tangent is undefined at $x = \\frac{\\pi}{2} + k\\pi$, so the domain is not all of $\\mathbb{R}$ — false.\n4. (C): $\\tan(-x) = -\\tan x$, so tangent is ODD, not even — false.",
    "1. (D)：$\\tan x$ 每隔 $\\pi$ 重复，最小正周期为 $\\pi$ —— 成立，选 (D)。\n2. (A)：正切的值域为全体实数，而非 $[-1, 1]$ —— 错。\n3. (B)：正切在 $x = \\frac{\\pi}{2} + k\\pi$ 处无定义，定义域不是全体实数 —— 错。\n4. (C)：$\\tan(-x) = -\\tan x$，正切为奇函数而非偶函数 —— 错。")

add(40, "sequence", "medium", 2,
    r"The general term of the sequence $-\dfrac{1}{5}, \dfrac{1}{7}, -\dfrac{1}{9}, \dfrac{1}{11}, \dots$ is $a_n =$",
    r"数列 $-\dfrac{1}{5}, \dfrac{1}{7}, -\dfrac{1}{9}, \dfrac{1}{11}, \cdots$ 的通项公式为 $a_n =$",
    [r"$\dfrac{(-1)^{n-1}}{3n+2}$", r"$\dfrac{(-1)^n}{2n+3}$", r"$\dfrac{(-1)^{n-1}}{2n+3}$", r"$\dfrac{(-1)^n}{3n+2}$"],
    [r"$\dfrac{(-1)^{n-1}}{3n+2}$", r"$\dfrac{(-1)^n}{2n+3}$", r"$\dfrac{(-1)^{n-1}}{2n+3}$", r"$\dfrac{(-1)^n}{3n+2}$"],
    1,
    "1. Look at the denominators: $5, 7, 9, 11, \\dots$ increase by $2$, matching $2n + 3$ (check $n=1: 5$ ✓).\n2. Look at the signs: $-, +, -, +, \\dots$ starting NEGATIVE, which is $(-1)^n$ (check $n=1: -1$ ✓).\n3. Combine: $a_n = \\dfrac{(-1)^n}{2n+3}$ — answer (B).\nTip: $(-1)^{n-1}$ would start positive, the trap in options (A)/(C).",
    "1. 看分母：$5, 7, 9, 11, \\dots$ 每次加 $2$，对应 $2n + 3$（验 $n=1: 5$ ✓）。\n2. 看符号：$-, +, -, +, \\dots$ 从负开始，即 $(-1)^n$（验 $n=1: -1$ ✓）。\n3. 合并：$a_n = \\dfrac{(-1)^n}{2n+3}$，选 (B)。\n提示：$(-1)^{n-1}$ 从正开始，是选项 (A)/(C) 的陷阱。")

add(41, "logarithm", "medium", 2,
    r"If $f(x) = 2 + \log_a(x - 3)$ ($a>0, a\ne1$) passes through a fixed point $P$, then $P =$",
    r"若函数 $f(x) = 2 + \log_a(x - 3)$（$a>0, a\ne1$）经过定点 $P$，则 $P$ 的坐标为",
    [r"$(3, 1)$", r"$(3, 0)$", r"$(4, 0)$", r"$(4, 2)$"],
    [r"$(3, 1)$", r"$(3, 0)$", r"$(4, 0)$", r"$(4, 2)$"],
    3,
    "1. A log graph passes through a fixed point where its argument equals $1$ (since $\\log_a 1 = 0$ for every base $a$).\n2. Set $x - 3 = 1 \\Rightarrow x = 4$.\n3. Then $f(4) = 2 + \\log_a 1 = 2 + 0 = 2$.\n4. So the fixed point is $P(4, 2)$ — answer (D).\nTip: the '$+2$' shifts the basic fixed point $(\\cdot,0)$ up to height $2$.",
    "1. 对数图像的定点出现在真数等于 $1$ 处（因为对任意底 $a$ 都有 $\\log_a 1 = 0$）。\n2. 令 $x - 3 = 1 \\Rightarrow x = 4$。\n3. 则 $f(4) = 2 + \\log_a 1 = 2 + 0 = 2$。\n4. 故定点为 $P(4, 2)$，选 (D)。\n提示：‘$+2$’ 把基本定点的高度从 $0$ 抬高到 $2$。")

add(42, "coordinate-geometry", "medium", 2,
    r"The directrix of the parabola $y^2 = -x$ is",
    r"抛物线 $y^2 = -x$ 的准线方程是",
    [r"$x = \dfrac{1}{4}$", r"$x = -\dfrac{1}{4}$", r"$x = -\dfrac{1}{2}$", r"$x = \dfrac{1}{2}$"],
    [r"$x = \dfrac{1}{4}$", r"$x = -\dfrac{1}{4}$", r"$x = -\dfrac{1}{2}$", r"$x = \dfrac{1}{2}$"],
    0,
    "1. Write in the form $y^2 = 4cx$: here $4c = -1 \\Rightarrow c = -\\frac14$.\n2. For $y^2 = 4cx$ the directrix is $x = -c$.\n3. So directrix $x = -\\left(-\\frac14\\right) = \\frac14$ — answer (A).\nTip: the parabola opens LEFT ($-x$), so its focus is left of the origin and the directrix is to the RIGHT at $x = \\frac14$.",
    "1. 化为 $y^2 = 4cx$：此处 $4c = -1 \\Rightarrow c = -\\frac14$。\n2. 对 $y^2 = 4cx$，准线为 $x = -c$。\n3. 故准线 $x = -\\left(-\\frac14\\right) = \\frac14$，选 (A)。\n提示：抛物线开口向左（$-x$），焦点在原点左侧，准线在右侧 $x = \\frac14$。")

add(43, "coordinate-geometry", "medium", 2,
    r"For the ellipse $\dfrac{x^2}{4} + \dfrac{y^2}{2} = 1$ with foci $F_1, F_2$ and a point $P$ on it, $|PF_1| + |PF_2| =$",
    r"设椭圆 $\dfrac{x^2}{4} + \dfrac{y^2}{2} = 1$ 的焦点为 $F_1, F_2$，点 $P$ 在椭圆上，则 $|PF_1| + |PF_2| =$",
    [r"$2$", r"$4$", r"$8$", r"$6$"],
    [r"$2$", r"$4$", r"$8$", r"$6$"],
    1,
    "1. The defining property of an ellipse: the sum of distances to the two foci is constant and equals $2a$.\n2. The larger denominator is $a^2 = 4$, so $a = 2$.\n3. Therefore $|PF_1| + |PF_2| = 2a = 4$ — answer (B).\nTip: $2$ (option A) is $a$ itself; remember the sum is $2a$, not $a$.",
    "1. 椭圆的定义性质：到两焦点的距离之和为常数，等于 $2a$。\n2. 较大的分母为 $a^2 = 4$，故 $a = 2$。\n3. 因此 $|PF_1| + |PF_2| = 2a = 4$，选 (B)。\n提示：$2$（选项 A）是 $a$ 本身；记住距离之和为 $2a$ 而非 $a$。")

add(44, "vector", "hard", 2,
    r"Given $\vec{AB} = \vec{a} + 5\vec{b}$, $\vec{BC} = -2\vec{a} + 8\vec{b}$, $\vec{CD} = 3\vec{a} - 3\vec{b}$, then",
    r"已知 $\vec{AB} = \vec{a} + 5\vec{b}$，$\vec{BC} = -2\vec{a} + 8\vec{b}$，$\vec{CD} = 3\vec{a} - 3\vec{b}$，则",
    ["$A, C, D$ are collinear", "$A, B, D$ are collinear", "$B, C, D$ are collinear", "$A, B, C$ are collinear"],
    ["$A, C, D$ 三点共线", "$A, B, D$ 三点共线", "$B, C, D$ 三点共线", "$A, B, C$ 三点共线"],
    1,
    "1. Three points are collinear when one connecting vector is a scalar multiple of another sharing a point.\n2. Compute $\\vec{BD} = \\vec{BC} + \\vec{CD} = (-2\\vec a + 8\\vec b) + (3\\vec a - 3\\vec b) = \\vec a + 5\\vec b$.\n3. Notice $\\vec{BD} = \\vec a + 5\\vec b = \\vec{AB}$, so $\\vec{AB}$ and $\\vec{BD}$ are equal (parallel) and share point $B$.\n4. Hence $A, B, D$ are collinear — answer (B).",
    "1. 三点共线当其中一条连接向量是另一条（含公共点）的数乘。\n2. 计算 $\\vec{BD} = \\vec{BC} + \\vec{CD} = (-2\\vec a + 8\\vec b) + (3\\vec a - 3\\vec b) = \\vec a + 5\\vec b$。\n3. 注意 $\\vec{BD} = \\vec a + 5\\vec b = \\vec{AB}$，故 $\\vec{AB}$ 与 $\\vec{BD}$ 相等（平行）且共点 $B$。\n4. 因此 $A, B, D$ 三点共线，选 (B)。")

add(45, "coordinate-geometry", "hard", 2,
    r"Line $l$ is perpendicular to $l_1: x + 2y + 4 = 0$ and passes through the intersection of $l_2: x + y + 1 = 0$ and $l_3: 2x + y - 1 = 0$. Then $l$ is",
    r"直线 $l$ 垂直于 $l_1: x + 2y + 4 = 0$，且经过 $l_2: x + y + 1 = 0$ 与 $l_3: 2x + y - 1 = 0$ 的交点。则 $l$ 的方程为",
    [r"$2x - y - 7 = 0$", r"$x - 2y - 1 = 0$", r"$2x + y - 5 = 0$", r"$x + 2y - 3 = 0$"],
    [r"$2x - y - 7 = 0$", r"$x - 2y - 1 = 0$", r"$2x + y - 5 = 0$", r"$x + 2y - 3 = 0$"],
    0,
    "1. Find the intersection of $l_2, l_3$. Subtract: $(2x+y-1) - (x+y+1) = 0 \\Rightarrow x - 2 = 0 \\Rightarrow x = 2$; then $y = -3$. Point $(2, -3)$.\n2. $l_1: x + 2y + 4 = 0$ has slope $-\\frac12$, so a perpendicular line has slope $2$.\n3. Point-slope through $(2, -3)$: $y + 3 = 2(x - 2)$.\n4. Simplify: $y = 2x - 7$, i.e. $2x - y - 7 = 0$ — answer (A).",
    "1. 求 $l_2, l_3$ 的交点。相减：$(2x+y-1) - (x+y+1) = 0 \\Rightarrow x - 2 = 0 \\Rightarrow x = 2$；再得 $y = -3$。交点 $(2, -3)$。\n2. $l_1: x + 2y + 4 = 0$ 斜率为 $-\\frac12$，故垂线斜率为 $2$。\n3. 点斜式过 $(2, -3)$：$y + 3 = 2(x - 2)$。\n4. 化简：$y = 2x - 7$，即 $2x - y - 7 = 0$，选 (A)。")

add(46, "complex", "hard", 2,
    r"On the complex plane, $z$ lies on the line $x - y = 0$. If $z$ is a root of $x^2 + mx + 4 = 0$ (with real $m$), then $m =$",
    r"在复平面上，复数 $z$ 对应的点在直线 $x - y = 0$ 上。若 $z$ 是方程 $x^2 + mx + 4 = 0$（$m$ 为实数）的根，则 $m =$",
    [r"$\sqrt2$ or $2\sqrt2$", r"$2\sqrt2$ or $-2\sqrt2$", r"$-\sqrt2$ or $-2\sqrt2$", r"$\sqrt2$ or $-\sqrt2$"],
    [r"$\sqrt2$ 或 $2\sqrt2$", r"$2\sqrt2$ 或 $-2\sqrt2$", r"$-\sqrt2$ 或 $-2\sqrt2$", r"$\sqrt2$ 或 $-\sqrt2$"],
    1,
    "1. The point is on $x - y = 0$, so $z = t + ti$ for some real $t \\ne 0$ (a genuine complex root).\n2. With real coefficients, the other root is the conjugate $\\bar z = t - ti$. Product of roots $= \\frac{4}{1} = 4$.\n3. $z\\bar z = t^2 + t^2 = 2t^2 = 4 \\Rightarrow t^2 = 2 \\Rightarrow t = \\pm\\sqrt2$.\n4. Sum of roots $= z + \\bar z = 2t = -m$, so $m = -2t = \\mp 2\\sqrt2$, i.e. $m = 2\\sqrt2$ or $-2\\sqrt2$ — answer (B).",
    "1. 点在 $x - y = 0$ 上，故 $z = t + ti$（$t$ 为实数且 $t \\ne 0$，为真正的虚根）。\n2. 系数为实数时，另一根为共轭 $\\bar z = t - ti$。两根之积 $= \\frac{4}{1} = 4$。\n3. $z\\bar z = t^2 + t^2 = 2t^2 = 4 \\Rightarrow t^2 = 2 \\Rightarrow t = \\pm\\sqrt2$。\n4. 两根之和 $= z + \\bar z = 2t = -m$，故 $m = -2t = \\mp 2\\sqrt2$，即 $m = 2\\sqrt2$ 或 $-2\\sqrt2$，选 (B)。")

add(47, "sequence", "hard", 2,
    r"In a sequence $\{a_n\}$, $a_1 = 1$ and $\dfrac{1}{a_n} + \dfrac{2}{a_{n+1}} = 0$. Let $b_n = |a_n|$. The sum of the first $n$ terms $S_n =$",
    r"在数列 $\{a_n\}$ 中，$a_1 = 1$，且 $\dfrac{1}{a_n} + \dfrac{2}{a_{n+1}} = 0$。设 $b_n = |a_n|$，则前 $n$ 项和 $S_n =$",
    [r"$\dfrac{1 + 2^n}{3}$", r"$\dfrac{|1 - (-2)^n|}{3}$", r"$2^n - 1$", r"$(-2)^n - 1$"],
    [r"$\dfrac{1 + 2^n}{3}$", r"$\dfrac{|1 - (-2)^n|}{3}$", r"$2^n - 1$", r"$(-2)^n - 1$"],
    2,
    "1. Rearrange the recurrence: $\\dfrac{2}{a_{n+1}} = -\\dfrac{1}{a_n} \\Rightarrow a_{n+1} = -2a_n$.\n2. So $\\{a_n\\}$ is geometric with ratio $-2$: $a_n = (-2)^{n-1}$.\n3. Then $b_n = |a_n| = 2^{n-1}$, a geometric sequence with ratio $2$ and first term $1$.\n4. Sum: $S_n = \\dfrac{2^n - 1}{2 - 1} = 2^n - 1$ — answer (C).",
    "1. 整理递推：$\\dfrac{2}{a_{n+1}} = -\\dfrac{1}{a_n} \\Rightarrow a_{n+1} = -2a_n$。\n2. 故 $\\{a_n\\}$ 是公比为 $-2$ 的等比数列：$a_n = (-2)^{n-1}$。\n3. 则 $b_n = |a_n| = 2^{n-1}$，是首项 $1$、公比 $2$ 的等比数列。\n4. 求和：$S_n = \\dfrac{2^n - 1}{2 - 1} = 2^n - 1$，选 (C)。")

add(48, "probability", "hard", 2,
    r"App preferences are — High school (200): A:80 B:40 C:60 D:20; College (80): A:30 B:20 C:20 D:10. Picking one from each group independently, the probability their favorite apps differ is",
    r"最喜欢的跑步 App 统计——高中生（200 人）：A:80 B:40 C:60 D:20；大学生（80 人）：A:30 B:20 C:20 D:10。从两组各随机抽取一人，则两人喜欢的 App 不同的概率是",
    [r"$\dfrac{23}{80}$", r"$\dfrac{57}{80}$", r"$\dfrac{9}{20}$", r"$\dfrac{11}{20}$"],
    [r"$\dfrac{23}{80}$", r"$\dfrac{57}{80}$", r"$\dfrac{9}{20}$", r"$\dfrac{11}{20}$"],
    1,
    "1. It is easier to find $P(\\text{same app})$ first, then subtract from $1$.\n2. Multiply matching counts and divide by $200 \\times 80 = 16000$: same $= 80\\cdot30 + 40\\cdot20 + 60\\cdot20 + 20\\cdot10 = 2400+800+1200+200 = 4600$.\n3. $P(\\text{same}) = \\dfrac{4600}{16000} = \\dfrac{23}{80}$.\n4. So $P(\\text{different}) = 1 - \\dfrac{23}{80} = \\dfrac{57}{80}$ — answer (B).\nTip: computing 'different' directly needs 12 cross terms; 'same' needs only 4 — always look for the easier complement.",
    "1. 先求 $P(\\text{相同 App})$ 更简单，再用 $1$ 减去。\n2. 把对应人数相乘再除以 $200 \\times 80 = 16000$：相同 $= 80\\cdot30 + 40\\cdot20 + 60\\cdot20 + 20\\cdot10 = 2400+800+1200+200 = 4600$。\n3. $P(\\text{相同}) = \\dfrac{4600}{16000} = \\dfrac{23}{80}$。\n4. 故 $P(\\text{不同}) = 1 - \\dfrac{23}{80} = \\dfrac{57}{80}$，选 (B)。\n提示：直接算‘不同’要 12 个交叉项，而‘相同’只需 4 项——优先用更简单的对立事件。")

print(json.dumps(Q, ensure_ascii=False, indent=2))
