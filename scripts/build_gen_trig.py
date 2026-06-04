#!/usr/bin/env python3
"""
15 AI-generated trigonometry PRACTICE questions (source: "AI-generated").
These supplement — never replace — the real-exam bank. Every answer was solved
independently and is numerically re-checked by scripts/verify_gen_trig.py.

Run:  python3 scripts/build_gen_trig.py   (prints JSON to stdout)
"""
import json

Q = []
def add(n, diff, qen, qzh, oen, ozh, ans, een, ezh):
    Q.append({
        "id": f"math-gen-{n:04d}",
        "subject": "math", "topic": "trigonometry", "source": "AI-generated",
        "points": 2, "difficulty": diff,
        "question": {"en": qen, "zh": qzh},
        "options": {"en": oen, "zh": ozh},
        "answer": ans,
        "explanation": {"en": een, "zh": ezh},
    })

add(1, "medium",
    r"If $\sin\alpha = \dfrac{1}{3}$, then $\cos 2\alpha =$",
    r"若 $\sin\alpha = \dfrac{1}{3}$，则 $\cos 2\alpha =$",
    [r"$\dfrac{7}{9}$", r"$-\dfrac{7}{9}$", r"$\dfrac{1}{9}$", r"$\dfrac{8}{9}$"],
    [r"$\dfrac{7}{9}$", r"$-\dfrac{7}{9}$", r"$\dfrac{1}{9}$", r"$\dfrac{8}{9}$"],
    0,
    "1. Pick the double-angle form that uses only $\\sin\\alpha$: $\\cos 2\\alpha = 1 - 2\\sin^2\\alpha$.\n2. Square: $\\sin^2\\alpha = \\left(\\frac13\\right)^2 = \\frac19$.\n3. Substitute: $\\cos 2\\alpha = 1 - 2\\cdot\\frac19 = 1 - \\frac29 = \\frac79$ — answer (A).\nTip: this form needs no quadrant info, since only $\\sin^2\\alpha$ appears.",
    "1. 选用只含 $\\sin\\alpha$ 的二倍角公式：$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha$。\n2. 平方：$\\sin^2\\alpha = \\left(\\frac13\\right)^2 = \\frac19$。\n3. 代入：$\\cos 2\\alpha = 1 - 2\\cdot\\frac19 = 1 - \\frac29 = \\frac79$，选 (A)。\n提示：此公式只含 $\\sin^2\\alpha$，无需象限信息。")

add(2, "easy",
    r"$\sin\dfrac{5\pi}{6} =$",
    r"$\sin\dfrac{5\pi}{6} =$",
    [r"$\dfrac{1}{2}$", r"$\dfrac{\sqrt3}{2}$", r"$-\dfrac{1}{2}$", r"$-\dfrac{\sqrt3}{2}$"],
    [r"$\dfrac{1}{2}$", r"$\dfrac{\sqrt3}{2}$", r"$-\dfrac{1}{2}$", r"$-\dfrac{\sqrt3}{2}$"],
    0,
    "1. $\\frac{5\\pi}{6}$ is in the second quadrant, where sine is positive.\n2. Its reference angle is $\\pi - \\frac{5\\pi}{6} = \\frac{\\pi}{6}$.\n3. So $\\sin\\frac{5\\pi}{6} = \\sin\\frac{\\pi}{6} = \\frac12$ — answer (A).",
    "1. $\\frac{5\\pi}{6}$ 在第二象限，正弦为正。\n2. 参考角为 $\\pi - \\frac{5\\pi}{6} = \\frac{\\pi}{6}$。\n3. 故 $\\sin\\frac{5\\pi}{6} = \\sin\\frac{\\pi}{6} = \\frac12$，选 (A)。")

add(3, "medium",
    r"If $\cos\alpha = -\dfrac{4}{5}$ and $\alpha$ is in the third quadrant, then $\tan\alpha =$",
    r"若 $\cos\alpha = -\dfrac{4}{5}$，且 $\alpha$ 在第三象限，则 $\tan\alpha =$",
    [r"$\dfrac{3}{4}$", r"$-\dfrac{3}{4}$", r"$\dfrac{4}{3}$", r"$-\dfrac{4}{3}$"],
    [r"$\dfrac{3}{4}$", r"$-\dfrac{3}{4}$", r"$\dfrac{4}{3}$", r"$-\dfrac{4}{3}$"],
    0,
    "1. Find $\\sin\\alpha$ from $\\sin^2\\alpha = 1 - \\cos^2\\alpha = 1 - \\frac{16}{25} = \\frac{9}{25}$, so $|\\sin\\alpha| = \\frac35$.\n2. In the third quadrant sine is NEGATIVE, so $\\sin\\alpha = -\\frac35$.\n3. $\\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha} = \\dfrac{-3/5}{-4/5} = \\dfrac34$ — answer (A).\nTip: in QIII both sine and cosine are negative, so their ratio (tangent) is positive.",
    "1. 由 $\\sin^2\\alpha = 1 - \\cos^2\\alpha = 1 - \\frac{16}{25} = \\frac{9}{25}$，得 $|\\sin\\alpha| = \\frac35$。\n2. 第三象限正弦为负，故 $\\sin\\alpha = -\\frac35$。\n3. $\\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha} = \\dfrac{-3/5}{-4/5} = \\dfrac34$，选 (A)。\n提示：第三象限正弦、余弦都为负，其比值（正切）为正。")

add(4, "hard",
    r"If $\cos\alpha = \dfrac{3}{5}$ and $\cos\beta = \dfrac{12}{13}$ with both $\alpha, \beta$ in the first quadrant, then $\cos(\alpha+\beta) =$",
    r"若 $\cos\alpha = \dfrac{3}{5}$，$\cos\beta = \dfrac{12}{13}$，且 $\alpha, \beta$ 都在第一象限，则 $\cos(\alpha+\beta) =$",
    [r"$\dfrac{16}{65}$", r"$\dfrac{56}{65}$", r"$-\dfrac{16}{65}$", r"$\dfrac{33}{65}$"],
    [r"$\dfrac{16}{65}$", r"$\dfrac{56}{65}$", r"$-\dfrac{16}{65}$", r"$\dfrac{33}{65}$"],
    0,
    "1. Get the sines (positive in QI): $\\sin\\alpha = \\sqrt{1 - \\frac{9}{25}} = \\frac45$, $\\sin\\beta = \\sqrt{1 - \\frac{144}{169}} = \\frac{5}{13}$.\n2. Addition formula: $\\cos(\\alpha+\\beta) = \\cos\\alpha\\cos\\beta - \\sin\\alpha\\sin\\beta$.\n3. Substitute: $\\frac35\\cdot\\frac{12}{13} - \\frac45\\cdot\\frac{5}{13} = \\frac{36}{65} - \\frac{20}{65}$.\n4. So $\\cos(\\alpha+\\beta) = \\frac{16}{65}$ — answer (A).\nTip: $\\cos(\\alpha+\\beta)$ uses a MINUS sign; using a plus gives $\\frac{56}{65}$, the trap in (B).",
    "1. 求正弦（第一象限为正）：$\\sin\\alpha = \\sqrt{1 - \\frac{9}{25}} = \\frac45$，$\\sin\\beta = \\sqrt{1 - \\frac{144}{169}} = \\frac{5}{13}$。\n2. 和角公式：$\\cos(\\alpha+\\beta) = \\cos\\alpha\\cos\\beta - \\sin\\alpha\\sin\\beta$。\n3. 代入：$\\frac35\\cdot\\frac{12}{13} - \\frac45\\cdot\\frac{5}{13} = \\frac{36}{65} - \\frac{20}{65}$。\n4. 故 $\\cos(\\alpha+\\beta) = \\frac{16}{65}$，选 (A)。\n提示：$\\cos(\\alpha+\\beta)$ 用减号；用加号会得 $\\frac{56}{65}$，即 (B) 的陷阱。")

add(5, "easy",
    r"The smallest positive period of $y = \sin 2x$ is",
    r"函数 $y = \sin 2x$ 的最小正周期是",
    [r"$\pi$", r"$2\pi$", r"$\dfrac{\pi}{2}$", r"$4\pi$"],
    [r"$\pi$", r"$2\pi$", r"$\dfrac{\pi}{2}$", r"$4\pi$"],
    0,
    "1. For $y = \\sin(\\omega x)$ the period is $T = \\dfrac{2\\pi}{|\\omega|}$.\n2. Here $\\omega = 2$, so $T = \\dfrac{2\\pi}{2} = \\pi$ — answer (A).\nTip: a larger $\\omega$ compresses the wave, giving a SHORTER period.",
    "1. 对 $y = \\sin(\\omega x)$，周期 $T = \\dfrac{2\\pi}{|\\omega|}$。\n2. 此处 $\\omega = 2$，故 $T = \\dfrac{2\\pi}{2} = \\pi$，选 (A)。\n提示：$\\omega$ 越大，波形被压缩，周期越短。")

add(6, "easy",
    r"The maximum value of $y = 3\sin x + 1$ is",
    r"函数 $y = 3\sin x + 1$ 的最大值是",
    [r"$4$", r"$3$", r"$2$", r"$1$"],
    [r"$4$", r"$3$", r"$2$", r"$1$"],
    0,
    "1. $\\sin x$ ranges over $[-1, 1]$, so its maximum is $1$.\n2. Multiplying by $3$: $3\\sin x$ has maximum $3\\cdot 1 = 3$.\n3. Adding $1$: the maximum of $3\\sin x + 1$ is $3 + 1 = 4$ — answer (A).\nTip: in general $a\\sin x + b$ (with $a>0$) has maximum $a + b$ and minimum $-a + b$.",
    "1. $\\sin x$ 的取值范围是 $[-1, 1]$，最大值为 $1$。\n2. 乘以 $3$：$3\\sin x$ 的最大值为 $3\\cdot 1 = 3$。\n3. 加 $1$：$3\\sin x + 1$ 的最大值为 $3 + 1 = 4$，选 (A)。\n提示：一般地 $a\\sin x + b$（$a>0$）最大值为 $a + b$，最小值为 $-a + b$。")

add(7, "easy",
    r"Convert $120^\circ$ to radians.",
    r"将 $120^\circ$ 化为弧度。",
    [r"$\dfrac{2\pi}{3}$", r"$\dfrac{3\pi}{4}$", r"$\dfrac{5\pi}{6}$", r"$\dfrac{\pi}{3}$"],
    [r"$\dfrac{2\pi}{3}$", r"$\dfrac{3\pi}{4}$", r"$\dfrac{5\pi}{6}$", r"$\dfrac{\pi}{3}$"],
    0,
    "1. Multiply degrees by $\\dfrac{\\pi}{180^\\circ}$ to get radians.\n2. $120^\\circ \\times \\dfrac{\\pi}{180^\\circ} = \\dfrac{120\\pi}{180}$.\n3. Simplify $\\dfrac{120}{180} = \\dfrac{2}{3}$, so the answer is $\\dfrac{2\\pi}{3}$ — answer (A).",
    "1. 度数乘以 $\\dfrac{\\pi}{180^\\circ}$ 即得弧度。\n2. $120^\\circ \\times \\dfrac{\\pi}{180^\\circ} = \\dfrac{120\\pi}{180}$。\n3. 化简 $\\dfrac{120}{180} = \\dfrac{2}{3}$，故答案为 $\\dfrac{2\\pi}{3}$，选 (A)。")

add(8, "hard",
    r"If $\tan\alpha = 2$, then $\tan\left(\alpha + \dfrac{\pi}{4}\right) =$",
    r"若 $\tan\alpha = 2$，则 $\tan\left(\alpha + \dfrac{\pi}{4}\right) =$",
    [r"$-3$", r"$3$", r"$\dfrac{1}{3}$", r"$-\dfrac{1}{3}$"],
    [r"$-3$", r"$3$", r"$\dfrac{1}{3}$", r"$-\dfrac{1}{3}$"],
    0,
    "1. Tangent addition: $\\tan\\left(\\alpha + \\frac{\\pi}{4}\\right) = \\dfrac{\\tan\\alpha + \\tan\\frac{\\pi}{4}}{1 - \\tan\\alpha\\tan\\frac{\\pi}{4}}$, and $\\tan\\frac{\\pi}{4} = 1$.\n2. Substitute $\\tan\\alpha = 2$: $\\dfrac{2 + 1}{1 - 2\\cdot 1} = \\dfrac{3}{-1}$.\n3. So $\\tan\\left(\\alpha + \\frac{\\pi}{4}\\right) = -3$ — answer (A).\nTip: don't drop the minus in the denominator; $1 - \\tan\\alpha$ becomes $-1$ here.",
    "1. 正切和角公式：$\\tan\\left(\\alpha + \\frac{\\pi}{4}\\right) = \\dfrac{\\tan\\alpha + \\tan\\frac{\\pi}{4}}{1 - \\tan\\alpha\\tan\\frac{\\pi}{4}}$，且 $\\tan\\frac{\\pi}{4} = 1$。\n2. 代入 $\\tan\\alpha = 2$：$\\dfrac{2 + 1}{1 - 2\\cdot 1} = \\dfrac{3}{-1}$。\n3. 故 $\\tan\\left(\\alpha + \\frac{\\pi}{4}\\right) = -3$，选 (A)。\n提示：分母不要漏掉负号；此处 $1 - \\tan\\alpha$ 等于 $-1$。")

add(9, "medium",
    r"$2\sin 15^\circ\cos 15^\circ =$",
    r"$2\sin 15^\circ\cos 15^\circ =$",
    [r"$\dfrac{1}{2}$", r"$\dfrac{\sqrt3}{2}$", r"$1$", r"$\dfrac{\sqrt2}{2}$"],
    [r"$\dfrac{1}{2}$", r"$\dfrac{\sqrt3}{2}$", r"$1$", r"$\dfrac{\sqrt2}{2}$"],
    0,
    "1. Recognize the double-angle pattern $2\\sin\\theta\\cos\\theta = \\sin 2\\theta$.\n2. With $\\theta = 15^\\circ$: $2\\sin 15^\\circ\\cos 15^\\circ = \\sin 30^\\circ$.\n3. $\\sin 30^\\circ = \\frac12$ — answer (A).\nTip: spotting $2\\sin\\theta\\cos\\theta$ avoids computing $\\sin 15^\\circ$ and $\\cos 15^\\circ$ separately.",
    "1. 识别二倍角形式 $2\\sin\\theta\\cos\\theta = \\sin 2\\theta$。\n2. 取 $\\theta = 15^\\circ$：$2\\sin 15^\\circ\\cos 15^\\circ = \\sin 30^\\circ$。\n3. $\\sin 30^\\circ = \\frac12$，选 (A)。\n提示：认出 $2\\sin\\theta\\cos\\theta$ 可免去分别计算 $\\sin 15^\\circ$、$\\cos 15^\\circ$。")

add(10, "medium",
    r"$\cos^2\dfrac{\pi}{12} - \sin^2\dfrac{\pi}{12} =$",
    r"$\cos^2\dfrac{\pi}{12} - \sin^2\dfrac{\pi}{12} =$",
    [r"$\dfrac{\sqrt3}{2}$", r"$\dfrac{1}{2}$", r"$\dfrac{\sqrt2}{2}$", r"$1$"],
    [r"$\dfrac{\sqrt3}{2}$", r"$\dfrac{1}{2}$", r"$\dfrac{\sqrt2}{2}$", r"$1$"],
    0,
    "1. Use the double-angle identity $\\cos^2\\theta - \\sin^2\\theta = \\cos 2\\theta$.\n2. With $\\theta = \\frac{\\pi}{12}$: $\\cos^2\\frac{\\pi}{12} - \\sin^2\\frac{\\pi}{12} = \\cos\\frac{\\pi}{6}$.\n3. $\\cos\\frac{\\pi}{6} = \\frac{\\sqrt3}{2}$ — answer (A).",
    "1. 用二倍角恒等式 $\\cos^2\\theta - \\sin^2\\theta = \\cos 2\\theta$。\n2. 取 $\\theta = \\frac{\\pi}{12}$：$\\cos^2\\frac{\\pi}{12} - \\sin^2\\frac{\\pi}{12} = \\cos\\frac{\\pi}{6}$。\n3. $\\cos\\frac{\\pi}{6} = \\frac{\\sqrt3}{2}$，选 (A)。")

add(11, "medium",
    r"If $\tan\alpha = \dfrac{3}{4}$ and $\alpha$ is in the first quadrant, then $\sin\alpha =$",
    r"若 $\tan\alpha = \dfrac{3}{4}$，且 $\alpha$ 在第一象限，则 $\sin\alpha =$",
    [r"$\dfrac{3}{5}$", r"$\dfrac{4}{5}$", r"$\dfrac{3}{4}$", r"$\dfrac{5}{3}$"],
    [r"$\dfrac{3}{5}$", r"$\dfrac{4}{5}$", r"$\dfrac{3}{4}$", r"$\dfrac{5}{3}$"],
    0,
    "1. $\\tan\\alpha = \\frac{\\text{opposite}}{\\text{adjacent}} = \\frac34$ suggests a $3$–$4$–$5$ right triangle.\n2. The hypotenuse is $\\sqrt{3^2 + 4^2} = 5$.\n3. $\\sin\\alpha = \\frac{\\text{opposite}}{\\text{hypotenuse}} = \\frac35$, positive in QI — answer (A).\nTip: $\\frac45$ (option B) is $\\cos\\alpha$, not $\\sin\\alpha$.",
    "1. $\\tan\\alpha = \\frac{\\text{对边}}{\\text{邻边}} = \\frac34$，对应 $3$–$4$–$5$ 直角三角形。\n2. 斜边为 $\\sqrt{3^2 + 4^2} = 5$。\n3. $\\sin\\alpha = \\frac{\\text{对边}}{\\text{斜边}} = \\frac35$，第一象限为正，选 (A)。\n提示：$\\frac45$（选项 B）是 $\\cos\\alpha$，不是 $\\sin\\alpha$。")

add(12, "easy",
    r"$\sin\left(-\dfrac{\pi}{6}\right) =$",
    r"$\sin\left(-\dfrac{\pi}{6}\right) =$",
    [r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$", r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$"],
    [r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$", r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$"],
    0,
    "1. Sine is an odd function: $\\sin(-x) = -\\sin x$.\n2. So $\\sin\\left(-\\frac{\\pi}{6}\\right) = -\\sin\\frac{\\pi}{6}$.\n3. $\\sin\\frac{\\pi}{6} = \\frac12$, hence the value is $-\\frac12$ — answer (A).",
    "1. 正弦是奇函数：$\\sin(-x) = -\\sin x$。\n2. 故 $\\sin\\left(-\\frac{\\pi}{6}\\right) = -\\sin\\frac{\\pi}{6}$。\n3. $\\sin\\frac{\\pi}{6} = \\frac12$，因此值为 $-\\frac12$，选 (A)。")

add(13, "easy",
    r"$\cos 120^\circ =$",
    r"$\cos 120^\circ =$",
    [r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$", r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$"],
    [r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$", r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$"],
    0,
    "1. $120^\\circ$ is in the second quadrant, where cosine is NEGATIVE.\n2. Its reference angle is $180^\\circ - 120^\\circ = 60^\\circ$.\n3. So $\\cos 120^\\circ = -\\cos 60^\\circ = -\\frac12$ — answer (A).",
    "1. $120^\\circ$ 在第二象限，余弦为负。\n2. 参考角为 $180^\\circ - 120^\\circ = 60^\\circ$。\n3. 故 $\\cos 120^\\circ = -\\cos 60^\\circ = -\\frac12$，选 (A)。")

add(14, "medium",
    r"If $\sin\alpha = \dfrac{4}{5}$ and $\alpha$ is in the second quadrant, then $\cos 2\alpha =$",
    r"若 $\sin\alpha = \dfrac{4}{5}$，且 $\alpha$ 在第二象限，则 $\cos 2\alpha =$",
    [r"$-\dfrac{7}{25}$", r"$\dfrac{7}{25}$", r"$\dfrac{24}{25}$", r"$-\dfrac{24}{25}$"],
    [r"$-\dfrac{7}{25}$", r"$\dfrac{7}{25}$", r"$\dfrac{24}{25}$", r"$-\dfrac{24}{25}$"],
    0,
    "1. Use $\\cos 2\\alpha = 1 - 2\\sin^2\\alpha$ (only $\\sin\\alpha$ needed).\n2. $\\sin^2\\alpha = \\left(\\frac45\\right)^2 = \\frac{16}{25}$.\n3. $\\cos 2\\alpha = 1 - 2\\cdot\\frac{16}{25} = 1 - \\frac{32}{25} = -\\frac{7}{25}$ — answer (A).\nTip: the quadrant of $\\alpha$ is a distractor here — this formula doesn't need it.",
    "1. 用 $\\cos 2\\alpha = 1 - 2\\sin^2\\alpha$（只需 $\\sin\\alpha$）。\n2. $\\sin^2\\alpha = \\left(\\frac45\\right)^2 = \\frac{16}{25}$。\n3. $\\cos 2\\alpha = 1 - 2\\cdot\\frac{16}{25} = 1 - \\frac{32}{25} = -\\frac{7}{25}$，选 (A)。\n提示：本题象限信息是干扰项，此公式用不到。")

add(15, "hard",
    r"$\sin 75^\circ =$",
    r"$\sin 75^\circ =$",
    [r"$\dfrac{\sqrt6 + \sqrt2}{4}$", r"$\dfrac{\sqrt6 - \sqrt2}{4}$", r"$\dfrac{\sqrt2 - \sqrt6}{4}$", r"$\dfrac{\sqrt3 + 1}{4}$"],
    [r"$\dfrac{\sqrt6 + \sqrt2}{4}$", r"$\dfrac{\sqrt6 - \sqrt2}{4}$", r"$\dfrac{\sqrt2 - \sqrt6}{4}$", r"$\dfrac{\sqrt3 + 1}{4}$"],
    0,
    "1. Split into known angles: $75^\\circ = 45^\\circ + 30^\\circ$.\n2. Addition formula: $\\sin(45^\\circ + 30^\\circ) = \\sin 45^\\circ\\cos 30^\\circ + \\cos 45^\\circ\\sin 30^\\circ$.\n3. Substitute: $\\frac{\\sqrt2}{2}\\cdot\\frac{\\sqrt3}{2} + \\frac{\\sqrt2}{2}\\cdot\\frac12 = \\frac{\\sqrt6}{4} + \\frac{\\sqrt2}{4}$.\n4. So $\\sin 75^\\circ = \\frac{\\sqrt6 + \\sqrt2}{4}$ — answer (A).\nTip: $\\frac{\\sqrt6 - \\sqrt2}{4}$ (option B) is actually $\\sin 15^\\circ$.",
    "1. 拆成已知角：$75^\\circ = 45^\\circ + 30^\\circ$。\n2. 和角公式：$\\sin(45^\\circ + 30^\\circ) = \\sin 45^\\circ\\cos 30^\\circ + \\cos 45^\\circ\\sin 30^\\circ$。\n3. 代入：$\\frac{\\sqrt2}{2}\\cdot\\frac{\\sqrt3}{2} + \\frac{\\sqrt2}{2}\\cdot\\frac12 = \\frac{\\sqrt6}{4} + \\frac{\\sqrt2}{4}$。\n4. 故 $\\sin 75^\\circ = \\frac{\\sqrt6 + \\sqrt2}{4}$，选 (A)。\n提示：$\\frac{\\sqrt6 - \\sqrt2}{4}$（选项 B）其实是 $\\sin 15^\\circ$。")

import random

# Remove the few distractor references that named a letter (answers get shuffled below,
# so letters move). Each value is still named, so the explanations stay clear.
for q in Q:
    for lang in ("en", "zh"):
        e = q["explanation"][lang]
        e = e.replace(", the trap in (B).", ".")
        e = e.replace("，即 (B) 的陷阱。", "。")
        e = e.replace(r" (option B) is $\cos\alpha$", r" is $\cos\alpha$")
        e = e.replace(r"（选项 B）是 $\cos\alpha$", r" 是 $\cos\alpha$")
        e = e.replace(" (option B) is actually", " is actually")
        e = e.replace("（选项 B）其实是", " 其实是")
        q["explanation"][lang] = e

# Shuffle option order per question (deterministic seed) so the correct answer is not
# always at position A, and fix the "answer (A)" letter reference accordingly.
rng = random.Random(20260604)
LET = "ABCD"
for q in Q:
    perm = [0, 1, 2, 3]
    rng.shuffle(perm)
    for lang in ("en", "zh"):
        q["options"][lang] = [q["options"][lang][i] for i in perm]
    new_idx = perm.index(0)  # original correct option was at index 0
    q["answer"] = new_idx
    letter = LET[new_idx]
    for lang in ("en", "zh"):
        q["explanation"][lang] = (
            q["explanation"][lang]
            .replace("answer (A)", f"answer ({letter})")
            .replace("选 (A)", f"选 ({letter})")
        )

print(json.dumps(Q, ensure_ascii=False, indent=2))
