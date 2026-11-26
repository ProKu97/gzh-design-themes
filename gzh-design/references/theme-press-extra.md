# 公众号排版组件库 —— 铅字·号外

> **使用说明**：本组件库为「铅字·号外（Press Extra）」主题，原创主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：老报纸"号外"的版面感——新闻纸米白底 + 油墨黑粗线 + 一抹号外红。报头用一粗一细两道黑线压住版面；章节标题是红底白字的栏目号 + 黑体大标题 + 通栏黑线；关键数字做成"数据块"（大号红字 + 小字说明）；引语用上下粗黑线夹住、左上一个红色引号；收束处是一张黑底的"本期结论"卡。整体节奏快、对比强、信息密度高，读起来像在看一份当天的快报。适合热点快评、行业快讯、数据新闻、周报月报、事件复盘、立场鲜明的观点稿。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`、`transform`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
> - font-size ≤ 24px；正文强调用下划线/竖条/卡片，**不用四周虚线框**
>
> **WeChat 兼容铁律**：
> - 装饰性空元素（报头粗细线、通栏黑线、方块项目符号、短横）内部必须放 `<span leaf=""><br></span>`
> - 高亮样式挂在外层 `<span>` 上，文字放内层 `<span leaf="">`；不要把 `font-size`/`border-bottom` 打在 `<strong>` 上
> - 没内容的结构块整块删掉，不留空 section

---

## 设计变量速查表

```
油墨黑（主色）：     #111111（报头粗线 / 通栏线 / 章节标题字 / 收束卡底 / 方块符号）
号外红（点缀）：     #C8102E（栏目号底 / 数据块数字 / 引号 / 下划线 / 收束卡顶条）
正文色：             #2A2A2A
次要文字色：         #6E6A62（数据块说明 / 结尾小字）
弱化文字色：         #9C978C（免责小字）
新闻纸底（容器）：   #F4F1EA
白卡底：             #FFFFFF（要点速览 / 数据块）
浅灰纸底：           #EAE6DC（编者按）
浅红底：             #F6E3E3（引语内荧光）
细线色：             #CFC9BC（数据块分隔 / 列表分隔）
收束卡内次要字：     #BDB8AE
正文字号：           15px（卡片说明 13~14px）
行高：               1.8
字间距：             0.3px
最大宽度：           677px
内容区边距：         0 14px
章节间距：           第一章 margin-top 10px，之后 34px
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`（标题用 900 字重做出"铅字"感，正文 400）

**段后距铁律**（全主题通用）：正文自然段相邻 `margin-bottom:0`；段落后紧跟小标题改 `margin-bottom:8px`；小标题不叠加顶部空隙。

**用色铁律**：号外红只做栏目号、数据数字、引号、下划线、顶条这些"点"，**不做大段正文字色**；黑色大色块全篇只有一张"本期结论"卡；数据块全篇 ≤2 组，多了就成了报表。

---

## 组件 1 全局容器 + 报头双线

```html
<section style="max-width:677px;margin:0 auto;padding:10px 0;box-sizing:border-box;background:#f4f1ea;color:#2a2a2a;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.8;letter-spacing:0.3px;overflow-x:hidden;">
  <section style="margin:0 14px 4px;height:5px;background:#111111;"><span leaf=""><br></span></section>
  <section style="margin:0 14px 18px;height:1px;background:#111111;"><span leaf=""><br></span></section>

  <!-- 所有组件放在这里 -->

</section>
```

### 1b 报头标签行（可选，放在报头双线下方，全篇 ≤1）

> 左边红底"号外"小标签，右边一行灰色小字写本篇的栏目/期号/日期（原文有才写，没有就只留"号外"标签）。

```html
<section style="padding:0 14px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin:0 0 16px;">
    <p style="margin:0;"><span style="display:inline-block;background:#c8102e;color:#ffffff;font-size:13px;font-weight:900;letter-spacing:3px;padding:2px 10px;"><span leaf="">号外</span></span></p>
    <p style="margin:0;font-size:12px;color:#6e6a62;letter-spacing:1px;"><span leaf="">{{栏目 · 期号}}</span></p>
  </section>
</section>
```

---

## 组件 2 章节标题（红底栏目号 + 黑体标题 + 通栏黑线）

> 编号取原文的；原文没编号也补顺序号（栏目号是本主题的版面锚点）。第一章 `margin-top` 10px，之后 34px。

```html
<section style="padding:0 14px;">
  <section style="margin:34px 0 14px;">
    <section style="display:flex;align-items:center;margin:0 0 8px;">
      <p style="margin:0 10px 0 0;flex-shrink:0;"><span style="display:inline-block;background:#c8102e;color:#ffffff;font-size:14px;font-weight:900;padding:2px 8px;line-height:1.5;"><span leaf="">01</span></span></p>
      <p style="margin:0;font-size:19px;font-weight:900;color:#111111;line-height:1.45;"><span leaf="">{{章节标题}}</span></p>
    </section>
    <section style="height:2px;background:#111111;"><span leaf=""><br></span></section>
  </section>
</section>
```

---

## 组件 3 小节标题（黑方块 + 粗标题）

> `margin-top:0`，间距交给前一段的 `margin-bottom:8px`。

```html
<section style="padding:0 14px;">
  <section style="display:flex;align-items:center;margin:0 0 10px;">
    <section style="width:8px;height:8px;background:#111111;flex-shrink:0;margin-right:8px;"><span leaf=""><br></span></section>
    <p style="margin:0;font-size:16px;font-weight:900;color:#111111;line-height:1.6;"><span leaf="">{{小节标题}}</span></p>
  </section>
</section>
```

---

## 组件 4 正文段落

```html
<section style="padding:0 14px;">
  <p style="margin:0;font-size:15px;line-height:1.8;text-align:justify;color:#2a2a2a;"><span leaf="">{{正文}}</span></p>
</section>
```

紧接小标题前的最后一段，把 `margin:0` 换成 `margin:0 0 8px`。

### 4b 导语段（每章第一段可用，加粗黑字 + 左红竖线，像新闻导语）

```html
<section style="padding:0 14px;">
  <p style="margin:0 0 10px;font-size:15px;line-height:1.8;text-align:justify;color:#111111;font-weight:700;border-left:3px solid #c8102e;padding-left:10px;"><span leaf="">{{导语}}</span></p>
</section>
```

---

## 组件 5 行内标记

### 5a 号外红下划线（正文关键词默认标记，每段 ≤2 处）

```html
<span style="border-bottom:2px solid #c8102e;font-weight:700;color:#111111;"><span leaf="">{{关键词}}</span></span>
```

### 5b 油墨黑加粗

```html
<span style="font-weight:900;color:#111111;"><span leaf="">{{加粗}}</span></span>
```

### 5c 浅红荧光（只在引语 8a 内用）

```html
<span style="font-weight:900;color:#111111;background:linear-gradient(180deg,transparent 58%,#f6e3e3 58%);"><span leaf="">{{引语里的关键句}}</span></span>
```

---

## 组件 6 列表 / 数据

### 6a 要点速览（白卡 + 黑色粗顶线 + 黑方块符号；普通无序列表）

```html
<section style="padding:0 14px;">
  <section style="background:#ffffff;border-top:3px solid #111111;padding:12px 14px 6px;margin:2px 0 16px;">
    <p style="margin:0 0 8px;font-size:12px;font-weight:900;color:#c8102e;letter-spacing:2px;"><span leaf="">要点速览</span></p>
    <section style="display:flex;align-items:flex-start;padding:6px 0;border-bottom:1px solid #cfc9bc;">
      <section style="width:6px;height:6px;background:#111111;margin:10px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.75;color:#2a2a2a;text-align:justify;flex:1;"><span leaf="">{{要点一}}</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;padding:6px 0;">
      <section style="width:6px;height:6px;background:#111111;margin:10px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.75;color:#2a2a2a;text-align:justify;flex:1;"><span leaf="">{{最后一条不加底线}}</span></p>
    </section>
  </section>
</section>
```

> 标签文字"要点速览"可按语境换成"三件事""一图看懂之前""划重点"等，4~6 字。

### 6b 数据块（两格并排；原文有关键数字时用，全篇 ≤2 组）

> 数字用红色 24px（平台上限），下面一行灰色小字说明；只有一个数字时删掉右格和中间竖线。数字必须来自原文，**不要编数字**。

```html
<section style="padding:0 14px;">
  <section style="display:flex;background:#ffffff;border-top:3px solid #111111;border-bottom:1px solid #111111;margin:2px 0 16px;">
    <section style="flex:1;padding:12px 12px;text-align:center;">
      <p style="margin:0 0 4px;font-size:24px;font-weight:900;color:#c8102e;line-height:1.2;"><span leaf="">{{数字一}}</span></p>
      <p style="margin:0;font-size:12px;color:#6e6a62;line-height:1.5;"><span leaf="">{{说明一}}</span></p>
    </section>
    <section style="width:1px;background:#cfc9bc;margin:12px 0;"><span leaf=""><br></span></section>
    <section style="flex:1;padding:12px 12px;text-align:center;">
      <p style="margin:0 0 4px;font-size:24px;font-weight:900;color:#c8102e;line-height:1.2;"><span leaf="">{{数字二}}</span></p>
      <p style="margin:0;font-size:12px;color:#6e6a62;line-height:1.5;"><span leaf="">{{说明二}}</span></p>
    </section>
  </section>
</section>
```

### 6c 编号条目（"第一/第二/第三"或有先后顺序的列表）

```html
<section style="padding:0 14px;">
  <section style="margin:2px 0 14px;">
    <section style="display:flex;align-items:flex-start;margin:0 0 8px;">
      <p style="margin:0 10px 0 0;flex-shrink:0;font-size:18px;font-weight:900;color:#c8102e;line-height:1.4;"><span leaf="">1</span></p>
      <p style="margin:0;font-size:15px;line-height:1.75;color:#2a2a2a;text-align:justify;flex:1;"><span leaf="">{{条目一}}</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;margin:0;">
      <p style="margin:0 10px 0 0;flex-shrink:0;font-size:18px;font-weight:900;color:#c8102e;line-height:1.4;"><span leaf="">2</span></p>
      <p style="margin:0;font-size:15px;line-height:1.75;color:#2a2a2a;text-align:justify;flex:1;"><span leaf="">{{条目二}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 7 图片（直角 + 底部图注条）

> 报纸图片不做圆角；有图注时下方一条黑字小注，左侧加"图｜"前缀；没有图注删掉 `<p>`。

```html
<section style="padding:0 14px;">
  <section style="margin:4px 0 6px;line-height:0;">
    <span leaf=""><img src="{{图片URL}}" style="width:100%;height:auto;display:block;"></span>
  </section>
  <p style="margin:0 0 16px;font-size:12px;color:#6e6a62;line-height:1.6;"><span style="font-weight:900;color:#111111;"><span leaf="">图｜</span></span><span leaf="">{{图注}}</span></p>
</section>
```

---

## 组件 8 引语 / 编者按

### 8a 引语（上下粗黑线 + 红引号；原文 `>` 引用、全文金句）

```html
<section style="padding:0 14px;">
  <section style="border-top:3px solid #111111;border-bottom:1px solid #111111;padding:10px 4px 12px;margin:4px 0 18px;">
    <p style="margin:0;font-size:24px;font-weight:900;color:#c8102e;line-height:1;"><span leaf="">“</span></p>
    <p style="margin:0;font-size:17px;font-weight:900;color:#111111;line-height:1.7;text-align:justify;"><span leaf="">{{引语}}</span></p>
  </section>
</section>
```

### 8b 编者按（浅灰纸底 + 红色小标签；转折说明、背景补充）

```html
<section style="padding:0 14px;">
  <section style="background:#eae6dc;padding:12px 14px;margin:2px 0 16px;">
    <p style="margin:0 0 6px;"><span style="display:inline-block;background:#111111;color:#ffffff;font-size:11px;font-weight:900;letter-spacing:2px;padding:1px 8px;"><span leaf="">编者按</span></span></p>
    <p style="margin:0;font-size:14px;line-height:1.8;color:#2a2a2a;text-align:justify;"><span leaf="">{{补充说明}}</span></p>
  </section>
</section>
```

> 标签可换："背景""注意""延伸"等，2~3 字。

---

## 组件 9 本期结论卡（黑底 + 红顶条，全篇 ≤1）

```html
<section style="padding:0 14px;">
  <section style="background:#111111;margin:4px 0 18px;">
    <section style="height:4px;background:#c8102e;"><span leaf=""><br></span></section>
    <section style="padding:14px 16px 16px;">
      <p style="margin:0 0 8px;font-size:12px;font-weight:900;color:#c8102e;letter-spacing:3px;"><span leaf="">本期结论</span></p>
      <p style="margin:0 0 6px;font-size:18px;font-weight:900;color:#ffffff;line-height:1.6;"><span leaf="">{{结论大字}}</span></p>
      <p style="margin:0;font-size:14px;color:#bdb8ae;line-height:1.8;"><span leaf="">{{补充一句}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 10 结尾（"— 完 —" + 一句收尾）

```html
<section style="padding:0 14px;">
  <section style="margin:26px 0 8px;text-align:center;">
    <section style="display:flex;align-items:center;justify-content:center;margin:0 0 10px;">
      <section style="width:40px;height:1px;background:#111111;"><span leaf=""><br></span></section>
      <p style="margin:0 10px;font-size:13px;font-weight:900;color:#111111;letter-spacing:4px;"><span leaf="">完</span></p>
      <section style="width:40px;height:1px;background:#111111;"><span leaf=""><br></span></section>
    </section>
    <p style="margin:0;font-size:14px;color:#6e6a62;line-height:1.8;"><span leaf="">{{收尾一句}}</span></p>
  </section>
</section>
```

---

## 组件 11 文末免责小字（原文有才放）

```html
<section style="padding:0 14px;">
  <section style="border-top:1px solid #cfc9bc;padding:10px 2px 0;margin:16px 0 0;">
    <p style="margin:0;font-size:12px;line-height:1.7;color:#9c978c;text-align:justify;"><span leaf="">{{免责内容}}</span></p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:10px 0;box-sizing:border-box;background:#f4f1ea;color:#2a2a2a;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.8;letter-spacing:0.3px;overflow-x:hidden;">

  <!-- 1. 报头双线（组件1）+ 报头标签行（组件1b，可选） -->

  <!-- 2. 开篇：引语（组件8a，原文开头有金句时）或导语段（组件4b）+ 正文段落 -->

  <!-- 3. 第一章（组件2，margin-top 10px）
         章内：导语 4b（可选）+ 正文 4 + 小节 3 + 行内标记 5 + 要点速览 6a / 数据块 6b / 编号条目 6c + 图片 7 + 引语 8a / 编者按 8b -->

  <!-- 4. 第二章…第N章（组件2，margin-top 34px）；本期结论卡（组件9）全篇 ≤1，放在最后一章末尾或全文总结处 -->

  <!-- 5. 结尾"完"（组件10） -->

  <!-- 6. 文末免责（组件11，原文有才放） -->

</section>
```

**骨架铁律**：报头双线必须有，它是这个主题的第一眼识别；章节之间靠栏目号 + 通栏黑线分隔，不另加分割线；数据块只放原文真实出现的数字；本期结论卡全篇只有一张。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 报头双线 1 / 栏目号章节 2 / 本期结论卡 9 | 版面骨架与唯一高潮 | 报头 1 + 章节数 + 结论卡 ≤1 |
| **标记层** | 号外红下划线 5a（默认）/ 黑色加粗 5b | 正文关键词 | 每段 ≤2 处 |
| **容器层** | 导语 4b / 要点速览 6a / 数据块 6b / 编号条目 6c / 引语 8a / 编者按 8b | 结构化信息、数字、金句 | 每章至少 1 个 |

**克制原则**：红色只做"点"，不做"面"（除了栏目号小块和结论卡顶条）；数据块 ≤2 组、引语 ≤3 处；不用圆角（直角才有报纸感，标签/卡片一律 `border-radius:0`）；不用四周虚线框。

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 热点快评 / 立场观点 | 章节 2 + 导语 4b + 引语 8a | 编者按 8b、本期结论 9 |
| 行业快讯 / 数据新闻 | 章节 2 + 数据块 6b + 要点速览 6a | 图片 7、本期结论 9 |
| 周报 / 月报 / 事件复盘 | 报头标签 1b + 章节 2 + 编号条目 6c + 要点速览 6a | 数据块 6b、编者按 8b |

所有类型共用：报头双线 1 + 栏目号章节 2 + 结尾"完" 10。

---

## Markdown → 铅字·号外 映射规则

| 原文元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号标题在平台设置 |
| `## 章节` | 组件 2 栏目号章节 | 没编号也补顺序号 |
| `### 小节` | 组件 3 黑方块小节 | `margin-top:0` |
| 每章第一段（总起句） | 组件 4b 导语段 | 可选，每章 ≤1 |
| 普通段落 | 组件 4 | 段后距按铁律 0/8px |
| `**加粗**`（核心观点） | 组件 5a 号外红下划线 | |
| `**加粗**`（普通） | 组件 5b 黑色加粗 | |
| `- 列表`（普通） | 组件 6a 要点速览 | |
| 原文里成对/成组的关键数字 | 组件 6b 数据块 | 只用原文数字，≤2 组 |
| `1. 2. 3.` / 第一第二第三 | 组件 6c 编号条目 | |
| `![](图)` | 组件 7 直角图片 + 图注 | |
| `> 引用` / 全文金句 | 组件 8a 引语 | 引语内加粗用 5c |
| 背景补充 / 转折说明 | 组件 8b 编者按 | |
| 全文最核心的结论 | 组件 9 本期结论卡 | 全篇 ≤1 |
| 文末收尾句 | 组件 10 结尾"完" | |
| `本文仅为……` | 组件 11 免责小字 | |

---

## Gotchas

- **数据块不编数字**：原文没有具体数字就不要用 6b，宁可用要点速览；一旦编数字就是事实错误。
- **不要圆角**：本主题所有卡片、标签、图片都是直角，加圆角会立刻失去报纸感。
- **红色别铺满**：红只做栏目号、数字、引号、下划线、顶条；段落文字、卡片底色都不用红。
- **"号外"标签只用一次**：报头标签行全篇最多一处，不要每章都贴一个"号外"。
- **引号字符用全角弯引号 `“`**，24px 红色，单独一行；不要用英文直引号。
