# 公众号排版组件库 —— 极光链语

> **使用说明**：本组件库为「极光链语（Aurora Chain）」主题，原创主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：白底 + 靛紫渐变章节块 + 青色荧光点缀，气质偏未来科技/网络感，像极光划过夜空的一道冷色光带。章节标题用靛紫→紫罗兰渐变色块，青色大号编号；正文关键词用青色下划线（带极淡的发光描边）；列表/卡片用浅紫或浅青底；收束卡是全篇唯一一张靛紫渐变深色卡，边缘加一层淡紫光晕（`box-shadow`）。比「品牌深蓝·蓝图」更跳、更"网络感"，比纯科技蓝更有未来感。适合区块链/分布式网络、算力、数据基础设施、"面向未来"的产业科普和愿景类内容。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`、`background-clip:text`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
> - font-size ≤ 24px；正文强调用左竖条/下划线/卡片，**不用四周虚线框**（dashed）
>
> **WeChat 兼容铁律**：
> - 所有"装饰性空元素"（顶部双线、竖分隔线、短线、光点）**必须在内部放 `<span leaf=""><br></span>` 占位**
> - 高亮样式统一挂在外层 `<span>` 上，文字放内层 `<span leaf="">`；不要把 `font-size`/`border-bottom` 打在 `<strong>` 上
> - 结构化区域没有内容时**整块删掉**，不留空 section
> - **渐变/光晕只用 `linear-gradient` 和 `box-shadow` 实现**，不要用 `background-clip:text`（微信不支持，文字会直接不可见）

---

## 设计变量速查表

```
靛紫（主色）：       #2E2A6B（章节色块起点 / 收束卡 / 标题强调）
紫罗兰（主色渐变终点）：#6D4FD6（章节色块终点 / 收束卡渐变）
青色荧光（点缀）：   #00C2B8（正文下划线 / 编号 / 竖条 / 短线）
标题深色：           #16152E
正文色：             #2A2E3D
次要文字色：         #6B7280
弱化文字色：         #9CA0B0
细线色：             #E2E4F0
浅紫底：             #F2EFFC
浅青底：             #E6FBF8
深紫卡内次要字：     #D8D4F5
荧光描边（下划线用）：box-shadow:0 1px 0 rgba(0,194,184,0.4)
正文字号：           15px（卡片说明 14px）
行高：               1.85
字间距：             0.3px
最大宽度：           677px
内容区边距：         0 12px
章节间距：           第一章 margin-top 8px，之后 32px
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

**段后距铁律**（全主题通用）：正文自然段与下一段相邻 `margin-bottom:0`；段落后紧跟小标题改 `margin-bottom:8px`，小标题不叠加顶部空隙。

**用色铁律**：青色只做下划线、编号、竖条、短线，**不做大段正文字色**；靛紫渐变大色块只有章节标题和全篇唯一一张收束卡；一篇文章点缀组件种类 ≤3。

---

## 组件 1 全局容器 + 顶部渐变细线

```html
<section style="max-width:677px;margin:0 auto;padding:8px 0;box-sizing:border-box;background:#ffffff;color:#2a2e3d;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.85;letter-spacing:0.3px;overflow-x:hidden;">
  <section style="height:3px;background:linear-gradient(90deg,#2e2a6b,#6d4fd6,#00c2b8);margin:0 12px 18px;border-radius:2px;"><span leaf=""><br></span></section>

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 章节标题（靛紫→紫罗兰渐变块 + 青色编号 + 白标题）

> 编号取原文的；原文没有编号就不要编号 `<p>` 和竖分隔线，整块只留标题。第一章 `margin-top` 8px，之后 32px。

```html
<section style="padding:0 12px;">
  <section style="margin:32px 0 16px;background:linear-gradient(115deg,#2e2a6b,#6d4fd6);border-radius:8px;padding:13px 16px;display:flex;align-items:center;">
    <p style="margin:0 12px 0 0;font-size:23px;font-weight:800;color:#00c2b8;line-height:1;flex-shrink:0;"><span leaf="">01</span></p>
    <section style="width:1px;height:26px;background:rgba(255,255,255,0.28);flex-shrink:0;margin-right:12px;"><span leaf=""><br></span></section>
    <p style="margin:0;font-size:16px;font-weight:800;color:#ffffff;line-height:1.5;"><span leaf="">{{章节标题}}</span></p>
  </section>
</section>
```

---

## 组件 3 小节标题（青色序号 + 深色标题 + 底线）

> `margin-top:0`，序号只用原文自带的，没有就删掉序号 `<p>`。

```html
<section style="padding:0 12px;">
  <section style="display:flex;align-items:flex-start;margin:0 0 12px;padding-bottom:8px;border-bottom:1px solid #e2e4f0;">
    <p style="margin:0 8px 0 0;font-size:19px;line-height:1.3;color:#00a89f;flex-shrink:0;"><span leaf="">❶</span></p>
    <p style="margin:0;font-size:16px;font-weight:800;line-height:1.6;color:#16152e;"><span leaf="">{{小节标题}}</span></p>
  </section>
</section>
```

---

## 组件 4 正文段落

```html
<section style="padding:0 12px;">
  <p style="margin:0;font-size:15px;line-height:1.85;text-align:justify;color:#2a2e3d;"><span leaf="">{{正文}}</span></p>
</section>
```

紧接小标题前的最后一段，把 `margin:0` 换成 `margin:0 0 8px`。

---

## 组件 5 行内标记

### 5a 青色荧光下划线（正文关键词默认标记，每段 ≤2 处）

```html
<span style="border-bottom:2px solid #00c2b8;font-weight:600;color:#16152e;box-shadow:0 1px 0 rgba(0,194,184,0.35);"><span leaf="">{{关键词}}</span></span>
```

### 5b 紫罗兰加粗

```html
<span style="font-weight:700;color:#6d4fd6;"><span leaf="">{{加粗}}</span></span>
```

### 5c 浅青荧光笔（只在引用卡 9a 内用）

```html
<span style="font-weight:800;color:#2e2a6b;background:linear-gradient(180deg,transparent 60%,#e6fbf8 60%);"><span leaf="">{{引用里的加粗句}}</span></span>
```

### 5d 收束卡内青色强调（只在收束卡 10 内用，一张卡 ≤1 处）

```html
<span style="font-weight:800;color:#00c2b8;"><span leaf="">{{强调词}}</span></span>
```

---

## 组件 6 列表

### 6a 浅紫底要点列表（普通无序列表）

```html
<section style="padding:0 12px;">
  <section style="background:#f2effc;border-radius:8px;padding:12px 14px;margin:0 0 14px;">
    <section style="display:flex;align-items:flex-start;margin:0 0 6px;">
      <section style="width:6px;height:6px;background:#6d4fd6;border-radius:50%;margin:11px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.8;color:#2a2e3d;text-align:justify;flex:1;"><span leaf="">{{要点一}}</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;margin:0;">
      <section style="width:6px;height:6px;background:#6d4fd6;border-radius:50%;margin:11px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.8;color:#2a2e3d;text-align:justify;flex:1;"><span leaf="">{{最后一条}}</span></p>
    </section>
  </section>
</section>
```

### 6b 青色竖条能力卡（白卡 + 青色左竖条；"节点能做到：/第一，……"这类能力拆解）

```html
<section style="padding:0 12px;">
  <section style="background:#ffffff;border:1px solid #e2e4f0;border-left:3px solid #00c2b8;border-radius:0 8px 8px 0;padding:10px 14px;margin:0 0 10px;">
    <p style="margin:0 0 4px;font-size:15px;font-weight:800;color:#16152e;line-height:1.6;"><span leaf="">{{小标题：}}</span></p>
    <p style="margin:0;font-size:14px;line-height:1.8;color:#2a2e3d;text-align:justify;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 6c 时间线/路线卡（"时间：事件"条目，冒号前做靛紫标签）

```html
<section style="padding:0 12px;">
  <section style="background:#ffffff;border:1px solid #e2e4f0;border-radius:8px;padding:12px 14px 4px;margin:2px 0 14px;">
    <section style="display:flex;align-items:flex-start;margin:0 0 8px;">
      <section style="flex-shrink:0;background:linear-gradient(115deg,#2e2a6b,#6d4fd6);color:#fff;border-radius:4px;padding:2px 8px;margin:3px 10px 0 0;">
        <p style="margin:0;font-size:13px;font-weight:800;line-height:1.6;color:#fff;"><span leaf="">{{2026年Q4：}}</span></p>
      </section>
      <p style="margin:0;font-size:14px;line-height:1.8;color:#2a2e3d;text-align:justify;"><span leaf="">{{事件}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 7 图片容器（整宽圆角，无图注）

```html
<section style="padding:0 12px;">
  <section style="margin:2px 0 16px;line-height:0;">
    <span leaf=""><img src="{{图片URL}}" style="width:100%;height:auto;display:block;border-radius:8px;"></span>
  </section>
</section>
```

---

## 组件 8 引用 / 金句

### 8a 浅青引用卡（浅青底 + 青色竖条；原文 `>` 引用）

```html
<section style="padding:0 12px;">
  <section style="background:#e6fbf8;border-left:4px solid #00c2b8;border-radius:0 8px 8px 0;padding:12px 16px;margin:2px 0 16px;">
    <p style="margin:0;font-size:15px;line-height:1.85;color:#16152e;font-weight:600;text-align:justify;"><span leaf="">{{引用}}</span></p>
  </section>
</section>
```

### 8b 重点观点卡（浅紫底 + 紫罗兰竖条；承上启下的追问/核心判断）

```html
<section style="padding:0 12px;">
  <section style="background:#f2effc;border-left:4px solid #6d4fd6;border-radius:0 8px 8px 0;padding:12px 16px;margin:2px 0 14px;">
    <p style="margin:0;font-size:15px;line-height:1.85;color:#16152e;text-align:justify;font-weight:700;"><span leaf="">{{重点观点}}</span></p>
  </section>
</section>
```

### 8c 居中金句（上下渐变细线）

```html
<section style="padding:0 12px;">
  <section style="border-top:1px solid #e2e4f0;border-bottom:1px solid #e2e4f0;padding:10px 4px;margin:0 0 16px;">
    <p style="margin:0;font-size:15px;line-height:1.9;color:#16152e;font-weight:600;text-align:center;"><span leaf="">{{居中金句}}</span></p>
  </section>
</section>
```

---

## 组件 9 靛紫渐变收束卡（全篇 ≤1 张，带淡紫光晕）

```html
<section style="padding:0 12px;">
  <section style="background:linear-gradient(135deg,#2e2a6b,#6d4fd6);padding:7px;border-radius:10px;margin:2px 0 16px;box-shadow:0 8px 24px -8px rgba(109,79,214,0.45);">
    <section style="border:1px solid rgba(255,255,255,0.18);border-radius:7px;padding:16px 16px;">
      <p style="margin:0 0 6px;font-size:17px;font-weight:800;color:#ffffff;text-align:center;line-height:1.7;letter-spacing:1px;"><span leaf="">{{大字结论}}</span></p>
      <p style="margin:0 0 10px;font-size:14px;color:#d8d4f5;text-align:center;line-height:1.8;"><span leaf="">{{次要说明}}</span></p>
      <section style="width:32px;height:2px;background:#00c2b8;margin:0 auto 10px;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;color:#ffffff;text-align:center;line-height:1.7;"><span leaf="">{{这正是}}</span><span style="font-weight:800;color:#00c2b8;"><span leaf="">{{核心主张}}</span></span><span leaf="">{{存在的意义。}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 10 结尾收束（居中靛紫大字 + 青色短线 + 小字）

```html
<section style="padding:0 12px;">
  <section style="margin:26px 0 8px;text-align:center;">
    <p style="margin:0 0 12px;font-size:20px;font-weight:800;color:#2e2a6b;letter-spacing:2px;line-height:1.6;"><span leaf="">{{收束句}}</span></p>
    <section style="width:40px;height:2px;background:#00c2b8;margin:0 auto 12px;"><span leaf=""><br></span></section>
    <p style="margin:0;font-size:14px;color:#6b7280;letter-spacing:1px;line-height:1.8;"><span leaf="">{{收尾一句}}</span></p>
  </section>
</section>
```

---

## 组件 11 文末免责小字（原文有才放）

```html
<section style="padding:0 12px;">
  <section style="border-top:1px solid #e2e4f0;padding:10px 2px 0;margin:16px 0 0;">
    <p style="margin:0;font-size:12px;line-height:1.7;color:#9ca0b0;text-align:justify;"><span leaf="">{{免责内容}}</span></p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:8px 0;box-sizing:border-box;background:#ffffff;color:#2a2e3d;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.85;letter-spacing:0.3px;overflow-x:hidden;">

  <!-- 1. 顶部渐变细线（组件1） -->

  <!-- 2. 头图（组件7，有头图时）+ 开场段落（组件4，第一章之前的话） -->

  <!-- 3. 第一章（组件2，margin-top 8px） -->
  <!--    章内：组件4 正文 + 3 小节 + 5 行内标记 + 6 列表 + 7 配图 + 8 引用 -->

  <!-- 4. 第二章…第N章（组件2，margin-top 32px）；靛紫收束卡（组件9）全篇最多一张，放在转折处 -->

  <!-- 5. 结尾收束（组件10） -->

  <!-- 6. 文末免责（组件11，原文有才放） -->

</section>
```

**骨架铁律**：没有导读卡/目录卡；章节靠渐变色块分隔，不另加分割线；每张配图放在原稿位置；收束卡全篇唯一，放在"问题讲完、方案登场"的转折处。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 渐变章节块 2 / 渐变收束卡 9 / 结尾靛紫大字 10 | 全文骨架与唯一高潮 | 章节数 + 收束卡 ≤1 + 结尾 1 |
| **标记层** | 青色下划线 5a（默认）/ 紫罗兰加粗 5b | 正文关键词强调 | 每段 ≤2 处 |
| **容器层** | 要点列表 6a / 能力卡 6b / 路线卡 6c / 引用 8a / 重点卡 8b / 居中金句 8c | 结构化信息、引用、金句 | 按原文结构，每章至少 1 个 |

**克制原则**：青色只做下划线、编号、竖条、短线，不做大段正文字色；渐变大色块只有章节标题和一张收束卡；一篇文章点缀组件种类 ≤3；不用四周虚线框；不用 `background-clip:text` 做渐变文字。

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 区块链/分布式网络科普（机制说明） | 章节 2 + 能力卡 6b + 重点观点卡 8b | 居中金句 8c、收束卡 9 |
| 算力/数据基础设施、路线图 | 章节 2 + 时间线卡 6c + 浅紫列表 6a | 能力卡 6b、引用 8a |
| 愿景/趋势评论 | 章节 2 + 正文 4 + 引用 8a + 居中金句 8c | 重点观点卡 8b、收束卡 9 |

所有类型共用：顶部渐变线 1 + 渐变章节 2 + 结尾收束 10。

---

## Markdown → 极光链语 映射规则

| 原文元素 | 对应组件 | 说明 |
|---|---|---|
| `## 01 章节` | 组件 2 渐变章节块 | 编号取原文 |
| `### 小节` | 组件 3 青色序号小节 | `margin-top:0` |
| 普通段落 | 组件 4 | 段后距按铁律 0/8px |
| `**加粗**`（核心观点） | 组件 5a 青色荧光下划线 | |
| `**加粗**`（普通） | 组件 5b 紫罗兰加粗 | |
| `- 列表`（每条"**小标题：**说明"） | 组件 6b 青色竖条能力卡 | |
| `- 列表`（普通） | 组件 6a 浅紫底要点列表 | |
| "时间：事件" 条目 | 组件 6c 时间线卡 | |
| `![](图)` | 组件 7 图片容器 | |
| `> 引用` | 组件 8a 浅青引用卡 | 引用内加粗用 5c |
| 承上启下的追问/核心判断 | 组件 8b 重点观点卡 | |
| 单句金句/排比 | 组件 8c 居中金句 | |
| 全文最重要的一段转折/总结 | 组件 9 靛紫渐变收束卡 | 全篇 ≤1 |
| 文末收束句 | 组件 10 结尾收束 | |
| `本文仅为……` | 组件 11 免责小字 | |

---

## Gotchas

- **不用 `background-clip:text` 做渐变文字**：微信不支持，文字会直接看不见；所有"渐变感"都靠色块背景（`linear-gradient`）或外层 `box-shadow` 光晕实现，文字本身用纯色。
- **青色不做大段正文字色**：只用在下划线、编号、竖条、短线；白底正文里不出现青色字。
- **渐变色块只有两处**：章节标题区和全篇唯一一张收束卡，其余卡片都是浅紫/浅青/白底，避免整篇看起来"花"。
- **`box-shadow` 光晕要淡**：收束卡的光晕 `rgba(109,79,214,0.45)` 已经是上限，不要加深，否则在微信深色模式下会糊成一团。
