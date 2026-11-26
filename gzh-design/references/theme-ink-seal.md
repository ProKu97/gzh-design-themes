# 公众号排版组件库 —— 宣纸·朱印

> **使用说明**：本组件库为「宣纸·朱印（Ink Seal）」主题，原创主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：水墨宣纸质感——暖米底（像晒旧的宣纸）+ 墨色标题 + 朱红印章点缀。章节编号做成一方朱红印章（方框+细边），标题用墨色衬线体；正文关键词用朱红细下划线；引用做成竖排题跋卡（细竖线分隔，模拟卷轴装裱）；收束处盖一方朱印句。整体像一幅题了字的手卷：安静、有笔触感，又不失庄重。适合文化/历史叙事、科普中的"故事感"段落、品牌年度总结、有传承/匠心调性的内容。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`、`transform`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
> - font-size ≤ 24px；正文强调用左竖条/下划线/卡片，**不用四周虚线框**（dashed）
>
> **WeChat 兼容铁律**：
> - 所有"装饰性空元素"（顶部双线、竖分隔线、印章方框、短线）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - 高亮样式统一挂在外层 `<span>` 上，文字放内层 `<span leaf="">`；不要把 `font-size`/`border-bottom` 打在 `<strong>` 上
> - 结构化区域没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
墨色（主色）：       #1C1C1A（标题 / 印章方框文字 / 收束卡底）
正文色：             #3A3A33
次要文字色：         #8A8373（收束小字 / 免责小字）
朱红（点缀）：       #A92524（印章方框 / 竖条 / 下划线 / 短线）
浅朱底：             #F3E3DD（引用卡底 / 要点卡底）
宣纸底（容器背景）： #FBF8F1
暖米卡底：           #F6F1E7（题跋卡 / 章节标题区）
细线色（发丝线）：   #D8CFBB
墨色卡内次要字：     #D9CFC0（收束卡内次要说明）
正文字号：           15px（卡片说明 14px）
行高：               1.85
字间距：             0.5px
最大宽度：           677px
内容区边距：         0 14px
首行缩进：           2em（本主题正文段落统一缩进，呼应手卷题字感）
```

字体栈：`'Noto Serif SC','Songti SC',SimSun,-apple-system,'PingFang SC','Microsoft YaHei',sans-serif`（标题/引用用衬线体，正文可衬线可无衬线，组件里统一给了衬线栈，不想要衬线感可换成 `-apple-system,'PingFang SC','Microsoft YaHei',sans-serif`）

**段后距铁律**（全主题通用，详见 SKILL.md）：正文自然段与下一段相邻时 `margin-bottom:0`；段落后紧跟小标题时该段改 `margin-bottom:8px`，小标题自身不叠加顶部空隙。本主题额外给正文加 `text-indent:2em` 首行缩进，是本主题独有的文学质感标志，其它主题不必跟随。

**用色铁律**：朱红只做印章方框、竖条、短线、下划线这类点睛，**不做大段正文字色**；墨色大色块只有章节标题区和全篇唯一一张收束卡；一篇文章点缀组件种类 ≤3。

---

## 组件 1 全局容器 + 顶部双线（卷轴装裱感）

```html
<section style="max-width:677px;margin:0 auto;padding:10px 0;box-sizing:border-box;background:#fbf8f1;color:#3a3a33;font-family:'Noto Serif SC','Songti SC',SimSun,-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;line-height:1.85;letter-spacing:0.5px;overflow-x:hidden;">
  <section style="border-top:1px solid #d8cfbb;border-bottom:3px solid #1c1c1a;height:5px;margin:0 14px 18px;"><span leaf=""><br></span></section>

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 章节标题（朱印方框编号 + 墨色标题）

> 编号取原文（01/02、一/二 → 统一转为 01/02）；原文没有编号也补上顺序号——印章式编号是本主题标志性视觉锚点，不省略。第一章 `margin-top` 8px，之后 36px。

```html
<section style="padding:0 14px;">
  <section style="margin:36px 0 18px;background:#f6f1e7;border-radius:4px;padding:12px 16px;display:flex;align-items:center;border-left:3px solid #a92524;">
    <section style="flex-shrink:0;width:34px;height:34px;border:2px solid #a92524;border-radius:3px;display:flex;align-items:center;justify-content:center;margin-right:14px;">
      <p style="margin:0;font-size:15px;font-weight:800;color:#a92524;line-height:1;"><span leaf="">01</span></p>
    </section>
    <p style="margin:0;font-size:17px;font-weight:800;color:#1c1c1a;line-height:1.5;"><span leaf="">{{章节标题}}</span></p>
  </section>
</section>
```

---

## 组件 3 小节标题（细朱红字号 + 墨色标题 + 左竖线）

> `margin-top:0`——小标题不叠加顶部空隙，间距由前一段落的 `margin-bottom:8px` 负责。

```html
<section style="padding:0 14px;">
  <section style="display:flex;align-items:center;margin:0 0 12px;padding-left:10px;border-left:2px solid #a92524;">
    <p style="margin:0;font-size:16px;font-weight:800;line-height:1.6;color:#1c1c1a;"><span leaf="">{{小节标题}}</span></p>
  </section>
</section>
```

---

## 组件 4 正文段落（首行缩进 2em）

```html
<section style="padding:0 14px;">
  <p style="margin:0;font-size:15px;line-height:1.85;text-align:justify;color:#3a3a33;text-indent:2em;"><span leaf="">{{正文}}</span></p>
</section>
```

紧接小标题前的最后一段，把 `margin:0` 换成 `margin:0 0 8px`。

---

## 组件 5 行内标记

### 5a 朱红下划线（正文关键词默认标记，每段 ≤2 处）

```html
<span style="border-bottom:1.5px solid #a92524;font-weight:700;color:#1c1c1a;"><span leaf="">{{关键词}}</span></span>
```

### 5b 墨色加粗

```html
<span style="font-weight:700;color:#1c1c1a;"><span leaf="">{{加粗}}</span></span>
```

### 5c 浅朱荧光笔（只在题跋卡 9a 内用）

```html
<span style="font-weight:800;color:#1c1c1a;background:linear-gradient(180deg,transparent 60%,#f3e3dd 60%);"><span leaf="">{{引用里的加粗句}}</span></span>
```

---

## 组件 6 列表

### 6a 方点要点列表（暖米底，普通无序列表）

```html
<section style="padding:0 14px;">
  <section style="background:#f6f1e7;border-radius:4px;padding:14px 16px;margin:0 0 16px;">
    <section style="display:flex;align-items:flex-start;margin:0 0 8px;">
      <section style="width:5px;height:5px;background:#a92524;border-radius:50%;margin:11px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.8;color:#3a3a33;text-align:justify;flex:1;"><span leaf="">{{要点一}}</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;margin:0;">
      <section style="width:5px;height:5px;background:#a92524;border-radius:50%;margin:11px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.8;color:#3a3a33;text-align:justify;flex:1;"><span leaf="">{{最后一条}}</span></p>
    </section>
  </section>
</section>
```

### 6b 卷册小标题卡（白底描边 + 朱红左竖条；列表每条都是"**小标题：**说明"时用）

```html
<section style="padding:0 14px;">
  <section style="background:#fffdf8;border:1px solid #d8cfbb;border-left:3px solid #a92524;border-radius:0 4px 4px 0;padding:10px 14px;margin:0 0 10px;">
    <p style="margin:0 0 4px;font-size:15px;font-weight:800;color:#1c1c1a;line-height:1.6;"><span leaf="">{{小标题：}}</span></p>
    <p style="margin:0;font-size:14px;line-height:1.8;color:#3a3a33;text-align:justify;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

---

## 组件 7 图片容器（整宽圆角，无图注）

```html
<section style="padding:0 14px;">
  <section style="margin:4px 0 18px;line-height:0;">
    <span leaf=""><img src="{{图片URL}}" style="width:100%;height:auto;display:block;border-radius:4px;"></span>
  </section>
</section>
```

---

## 组件 8 题跋引用卡（竖线分隔，模拟卷轴装裱）

### 8a 朱边题跋卡（浅朱底 + 朱红竖条；原文 `>` 引用）

```html
<section style="padding:0 14px;">
  <section style="background:#f3e3dd;border-left:4px solid #a92524;border-radius:0 4px 4px 0;padding:14px 18px;margin:4px 0 18px;">
    <p style="margin:0;font-size:15px;line-height:1.9;color:#1c1c1a;font-weight:600;text-align:justify;font-family:'Noto Serif SC','Songti SC',SimSun,serif;"><span leaf="">{{引用}}</span></p>
  </section>
</section>
```

### 8b 居中短句（上下细线，像题在卷首的一句跋语）

```html
<section style="padding:0 14px;">
  <section style="border-top:1px solid #d8cfbb;border-bottom:1px solid #d8cfbb;padding:12px 4px;margin:0 0 18px;">
    <p style="margin:0;font-size:15px;line-height:1.9;color:#1c1c1a;font-weight:600;text-align:center;font-family:'Noto Serif SC','Songti SC',SimSun,serif;"><span leaf="">{{居中短句}}</span></p>
  </section>
</section>
```

---

## 组件 9 墨色收束卡（全篇 ≤1 张，盖一方朱印）

```html
<section style="padding:0 14px;">
  <section style="background:#1c1c1a;padding:7px;border-radius:4px;margin:4px 0 18px;">
    <section style="border:1px solid rgba(255,255,255,0.14);border-radius:3px;padding:18px 16px;position:relative;">
      <p style="margin:0 0 8px;font-size:17px;font-weight:800;color:#fbf8f1;text-align:center;line-height:1.7;letter-spacing:1px;font-family:'Noto Serif SC','Songti SC',SimSun,serif;"><span leaf="">{{大字结论}}</span></p>
      <p style="margin:0;font-size:14px;color:#d9cfc0;text-align:center;line-height:1.8;"><span leaf="">{{次要说明}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 10 结尾收束（居中墨色大字 + 朱红短线 + 小字）

```html
<section style="padding:0 14px;">
  <section style="margin:30px 0 10px;text-align:center;">
    <p style="margin:0 0 12px;font-size:19px;font-weight:800;color:#1c1c1a;letter-spacing:2px;line-height:1.6;font-family:'Noto Serif SC','Songti SC',SimSun,serif;"><span leaf="">{{收束句}}</span></p>
    <section style="width:36px;height:2px;background:#a92524;margin:0 auto 12px;"><span leaf=""><br></span></section>
    <p style="margin:0;font-size:14px;color:#8a8373;letter-spacing:1px;line-height:1.8;"><span leaf="">{{收尾一句}}</span></p>
  </section>
</section>
```

---

## 组件 11 文末免责小字（原文有才放）

```html
<section style="padding:0 14px;">
  <section style="border-top:1px solid #d8cfbb;padding:10px 2px 0;margin:16px 0 0;">
    <p style="margin:0;font-size:12px;line-height:1.7;color:#8a8373;text-align:justify;"><span leaf="">{{免责内容}}</span></p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:10px 0;box-sizing:border-box;background:#fbf8f1;color:#3a3a33;font-family:'Noto Serif SC','Songti SC',SimSun,-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;line-height:1.85;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 顶部双线（组件1） -->

  <!-- 2. 头图（组件7，有头图时）+ 开场段落（组件4）或开场题跋（组件8a，原文开头有引用时） -->

  <!-- 3. 第一章（组件2，margin-top 8px） -->
  <!--    章内：组件4 正文 + 3 小节 + 5 行内标记 + 6 列表 + 7 配图 + 8 题跋 -->

  <!-- 4. 第二章…第N章（组件2，margin-top 36px）；墨色收束卡（组件9）全篇最多一张，放在转折或总结处 -->

  <!-- 5. 结尾收束（组件10） -->

  <!-- 6. 文末免责（组件11，原文有才放） -->

</section>
```

**骨架铁律**：没有导读卡/目录卡；章节靠印章方框编号分隔，不另加分割线；每张配图放在原稿位置（一般章节标题后或章末引用前）；收束卡全篇唯一，放在信息密度最高的转折点。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 朱印编号 2 / 墨色收束卡 9 / 结尾墨色大字 10 | 全文骨架与唯一高潮 | 章节数 + 收束卡 ≤1 + 结尾 1 |
| **标记层** | 朱红下划线 5a（默认）/ 墨色加粗 5b | 正文关键词强调 | 每段 ≤2 处 |
| **容器层** | 要点列表 6a / 卷册小标题卡 6b / 题跋卡 8a / 居中短句 8b | 结构化信息、引用、金句 | 按原文结构，每章至少 1 个 |

**克制原则**：朱红只做印章、竖条、短线、下划线，不做大段正文字色；墨色大色块只有章节标题区和一张收束卡；一篇文章点缀组件种类 ≤3；不用四周虚线框。

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 文化/历史叙事、有传承调性的科普 | 章节 2 + 正文 4 + 题跋卡 8a | 居中短句 8b、收束卡 9 |
| 匠心/案例复盘、年度总结 | 章节 2 + 卷册小标题卡 6b + 方点列表 6a | 题跋卡 8a、收束卡 9 |
| 观点/评论（带文学气质） | 章节 2 + 正文 4 + 居中短句 8b | 题跋卡 8a、收束卡 9 |

所有类型共用：顶部双线 1 + 朱印章节 2 + 结尾收束 10。

---

## Markdown → 宣纸·朱印 映射规则

| 原文元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号标题在平台设置 |
| `## 01 章节` | 组件 2 朱印方框章节 | 编号取原文，没有编号也补顺序号 |
| `### 小节` | 组件 3 左竖线小节标题 | `margin-top:0` |
| 普通段落 | 组件 4，首行缩进 2em | 段后距按铁律 0/8px |
| `**加粗**`（核心观点） | 组件 5a 朱红下划线 | |
| `**加粗**`（普通） | 组件 5b 墨色加粗 | |
| `- 列表`（每条"**小标题：**说明"） | 组件 6b 卷册小标题卡 | |
| `- 列表`（普通） | 组件 6a 方点要点列表 | |
| `![](图)` | 组件 7 图片容器 | |
| `> 引用` | 组件 8a 朱边题跋卡 | 引用内加粗用 5c |
| 单句金句 / 排比 | 组件 8b 居中短句 | |
| 全文最重要的一段转折/总结 | 组件 9 墨色收束卡 | 全篇 ≤1 |
| 文末收束句 | 组件 10 结尾收束 | |
| `本文仅为……` | 组件 11 免责小字 | |

---

## Gotchas

- **印章编号别省**：没有编号的原文也要补上顺序号，这是本主题的标志性视觉锚点；省略后主题辨识度会明显下降。
- **首行缩进是本主题专属**：`text-indent:2em` 只在本主题用，不要带到其它主题的正文段落里。
- **朱红不做大段正文字色**：只用在编号方框、竖条、短线、下划线，白底/米底正文里不出现朱红字。
- **不用 `transform`**：微信编辑器对 `transform:rotate()` 支持不稳定，印章方框保持方正，不要加旋转角度制造"盖歪了"的效果。
