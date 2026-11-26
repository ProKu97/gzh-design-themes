# 公众号排版组件库 —— 便笺·手帐

> **使用说明**：本组件库为「便笺·手帐（Memo Notebook）」主题，原创主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：一本摊开的手帐——米白纸面、顶部一排活页孔；章节标题是贴上去的彩色和纸胶带（黄 / 薄荷 / 粉 / 天蓝轮换）；正文重点用荧光笔涂一道；列表是打勾清单；补充信息写在便利贴上；图片像拍立得一样带白边和手写图注；最后贴一张"今日小结"。整体轻松、亲切、有生活感，是这套 skill 里唯一一套"不严肃"的主题，和其它主题的理性/克制形成反差。适合生活方式、新手入门教程、团队日常与活动回顾、读书/学习笔记、轻松向的科普。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`、`transform`（所以胶带和便利贴都**不做旋转**，靠颜色和阴影营造"贴上去"的感觉）
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`rgba()` 颜色、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
> - font-size ≤ 24px；**不用四周虚线框**
>
> **WeChat 兼容铁律**：
> - 装饰性空元素（活页孔、胶带短条）内部必须放 `<span leaf=""><br></span>`
> - 高亮样式挂在外层 `<span>` 上，文字放内层 `<span leaf="">`
> - 没内容的结构块整块删掉

---

## 设计变量速查表

```
墨水蓝（主色）：     #2F3E5C（标题 / 胶带上的字 / 加粗 / 图注）
正文色：             #4A4A48
次要文字色：         #8A8578（结尾小字）
弱化文字色：         #B0AA9C（免责小字）
米白纸（容器）：     #FFFDF7
白卡底：             #FFFFFF（清单卡 / 拍立得边框）
细线色：             #E8E2D4（卡片描边 / 活页孔描边）

胶带四色（章节按 01→02→03→04→01… 轮换）：
  胶带黄：           rgba(247,215,116,0.85)   ≈ #F7D774
  胶带薄荷：         rgba(168,220,200,0.85)   ≈ #A8DCC8
  胶带粉：           rgba(244,184,184,0.85)   ≈ #F4B8B8
  胶带天蓝：         rgba(184,212,240,0.85)   ≈ #B8D4F0

便利贴三色：
  便利贴黄：         #FFF4C2
  便利贴薄荷：       #E3F5EC
  便利贴粉：         #FDE8E8

荧光笔黄（正文关键词默认）：#F7D774
荧光笔粉（只在黄色便利贴内用，避免黄上涂黄看不见）：#F4B8B8
打勾绿：             #3E9C7E

正文字号：           15px（便利贴/卡片 14px）
行高：               1.85
字间距：             0.4px
最大宽度：           677px
内容区边距：         0 14px
章节间距：           第一章 margin-top 6px，之后 32px
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

**段后距铁律**（全主题通用）：正文自然段相邻 `margin-bottom:0`；段落后紧跟小标题改 `margin-bottom:8px`；小标题不叠加顶部空隙。

**用色铁律**：胶带色和便利贴色都是"大块浅色"，**文字一律用墨水蓝或正文色**，不要在彩色底上再用彩色字；一屏之内不要同时出现超过 3 种便利贴/胶带颜色，否则会花。

---

## 组件 1 全局容器 + 活页孔

```html
<section style="max-width:677px;margin:0 auto;padding:10px 0;box-sizing:border-box;background:#fffdf7;color:#4a4a48;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.85;letter-spacing:0.4px;overflow-x:hidden;">
  <section style="display:flex;justify-content:space-around;margin:0 24px 20px;">
    <section style="width:10px;height:10px;border-radius:50%;border:2px solid #e8e2d4;background:#ffffff;"><span leaf=""><br></span></section>
    <section style="width:10px;height:10px;border-radius:50%;border:2px solid #e8e2d4;background:#ffffff;"><span leaf=""><br></span></section>
    <section style="width:10px;height:10px;border-radius:50%;border:2px solid #e8e2d4;background:#ffffff;"><span leaf=""><br></span></section>
    <section style="width:10px;height:10px;border-radius:50%;border:2px solid #e8e2d4;background:#ffffff;"><span leaf=""><br></span></section>
    <section style="width:10px;height:10px;border-radius:50%;border:2px solid #e8e2d4;background:#ffffff;"><span leaf=""><br></span></section>
    <section style="width:10px;height:10px;border-radius:50%;border:2px solid #e8e2d4;background:#ffffff;"><span leaf=""><br></span></section>
    <section style="width:10px;height:10px;border-radius:50%;border:2px solid #e8e2d4;background:#ffffff;"><span leaf=""><br></span></section>
  </section>

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 章节标题（和纸胶带）

> 胶带颜色按章节顺序轮换：01 黄 → 02 薄荷 → 03 粉 → 04 天蓝 → 05 再从黄开始。编号取原文的，没有也补上。第一章 `margin-top` 6px，之后 32px。

```html
<section style="padding:0 14px;">
  <p style="margin:32px 0 14px;">
    <span style="display:inline-block;background:rgba(247,215,116,0.85);color:#2f3e5c;font-size:17px;font-weight:800;line-height:1.5;padding:4px 16px 4px 12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);"><span leaf="">01 · {{章节标题}}</span></span>
  </p>
</section>
```

其余三色只换 `background`：薄荷 `rgba(168,220,200,0.85)`、粉 `rgba(244,184,184,0.85)`、天蓝 `rgba(184,212,240,0.85)`。

---

## 组件 3 小节标题（✎ 铅笔记号 + 标题）

> `margin-top:0`，间距交给前一段的 `margin-bottom:8px`。

```html
<section style="padding:0 14px;">
  <p style="margin:0 0 10px;font-size:16px;font-weight:800;color:#2f3e5c;line-height:1.6;"><span style="color:#3e9c7e;margin-right:6px;"><span leaf="">✎</span></span><span leaf="">{{小节标题}}</span></p>
</section>
```

---

## 组件 4 正文段落

```html
<section style="padding:0 14px;">
  <p style="margin:0;font-size:15px;line-height:1.85;text-align:justify;color:#4a4a48;"><span leaf="">{{正文}}</span></p>
</section>
```

紧接小标题前的最后一段，把 `margin:0` 换成 `margin:0 0 8px`。

---

## 组件 5 行内标记

### 5a 荧光笔黄（正文关键词默认标记，每段 ≤2 处）

```html
<span style="background:linear-gradient(180deg,transparent 56%,#f7d774 56%);font-weight:600;color:#2f3e5c;"><span leaf="">{{关键词}}</span></span>
```

### 5b 墨水蓝加粗

```html
<span style="font-weight:800;color:#2f3e5c;"><span leaf="">{{加粗}}</span></span>
```

### 5c 荧光笔粉（只在黄色便利贴 / 黄色引用里用）

```html
<span style="background:linear-gradient(180deg,transparent 56%,#f4b8b8 56%);font-weight:700;color:#2f3e5c;"><span leaf="">{{关键词}}</span></span>
```

---

## 组件 6 清单 / 便利贴

### 6a 打勾清单（白卡 + 绿勾；普通无序列表、步骤、要做的事）

```html
<section style="padding:0 14px;">
  <section style="background:#ffffff;border:1px solid #e8e2d4;border-radius:10px;padding:10px 14px;margin:2px 0 16px;">
    <section style="display:flex;align-items:flex-start;margin:0 0 6px;">
      <p style="margin:0 8px 0 0;flex-shrink:0;font-size:15px;font-weight:800;color:#3e9c7e;line-height:1.75;"><span leaf="">✓</span></p>
      <p style="margin:0;font-size:15px;line-height:1.75;color:#4a4a48;text-align:justify;flex:1;"><span leaf="">{{第一条}}</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;margin:0;">
      <p style="margin:0 8px 0 0;flex-shrink:0;font-size:15px;font-weight:800;color:#3e9c7e;line-height:1.75;"><span leaf="">✓</span></p>
      <p style="margin:0;font-size:15px;line-height:1.75;color:#4a4a48;text-align:justify;flex:1;"><span leaf="">{{最后一条}}</span></p>
    </section>
  </section>
</section>
```

### 6b 便利贴组（"**小标题：**说明"式列表；两条并排，三条以上改成上下堆叠）

> 颜色按顺序轮换黄 → 薄荷 → 粉；并排时两张之间留 10px。

```html
<section style="padding:0 14px;">
  <section style="display:flex;margin:2px 0 16px;">
    <section style="flex:1;background:#fff4c2;border-radius:2px;padding:12px 12px;margin-right:10px;box-shadow:0 2px 6px rgba(0,0,0,0.08);">
      <p style="margin:0 0 4px;font-size:15px;font-weight:800;color:#2f3e5c;line-height:1.5;"><span leaf="">{{便利贴标题一}}</span></p>
      <p style="margin:0;font-size:14px;line-height:1.75;color:#4a4a48;text-align:justify;"><span leaf="">{{说明一}}</span></p>
    </section>
    <section style="flex:1;background:#e3f5ec;border-radius:2px;padding:12px 12px;box-shadow:0 2px 6px rgba(0,0,0,0.08);">
      <p style="margin:0 0 4px;font-size:15px;font-weight:800;color:#2f3e5c;line-height:1.5;"><span leaf="">{{便利贴标题二}}</span></p>
      <p style="margin:0;font-size:14px;line-height:1.75;color:#4a4a48;text-align:justify;"><span leaf="">{{说明二}}</span></p>
    </section>
  </section>
</section>
```

堆叠版：每张便利贴单独一个 `<section>`（去掉 `flex:1` 和 `margin-right`），之间 `margin:0 0 10px`。

---

## 组件 7 拍立得图片（白边 + 下方手写式图注）

```html
<section style="padding:0 14px;">
  <section style="background:#ffffff;padding:8px 8px 0;margin:4px 6px 18px;box-shadow:0 3px 10px rgba(0,0,0,0.12);">
    <section style="line-height:0;">
      <span leaf=""><img src="{{图片URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
    </section>
    <p style="margin:0;padding:8px 4px 10px;font-size:13px;color:#2f3e5c;text-align:center;line-height:1.6;"><span leaf="">{{图注}}</span></p>
  </section>
</section>
```

没有图注时删掉 `<p>`，并把外框 `padding` 改成四边一样的 `8px`，否则底部会多出一条空白。图注只写原文给的，不要替用户编。

---

## 组件 8 记一笔 / 小提示

### 8a 记一笔（黄色便利贴引用；原文 `>` 引用、金句）

```html
<section style="padding:0 14px;">
  <section style="background:#fff4c2;border-radius:2px;padding:12px 16px;margin:4px 0 18px;box-shadow:0 2px 6px rgba(0,0,0,0.08);">
    <p style="margin:0 0 4px;font-size:12px;font-weight:800;color:#8a8578;letter-spacing:1px;"><span leaf="">★ 记一笔</span></p>
    <p style="margin:0;font-size:15px;line-height:1.85;color:#2f3e5c;font-weight:600;text-align:justify;"><span leaf="">{{引用}}</span></p>
  </section>
</section>
```

### 8b 小提示（薄荷圆角气泡；补充说明、注意事项、小技巧）

```html
<section style="padding:0 14px;">
  <section style="background:#e3f5ec;border-radius:14px;padding:12px 16px;margin:2px 0 16px;">
    <p style="margin:0 0 4px;font-size:13px;font-weight:800;color:#3e9c7e;"><span leaf="">💡 小提示</span></p>
    <p style="margin:0;font-size:14px;line-height:1.8;color:#4a4a48;text-align:justify;"><span leaf="">{{提示内容}}</span></p>
  </section>
</section>
```

---

## 组件 9 今日小结（粉色便利贴 + 顶部一小截胶带，全篇 ≤1）

```html
<section style="padding:0 14px;">
  <section style="background:#fde8e8;border-radius:2px;padding:0 16px 16px;margin:6px 0 18px;box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <section style="width:72px;height:14px;background:rgba(247,215,116,0.9);margin:0 auto 12px;"><span leaf=""><br></span></section>
    <p style="margin:0 0 6px;font-size:13px;font-weight:800;color:#8a8578;text-align:center;letter-spacing:2px;"><span leaf="">今日小结</span></p>
    <p style="margin:0 0 6px;font-size:17px;font-weight:800;color:#2f3e5c;text-align:center;line-height:1.6;"><span leaf="">{{一句话总结}}</span></p>
    <p style="margin:0;font-size:14px;color:#4a4a48;text-align:center;line-height:1.8;"><span leaf="">{{补充一句}}</span></p>
  </section>
</section>
```

---

## 组件 10 结尾（"今天就记到这里"）

```html
<section style="padding:0 14px;">
  <section style="margin:24px 0 8px;text-align:center;">
    <p style="margin:0 0 6px;font-size:13px;font-weight:800;color:#2f3e5c;letter-spacing:2px;"><span leaf="">— 今天就记到这里 —</span></p>
    <p style="margin:0;font-size:14px;color:#8a8578;line-height:1.8;"><span leaf="">{{收尾一句}}</span></p>
  </section>
</section>
```

---

## 组件 11 文末免责小字（原文有才放）

```html
<section style="padding:0 14px;">
  <section style="border-top:1px solid #e8e2d4;padding:10px 2px 0;margin:16px 0 0;">
    <p style="margin:0;font-size:12px;line-height:1.7;color:#b0aa9c;text-align:justify;"><span leaf="">{{免责内容}}</span></p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:10px 0;box-sizing:border-box;background:#fffdf7;color:#4a4a48;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.85;letter-spacing:0.4px;overflow-x:hidden;">

  <!-- 1. 活页孔（组件1） -->

  <!-- 2. 开篇：记一笔（组件8a，原文开头有金句时）+ 正文段落 -->

  <!-- 3. 第一章（组件2 黄胶带，margin-top 6px）
         章内：正文 4 + 小节 3 + 荧光笔 5 + 打勾清单 6a / 便利贴 6b + 拍立得 7 + 记一笔 8a / 小提示 8b -->

  <!-- 4. 第二章…第N章（组件2，胶带颜色轮换，margin-top 32px）；今日小结（组件9）全篇 ≤1，放在全文最后 -->

  <!-- 5. 结尾（组件10） -->

  <!-- 6. 文末免责（组件11，原文有才放） -->

</section>
```

**骨架铁律**：顶部活页孔必须有；章节胶带颜色必须轮换，不能全篇一个色；今日小结只在文末出现一次；本主题不用深色大色块。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 胶带章节 2 / 今日小结 9 | 骨架与收束 | 章节数 + 小结 1 |
| **标记层** | 荧光笔黄 5a（默认）/ 墨水蓝加粗 5b | 正文关键词 | 每段 ≤2 处 |
| **容器层** | 打勾清单 6a / 便利贴 6b / 拍立得 7 / 记一笔 8a / 小提示 8b | 列表、补充、金句、图片 | 每章至少 1 个 |

**克制原则**：轻松不等于乱——一屏内颜色不超过 3 种；彩色底上只用墨水蓝/正文色文字；便利贴阴影保持很淡（`rgba(0,0,0,0.08)` 左右）；emoji 只用组件里规定的那几个（✎ ✓ ★ 💡），不要在正文里随手加。

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 新手教程 / 入门指南 | 胶带章节 2 + 打勾清单 6a + 小提示 8b | 拍立得 7、今日小结 9 |
| 生活方式 / 读书学习笔记 | 胶带章节 2 + 正文 4 + 记一笔 8a | 便利贴 6b、今日小结 9 |
| 团队日常 / 活动回顾 | 胶带章节 2 + 拍立得 7 + 便利贴 6b | 打勾清单 6a、记一笔 8a |

所有类型共用：活页孔 1 + 胶带章节 2 + 结尾 10。

---

## Markdown → 便笺·手帐 映射规则

| 原文元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号标题在平台设置 |
| `## 章节` | 组件 2 胶带章节 | 颜色按顺序轮换 |
| `### 小节` | 组件 3 ✎ 小节 | `margin-top:0` |
| 普通段落 | 组件 4 | 段后距按铁律 0/8px |
| `**加粗**`（核心观点） | 组件 5a 荧光笔黄 | 在黄色便利贴里改用 5c 粉色 |
| `**加粗**`（普通） | 组件 5b 墨水蓝加粗 | |
| `- 列表` / `1. 2. 3.` | 组件 6a 打勾清单 | |
| `- 列表`（每条"**小标题：**说明"） | 组件 6b 便利贴组 | 2 条并排，3 条以上堆叠 |
| `![](图)` | 组件 7 拍立得 | 有图注写在白边下 |
| `> 引用` / 金句 | 组件 8a 记一笔 | |
| 补充说明 / 注意 / 小技巧 | 组件 8b 小提示 | |
| 全文总结 | 组件 9 今日小结 | 全篇 ≤1，放最后 |
| 文末收尾句 | 组件 10 结尾 | |
| `本文仅为……` | 组件 11 免责小字 | |

---

## Gotchas

- **不做旋转**：`transform:rotate()` 在微信里不稳定，胶带和便利贴都保持水平，靠颜色、阴影、圆角差异营造手作感。
- **黄底上别涂黄**：黄色便利贴（6b 黄、8a）里的强调要用 5c 粉色荧光笔，否则看不见。
- **胶带必须轮换颜色**：全篇同一色会显得像普通标签，失去"贴胶带"的手帐感。
- **emoji 不要加戏**：只用 ✎ ✓ ★ 💡 这几个固定位置的符号，正文里不要再随手插表情。
- **这套主题不适合严肃内容**：财报、政策解读、安全通告、深度评论请换品牌深蓝·蓝图、铅字·号外或原石·雅痕。
