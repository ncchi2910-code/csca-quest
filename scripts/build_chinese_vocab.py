#!/usr/bin/env python3
"""
Chinese vocabulary flashcards for the humanities track (大文科专业汉语).
Grounded in the topics the source textbook explicitly covers: Chinese language
& characters, the Silk Road, Records of the Grand Historian (Sima Qian), law,
philosophy (Confucius / Laozi), diplomacy & international relations, art &
ink painting, and journalism.

Format: the prompt gives an English term; the four options are Chinese words
(the correct one plus three semantically-related distractors). Each explanation
gives pinyin + meaning for all four options, so the card teaches a small cluster.

Run:  python3 scripts/build_chinese_vocab.py   (prints JSON to stdout)
"""
import json

V = []
def add(n, en_term, pinyin, options_zh, ans, gloss_en, gloss_zh, diff="easy"):
    # options_zh: list of 4 Chinese words; ans: index of correct
    V.append({
        "id": f"chinese-vocab-{n:04d}",
        "subject": "chinese", "topic": "vocab",
        "source": "大文科 (Humanities Chinese)",
        "points": 1, "difficulty": diff,
        "question": {
            "en": f"Which Chinese word means “{en_term}” ({pinyin})?",
            "zh": f"下列哪个词的意思是「{en_term}」（{pinyin}）？",
        },
        "options": {"en": options_zh, "zh": options_zh},
        "answer": ans,
        "explanation": {"en": gloss_en, "zh": gloss_zh},
    })

# --- Language & characters ---
add(1, "civilization", "wénmíng", ["文明", "文化", "文字", "文献"], 0,
    "文明 (wénmíng) = civilization. 文化 = culture; 文字 = writing system / script; 文献 = documents & literature.",
    "文明（wénmíng）＝ civilization。文化＝文化；文字＝书写系统；文献＝文献资料。")
add(2, "character / written word", "hànzì", ["汉字", "汉语", "拼音", "笔画"], 0,
    "汉字 (hànzì) = Chinese characters. 汉语 = the Chinese language; 拼音 = pinyin (romanization); 笔画 = strokes.",
    "汉字（hànzì）＝ Chinese characters。汉语＝汉语；拼音＝拼音；笔画＝笔画。")
add(3, "evolution / development", "yǎnjìn", ["演进", "演讲", "演出", "演员"], 0,
    "演进 (yǎnjìn) = evolution / gradual development. 演讲 = lecture; 演出 = performance; 演员 = actor.",
    "演进（yǎnjìn）＝ evolution。演讲＝演讲；演出＝演出；演员＝演员。")
add(4, "tone (in speech)", "shēngdiào", ["声调", "音节", "声母", "韵母"], 0,
    "声调 (shēngdiào) = tone. 音节 = syllable; 声母 = initial consonant; 韵母 = final.",
    "声调（shēngdiào）＝ tone。音节＝音节；声母＝声母；韵母＝韵母。")

# --- History & Silk Road ---
add(5, "the Silk Road", "Sīchóu zhī Lù", ["丝绸之路", "茶马古道", "大运河", "长城"], 0,
    "丝绸之路 (Sīchóu zhī Lù) = the Silk Road. 茶马古道 = Tea-Horse Road; 大运河 = Grand Canal; 长城 = Great Wall.",
    "丝绸之路（Sīchóu zhī Lù）＝ the Silk Road。茶马古道＝茶马古道；大运河＝大运河；长城＝长城。")
add(6, "silk", "sīchóu", ["丝绸", "瓷器", "茶叶", "香料"], 0,
    "丝绸 (sīchóu) = silk. 瓷器 = porcelain; 茶叶 = tea; 香料 = spices — all famous Silk Road goods.",
    "丝绸（sīchóu）＝ silk。瓷器＝瓷器；茶叶＝茶叶；香料＝香料——均为丝路名物。")
add(7, "history", "lìshǐ", ["历史", "历法", "历程", "经历"], 0,
    "历史 (lìshǐ) = history. 历法 = calendar system; 历程 = course / journey; 经历 = experience.",
    "历史（lìshǐ）＝ history。历法＝历法；历程＝历程；经历＝经历。", "medium")
add(8, "Records of the Grand Historian", "Shǐjì", ["史记", "汉书", "春秋", "诗经"], 0,
    "史记 (Shǐjì) = Records of the Grand Historian, by Sima Qian. 汉书 = Book of Han; 春秋 = Spring and Autumn Annals; 诗经 = Classic of Poetry.",
    "史记（Shǐjì）＝《史记》，司马迁著。汉书＝《汉书》；春秋＝《春秋》；诗经＝《诗经》。", "medium")
add(9, "dynasty", "cháodài", ["朝代", "时代", "年代", "古代"], 0,
    "朝代 (cháodài) = dynasty. 时代 = era; 年代 = decade / period; 古代 = ancient times.",
    "朝代（cháodài）＝ dynasty。时代＝时代；年代＝年代；古代＝古代。", "medium")

# --- Law ---
add(10, "law", "fǎlǜ", ["法律", "法院", "法官", "法治"], 0,
    "法律 (fǎlǜ) = law. 法院 = court; 法官 = judge; 法治 = rule of law.",
    "法律（fǎlǜ）＝ law。法院＝法院；法官＝法官；法治＝法治。")
add(11, "rights and interests", "quányì", ["权益", "权力", "权利", "义务"], 0,
    "权益 (quányì) = rights and interests. 权力 = power (authority); 权利 = rights (legal entitlement); 义务 = duty / obligation.",
    "权益（quányì）＝ rights and interests。权力＝权力（authority）；权利＝权利（legal rights）；义务＝义务（duty）。")
add(12, "citizen", "gōngmín", ["公民", "市民", "人民", "居民"], 0,
    "公民 (gōngmín) = citizen (legal status). 市民 = city resident; 人民 = the people; 居民 = resident.",
    "公民（gōngmín）＝ citizen。市民＝市民；人民＝人民；居民＝居民。", "medium")
add(13, "constitution", "xiànfǎ", ["宪法", "刑法", "民法", "条例"], 0,
    "宪法 (xiànfǎ) = constitution. 刑法 = criminal law; 民法 = civil law; 条例 = regulation.",
    "宪法（xiànfǎ）＝ constitution。刑法＝刑法；民法＝民法；条例＝条例。", "medium")

# --- Philosophy ---
add(14, "philosophy", "zhéxué", ["哲学", "科学", "文学", "美学"], 0,
    "哲学 (zhéxué) = philosophy. 科学 = science; 文学 = literature; 美学 = aesthetics.",
    "哲学（zhéxué）＝ philosophy。科学＝科学；文学＝文学；美学＝美学。")
add(15, "Confucius", "Kǒngzǐ", ["孔子", "老子", "孟子", "庄子"], 0,
    "孔子 (Kǒngzǐ) = Confucius, founder of Confucianism. 老子 = Laozi; 孟子 = Mencius; 庄子 = Zhuangzi.",
    "孔子（Kǒngzǐ）＝ Confucius，儒家创始人。老子＝老子；孟子＝孟子；庄子＝庄子。", "medium")
add(16, "Laozi", "Lǎozǐ", ["老子", "孔子", "韩非子", "墨子"], 0,
    "老子 (Lǎozǐ) = Laozi, founder of Daoism. 孔子 = Confucius; 韩非子 = Han Feizi (Legalism); 墨子 = Mozi (Mohism).",
    "老子（Lǎozǐ）＝ Laozi，道家创始人。孔子＝孔子；韩非子＝韩非子；墨子＝墨子。", "medium")
add(17, "thought / ideology", "sīxiǎng", ["思想", "思考", "想法", "理想"], 0,
    "思想 (sīxiǎng) = thought / ideology. 思考 = to think (verb); 想法 = idea / opinion; 理想 = ideal.",
    "思想（sīxiǎng）＝ thought / ideology。思考＝思考；想法＝想法；理想＝理想。")
add(18, "benevolence (Confucian virtue)", "rén", ["仁", "义", "礼", "智"], 0,
    "仁 (rén) = benevolence, the core Confucian virtue. 义 = righteousness; 礼 = ritual propriety; 智 = wisdom.",
    "仁（rén）＝ benevolence，儒家核心德行。义＝义；礼＝礼；智＝智。", "medium")

# --- Diplomacy & international relations ---
add(19, "diplomacy", "wàijiāo", ["外交", "外贸", "外语", "外国"], 0,
    "外交 (wàijiāo) = diplomacy. 外贸 = foreign trade; 外语 = foreign language; 外国 = foreign country.",
    "外交（wàijiāo）＝ diplomacy。外贸＝外贸；外语＝外语；外国＝外国。")
add(20, "international relations", "guójì guānxì", ["国际关系", "国内事务", "国家利益", "国民经济"], 0,
    "国际关系 (guójì guānxì) = international relations. 国内事务 = domestic affairs; 国家利益 = national interest; 国民经济 = national economy.",
    "国际关系（guójì guānxì）＝ international relations。国内事务＝国内事务；国家利益＝国家利益；国民经济＝国民经济。", "medium")
add(21, "cooperation", "hézuò", ["合作", "合同", "合理", "合适"], 0,
    "合作 (hézuò) = cooperation. 合同 = contract; 合理 = reasonable; 合适 = suitable.",
    "合作（hézuò）＝ cooperation。合同＝合同；合理＝合理；合适＝合适。")
add(22, "treaty / agreement", "tiáoyuē", ["条约", "条件", "条款", "条理"], 0,
    "条约 (tiáoyuē) = treaty. 条件 = condition; 条款 = clause / article; 条理 = orderliness.",
    "条约（tiáoyuē）＝ treaty。条件＝条件；条款＝条款；条理＝条理。", "medium")
add(23, "embassy", "dàshǐguǎn", ["大使馆", "领事馆", "博物馆", "图书馆"], 0,
    "大使馆 (dàshǐguǎn) = embassy. 领事馆 = consulate; 博物馆 = museum; 图书馆 = library.",
    "大使馆（dàshǐguǎn）＝ embassy。领事馆＝领事馆；博物馆＝博物馆；图书馆＝图书馆。", "medium")
add(24, "sovereignty", "zhǔquán", ["主权", "主义", "主张", "主席"], 0,
    "主权 (zhǔquán) = sovereignty. 主义 = -ism / doctrine; 主张 = stance / advocate; 主席 = chairperson.",
    "主权（zhǔquán）＝ sovereignty。主义＝主义；主张＝主张；主席＝主席。", "medium")

# --- Art & painting ---
add(25, "art", "yìshù", ["艺术", "美术", "技术", "学术"], 0,
    "艺术 (yìshù) = art. 美术 = fine arts; 技术 = technology / technique; 学术 = academic scholarship.",
    "艺术（yìshù）＝ art。美术＝美术；技术＝技术；学术＝学术。")
add(26, "Chinese ink painting", "guóhuà", ["国画", "油画", "版画", "壁画"], 0,
    "国画 (guóhuà) = traditional Chinese painting. 油画 = oil painting; 版画 = printmaking; 壁画 = mural.",
    "国画（guóhuà）＝ Chinese ink painting。油画＝油画；版画＝版画；壁画＝壁画。", "medium")
add(27, "calligraphy", "shūfǎ", ["书法", "书架", "书店", "书桌"], 0,
    "书法 (shūfǎ) = calligraphy. 书架 = bookshelf; 书店 = bookstore; 书桌 = desk.",
    "书法（shūfǎ）＝ calligraphy。书架＝书架；书店＝书店；书桌＝书桌。")
add(28, "tradition", "chuántǒng", ["传统", "传说", "传播", "传记"], 0,
    "传统 (chuántǒng) = tradition. 传说 = legend; 传播 = to spread / disseminate; 传记 = biography.",
    "传统（chuántǒng）＝ tradition。传说＝传说；传播＝传播；传记＝传记。")
add(29, "to inherit / carry on", "jìchéng", ["继承", "继续", "接受", "承担"], 0,
    "继承 (jìchéng) = to inherit / carry on. 继续 = to continue; 接受 = to accept; 承担 = to undertake.",
    "继承（jìchéng）＝ to inherit。继续＝继续；接受＝接受；承担＝承担。", "medium")

# --- Journalism / news ---
add(30, "news value", "xīnwén jiàzhí", ["新闻价值", "新闻媒体", "新闻自由", "新闻发布"], 0,
    "新闻价值 (xīnwén jiàzhí) = news value. 新闻媒体 = news media; 新闻自由 = press freedom; 新闻发布 = press release.",
    "新闻价值（xīnwén jiàzhí）＝ news value。新闻媒体＝新闻媒体；新闻自由＝新闻自由；新闻发布＝新闻发布。", "medium")
add(31, "media", "méitǐ", ["媒体", "媒介", "传媒", "报刊"], 0,
    "媒体 (méitǐ) = media. 媒介 = medium / intermediary; 传媒 = mass media; 报刊 = newspapers & periodicals.",
    "媒体（méitǐ）＝ media。媒介＝媒介；传媒＝传媒；报刊＝报刊。", "medium")
add(32, "report (news)", "bàodào", ["报道", "报告", "报纸", "报名"], 0,
    "报道 (bàodào) = (news) report. 报告 = report / presentation; 报纸 = newspaper; 报名 = to sign up.",
    "报道（bàodào）＝ news report。报告＝报告；报纸＝报纸；报名＝报名。")
add(33, "public opinion", "yúlùn", ["舆论", "议论", "评论", "言论"], 0,
    "舆论 (yúlùn) = public opinion. 议论 = to discuss; 评论 = commentary; 言论 = speech / expression.",
    "舆论（yúlùn）＝ public opinion。议论＝议论；评论＝评论；言论＝言论。", "medium")

# --- General academic terms ---
add(34, "society", "shèhuì", ["社会", "社区", "团体", "群众"], 0,
    "社会 (shèhuì) = society. 社区 = community; 团体 = group / organization; 群众 = the masses.",
    "社会（shèhuì）＝ society。社区＝社区；团体＝团体；群众＝群众。")
add(35, "economy", "jīngjì", ["经济", "经营", "经验", "经历"], 0,
    "经济 (jīngjì) = economy. 经营 = to operate (a business); 经验 = experience; 经历 = to go through.",
    "经济（jīngjì）＝ economy。经营＝经营；经验＝经验；经历＝经历。")
add(36, "to influence / impact", "yǐngxiǎng", ["影响", "印象", "形象", "现象"], 0,
    "影响 (yǐngxiǎng) = to influence / impact. 印象 = impression; 形象 = image / figure; 现象 = phenomenon.",
    "影响（yǐngxiǎng）＝ to influence。印象＝印象；形象＝形象；现象＝现象。", "medium")

print(json.dumps(V, ensure_ascii=False, indent=2))
