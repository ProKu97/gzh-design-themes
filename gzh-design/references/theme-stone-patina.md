# 公众号排版组件库 —— 原石·雅痕

> **使用说明**：本组件库为「原石·雅痕（Stone Patina）」主题，原创主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：暖灰白底 + 细金线点缀，高级静谧、留白克制，像一块打磨过的原石——不花哨，但经得起细看。章节标题只用一道细金线 + 衬线体大字，不做色块；正文关键词用极细的金色下划线；引用用无背景色、只靠左侧细线分隔的"碑铭"式排版；收束处是一整行居中大字，像刻在石面上的一句话。整体克制、留白多、信息密度低但质感高，是品牌调性/高端定位内容的首选，和"品牌深蓝·蓝图"（深色科技感）、"极光链语"（跳色未来感）形成互补的"静"的一端。适合品牌故事、年度/阶段性总结、高端定位的产品发布、企业文化类内容。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
> - font-size ≤ 24px；正文强调用左竖条/下划线，**不用任何色块/虚线框**（本主题比其它主题更克制，连底色卡片都少用）
>
> **WeChat 兼容铁律**：
> - 所有"装饰性空元素"（细金线、竖分隔线）**必须在内部放 `<span leaf=""><br></span>` 占位**
> - 高亮样式统一挂在外层 `<span>` 上，文字放内层 `<span leaf="">`
> - 结构化区域没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
标题深色（主色）：   #2B2824（标题 / 加粗 / 收束大字）
正文色：             #4A463F
次要文字色：         #8C8679
弱化文字色：         #B3AC9C（免责小字）
细金线（点缀）：     #B8923F（章节分隔线 / 下划线 / 竖条 / 短线）
浅金底（极少用）：   #F7F1E2（仅题跋式引用卡用，一篇 ≤1 处）
暖灰白底（容器背景）：#F8F6F1
纯白卡底：           #FFFFFF
细线色（分隔线）：   #E5E0D3
正文字号：           15px
行高：               1.9（本主题行高高于其它主题，呼应"留白"气质）
字间距：             0.6px
最大宽度：           677px
内容区边距：         0 16px
章节间距：           第一章 margin-top 12px，之后 40px（间距大于其它主题）
```

字体栈：标题用 `'Noto Serif SC','Songti SC',SimSun,serif`；正文用 `-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

**段后距铁律**（全主题通用）：正文自然段与下一段相邻 `margin-bottom:0`；段落后紧跟小标题改 `margin-bottom:8px`，小标题不叠加顶部空隙。

**用色铁律**：金色只做细线、下划线、竖条、短线这类点睛，**不做大段正文字色，也不做大面积底色**；本主题几乎不用深色大色块（克制是本主题的核心卖点），收束处只用居中大字 + 一道细金线，不做深色卡。

**"不要素"提示（本主题专属）**：本主题整体视觉密度低于其它主题，更容易显得单薄。为避免真的排成一篇"素稿"，**每章至少用 1 次题跋引用卡（9a）或左竖条要点卡（6b）**，不能全篇只有标题+正文；行距大、留白多是气质，不等于可以跳过容器层组件。

---

## 组件 1 全局容器 + 顶部细金线

```html
<section style="max-width:677px;margin:0 auto;padding:12px 0;box-sizing:border-box;background:#f8f6f1;color:#4a463f;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.9;letter-spacing:0.6px;overflow-x:hidden;">
  <section style="height:1px;background:#b8923f;margin:0 16px 20px;"><span leaf=""><br></span></section>

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 章节标题（细金线 + 衬线体大字，不做色块）

> 编号用原文的（阿拉伯数字或中文数字皆可，统一用细体数字，不加粗）；原文没有编号就不加编号，只留标题。第一章 `margin-top` 12px，之后 40px。

```html
<section style="padding:0 16px;">
  <section style="margin:40px 0 18px;">
    <p style="margin:0 0 6px;font-size:13px;font-weight:400;color:#b8923f;letter-spacing:3px;"><span leaf="">01</span></p>
    <p style="margin:0 0 10px;font-size:21px;font-weight:700;color:#2b2824;line-height:1.5;font-family:'Noto Serif SC','Songti SC',SimSun,serif;"><span leaf="">{{章节标题}}</span></p>
    <section style="width:28px;height:1.5px;background:#b8923f;"><span leaf=""><br></span></section>
  </section>
</section>
```

---

## 组件 3 小节标题（细金竖线 + 标题，不加粗过重）

> `margin-top:0`，间距由前一段落的 `margin-bottom:8px` 负责。

```html
<section style="padding:0 16px;">
  <section style="display:flex;align-items:center;margin:0 0 12px;padding-left:12px;border-left:1.5px solid #b8923f;">
    <p style="margin:0;font-size:16px;font-weight:700;line-height:1.6;color:#2b2824;"><span leaf="">{{小节标题}}</span></p>
  </section>
</section>
```

---

## 组件 4 正文段落

```html
<section style="padding:0 16px;">
  <p style="margin:0;font-size:15px;line-height:1.9;text-align:justify;color:#4a463f;"><span leaf="">{{正文}}</span></p>
</section>
```

紧接小标题前的最后一段，把 `margin:0` 换成 `margin:0 0 8px`。

---

## 组件 5 行内标记

### 5a 细金下划线（正文关键词默认标记，每段 ≤2 处）

```html
<span style="border-bottom:1px solid #b8923f;font-weight:600;color:#2b2824;"><span leaf="">{{关键词}}</span></span>
```

### 5b 深色加粗

```html
<span style="font-weight:700;color:#2b2824;"><span leaf="">{{加粗}}</span></span>
```

### 5c 浅金荧光笔（只在题跋卡 8a 内用）

```html
<span style="font-weight:700;color:#2b2824;background:linear-gradient(180deg,transparent 60%,#f7f1e2 60%);"><span leaf="">{{引用里的加粗句}}</span></span>
```

---

## 组件 6 列表 / 卡片

### 6a 细线分隔列表（无底色，靠细线分隔，普通无序列表）

```html
<section style="padding:0 16px;">
  <section style="margin:0 0 16px;">
    <section style="padding:10px 0;border-bottom:1px solid #e5e0d3;">
      <p style="margin:0;font-size:15px;line-height:1.8;color:#4a463f;text-align:justify;"><span leaf="">{{要点一}}</span></p>
    </section>
    <section style="padding:10px 0;">
      <p style="margin:0;font-size:15px;line-height:1.8;color:#4a463f;text-align:justify;"><span leaf="">{{最后一条，不加底边线}}</span></p>
    </section>
  </section>
</section>
```

### 6b 细金竖条要点卡（白卡 + 细金左竖条；列表每条都是"**小标题：**说明"时用——本主题弥补"留白过多"的核心容器组件，每章至少用 1 次）

```html
<section style="padding:0 16px;">
  <section style="background:#ffffff;border:1px solid #e5e0d3;border-left:2px solid #b8923f;border-radius:0 3px 3px 0;padding:12px 16px;margin:0 0 10px;">
    <p style="margin:0 0 4px;font-size:15px;font-weight:700;color:#2b2824;line-height:1.6;"><span leaf="">{{小标题：}}</span></p>
    <p style="margin:0;font-size:14px;line-height:1.85;color:#4a463f;text-align:justify;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

---

## 组件 7 图片容器（整宽直角或极小圆角，呼应"原石"质感）

```html
<section style="padding:0 16px;">
  <section style="margin:4px 0 18px;line-height:0;">
    <span leaf=""><img src="{{图片URL}}" style="width:100%;height:auto;display:block;border-radius:2px;"></span>
  </section>
</section>
```

---

## 组件 8 引用 / 金句

### 8a 碑铭式题跋卡（极浅金底 + 细金竖线；原文 `>` 引用，一篇 ≤1 处，用在全文最值得被记住的一句话）

```html
<section style="padding:0 16px;">
  <section style="background:#f7f1e2;border-left:2px solid #b8923f;padding:16px 20px;margin:4px 0 18px;">
    <p style="margin:0;font-size:16px;line-height:1.9;color:#2b2824;font-weight:600;text-align:justify;font-family:'Noto Serif SC','Songti SC',SimSun,serif;"><span leaf="">{{引用}}</span></p>
  </section>
</section>
```

### 8b 居中短句（无底色，只靠上下细线）

```html
<section style="padding:0 16px;">
  <section style="border-top:1px solid #e5e0d3;border-bottom:1px solid #e5e0d3;padding:14px 4px;margin:0 0 18px;">
    <p style="margin:0;font-size:15px;line-height:2;color:#2b2824;font-weight:600;text-align:center;letter-spacing:1px;"><span leaf="">{{居中短句}}</span></p>
  </section>
</section>
```

---

## 组件 9 结尾收束（居中大字 + 细金短线，不用深色卡——本主题的"高潮"就是克制本身）

```html
<section style="padding:0 16px;">
  <section style="margin:34px 0 10px;text-align:center;">
    <p style="margin:0 0 14px;font-size:21px;font-weight:700;color:#2b2824;letter-spacing:2px;line-height:1.7;font-family:'Noto Serif SC','Songti SC',SimSun,serif;"><span leaf="">{{收束句}}</span></p>
    <section style="width:32px;height:1.5px;background:#b8923f;margin:0 auto 14px;"><span leaf=""><br></span></section>
    <p style="margin:0;font-size:14px;color:#8c8679;letter-spacing:1px;line-height:1.9;"><span leaf="">{{收尾一句}}</span></p>
  </section>
</section>
```

---

## 组件 10 文末免责小字（原文有才放）

```html
<section style="padding:0 16px;">
  <section style="border-top:1px solid #e5e0d3;padding:12px 2px 0;margin:18px 0 0;">
    <p style="margin:0;font-size:12px;line-height:1.8;color:#b3ac9c;text-align:justify;"><span leaf="">{{免责内容}}</span></p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:12px 0;box-sizing:border-box;background:#f8f6f1;color:#4a463f;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.9;letter-spacing:0.6px;overflow-x:hidden;">

  <!-- 1. 顶部细金线（组件1） -->

  <!-- 2. 头图（组件7，有头图时）+ 开场段落（组件4） -->

  <!-- 3. 第一章（组件2，margin-top 12px） -->
  <!--    章内：组件4 正文 + 3 小节 + 5 行内标记 + 6 列表/卡片（至少 1 次）+ 7 配图 + 8 引用（全篇 ≤1） -->

  <!-- 4. 第二章…第N章（组件2，margin-top 40px） -->

  <!-- 5. 结尾收束（组件9） -->

  <!-- 6. 文末免责（组件10，原文有才放） -->

</section>
```

**骨架铁律**：没有导读卡/目录卡/深色收束卡；章节靠细金线+留白分隔，不加色块；全篇只允许 1 处碑铭式题跋卡（8a），多了就不"克制"了；每章至少 1 个细金竖条要点卡（6b）防止通篇素稿。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 结尾居中大字 9 | 全文唯一高潮，没有章节色块、没有深色卡 | 结尾 1 处 |
| **标记层** | 细金下划线 5a（默认）/ 深色加粗 5b | 正文关键词强调 | 每段 ≤2 处 |
| **容器层** | 细线列表 6a / 细金竖条要点卡 6b / 碑铭题跋卡 8a（全篇 ≤1）/ 居中短句 8b | 结构化信息、引用 | 每章至少 1 个容器层组件 |

**克制原则**：金色只做细线、下划线、竖条，不做底色也不做正文字色；本主题没有深色大色块（这是和其它主题最大的区别）；碑铭题跋卡全篇 ≤1 处，多了就失去"碑铭感"的稀缺性；不用四周虚线框、不用任何圆角较大的色块卡片。

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 品牌故事/企业文化 | 章节 2 + 正文 4 + 细金竖条卡 6b | 碑铭题跋卡 8a（全篇仅 1） |
| 年度/阶段性总结 | 章节 2 + 细线列表 6a + 细金竖条卡 6b | 居中短句 8b |
| 高端产品发布 | 章节 2 + 正文 4 + 细金竖条卡 6b | 碑铭题跋卡 8a、居中短句 8b |

所有类型共用：顶部细金线 1 + 细线章节 2 + 结尾收束 9。

---

## Markdown → 原石·雅痕 映射规则

| 原文元素 | 对应组件 | 说明 |
|---|---|---|
| `## 01 章节` | 组件 2 细金线章节标题 | 编号取原文，没有就不加 |
| `### 小节` | 组件 3 细金竖线小节标题 | `margin-top:0` |
| 普通段落 | 组件 4 | 段后距按铁律 0/8px |
| `**加粗**`（核心观点） | 组件 5a 细金下划线 | |
| `**加粗**`（普通） | 组件 5b 深色加粗 | |
| `- 列表`（每条"**小标题：**说明"） | 组件 6b 细金竖条要点卡 | |
| `- 列表`（普通） | 组件 6a 细线分隔列表 | |
| `![](图)` | 组件 7 图片容器 | |
| `> 引用`（全文最重要的一句） | 组件 8a 碑铭式题跋卡 | 全篇 ≤1，引用内加粗用 5c |
| 单句金句/排比 | 组件 8b 居中短句 | |
| 文末收束句 | 组件 9 结尾收束 | |
| `本文仅为……` | 组件 10 免责小字 | |

---

## Gotchas

- **全篇只留 1 处碑铭题跋卡**：这是本主题最该克制的地方，多了就不"碑铭"了，变成普通引用堆砌。
- **不要为了"克制"排成素稿**：留白多、色彩少不等于可以通篇标题+正文；每章至少放 1 个细金竖条要点卡（6b），否则读者会觉得"这篇什么都没排"。
- **不用深色大色块**：本主题故意不用深色收束卡，如果想要更强的"高潮感"，应该选品牌深蓝·蓝图或极光链语，不要在本主题里硬加深色卡破坏克制气质。
- **章节编号别加粗**：细体数字 + 宽字间距才是本主题的章节编号气质，加粗会显得突兀。
