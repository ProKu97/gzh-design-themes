# 通用组件库 —— 代码块 / 图片 / 强调标签

> 这些组件和具体主题无关，任何主题排版时都可能用到：代码/命令片段、图片与 GIF、以及"给一段内容起个小标题或强调它"这件事本身。主题专属的章节标题、引用卡、收束卡等，读对应主题自己的组件库文件。
>
> **换色方式**：下面示例统一用品牌深蓝·蓝图的色值（主色 `#020581`、浅底 `#EEF2FC`、浅标底 `#FBF6EA`、深字 `#0B1033`）打样。套到别的主题时，把这几个颜色换成该主题"设计变量速查表"里对应的角色即可，组件结构不用变。
>
> **平台红线同主题库**：不能出现 `<style>/<script>/class/id/<div>/position/float/@media/display:grid`；只能用内联 `style` 和有限的 `flex`；每个文字节点都要包在 `<span leaf="">` 里。

---

## 代码 / 命令片段

文章里出现的代码、终端命令、Prompt、配置样例，一律走这里，不要塞进普通段落或引用块——那样会丢失等宽字体和缩进。

### 深色代码块（默认）

```html
<section style="margin:0 0 20px;border-radius:8px;overflow:hidden;background:#1E293B;box-shadow:0 4px 16px -8px rgba(15,23,42,0.4);">
  <section style="display:flex;align-items:center;padding:9px 14px;background:#0F172A;">
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#FF5F56;margin-right:7px;"><span leaf=""><br></span></span>
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#FFBD2E;margin-right:7px;"><span leaf=""><br></span></span>
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#27C93F;"><span leaf=""><br></span></span>
    <span style="margin-left:12px;font-size:12px;color:#64748B;font-family:Consolas,Monaco,monospace;letter-spacing:1px;"><span leaf="">{{语言名}}</span></span>
  </section>
  <section style="padding:11px 14px;">
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">{{第一行代码}}</span></p>
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">{{第二行代码}}</span></p>
  </section>
</section>
```

写法上有几条硬性要求，踩了坑才知道有多重要：

1. 顶栏三个圆点模拟终端窗口，配一个语言名标签；没有明确语言就删掉那个 `<span>`。
2. **逐行一个 `<p style="margin:0">`，绝不要 `white-space:pre`**——`pre` 会把源码里 span 前面的缩进和换行原样渲染出来，变成一大片空白加左缩进。
3. 需要表示缩进时，在文字里直接打全角空格 `　`，不要依赖源码里的半角空格。
4. 行距只交给 `line-height:1.6`，`padding` 固定 `11px 14px`，别再额外加空行撑高度。

### 浅色代码块（配色偏浅的主题用这个，深色块太重）

```html
<section style="margin:0 0 20px;border-radius:8px;overflow:hidden;background:#F6F8FA;border:1px solid #E5E7EB;border-left:3px solid #020581;">
  <section style="padding:7px 14px;border-bottom:1px solid #E5E7EB;">
    <span style="font-size:12px;color:#9CA3AF;font-family:Consolas,Monaco,monospace;letter-spacing:1px;"><span leaf="">{{语言名}}</span></span>
  </section>
  <section style="padding:11px 14px;">
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#24292F;"><span leaf="">{{命令}}</span></p>
  </section>
</section>
```

左竖条颜色换成当前主题主色；多行规则和深色版一致：一行一个 `<p>`，不用 `pre`，缩进用全角空格。

### 行内代码

```html
<span style="background:#F1F5F9;color:#020581;padding:1px 6px;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:14px;"><span leaf="">{{code}}</span></span>
```

文字颜色换成主题主色，底色保持中性浅灰不变。

---

## 图片与 GIF

每一处原文的图片、截图、动图占位都要转换，不能漏；`src` 保留原文给的地址（URL 或相对路径）。GIF 和普通图片都用 `<img>`（微信原生支持 GIF 自动播放），区别只在要不要加"动图"角标。

### 带说明文字的图片

```html
<section style="background:#FFFFFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.08);margin:0 0 8px;">
  <section style="border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="{{图片URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;"><span leaf="">{{图片说明}}</span></p>
```

原文没有说明文字就删掉下面那个 `<p>`，并把图片容器的 `margin` 改回 `0 0 10px`——**不要替用户编一句说明出来**。

图片尺寸固定用 `max-width:100%;height:auto;display:block;margin:0 auto`：按原图尺寸显示并居中，大图自动缩到容器宽、小图保持原样。千万不要写 `width:100%`，那会把本来就小的图强行拉伸变糊。

### 动图（GIF）

```html
<section style="background:#FFFFFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.08);margin:0 0 8px;">
  <section style="border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="{{动图URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
<p style="text-align:center;margin:0 0 24px;">
  <span style="display:inline-block;background:#FBF6EA;color:#0B1033;font-size:11px;font-weight:700;padding:1px 8px;border-radius:4px;margin-right:6px;"><span leaf="">GIF</span></span>
  <span style="font-size:12px;color:#9CA3AF;"><span leaf="">{{动图说明}}</span></span>
</p>
```

角标底色/字色换成当前主题的浅底色/深字色；如果所选主题是不用色块的极简风格，角标改成细描边胶囊（边框和字都用主题主色，背景透明）会更贴合气质。原文只提到"这里有图"但没给地址时，用 `{{图片URL}}` 占位并在交付时提醒用户自己补上，不要凭空造一个图床链接。

### 待补素材占位（居中板块）

原文里"【插入xxx】"、待录屏、待补 GIF/视频/截图这类占位，统一用下面这个居中板块，不要用左对齐的提示条：

```html
<section style="margin:0 0 24px;padding:30px 20px;border:1.5px dashed #DAD7D2;border-radius:14px;background:#FAFAF8;text-align:center;">
  <p style="margin:0 0 10px;font-size:26px;line-height:1;"><span leaf="">🎬</span></p>
  <p style="margin:0;font-size:14px;font-weight:700;color:#9CA3AF;letter-spacing:1px;"><span leaf="">待补素材</span></p>
  <p style="margin:8px 0 0;font-size:13px;color:#B8B5B0;line-height:1.7;"><span leaf="">{{待补内容说明}}</span></p>
</section>
```

- 图标按素材类型换：🎬 视频/录屏、🖼 图片、📊 信息图、📎 附件。
- **这是唯一允许用虚线框（`dashed`）的地方**——它表达的是"这里还没做"，和正文强调的虚线滥用是两回事。
- 虚线色和底色可以按主题微调成中性色，但始终居中、留白、不抢眼。

---

## 强调与小标题（不用虚线框）

要给一段内容起个小标题或突出它时，优先用下面这几种"小标签 / 左竖条"形式，**不要用四周虚线框把标题圈起来**——那样又重又抢戏。

先查所选主题自己的组件库：如果主题已经有等价的金句块/提示块/小标题组件，优先用主题自己那套保持气质统一；主题没有对应组件时，才用这里的通用版本，并把下面的颜色按当前主题替换：

- 左竖条、药丸底色 → 主题主色（药丸内文字保持白色）
- 序号药丸底色 → 主题浅底色，序号文字色 → 主题深字色
- 金句/提示块的底色、竖条色 → 主题浅底色 / 主题主色
- 不用色块的极简主题：竖条细化到 `2–3px`，金句/提示块去掉底色、只留竖条和更大的留白

### 左竖条小标题（默认首选，最干净）

```html
<p style="margin:28px 0 14px;font-size:16px;font-weight:800;color:#0B1033;line-height:1.5;border-left:4px solid #020581;padding-left:12px;"><span leaf="">{{小标题}}</span></p>
```

### 实色药丸标题（最醒目，用于真正重要的分节）

```html
<p style="margin:28px 0 14px;">
  <span style="display:inline-block;background:#020581;color:#FFFFFF;font-size:14px;font-weight:700;padding:5px 16px;border-radius:6px;"><span leaf="">{{小标题}}</span></span>
</p>
```

### 序号药丸 + 标题（清单/步骤场景）

```html
<p style="margin:24px 0 12px;font-size:15px;font-weight:800;color:#0B1033;line-height:1.6;">
  <span style="display:inline-block;background:#FBF6EA;color:#0B1033;border-radius:5px;padding:1px 9px;margin-right:8px;font-weight:900;"><span leaf="">01</span></span><span leaf="">{{要点标题}}</span>
</p>
```

### 金句块（左竖条版）

```html
<section style="margin:0 0 24px;background:#EEF2FC;border-radius:0 10px 10px 0;border-left:4px solid #020581;padding:16px 20px;">
  <p style="font-size:16px;font-weight:800;color:#0B1033;margin:0;line-height:1.8;"><span leaf="">{{核心金句}}</span></p>
</section>
```

### 提示 / 旁注块

```html
<section style="margin:0 0 24px;background:#EEF2FC;border-radius:0 8px 8px 0;border-left:4px solid #020581;padding:14px 18px;">
  <p style="margin:0 0 6px;"><span style="display:inline-block;background:#020581;color:#FFFFFF;font-size:11px;font-weight:700;padding:2px 10px;border-radius:4px;letter-spacing:1px;"><span leaf="">提示</span></span></p>
  <p style="font-size:14px;color:#3D4256;margin:0;line-height:1.8;"><span leaf="">{{提示内容}}</span></p>
</section>
```

标签文字可以换成"注意 / 重点 / Prompt / 旁注"等，整块都没有虚线框，靠左竖条 + 浅底 + 小标签分层。

---

## 速查表

| 原文出现 | 用哪个组件 |
|---|---|
| 代码/命令/Prompt 围栏 | 深色代码块（默认）或浅色代码块（浅色主题） |
| 行内 `code` | 行内代码 |
| `![](图片)` | 带说明/无说明的图片 |
| `![](xxx.gif)` 或明确标注的动图 | 动图（GIF） |
| 想起一个小标题 / 强调一段 | 左竖条（首选）/ 实色药丸 / 序号药丸 |
| 金句引用 | 金句块 |
| 提示 / 注意 / 旁注 | 提示块（不要虚线框） |
| 待录屏/待配图/待补素材占位 | 居中占位板块 |
