#!/usr/bin/env python3
"""
15 AI-generated coordinate-geometry PRACTICE questions (source: "AI-generated").
Supplement — never replace — the real-exam bank. Every answer was solved
independently and is numerically re-checked by the merge step.

Run:  python3 scripts/build_gen_coordgeo.py   (prints JSON to stdout)
"""
import json

Q = []
def add(n, diff, qen, qzh, oen, ozh, ans, een, ezh):
    Q.append({
        "id": f"math-gen-{n:04d}",
        "subject": "math", "topic": "coordinate-geometry", "source": "AI-generated",
        "points": 2, "difficulty": diff,
        "question": {"en": qen, "zh": qzh},
        "options": {"en": oen, "zh": ozh},
        "answer": ans,                       # correct option authored at index 0; shuffled below
        "explanation": {"en": een, "zh": ezh},
    })

add(16, "easy",
    r"The midpoint of the segment joining $A(-1, 4)$ and $B(5, -2)$ is",
    r"连接 $A(-1, 4)$ 与 $B(5, -2)$ 的线段中点是",
    [r"$(2, 1)$", r"$(2, 3)$", r"$(3, 1)$", r"$(4, 2)$"],
    [r"$(2, 1)$", r"$(2, 3)$", r"$(3, 1)$", r"$(4, 2)$"],
    0,
    "1. Midpoint formula: $\\left(\\dfrac{x_1+x_2}{2}, \\dfrac{y_1+y_2}{2}\\right)$.\n2. $x$: $\\dfrac{-1+5}{2} = \\dfrac{4}{2} = 2$.\n3. $y$: $\\dfrac{4+(-2)}{2} = \\dfrac{2}{2} = 1$.\n4. So the midpoint is $(2, 1)$ — answer (A).",
    "1. 中点公式：$\\left(\\dfrac{x_1+x_2}{2}, \\dfrac{y_1+y_2}{2}\\right)$。\n2. 横坐标：$\\dfrac{-1+5}{2} = \\dfrac{4}{2} = 2$。\n3. 纵坐标：$\\dfrac{4+(-2)}{2} = \\dfrac{2}{2} = 1$。\n4. 故中点为 $(2, 1)$，选 (A)。")

add(17, "medium",
    r"The line through $(0, -1)$ that is parallel to $2x - y + 3 = 0$ has equation",
    r"过点 $(0, -1)$ 且平行于 $2x - y + 3 = 0$ 的直线方程是",
    [r"$2x - y - 1 = 0$", r"$2x - y + 1 = 0$", r"$x + 2y + 2 = 0$", r"$x - 2y - 2 = 0$"],
    [r"$2x - y - 1 = 0$", r"$2x - y + 1 = 0$", r"$x + 2y + 2 = 0$", r"$x - 2y - 2 = 0$"],
    0,
    "1. Parallel lines have equal slope. Rewrite $2x - y + 3 = 0$ as $y = 2x + 3$, so the slope is $2$.\n2. Use point-slope through $(0, -1)$: $y - (-1) = 2(x - 0)$, i.e. $y + 1 = 2x$.\n3. Rearrange: $2x - y - 1 = 0$ — answer (A).\nTip: parallel keeps the same $x,y$ coefficients ($2x - y$) and only the constant changes.",
    "1. 平行线斜率相等。把 $2x - y + 3 = 0$ 写成 $y = 2x + 3$，斜率为 $2$。\n2. 点斜式过 $(0, -1)$：$y - (-1) = 2(x - 0)$，即 $y + 1 = 2x$。\n3. 整理：$2x - y - 1 = 0$，选 (A)。\n提示：平行时 $x, y$ 的系数（$2x - y$）不变，只改变常数项。")

add(18, "medium",
    r"The distance from the point $(1, -2)$ to the line $3x - 4y + 1 = 0$ is",
    r"点 $(1, -2)$ 到直线 $3x - 4y + 1 = 0$ 的距离是",
    [r"$\dfrac{12}{5}$", r"$\dfrac{6}{5}$", r"$2$", r"$\dfrac{12}{7}$"],
    [r"$\dfrac{12}{5}$", r"$\dfrac{6}{5}$", r"$2$", r"$\dfrac{12}{7}$"],
    0,
    "1. Point-to-line distance: $d = \\dfrac{|Ax_0 + By_0 + C|}{\\sqrt{A^2 + B^2}}$.\n2. Numerator: $|3(1) - 4(-2) + 1| = |3 + 8 + 1| = 12$.\n3. Denominator: $\\sqrt{3^2 + (-4)^2} = \\sqrt{25} = 5$.\n4. So $d = \\dfrac{12}{5}$ — answer (A).",
    "1. 点到直线距离：$d = \\dfrac{|Ax_0 + By_0 + C|}{\\sqrt{A^2 + B^2}}$。\n2. 分子：$|3(1) - 4(-2) + 1| = |3 + 8 + 1| = 12$。\n3. 分母：$\\sqrt{3^2 + (-4)^2} = \\sqrt{25} = 5$。\n4. 故 $d = \\dfrac{12}{5}$，选 (A)。")

add(19, "medium",
    r"The center and radius of the circle $(x-1)^2 + (y+3)^2 = 9$ are",
    r"圆 $(x-1)^2 + (y+3)^2 = 9$ 的圆心和半径是",
    [r"center $(1, -3)$, radius $3$", r"center $(-1, 3)$, radius $3$", r"center $(1, -3)$, radius $9$", r"center $(-1, 3)$, radius $9$"],
    [r"圆心 $(1, -3)$，半径 $3$", r"圆心 $(-1, 3)$，半径 $3$", r"圆心 $(1, -3)$，半径 $9$", r"圆心 $(-1, 3)$，半径 $9$"],
    0,
    "1. Standard form $(x-a)^2 + (y-b)^2 = r^2$ has center $(a, b)$ and radius $r$.\n2. Match: $x - 1$ gives $a = 1$; $y + 3 = y - (-3)$ gives $b = -3$.\n3. Right side $9 = r^2$, so $r = 3$.\n4. Center $(1, -3)$, radius $3$ — answer (A).\nTip: read the center with FLIPPED signs, and take the square root for the radius ($9$ is $r^2$).",
    "1. 标准式 $(x-a)^2 + (y-b)^2 = r^2$ 的圆心为 $(a, b)$，半径为 $r$。\n2. 对照：$x - 1$ 得 $a = 1$；$y + 3 = y - (-3)$ 得 $b = -3$。\n3. 右边 $9 = r^2$，故 $r = 3$。\n4. 圆心 $(1, -3)$，半径 $3$，选 (A)。\n提示：圆心取相反符号，半径要开方（$9$ 是 $r^2$）。")

add(20, "medium",
    r"The slope of a line perpendicular to $y = \dfrac{2}{3}x + 5$ is",
    r"与直线 $y = \dfrac{2}{3}x + 5$ 垂直的直线的斜率是",
    [r"$-\dfrac{3}{2}$", r"$\dfrac{3}{2}$", r"$-\dfrac{2}{3}$", r"$\dfrac{2}{3}$"],
    [r"$-\dfrac{3}{2}$", r"$\dfrac{3}{2}$", r"$-\dfrac{2}{3}$", r"$\dfrac{2}{3}$"],
    0,
    "1. The given slope is $\\dfrac{2}{3}$.\n2. Perpendicular slopes are negative reciprocals: $k_\\perp = -\\dfrac{1}{k}$.\n3. So $k_\\perp = -\\dfrac{1}{2/3} = -\\dfrac{3}{2}$ — answer (A).\nTip: flip the fraction AND change the sign; option (B) only flips, option (C) only changes sign.",
    "1. 已知斜率为 $\\dfrac{2}{3}$。\n2. 垂直直线的斜率互为负倒数：$k_\\perp = -\\dfrac{1}{k}$。\n3. 故 $k_\\perp = -\\dfrac{1}{2/3} = -\\dfrac{3}{2}$，选 (A)。\n提示：要把分数取倒数并变号；(B) 只取倒数，(C) 只变号。")

add(21, "easy",
    r"The $x$-intercept of the line $3x + 2y - 6 = 0$ is",
    r"直线 $3x + 2y - 6 = 0$ 的 $x$ 轴截距是",
    [r"$2$", r"$3$", r"$-2$", r"$6$"],
    [r"$2$", r"$3$", r"$-2$", r"$6$"],
    0,
    "1. The $x$-intercept is where the line crosses the $x$-axis, so set $y = 0$.\n2. $3x + 2(0) - 6 = 0 \\Rightarrow 3x = 6$.\n3. $x = 2$ — answer (A).\nTip: for the $y$-intercept you would instead set $x = 0$ (giving $y = 3$).",
    "1. $x$ 轴截距是直线与 $x$ 轴的交点，故令 $y = 0$。\n2. $3x + 2(0) - 6 = 0 \\Rightarrow 3x = 6$。\n3. $x = 2$，选 (A)。\n提示：求 $y$ 轴截距则令 $x = 0$（得 $y = 3$）。")

add(22, "medium",
    r"The line $y = x + 1$ intersects the parabola $y^2 = 4x$ at how many points?",
    r"直线 $y = x + 1$ 与抛物线 $y^2 = 4x$ 有几个交点？",
    [r"$1$", r"$0$", r"$2$", r"$3$"],
    [r"$1$", r"$0$", r"$2$", r"$3$"],
    0,
    "1. Substitute $y = x + 1$ into $y^2 = 4x$: $(x+1)^2 = 4x$.\n2. Expand: $x^2 + 2x + 1 = 4x \\Rightarrow x^2 - 2x + 1 = 0$.\n3. Factor: $(x-1)^2 = 0$, a repeated root $x = 1$ (discriminant $= 0$).\n4. One intersection point — answer (A). (The line is tangent to the parabola.)",
    "1. 把 $y = x + 1$ 代入 $y^2 = 4x$：$(x+1)^2 = 4x$。\n2. 展开：$x^2 + 2x + 1 = 4x \\Rightarrow x^2 - 2x + 1 = 0$。\n3. 分解：$(x-1)^2 = 0$，重根 $x = 1$（判别式 $= 0$）。\n4. 只有一个交点，选 (A)。（直线与抛物线相切。）")

add(23, "hard",
    r"The eccentricity of the ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ is",
    r"椭圆 $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ 的离心率是",
    [r"$\dfrac{3}{5}$", r"$\dfrac{4}{5}$", r"$\dfrac{3}{4}$", r"$\dfrac{5}{3}$"],
    [r"$\dfrac{3}{5}$", r"$\dfrac{4}{5}$", r"$\dfrac{3}{4}$", r"$\dfrac{5}{3}$"],
    0,
    "1. For an ellipse $a^2 = 25$ (the larger denominator) and $b^2 = 16$, so $a = 5$, $b = 4$.\n2. $c^2 = a^2 - b^2 = 25 - 16 = 9$, so $c = 3$.\n3. Eccentricity $e = \\dfrac{c}{a} = \\dfrac{3}{5}$ — answer (A).\nTip: for an ellipse $c^2 = a^2 - b^2$ (subtract), unlike a hyperbola where you add.",
    "1. 椭圆中 $a^2 = 25$（较大分母）、$b^2 = 16$，故 $a = 5$、$b = 4$。\n2. $c^2 = a^2 - b^2 = 25 - 16 = 9$，故 $c = 3$。\n3. 离心率 $e = \\dfrac{c}{a} = \\dfrac{3}{5}$，选 (A)。\n提示：椭圆 $c^2 = a^2 - b^2$（相减），不同于双曲线的相加。")

add(24, "medium",
    r"The line $x = 2$ and the circle $x^2 + y^2 = 4$ are in what relationship?",
    r"直线 $x = 2$ 与圆 $x^2 + y^2 = 4$ 的位置关系是",
    [r"tangent", r"intersecting (two points)", r"separate (no intersection)", r"the line is a diameter"],
    [r"相切", r"相交（两点）", r"相离（无交点）", r"直线为直径"],
    0,
    "1. The circle $x^2 + y^2 = 4$ has center $(0, 0)$ and radius $r = 2$.\n2. Distance from the center to the vertical line $x = 2$ is $|2 - 0| = 2$.\n3. Since this distance equals the radius ($2 = 2$), the line touches the circle at exactly one point.\n4. They are tangent — answer (A).",
    "1. 圆 $x^2 + y^2 = 4$ 的圆心为 $(0, 0)$，半径 $r = 2$。\n2. 圆心到竖直线 $x = 2$ 的距离为 $|2 - 0| = 2$。\n3. 该距离等于半径（$2 = 2$），故直线与圆恰有一个公共点。\n4. 两者相切，选 (A)。")

add(25, "hard",
    r"The asymptotes of the hyperbola $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$ are",
    r"双曲线 $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$ 的渐近线是",
    [r"$y = \pm\dfrac{4}{3}x$", r"$y = \pm\dfrac{3}{4}x$", r"$y = \pm\dfrac{16}{9}x$", r"$y = \pm\dfrac{9}{16}x$"],
    [r"$y = \pm\dfrac{4}{3}x$", r"$y = \pm\dfrac{3}{4}x$", r"$y = \pm\dfrac{16}{9}x$", r"$y = \pm\dfrac{9}{16}x$"],
    0,
    "1. For $\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$ the asymptotes are $y = \\pm\\dfrac{b}{a}x$.\n2. Here $a^2 = 9 \\Rightarrow a = 3$ and $b^2 = 16 \\Rightarrow b = 4$.\n3. So the asymptotes are $y = \\pm\\dfrac{4}{3}x$ — answer (A).\nTip: take square roots first; $\\dfrac{16}{9}$ (option C) wrongly uses $b^2/a^2$.",
    "1. 对 $\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$，渐近线为 $y = \\pm\\dfrac{b}{a}x$。\n2. 此处 $a^2 = 9 \\Rightarrow a = 3$，$b^2 = 16 \\Rightarrow b = 4$。\n3. 故渐近线为 $y = \\pm\\dfrac{4}{3}x$，选 (A)。\n提示：先开方；$\\dfrac{16}{9}$（选项 C）误用了 $b^2/a^2$。")

add(26, "medium",
    r"If $A(2, 1)$, $B(4, 5)$ and the point $M$ divides $\overline{AB}$ such that $M$ is the midpoint, then a line through $M$ perpendicular to $AB$ (the perpendicular bisector) has slope",
    r"已知 $A(2, 1)$、$B(4, 5)$，$M$ 为 $\overline{AB}$ 的中点。则过 $M$ 且垂直于 $AB$ 的直线（中垂线）的斜率是",
    [r"$-\dfrac{1}{2}$", r"$2$", r"$\dfrac{1}{2}$", r"$-2$"],
    [r"$-\dfrac{1}{2}$", r"$2$", r"$\dfrac{1}{2}$", r"$-2$"],
    0,
    "1. Slope of $AB$: $\\dfrac{5 - 1}{4 - 2} = \\dfrac{4}{2} = 2$.\n2. The perpendicular bisector is perpendicular to $AB$, so its slope is the negative reciprocal of $2$.\n3. $k_\\perp = -\\dfrac{1}{2}$ — answer (A).\nTip: the question only asks for the slope, so the coordinates of $M$ aren't needed here.",
    "1. $AB$ 的斜率：$\\dfrac{5 - 1}{4 - 2} = \\dfrac{4}{2} = 2$。\n2. 中垂线垂直于 $AB$，其斜率为 $2$ 的负倒数。\n3. $k_\\perp = -\\dfrac{1}{2}$，选 (A)。\n提示：本题只问斜率，故无需求出 $M$ 的坐标。")

add(27, "hard",
    r"The length of the chord cut from the circle $x^2 + y^2 = 25$ by the line $y = 3$ is",
    r"直线 $y = 3$ 在圆 $x^2 + y^2 = 25$ 上截得的弦长是",
    [r"$8$", r"$4$", r"$10$", r"$6$"],
    [r"$8$", r"$4$", r"$10$", r"$6$"],
    0,
    "1. The circle has center $(0, 0)$ and radius $r = 5$.\n2. The distance from the center to the line $y = 3$ is $d = 3$.\n3. Half-chord length $= \\sqrt{r^2 - d^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4$.\n4. Full chord $= 2 \\times 4 = 8$ — answer (A).\nTip: substituting $y = 3$ gives $x^2 = 16$, $x = \\pm 4$, endpoints $(\\pm4, 3)$ — distance $8$, confirming the result.",
    "1. 圆心为 $(0, 0)$，半径 $r = 5$。\n2. 圆心到直线 $y = 3$ 的距离 $d = 3$。\n3. 半弦长 $= \\sqrt{r^2 - d^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4$。\n4. 整条弦长 $= 2 \\times 4 = 8$，选 (A)。\n提示：代入 $y = 3$ 得 $x^2 = 16$，$x = \\pm 4$，端点为 $(\\pm4, 3)$，距离 $8$，验证无误。")

add(28, "easy",
    r"Point $P(3, -5)$ is reflected through the origin to point $Q$. The coordinates of $Q$ are",
    r"点 $P(3, -5)$ 关于原点对称得到点 $Q$，则 $Q$ 的坐标是",
    [r"$(-3, 5)$", r"$(3, 5)$", r"$(-3, -5)$", r"$(5, -3)$"],
    [r"$(-3, 5)$", r"$(3, 5)$", r"$(-3, -5)$", r"$(5, -3)$"],
    0,
    "1. Reflection through the origin negates BOTH coordinates: $(x, y) \\to (-x, -y)$.\n2. Apply to $P(3, -5)$: $x \\to -3$, $y \\to -(-5) = 5$.\n3. So $Q = (-3, 5)$ — answer (A).\nTip: reflecting only about the $x$-axis would give $(3, 5)$ (option B); the origin flips both signs.",
    "1. 关于原点对称时两个坐标都取相反数：$(x, y) \\to (-x, -y)$。\n2. 代入 $P(3, -5)$：$x \\to -3$，$y \\to -(-5) = 5$。\n3. 故 $Q = (-3, 5)$，选 (A)。\n提示：只关于 $x$ 轴对称会得 $(3, 5)$（选项 B）；关于原点则两个符号都变。")

add(29, "medium",
    r"The two lines $2x + 3y - 6 = 0$ and $4x + 6y + 5 = 0$ are",
    r"两条直线 $2x + 3y - 6 = 0$ 与 $4x + 6y + 5 = 0$ 的关系是",
    [r"parallel", r"perpendicular", r"the same line", r"intersecting at one point"],
    [r"平行", r"垂直", r"是同一条直线", r"相交于一点"],
    0,
    "1. Compare coefficients. The second line's $x,y$ coefficients $(4, 6)$ are exactly $2\\times(2, 3)$, the first line's.\n2. Equal coefficient ratios $\\dfrac{4}{2} = \\dfrac{6}{3} = 2$ mean equal slopes, so the lines are parallel or identical.\n3. Check the constant: $\\dfrac{5}{-6} \\ne 2$, so they are NOT the same line.\n4. Hence the lines are parallel — answer (A).",
    "1. 比较系数。第二条直线的 $x, y$ 系数 $(4, 6)$ 恰为第一条 $(2, 3)$ 的 $2$ 倍。\n2. 系数比相等 $\\dfrac{4}{2} = \\dfrac{6}{3} = 2$ 说明斜率相等，故两线平行或重合。\n3. 检验常数项：$\\dfrac{5}{-6} \\ne 2$，故不是同一条直线。\n4. 因此两线平行，选 (A)。")

add(30, "hard",
    r"The equation of the circle with $A(1, 2)$ and $B(5, 6)$ as endpoints of a diameter is",
    r"以 $A(1, 2)$ 与 $B(5, 6)$ 为直径两端点的圆的方程是",
    [r"$(x-3)^2 + (y-4)^2 = 8$", r"$(x-3)^2 + (y-4)^2 = 32$", r"$(x-3)^2 + (y-4)^2 = 4$", r"$(x-2)^2 + (y-3)^2 = 8$"],
    [r"$(x-3)^2 + (y-4)^2 = 8$", r"$(x-3)^2 + (y-4)^2 = 32$", r"$(x-3)^2 + (y-4)^2 = 4$", r"$(x-2)^2 + (y-3)^2 = 8$"],
    0,
    "1. The center is the midpoint of the diameter: $\\left(\\dfrac{1+5}{2}, \\dfrac{2+6}{2}\\right) = (3, 4)$.\n2. The radius is half the diameter. Diameter $|AB| = \\sqrt{(5-1)^2 + (6-2)^2} = \\sqrt{16+16} = \\sqrt{32} = 4\\sqrt2$.\n3. Radius $r = 2\\sqrt2$, so $r^2 = 8$.\n4. Equation: $(x-3)^2 + (y-4)^2 = 8$ — answer (A).\nTip: $r^2 = 8$, not $32$ ($=|AB|^2$, the trap in B) nor the diameter itself.",
    "1. 圆心为直径中点：$\\left(\\dfrac{1+5}{2}, \\dfrac{2+6}{2}\\right) = (3, 4)$。\n2. 半径为直径的一半。直径 $|AB| = \\sqrt{(5-1)^2 + (6-2)^2} = \\sqrt{16+16} = \\sqrt{32} = 4\\sqrt2$。\n3. 半径 $r = 2\\sqrt2$，故 $r^2 = 8$。\n4. 方程：$(x-3)^2 + (y-4)^2 = 8$，选 (A)。\n提示：$r^2 = 8$，不是 $32$（$=|AB|^2$，选项 B 的陷阱），也不是直径本身。")

# --- Clean up distractor letter references (answers get shuffled below) ---
for q in Q:
    for lang in ("en", "zh"):
        e = q["explanation"][lang]
        e = e.replace(r"; option (B) only flips, option (C) only changes sign.",
                      r"; one common slip flips only, another changes only the sign.")
        e = e.replace(r"；(B) 只取倒数，(C) 只变号。",
                      r"；常见错误是只取倒数或只变号。")
        e = e.replace(r" $\dfrac{16}{9}$ (option C) wrongly uses", r" $\dfrac{16}{9}$ wrongly uses")
        e = e.replace(r"$\dfrac{16}{9}$（选项 C）误用了", r"$\dfrac{16}{9}$ 误用了")
        e = e.replace(r"would give $(3, 5)$ (option B); the origin", r"would give $(3, 5)$; the origin")
        e = e.replace(r"会得 $(3, 5)$（选项 B）；关于原点", r"会得 $(3, 5)$；关于原点")
        e = e.replace(r" ($=|AB|^2$, the trap in B) nor", r" ($=|AB|^2$) nor")
        e = e.replace(r"（$=|AB|^2$，选项 B 的陷阱）", r"（$=|AB|^2$）")
        q["explanation"][lang] = e

# --- Shuffle option order so the answer is not always A; fix the answer letter reference ---
import random
rng = random.Random(20260610)
LET = "ABCD"
for q in Q:
    perm = [0, 1, 2, 3]
    rng.shuffle(perm)
    for lang in ("en", "zh"):
        q["options"][lang] = [q["options"][lang][i] for i in perm]
    new_idx = perm.index(0)
    q["answer"] = new_idx
    letter = LET[new_idx]
    for lang in ("en", "zh"):
        q["explanation"][lang] = (
            q["explanation"][lang]
            .replace("answer (A)", f"answer ({letter})")
            .replace("选 (A)", f"选 ({letter})")
        )

print(json.dumps(Q, ensure_ascii=False, indent=2))
