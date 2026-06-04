#!/usr/bin/env python3
"""
15 AI-generated SEQUENCE practice questions (source: "AI-generated").
Supplement — never replace — the real-exam bank. Every answer was solved
independently and is numerically re-checked by the merge step.

Run:  python3 scripts/build_gen_sequence.py   (prints JSON to stdout)
"""
import json

Q = []
def add(n, diff, qen, qzh, oen, ozh, een, ezh):
    # correct option authored at index 0; positions are shuffled below
    Q.append({
        "id": f"math-gen-{n:04d}",
        "subject": "math", "topic": "sequence", "source": "AI-generated",
        "points": 2, "difficulty": diff,
        "question": {"en": qen, "zh": qzh},
        "options": {"en": oen, "zh": ozh},
        "answer": 0,
        "explanation": {"en": een, "zh": ezh},
    })

add(31, "easy",
    r"In an arithmetic sequence with $a_1 = 3$ and common difference $d = 4$, $a_{10} =$",
    r"等差数列中 $a_1 = 3$，公差 $d = 4$，则 $a_{10} =$",
    [r"$39$", r"$40$", r"$43$", r"$36$"],
    [r"$39$", r"$40$", r"$43$", r"$36$"],
    "1. Use $a_n = a_1 + (n-1)d$.\n2. Substitute $a_1 = 3$, $d = 4$, $n = 10$: $a_{10} = 3 + (10-1)\\times 4$.\n3. Compute: $3 + 9\\times 4 = 3 + 36 = 39$ — answer (A).\nTip: it is $(n-1)$ jumps of $d$, not $n$; using $10\\times4$ gives $43$, a trap.",
    "1. 用 $a_n = a_1 + (n-1)d$。\n2. 代入 $a_1 = 3$，$d = 4$，$n = 10$：$a_{10} = 3 + (10-1)\\times 4$。\n3. 计算：$3 + 9\\times 4 = 3 + 36 = 39$，选 (A)。\n提示：是 $(n-1)$ 个公差，不是 $n$ 个；用 $10\\times4$ 会得 $43$，是陷阱。")

add(32, "easy",
    r"In a geometric sequence with $a_1 = 2$ and common ratio $r = 3$, $a_4 =$",
    r"等比数列中 $a_1 = 2$，公比 $r = 3$，则 $a_4 =$",
    [r"$54$", r"$18$", r"$162$", r"$48$"],
    [r"$54$", r"$18$", r"$162$", r"$48$"],
    "1. Use $a_n = a_1 r^{\\,n-1}$.\n2. Substitute $a_1 = 2$, $r = 3$, $n = 4$: $a_4 = 2\\cdot 3^{3}$.\n3. Compute: $2\\cdot 27 = 54$ — answer (A).\nTip: the exponent is $n-1 = 3$, not $n = 4$; $2\\cdot3^4 = 162$ is the trap.",
    "1. 用 $a_n = a_1 r^{\\,n-1}$。\n2. 代入 $a_1 = 2$，$r = 3$，$n = 4$：$a_4 = 2\\cdot 3^{3}$。\n3. 计算：$2\\cdot 27 = 54$，选 (A)。\n提示：指数是 $n-1 = 3$，不是 $n = 4$；$2\\cdot3^4 = 162$ 是陷阱。")

add(33, "medium",
    r"$1 + 2 + 3 + \cdots + 50 =$",
    r"$1 + 2 + 3 + \cdots + 50 =$",
    [r"$1275$", r"$1250$", r"$2550$", r"$1225$"],
    [r"$1275$", r"$1250$", r"$2550$", r"$1225$"],
    "1. This is an arithmetic series; sum $= \\dfrac{n(a_1 + a_n)}{2}$.\n2. Here $n = 50$, $a_1 = 1$, $a_{50} = 50$.\n3. Sum $= \\dfrac{50(1 + 50)}{2} = \\dfrac{50\\times 51}{2} = 25\\times 51 = 1275$ — answer (A).\nTip: forgetting to divide by $2$ gives $2550$, a common trap.",
    "1. 这是等差数列求和；和 $= \\dfrac{n(a_1 + a_n)}{2}$。\n2. 此处 $n = 50$，$a_1 = 1$，$a_{50} = 50$。\n3. 和 $= \\dfrac{50(1 + 50)}{2} = \\dfrac{50\\times 51}{2} = 25\\times 51 = 1275$，选 (A)。\n提示：忘记除以 $2$ 会得 $2550$，是常见陷阱。")

add(34, "medium",
    r"For an arithmetic sequence with $a_1 = 5$ and $d = 2$, the sum of the first $10$ terms $S_{10} =$",
    r"等差数列中 $a_1 = 5$，$d = 2$，则前 $10$ 项和 $S_{10} =$",
    [r"$140$", r"$150$", r"$130$", r"$145$"],
    [r"$140$", r"$150$", r"$130$", r"$145$"],
    "1. Use $S_n = \\dfrac{n}{2}\\left[2a_1 + (n-1)d\\right]$.\n2. Substitute $n = 10$, $a_1 = 5$, $d = 2$: $S_{10} = \\dfrac{10}{2}\\left[2\\cdot 5 + 9\\cdot 2\\right]$.\n3. Inside: $10 + 18 = 28$; then $5\\times 28 = 140$ — answer (A).\nTip: you can also use $S_n = \\dfrac{n(a_1 + a_n)}{2}$ with $a_{10} = 5 + 18 = 23$: $\\dfrac{10(5+23)}{2} = 140$.",
    "1. 用 $S_n = \\dfrac{n}{2}\\left[2a_1 + (n-1)d\\right]$。\n2. 代入 $n = 10$，$a_1 = 5$，$d = 2$：$S_{10} = \\dfrac{10}{2}\\left[2\\cdot 5 + 9\\cdot 2\\right]$。\n3. 括号内：$10 + 18 = 28$；再算 $5\\times 28 = 140$，选 (A)。\n提示：也可用 $S_n = \\dfrac{n(a_1 + a_n)}{2}$，其中 $a_{10} = 5 + 18 = 23$：$\\dfrac{10(5+23)}{2} = 140$。")

add(35, "hard",
    r"The sum of the first $10$ terms of the geometric sequence $1, 2, 4, 8, \dots$ is",
    r"等比数列 $1, 2, 4, 8, \dots$ 的前 $10$ 项和是",
    [r"$1023$", r"$1024$", r"$511$", r"$2047$"],
    [r"$1023$", r"$1024$", r"$511$", r"$2047$"],
    "1. Here $a_1 = 1$, ratio $r = 2$. Use $S_n = \\dfrac{a_1(r^n - 1)}{r - 1}$.\n2. Substitute $n = 10$: $S_{10} = \\dfrac{1\\cdot(2^{10} - 1)}{2 - 1} = 2^{10} - 1$.\n3. $2^{10} = 1024$, so $S_{10} = 1023$ — answer (A).\nTip: the sum is $2^{10} - 1$, not $2^{10}$; off-by-one gives $1024$.",
    "1. 此处 $a_1 = 1$，公比 $r = 2$。用 $S_n = \\dfrac{a_1(r^n - 1)}{r - 1}$。\n2. 代入 $n = 10$：$S_{10} = \\dfrac{1\\cdot(2^{10} - 1)}{2 - 1} = 2^{10} - 1$。\n3. $2^{10} = 1024$，故 $S_{10} = 1023$，选 (A)。\n提示：和是 $2^{10} - 1$ 而非 $2^{10}$；差一会得 $1024$。")

add(36, "easy",
    r"If $4, x, 9$ form a geometric sequence with $x > 0$, then $x =$",
    r"若 $4, x, 9$ 成等比数列且 $x > 0$，则 $x =$",
    [r"$6$", r"$6.5$", r"$36$", r"$13$"],
    [r"$6$", r"$6.5$", r"$36$", r"$13$"],
    "1. In a geometric sequence the middle term is the geometric mean: $x^2 = 4\\times 9$.\n2. $x^2 = 36$, so $x = \\pm 6$.\n3. Since $x > 0$, $x = 6$ — answer (A).\nTip: $6.5$ is the ARITHMETIC mean $\\frac{4+9}{2}$ — a trap; geometric uses the product, not the sum.",
    "1. 等比数列中，中项是等比中项：$x^2 = 4\\times 9$。\n2. $x^2 = 36$，故 $x = \\pm 6$。\n3. 因 $x > 0$，得 $x = 6$，选 (A)。\n提示：$6.5$ 是等差中项 $\\frac{4+9}{2}$ —— 陷阱；等比用乘积而非和。")

add(37, "medium",
    r"In an arithmetic sequence with $a_1 = 1$ and $d = 3$, which term equals $100$?",
    r"等差数列中 $a_1 = 1$，$d = 3$，第几项等于 $100$？",
    [r"the $34$th", r"the $33$rd", r"the $35$th", r"the $30$th"],
    [r"第 $34$ 项", r"第 $33$ 项", r"第 $35$ 项", r"第 $30$ 项"],
    "1. Set $a_n = 100$ in $a_n = a_1 + (n-1)d$: $1 + (n-1)\\cdot 3 = 100$.\n2. So $(n-1)\\cdot 3 = 99 \\Rightarrow n - 1 = 33$.\n3. $n = 34$ — answer (A).\nTip: solve for $n-1$ first, then add $1$; stopping at $33$ is the trap.",
    "1. 在 $a_n = a_1 + (n-1)d$ 中令 $a_n = 100$：$1 + (n-1)\\cdot 3 = 100$。\n2. 故 $(n-1)\\cdot 3 = 99 \\Rightarrow n - 1 = 33$。\n3. $n = 34$，选 (A)。\n提示：先求 $n-1$ 再加 $1$；停在 $33$ 是陷阱。")

add(38, "hard",
    r"The sum to infinity $1 + \dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{8} + \cdots =$",
    r"无穷和 $1 + \dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{8} + \cdots =$",
    [r"$2$", r"$\dfrac{3}{2}$", r"$1$", r"$4$"],
    [r"$2$", r"$\dfrac{3}{2}$", r"$1$", r"$4$"],
    "1. This is an infinite geometric series with $a_1 = 1$ and $r = \\dfrac{1}{2}$ (and $|r| < 1$, so it converges).\n2. Use $S_\\infty = \\dfrac{a_1}{1 - r}$.\n3. $S_\\infty = \\dfrac{1}{1 - \\frac12} = \\dfrac{1}{\\frac12} = 2$ — answer (A).\nTip: the sum exists only because $|r| < 1$; the terms get arbitrarily small.",
    "1. 这是无穷等比级数，$a_1 = 1$，$r = \\dfrac{1}{2}$（且 $|r| < 1$，收敛）。\n2. 用 $S_\\infty = \\dfrac{a_1}{1 - r}$。\n3. $S_\\infty = \\dfrac{1}{1 - \\frac12} = \\dfrac{1}{\\frac12} = 2$，选 (A)。\n提示：和存在的前提是 $|r| < 1$，各项趋于无穷小。")

add(39, "medium",
    r"In a geometric sequence, $a_2 = 6$ and $a_5 = 48$. The common ratio $r =$",
    r"等比数列中 $a_2 = 6$，$a_5 = 48$。则公比 $r =$",
    [r"$2$", r"$3$", r"$4$", r"$8$"],
    [r"$2$", r"$3$", r"$4$", r"$8$"],
    "1. From $a_2$ to $a_5$ the index increases by $3$, so $a_5 = a_2 \\cdot r^{3}$.\n2. $48 = 6\\cdot r^3 \\Rightarrow r^3 = 8$.\n3. $r = \\sqrt[3]{8} = 2$ — answer (A).\nTip: it is $r^3$ (three steps), not $r^2$; $r^3 = 8$ gives $r = 2$, while $8$ is $r^3$ itself, a trap.",
    "1. 从 $a_2$ 到 $a_5$ 下标增加 $3$，故 $a_5 = a_2 \\cdot r^{3}$。\n2. $48 = 6\\cdot r^3 \\Rightarrow r^3 = 8$。\n3. $r = \\sqrt[3]{8} = 2$，选 (A)。\n提示：是 $r^3$（三步），不是 $r^2$；$r^3 = 8$ 得 $r = 2$，而 $8$ 是 $r^3$ 本身，是陷阱。")

add(40, "medium",
    r"In an arithmetic sequence, $a_3 = 7$ and $a_7 = 15$. Then $a_5 =$",
    r"等差数列中 $a_3 = 7$，$a_7 = 15$。则 $a_5 =$",
    [r"$11$", r"$10$", r"$12$", r"$13$"],
    [r"$11$", r"$10$", r"$12$", r"$13$"],
    "1. In an arithmetic sequence the middle index term is the average of equally-spaced neighbours.\n2. $a_5$ is exactly halfway between $a_3$ and $a_7$, so $a_5 = \\dfrac{a_3 + a_7}{2}$.\n3. $a_5 = \\dfrac{7 + 15}{2} = \\dfrac{22}{2} = 11$ — answer (A).\nTip: this works because $5$ is the midpoint of $3$ and $7$; no need to find $d$ first.",
    "1. 等差数列中，等间隔两项的中间项等于其平均值。\n2. $a_5$ 恰在 $a_3$ 与 $a_7$ 正中间，故 $a_5 = \\dfrac{a_3 + a_7}{2}$。\n3. $a_5 = \\dfrac{7 + 15}{2} = \\dfrac{22}{2} = 11$，选 (A)。\n提示：因为 $5$ 是 $3$ 与 $7$ 的中点，无需先求 $d$。")

add(41, "hard",
    r"A sequence has $S_n = n^2 + 2n$ (sum of the first $n$ terms). Then $a_n =$",
    r"数列前 $n$ 项和 $S_n = n^2 + 2n$。则 $a_n =$",
    [r"$2n + 1$", r"$2n - 1$", r"$n^2 + 1$", r"$2n$"],
    [r"$2n + 1$", r"$2n - 1$", r"$n^2 + 1$", r"$2n$"],
    "1. For $n \\ge 2$, $a_n = S_n - S_{n-1}$.\n2. $S_{n-1} = (n-1)^2 + 2(n-1) = n^2 - 2n + 1 + 2n - 2 = n^2 - 1$.\n3. So $a_n = (n^2 + 2n) - (n^2 - 1) = 2n + 1$.\n4. Check $n = 1$: $a_1 = S_1 = 3$, and $2(1)+1 = 3$ ✓, so $a_n = 2n + 1$ for all $n$ — answer (A).\nTip: always verify the $n=1$ case separately, since $S_{n-1}$ is undefined there.",
    "1. 当 $n \\ge 2$ 时，$a_n = S_n - S_{n-1}$。\n2. $S_{n-1} = (n-1)^2 + 2(n-1) = n^2 - 2n + 1 + 2n - 2 = n^2 - 1$。\n3. 故 $a_n = (n^2 + 2n) - (n^2 - 1) = 2n + 1$。\n4. 验证 $n = 1$：$a_1 = S_1 = 3$，而 $2(1)+1 = 3$ ✓，故对所有 $n$ 有 $a_n = 2n + 1$，选 (A)。\n提示：务必单独验证 $n=1$，因为此时 $S_{n-1}$ 无定义。")

add(42, "easy",
    r"In a geometric sequence with $a_1 = 1$ and ratio $r = -2$, $a_5 =$",
    r"等比数列中 $a_1 = 1$，公比 $r = -2$，则 $a_5 =$",
    [r"$16$", r"$-16$", r"$-8$", r"$8$"],
    [r"$16$", r"$-16$", r"$-8$", r"$8$"],
    "1. Use $a_n = a_1 r^{\\,n-1}$: $a_5 = 1\\cdot(-2)^{4}$.\n2. The exponent $4$ is even, so $(-2)^4 = +16$.\n3. $a_5 = 16$ — answer (A).\nTip: an even power of a negative number is positive; an odd power (like $a_4 = (-2)^3 = -8$) stays negative.",
    "1. 用 $a_n = a_1 r^{\\,n-1}$：$a_5 = 1\\cdot(-2)^{4}$。\n2. 指数 $4$ 为偶数，故 $(-2)^4 = +16$。\n3. $a_5 = 16$，选 (A)。\n提示：负数的偶次幂为正；奇次幂（如 $a_4 = (-2)^3 = -8$）为负。")

add(43, "easy",
    r"In an arithmetic sequence with $a_1 = 10$ and $d = -2$, $a_8 =$",
    r"等差数列中 $a_1 = 10$，$d = -2$，则 $a_8 =$",
    [r"$-4$", r"$-2$", r"$4$", r"$-6$"],
    [r"$-4$", r"$-2$", r"$4$", r"$-6$"],
    "1. Use $a_n = a_1 + (n-1)d$.\n2. $a_8 = 10 + (8-1)\\times(-2) = 10 + 7\\times(-2)$.\n3. $= 10 - 14 = -4$ — answer (A).\nTip: with a negative $d$ the terms decrease; keep track of the sign of $(n-1)d$.",
    "1. 用 $a_n = a_1 + (n-1)d$。\n2. $a_8 = 10 + (8-1)\\times(-2) = 10 + 7\\times(-2)$。\n3. $= 10 - 14 = -4$，选 (A)。\n提示：公差为负时数列递减；注意 $(n-1)d$ 的符号。")

add(44, "easy",
    r"How many terms are in the arithmetic sequence $2, 5, 8, \dots, 29$?",
    r"等差数列 $2, 5, 8, \dots, 29$ 共有多少项？",
    [r"$10$", r"$9$", r"$11$", r"$27$"],
    [r"$10$", r"$9$", r"$11$", r"$27$"],
    "1. Here $a_1 = 2$, $d = 3$, last term $a_n = 29$. Use $a_n = a_1 + (n-1)d$.\n2. $29 = 2 + (n-1)\\cdot 3 \\Rightarrow (n-1)\\cdot 3 = 27 \\Rightarrow n - 1 = 9$.\n3. $n = 10$ — answer (A).\nTip: counting terms always gives $n = \\dfrac{\\text{last} - \\text{first}}{d} + 1$; the '$+1$' is easy to forget.",
    "1. 此处 $a_1 = 2$，$d = 3$，末项 $a_n = 29$。用 $a_n = a_1 + (n-1)d$。\n2. $29 = 2 + (n-1)\\cdot 3 \\Rightarrow (n-1)\\cdot 3 = 27 \\Rightarrow n - 1 = 9$。\n3. $n = 10$，选 (A)。\n提示：项数 $n = \\dfrac{\\text{末项} - \\text{首项}}{d} + 1$；容易漏掉 '$+1$'。")

add(45, "medium",
    r"For the geometric sequence with $a_1 = 3$ and ratio $r = 2$, the sum of the first $5$ terms $S_5 =$",
    r"等比数列中 $a_1 = 3$，公比 $r = 2$，则前 $5$ 项和 $S_5 =$",
    [r"$93$", r"$96$", r"$45$", r"$31$"],
    [r"$93$", r"$96$", r"$45$", r"$31$"],
    "1. Use $S_n = \\dfrac{a_1(r^n - 1)}{r - 1}$.\n2. Substitute $a_1 = 3$, $r = 2$, $n = 5$: $S_5 = \\dfrac{3(2^5 - 1)}{2 - 1}$.\n3. $2^5 = 32$, so $S_5 = 3\\times(32 - 1) = 3\\times 31 = 93$ — answer (A).\nTip: $31$ is $2^5 - 1$ before multiplying by $a_1 = 3$ — a trap.",
    "1. 用 $S_n = \\dfrac{a_1(r^n - 1)}{r - 1}$。\n2. 代入 $a_1 = 3$，$r = 2$，$n = 5$：$S_5 = \\dfrac{3(2^5 - 1)}{2 - 1}$。\n3. $2^5 = 32$，故 $S_5 = 3\\times(32 - 1) = 3\\times 31 = 93$，选 (A)。\n提示：$31$ 是 $2^5 - 1$，还没乘 $a_1 = 3$ —— 陷阱。")

# --- Shuffle option order so the answer is not always A; fix the answer letter reference ---
import random
rng = random.Random(20260669)
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
