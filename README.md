# gzh-design

把一篇 Markdown / Word / PDF / 纯文本文章，排版成**可以直接复制粘贴进微信公众号编辑器、且粘贴后样式不会丢失**的 HTML。内置 6 套原创主题风格（其中「品牌深蓝·蓝图」自带 4 套配色变体，共 9 个可选排版），外加一套随技能自带的**主题图鉴**（`gzh-design/assets/theme-atlas.html`），本地浏览器打开即可逐个预览、一键复制主题指令。全部主题、组件库、示例文章均为原创内容，不含任何第三方代码或素材。

这不是一个"贴进去就能自动排版"的零 AI 小工具，而是一套**给 AI 用的操作手册**：真正干活的是 AI（解析文章结构、挑主题、把每个段落映射成对应的 HTML 组件、主动找关键词加下划线、必要时拆出卡片/引用/金句不让版面显得太素），这个仓库提供的是组件库、骨架、配方表和一个确定性校验脚本，保证不同的 AI 跑出来的排版气质统一、不踩微信编辑器的坑。

## 这不是 Claude 专用的

目录结构是 [Claude Skills](https://docs.claude.com/en/docs/claude-code/skills) 的约定（`SKILL.md` 带 YAML frontmatter + `references/` + `scripts/` + `assets/`），但内容本身只是：

- 纯 Markdown 操作说明（`SKILL.md`、`references/*.md`）——任何能读文件、按说明产出 HTML 的 AI/Agent 都能用，不依赖 Claude 专有能力。
- 两个独立的 Python 脚本（`scripts/component_lint.py` 校验组件库本身、`scripts/validate_gzh_html.py` 校验生成的文章 HTML、`scripts/wrap_preview.py` 包一层带"复制"按钮的预览页）——普通 `python3` 即可运行，没有额外依赖。
- 一个纯前端、零依赖的主题图鉴 HTML（`assets/theme-atlas.html`）——任何浏览器打开都能用，不需要联网、不需要起服务。

如果你用的是别的 Agent 框架（不认 `SKILL.md` frontmatter 这套约定），直接把 `references/` 下的内容当成"组件库文档"喂给模型做上下文即可，核心工作流写在 `SKILL.md` 正文里。

## 快速开始

1. 把 `gzh-design/` 整个目录丢进你的 Agent 技能目录（Claude Code 是 `~/.claude/skills/`，其它框架按各自约定）。
2. 打开 `gzh-design/assets/theme-atlas.html` 挑一套主题风格，复制图鉴给出的那句"公众号排版主题：XXX"。
3. 把你的文章内容 + 这句主题指令一起发给 Agent，让它按 `gzh-design/SKILL.md` 的工作流执行。
4. Agent 产出两份文件：干净的正文 HTML（用于校验/手动粘贴）+ 带「复制」按钮的预览页（浏览器打开点一下，直接粘进公众号编辑器）；并附一段配图提示词，供你丢进任意文生图工具。

## 目录结构

```
gzh-design/
  SKILL.md                     # 工作流主文档：输入归一化 → 选主题 → 读组件库 → 解析结构 → 装配 HTML → 校验 → 输出 → 配图提示词
  references/
    theme-index.md             # 全部主题的单一索引（主色/适用场景/组件库文件/下划线色值）
    theme-*.md                 # 每套主题的完整组件库（设计变量 + 组件 HTML + 骨架 + 配方表 + 映射规则）
    common-components.md       # 代码块/图片GIF/小标签标题——所有主题共用的通用组件
    theme-generator.md         # 自定义主题生成流程（按描述或参考图生成新主题）
    format-normalize.md        # 非 Markdown 输入（docx/pdf/纯文本）归一化规则
    eval-cases.md               # 触发与主题选择的回归用例
  assets/
    theme-atlas.html           # 主题图鉴：本地打开即可预览全部主题 + 配色变体、一键复制主题指令
    theme-previews/            # 自定义主题生成时的区块库预览
  scripts/
    component_lint.py          # 校验组件库源文件本身（0 ERROR 才算合规）
    validate_gzh_html.py       # 校验生成的文章 HTML（禁用标签/leaf 包裹/半角标点）
    wrap_preview.py            # 把干净正文包成带「一键复制」按钮的预览页
  docs/gallery/                # 同一篇示例文章跑全部主题的渲染预览（人工浏览对比用）
```

## 内置主题

| 主题 | 适合文章 |
|---|---|
| 品牌深蓝·蓝图（金/银/铜/青 4 套配色，默认推荐） | 科技/产业品牌的产品、技术科普，尤其配图是深蓝科技风 + 金属色点缀时 |
| 宣纸·朱印 | 文化/历史叙事、有传承或匠心调性的科普、品牌年度总结 |
| 极光链语 | 区块链/分布式网络、算力、数据基础设施、面向未来的愿景类内容 |
| 原石·雅痕 | 品牌故事、企业文化、年度/阶段性总结、高端产品发布（留白最多最克制） |
| 铅字·号外 | 热点快评、行业快讯、数据新闻、周报月报、事件复盘（报纸号外版面，节奏最快） |
| 便笺·手帐 | 新手教程、生活方式、学习笔记、团队日常与活动回顾（唯一一套轻松向主题） |

想要内置主题之外的风格，可以让 Agent 按 `references/theme-generator.md` 的流程，用你的描述或一张参考图现生成一套新主题，登记后与内置主题完全同权。

## 微信公众号平台限制（为什么不能随便写 HTML）

公众号编辑器粘贴时会剥掉大量标签/属性，所有组件库都已经按这套铁律写好：

- **禁止**：`<style>`/`<script>`/`<div>`、`class`/`id` 属性、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量。
- **必须**：样式全部内联 `style`；所有文字节点用 `<span leaf="">文字</span>` 包裹——漏包裹是粘贴后样式整片丢失的头号原因，`validate_gzh_html.py` 会兜底检查。
- **可用**：`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>/<h3>`。

## 关于品牌信息占位符

「品牌深蓝·蓝图」主题里的结尾模块（logo / 二维码 / 商城 / 官网链接）全部是 `{{占位符}}`，需要你换成自己的品牌资产；没有对应素材时按组件库说明整行删掉，不要把占位符留在产物里。

## License

MIT，见 [LICENSE](LICENSE)。
