# 公众号排版组件库 —— 品牌深蓝·蓝图

> **使用说明**：本组件库为「品牌深蓝·蓝图（Brand Blueprint）」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。本主题提供 4 套配色变体（见下方「配色变体」表），结构、组件、骨架完全共用，只替换色值。
>
> **设计风格**：深蓝/藏青底色 + 纯白 + 一个点缀色（默认金色）。深蓝圆角色块做章节标题、点缀色大号编号；正文关键词用亮色下划线；引用用浅色底描边卡，重点收束用一张深色卡。整体像一张"蓝图"：干净、理性、有分量，点缀色只做编号/竖条/短线这类点睛。特别适合配图是**深蓝/科技风 + 金属色点缀**的科技、产业、硬件类产品科普稿——把下方「{{品牌名}}」「{{logo URL}}」「{{二维码 URL}}」等占位替换成你自己的品牌信息即可。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
> - font-size ≤ 24px；正文强调用左竖条/下划线/卡片，**不用四周虚线框**（dashed）
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（顶部双线、章节色块里的竖分隔线、方块项目符号、金色短线）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`；高亮样式统一挂在外层 `<span>` 上，文字放内层 `<span leaf="">`
> - 结构化区域没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
品牌深蓝（主色）：   #020581（章节色块 / 深蓝收束卡 / 结尾大字 / 方块项目符号 / 方案卡竖条）
标题深色：           #0B1033（卡片小标题 / 加粗 / 引导句 / 引用卡正文）
正文色：             #3D4256
次要文字色：         #5B6178（结尾小字）
弱化文字色：         #9AA0B4（免责小字）
细线色：             #D6DCEF（顶部双线下线 / 小节底线 / 白卡描边）
浅蓝线：             #C9D3F5（居中金句上下细线）
浅蓝底：             #EEF2FC（要点列表底 / 方案卡底 / 重点观点卡底）
纯白底：             #FFFFFF
亮蓝（下划线）：     #2F6BFF（正文关键词下划线专用 / 重点观点卡竖条）
金色（点缀）：       #D6A841（章节编号 / 要点卡竖条 / 引用卡竖条 / 金色短线 / 深蓝卡内强调词）
深金（白底上的字）： #A87A1E（小节序号 ❶❷❸，白底上金色字一律用这个，保证可读）
浅金底：             #FBF6EA（引用卡底）
金色荧光：           #F1DCA4（引用卡内荧光笔）
深蓝卡内次要字：     #DFE4F7
正文字号：           15px（卡片说明 14px）
行高：               1.85（容器 1.75）
字间距：             0.5px
最大宽度：           677px
内容区边距：         0 12px（每个组件外包一层 padding:0 12px 的 section）
章节间距：           第一章 margin-top 6px，之后 32px
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

**用色铁律**：点缀色只做"编号、竖条、短线、荧光底、深色卡里的一个词"，**不做白底上的正文字色**（白底用"深点缀色"那一行，保证可读）；亮色下划线只做下划线和重点卡竖条；大面积色块只有章节标题和全篇唯一一张深色收束卡。

---

## 配色变体

同一套组件、同一套骨架，只替换下表对应角色的色值即可切出 4 种气质。选变体后，把下面所有组件 HTML 里出现的对应色值整体替换成该列的值（变量名对应「设计变量速查表」里的角色）。未在表中出现的角色（标题深色 `#0B1033`、正文色 `#3D4256`、次要文字色 `#5B6178`、弱化文字色 `#9AA0B4`、细线色 `#D6DCEF`）4 个变体通用，不需要替换。

| 角色 | 金（默认） | 银灰 | 铜橙 | 青绿 |
|---|---|---|---|---|
| 主色（章节色块/收束卡/方块项目符号/方案卡竖条） | `#020581` | `#0F1B4C` | `#142850` | `#1B3A5C` |
| 亮色下划线（正文关键词/重点观点卡竖条） | `#2F6BFF` | `#5B6FB8` | `#4D6FA8` | `#2FB6A3` |
| 点缀色（编号/竖条/短线/深色卡内强调词） | `#D6A841` | `#B8BDC9` | `#C77B3B` | `#2FB6A3` |
| 深点缀（白底上的点缀字，❶❷❸ 序号） | `#A87A1E` | `#6B7280` | `#8C4A1E` | `#1F8577` |
| 浅点缀底（引用卡底） | `#FBF6EA` | `#F3F4F7` | `#FBF3EA` | `#E9FBF7` |
| 点缀荧光（引用卡内荧光笔渐变终点） | `#F1DCA4` | `#DADDE3` | `#EAC9A8` | `#BDEDE4` |
| 浅主色线（居中金句上下细线） | `#C9D3F5` | `#C7CCDC` | `#CBD3E2` | `#BFE3DC` |
| 浅主色底（要点列表/方案卡/重点观点卡底） | `#EEF2FC` | `#EAF0FA` | `#EDF1F8` | `#E7F6F3` |
| 深色卡内次要字 | `#DFE4F7` | `#D7DAE3` | `#E3D9CC` | `#D7EFEA` |

- **适用气质**：金（默认，暖金点睛，最接近"品牌科技蓝图"原型）；银灰（更冷静、工业感，适合硬件/制造/安全类）；铜橙（比金色更内敛，适合深度评测/机制说明类）；青绿（更贴近互联网/数据科技气质，适合算力/数据/云服务类）。
- 下文所有组件 HTML 默认写的是「金」变体色值；用其它变体时按上表整体替换，组件结构、`<span leaf="">` 包裹、骨架顺序不变。

---

## 组件 1 全局容器 + 顶部双线

```html
<section style="max-width:677px;margin:0 auto;padding:8px 0;box-sizing:border-box;background:#ffffff;color:#3d4256;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">
  <section style="border-top:2px solid #020581;border-bottom:1px solid #d6dcef;height:3px;margin:0 12px 16px;"><span leaf=""><br></span></section>

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 章节标题（深蓝色块 + 金色编号 + 白标题）

> 编号用原文的（01/02、一/二 → 01/02）；原文没有编号就不要编号 `<p>` 和竖分隔线，整块只留标题。原文标题前的装饰符（如 `▎`）属于样式，去掉，由色块承担。第一章 `margin` 顶部 6px，之后 32px。

```html
<section style="padding:0 12px;">
  <section style="margin:32px 0 16px;background:#020581;border-radius:6px;padding:12px 16px;display:flex;align-items:center;">
    <p style="margin:0 12px 0 0;font-size:24px;font-weight:800;color:#d6a841;line-height:1;flex-shrink:0;"><span leaf="">01</span></p>
    <section style="width:1px;height:26px;background:rgba(255,255,255,0.3);flex-shrink:0;margin-right:12px;"><span leaf=""><br></span></section>
    <p style="margin:0;font-size:16px;font-weight:800;color:#ffffff;line-height:1.5;"><span leaf="">{{章节标题}}</span></p>
  </section>
</section>
```

---

## 组件 3 小节标题（`###`，金色序号 + 深色标题 + 底线）

> 序号只用原文自带的（❶❷❸ / 1、2、3 等）；原文没有序号就删掉序号 `<p>`。

```html
<section style="padding:0 12px;">
  <section style="display:flex;align-items:flex-start;margin:22px 0 12px;padding-bottom:8px;border-bottom:1px solid #d6dcef;">
    <p style="margin:0 8px 0 0;font-size:20px;line-height:1.3;color:#a87a1e;flex-shrink:0;"><span leaf="">❶</span></p>
    <p style="margin:0;font-size:16px;font-weight:800;line-height:1.6;color:#0b1033;"><span leaf="">{{小节标题}}</span></p>
  </section>
</section>
```

---

## 组件 4 正文段落

> 不缩进，段后 12px。

```html
<section style="padding:0 12px;">
  <p style="margin:0 0 12px;font-size:15px;line-height:1.85;text-align:justify;color:#3d4256;"><span leaf="">{{正文}}</span></p>
</section>
```

### 4b 引导句（紧跟列表/卡片的"……：" 句）

```html
<section style="padding:0 12px;">
  <p style="margin:0 0 8px;font-size:15px;line-height:1.85;color:#0b1033;font-weight:700;"><span leaf="">{{在 XX 的体系下：}}</span></p>
</section>
```

---

## 组件 5 行内标记

### 5a 亮蓝下划线（标志性标记，正文关键词默认用这个，每段 ≤2 处）

```html
<span style="border-bottom:2px solid #2f6bff;font-weight:600;color:#0b1033;"><span leaf="">{{关键词}}</span></span>
```

### 5b 深色加粗

```html
<span style="font-weight:700;color:#0b1033;"><span leaf="">{{加粗}}</span></span>
```

### 5c 金色荧光笔（只在引用卡 9a / 重点卡 9b 内用）

```html
<span style="font-weight:800;color:#020581;background:linear-gradient(180deg,transparent 62%,#f1dca4 62%);"><span leaf="">{{引用里的加粗句}}</span></span>
```

### 5d 深蓝卡内点缀色强调（只在深蓝收束卡 10 内用，一张卡 ≤1 处）

```html
<span style="font-weight:800;color:#d6a841;"><span leaf="">{{品牌名}}</span></span>
```

---

## 组件 6 列表

### 6a 方块要点列表（浅蓝底 + 深蓝小方块，普通无序列表）

```html
<section style="padding:0 12px;">
  <section style="background:#eef2fc;border-radius:6px;padding:12px 14px;margin:0 0 14px;">
    <section style="display:flex;align-items:flex-start;margin:0 0 6px;">
      <section style="width:6px;height:6px;background:#020581;margin:11px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.8;color:#3d4256;text-align:justify;flex:1;"><span leaf="">{{要点一}}</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;margin:0;">
      <section style="width:6px;height:6px;background:#020581;margin:11px 10px 0 0;flex-shrink:0;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;line-height:1.8;color:#3d4256;text-align:justify;flex:1;"><span leaf="">{{最后一条 margin 为 0}}</span></p>
    </section>
  </section>
</section>
```

### 6b 粗体小标题要点卡（白卡 + 金色左竖条；列表每条都是"**小标题：**说明"时用）

> 多条连排，最后一张 `margin-bottom:14px`，其余 8px。

```html
<section style="padding:0 12px;">
  <section style="background:#ffffff;border:1px solid #d6dcef;border-left:3px solid #d6a841;border-radius:0 6px 6px 0;padding:10px 14px;margin:0 0 8px;">
    <p style="margin:0 0 3px;font-size:15px;font-weight:800;color:#0b1033;line-height:1.6;"><span leaf="">{{打假防伪难：}}</span></p>
    <p style="margin:0;font-size:14px;line-height:1.8;color:#3d4256;text-align:justify;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 6c 路线图 / 时间卡（"时间：事件"条目，冒号前做深蓝标签）

```html
<section style="padding:0 12px;">
  <section style="background:#ffffff;border:1px solid #d6dcef;border-radius:6px;padding:12px 14px 4px;margin:2px 0 14px;">
    <section style="display:flex;align-items:flex-start;margin:0 0 8px;">
      <section style="flex-shrink:0;background:#020581;color:#fff;border-radius:4px;padding:2px 8px;margin:3px 10px 0 0;">
        <p style="margin:0;font-size:13px;font-weight:800;line-height:1.6;color:#fff;"><span leaf="">{{2026年Q4：}}</span></p>
      </section>
      <p style="margin:0;font-size:14px;line-height:1.8;color:#3d4256;text-align:justify;"><span leaf="">{{事件}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 7 卡片

### 7a 方案卡（浅蓝底 + 深蓝竖条；"1. 方案名" + 一段说明，两三种路线/做法并列时用）

```html
<section style="padding:0 12px;">
  <section style="background:#eef2fc;border-left:3px solid #020581;border-radius:0 6px 6px 0;padding:10px 14px;margin:0 0 10px;">
    <p style="margin:0 0 3px;font-size:15px;font-weight:800;color:#020581;line-height:1.6;"><span leaf="">{{1. 重金采购加密芯片}}</span></p>
    <p style="margin:0;font-size:14px;line-height:1.8;color:#3d4256;text-align:justify;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 7b 能力卡（白卡 + 深蓝竖条；"认得准：……""第一，……"这类能力/步骤拆解）

```html
<section style="padding:0 12px;">
  <section style="background:#ffffff;border:1px solid #d6dcef;border-left:3px solid #020581;border-radius:0 6px 6px 0;padding:10px 14px;margin:0 0 10px;">
    <p style="margin:0 0 4px;font-size:15px;font-weight:800;color:#0b1033;line-height:1.6;"><span leaf="">{{认得准：}}</span></p>
    <p style="margin:0;font-size:14px;line-height:1.8;color:#3d4256;text-align:justify;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

---

## 组件 8 图片容器（整宽圆角，无图注）

> 公众号自制正文配图可在左上合成自己的品牌横版 Logo（可选）。容器不加边框。正文图用微信图床地址（`mmbiz.qpic.cn`）；从已发文章复制来的地址去掉 `&watermark=1&tp=webp…#imgIndex=N`。

```html
<section style="padding:0 12px;">
  <section style="margin:2px 0 16px;line-height:0;">
    <span leaf=""><img src="{{图片URL}}" style="width:100%;height:auto;display:block;border-radius:6px;"></span>
  </section>
</section>
```

---

## 组件 9 引用 / 金句

### 9a 金边引用卡（浅金底 + 金色竖条；原文 `>` 引用、原稿里橙色/彩色的引用段）

> 多行时每行一个 `<p>`，最后一个 `margin:0`。引用里的加粗用 5c 金色荧光笔。

```html
<section style="padding:0 12px;">
  <section style="background:#fbf6ea;border-left:4px solid #d6a841;border-radius:0 6px 6px 0;padding:12px 16px;margin:2px 0 16px;">
    <p style="margin:0 0 4px;font-size:15px;line-height:1.85;color:#0b1033;font-weight:600;text-align:justify;"><span leaf="">{{引用第一行}}</span></p>
    <p style="margin:0;font-size:15px;line-height:1.85;color:#0b1033;font-weight:600;text-align:justify;"><span style="font-weight:800;color:#020581;background:linear-gradient(180deg,transparent 62%,#f1dca4 62%);"><span leaf="">{{加粗的那句}}</span></span></p>
  </section>
</section>
```

### 9b 重点观点卡（浅蓝底 + 亮蓝竖条；承上启下的追问/核心判断，单句加粗）

```html
<section style="padding:0 12px;">
  <section style="background:#eef2fc;border-left:4px solid #2f6bff;border-radius:0 6px 6px 0;padding:12px 16px;margin:2px 0 14px;">
    <p style="margin:0;font-size:15px;line-height:1.85;color:#0b1033;text-align:justify;font-weight:700;"><span leaf="">{{重点观点}}</span></p>
  </section>
</section>
```

### 9c 深蓝竖条提示（浅蓝底 + 深蓝竖条；"但……的回答是：" 这类转折结论）

```html
<section style="padding:0 12px;">
  <section style="background:#eef2fc;border-left:3px solid #020581;border-radius:0 6px 6px 0;padding:10px 16px;margin:2px 0 14px;">
    <p style="font-size:15px;font-weight:800;color:#0b1033;margin:0;line-height:1.8;"><span leaf="">{{提示}}</span></p>
  </section>
</section>
```

### 9d 居中金句 / 排比（上下浅蓝细线；单句金句，或两三句排比各占一行）

```html
<section style="padding:0 12px;">
  <section style="border-top:1px solid #c9d3f5;border-bottom:1px solid #c9d3f5;padding:10px 4px;margin:0 0 16px;">
    <p style="margin:0;font-size:15px;line-height:1.9;color:#0b1033;font-weight:600;text-align:center;"><span leaf="">{{从田间地头……；}}</span></p>
    <p style="margin:0;font-size:15px;line-height:1.9;color:#0b1033;font-weight:600;text-align:center;"><span leaf="">{{从一张……。}}</span></p>
  </section>
</section>
```

---

## 组件 10 深蓝收束卡（全篇 ≤1 张）

> 放在"问题讲完、方案登场"的转折处或全文总结句。三行版：大字结论 → 次要说明 → 金色短线 → 收尾一句（可含 5d 金色强调词）。只有一句话时删掉中间两行和短线。

```html
<section style="padding:0 12px;">
  <section style="background:#020581;padding:7px;border-radius:6px;margin:2px 0 16px;">
    <section style="border:1px solid rgba(255,255,255,0.16);border-radius:4px;padding:16px 16px;">
      <p style="margin:0 0 6px;font-size:17px;font-weight:800;color:#ffffff;text-align:center;line-height:1.7;letter-spacing:1px;"><span leaf="">{{大字结论}}</span></p>
      <p style="margin:0 0 10px;font-size:14px;color:#dfe4f7;text-align:center;line-height:1.8;"><span leaf="">{{次要说明}}</span></p>
      <section style="width:32px;height:2px;background:#d6a841;margin:0 auto 10px;"><span leaf=""><br></span></section>
      <p style="margin:0;font-size:15px;color:#ffffff;text-align:center;line-height:1.7;"><span leaf="">{{这正是}}</span><span style="font-weight:800;color:#d6a841;"><span leaf="">{{品牌名}}</span></span><span leaf="">{{诞生的初衷。}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 11 结尾收束（居中深蓝大字 + 金色短线 + 小字）

> 原文末尾的口号句 + 紧随的一句收尾。只有口号句时删掉最后的小字 `<p>`。

```html
<section style="padding:0 12px;">
  <section style="margin:26px 0 8px;text-align:center;">
    <p style="margin:0 0 12px;font-size:20px;font-weight:800;color:#020581;letter-spacing:2px;line-height:1.6;"><span leaf="">{{让数据可信，让实体受尊重。}}</span></p>
    <section style="width:40px;height:2px;background:#d6a841;margin:0 auto 12px;"><span leaf=""><br></span></section>
    <p style="margin:0;font-size:14px;color:#5b6178;letter-spacing:1px;line-height:1.8;"><span leaf="">{{收尾一句}}</span></p>
  </section>
</section>
```

---

## 组件 12 文末免责小字（原文有才放）

```html
<section style="padding:0 12px;">
  <section style="border-top:1px solid #d6dcef;padding:10px 2px 0;margin:16px 0 0;">
    <p style="margin:0;font-size:12px;line-height:1.7;color:#9aa0b4;text-align:justify;"><span leaf="">{{本文仅为产业技术科普与品牌展示，不构成任何投资建议或收益承诺。}}</span></p>
  </section>
</section>
```

---

## 组件 13 品牌结尾块（标签 / 商城 / 官网 / logo / 二维码，占位，按你自己的品牌信息填）

> 固定结尾，所有主题通用的样式。原稿自带结尾图就用原稿的图床地址；没有对应素材的行**整行删掉**，不要把占位符留在产物里：
> - 标签行：`#{{品牌名}}#{{本篇话题标签}}#{{公司/账号名}}`
> - 商城/官网行：按你自己的链接填，没有就删掉对应 `<p>`
> - logo / 二维码：替换成你自己的图床地址，没有就删掉对应 `<section>`

```html
<section style="height:1px;background:#E5E7EB;margin:32px 12px 24px;"><span leaf=""><br></span></section>
<section style="padding:0 12px;">
  <p style="font-size:14px;line-height:1.8;margin:0 0 8px;color:#576B95;"><span leaf="">#{{品牌名}}#{{标签}}#{{公司/账号名}}</span></p>
  <p style="font-size:14px;line-height:1.8;margin:0 0 4px;color:#2B59E8;font-style:italic;"><span leaf="">{{商城名}}: {{商城链接}}</span></p>
  <p style="font-size:14px;line-height:1.8;margin:0 0 16px;color:#2B59E8;font-style:italic;"><span leaf="">{{官网名}}: {{官网链接}}</span></p>
  <section style="margin:0 0 12px;"><span leaf=""><img src="{{logo URL}}" style="max-width:80%;height:auto;display:block;margin:0 auto;"></span></section>
  <section style="margin:0 0 12px;"><span leaf=""><img src="{{二维码 URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span></section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:8px 0;box-sizing:border-box;background:#ffffff;color:#3d4256;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 顶部双线（组件1） -->

  <!-- 2. 头图（组件8，有头图时）+ 开场段落（组件4，第一章之前的话） -->

  <!-- 3. 第一章（组件2，margin-top 6px） -->
  <!--    章内：组件4 正文 + 3 小节 + 5 行内标记 + 6 列表 + 7 卡片 + 8 配图 + 9 引用 -->

  <!-- 4. 第二章…第N章（组件2，margin-top 32px）；深蓝收束卡（组件10）全篇最多一张，放在转折处 -->

  <!-- 5. 结尾收束（组件11） -->

  <!-- 6. 文末免责（组件12，原文有才放） -->

  <!-- 7. 品牌结尾块（组件13） -->

</section>
```

**骨架铁律**：没有引言卡、导读卡、作者签名区、英文标签（成稿零改动，不新增文案）；章节靠深蓝色块分隔，不另加分割线；每张配图放在原稿的位置（一般是章节标题后或章末引用前）。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 深蓝章节色块 2 / 深蓝收束卡 10 / 结尾深蓝大字 11 | 全文骨架与唯一高潮 | 章节数 + 收束卡 ≤1 + 结尾 1 |
| **标记层** | 亮蓝下划线 5a（默认）/ 深色加粗 5b / 金色荧光 5c（仅卡内） | 正文关键词强调 | 每段 ≤2 处 |
| **容器层** | 要点列表 6 / 方案卡、能力卡 7 / 金边引用 9a / 重点卡 9b / 提示 9c / 居中金句 9d | 结构化信息、引用、金句 | 按原文结构 |

**克制原则**：
- 金色只做编号、竖条、短线、荧光底和深蓝卡里的一个词，白底正文里不出现金色字
- 深蓝大色块只有章节标题和一张收束卡，其余卡片都是浅蓝/浅金/白底
- 一篇文章点缀组件种类 ≤3（例如：要点卡 6b + 金边引用 9a + 居中排比 9d）
- 不用四周虚线框；强调一律左竖条或下划线

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 科技/产业品牌科普（痛点 → 方案 → 愿景） | 章节 2 + 要点卡 6b（痛点）+ 方案卡 7a + 小节 3（❶❷❸ 解法）+ 方块列表 6a | 金边引用 9a、深蓝收束卡 10、结尾收束 11 |
| 技术拆解 / 安全机制说明 | 章节 2 + 能力卡 7b + 重点观点卡 9b + 提示 9c | 居中金句 9d、深蓝收束卡 10 |
| 路线图 / 进展 / 活动稿 | 章节 2 + 路线图 6c + 方块列表 6a | 能力卡 7b、金边引用 9a |
| 观点 / 趋势评论 | 章节 2 + 正文 4 + 金边引用 9a + 居中金句 9d | 重点观点卡 9b、深蓝收束卡 10 |

所有类型共用：顶部双线 1 + 深蓝章节 2 + 结尾收束 11（原文有口号句时）+ 品牌结尾块 13。

---

## Markdown / 原稿 → 品牌深蓝·蓝图 映射规则

| 原文元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号标题在平台设置 |
| `## 01 章节` / 原稿 `▎01标题` | 组件 2 深蓝章节色块 | 编号取原文；`▎` 这类装饰符去掉 |
| `### ❶ 小节` | 组件 3 金色序号小节 | 序号取原文，没有就不加 |
| 普通段落 | 组件 4 | |
| 以"：" 结尾、后面紧跟列表的句子 | 组件 4b 引导句 | |
| `**加粗**`（原稿蓝色/彩色加粗） | 组件 5a 亮蓝下划线 | |
| `**加粗**`（普通） | 组件 5b 深色加粗 | |
| `- 列表`（每条"**小标题：**说明"） | 组件 6b 金色竖条要点卡 | |
| `- 列表`（普通） | 组件 6a 方块要点列表 | |
| "时间：事件" 条目 | 组件 6c 路线图 | |
| `**1. 方案名**` + 说明段 | 组件 7a 方案卡 | "1." 原样保留在标题里 |
| "认得准：/第一，" 开头的能力段 | 组件 7b 能力卡 | 冒号或首句做卡片标题 |
| `![](图)` | 组件 8 图片容器 | |
| `> 引用`（原稿橙色/彩色引用） | 组件 9a 金边引用卡 | 引用内加粗用 5c |
| 承上启下的追问 / 核心判断 | 组件 9b 重点观点卡 | |
| 转折结论（"但……的回答是"） | 组件 9c 深蓝竖条提示 | |
| 单句金句 / 两三句排比 | 组件 9d 居中金句 | |
| 全文最重要的一段转折/总结 | 组件 10 深蓝收束卡 | 全篇 ≤1 |
| 文末口号句 + 收尾句 | 组件 11 结尾收束 | |
| `本文仅为……` | 组件 12 免责小字 | |
| `#标签` / 商城 / 官网 / logo / 二维码 | 组件 13 品牌结尾块 | |
