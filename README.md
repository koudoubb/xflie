# Xflie · 帖子转动态视频卡片

**中文** · 将 X / Twitter 帖子的核心内容转为自然简体中文动态竖版视频卡片：HTML/CSS 动画、真实案例媒体、女性口播、字幕及同规格封面。后台发布仅在用户明确授权后进行。

**English** · An agent skill that turns the core content of X / Twitter posts into vertical motion cards with natural Simplified Chinese narration, HTML/CSS animation, real example media, subtitles, and matching covers. Publishing requires explicit user authorization.

## 安装 · Installation

下载本仓库中的 **`xflie-public.zip`** 并解压，将其中的 `xflie/` 文件夹复制到代理的技能目录。Codex 可使用 `~/.codex/skills/xflie/`。确认 `SKILL.md` 位于该文件夹第一层，再重新载入技能。

Download **`xflie-public.zip`** from this repository, extract it, and copy the enclosed `xflie/` folder into your agent's skills directory. For Codex, use `~/.codex/skills/xflie/`. Keep `SKILL.md` at the top level of the skill folder, then reload skills.

也可以下载整个仓库，将含 `SKILL.md` 的目录重命名为 `xflie` 后安装。

Alternatively, download the repository and install the directory containing `SKILL.md` as `xflie`.

## 新人引导 · Quick start

```text
使用 $xflie，把这个 X 帖子的核心内容做成中文动态视频卡片。
先给我确认中英混合标题和完整口播稿，确认后再制作。
帖子链接：<粘贴链接>
```

```text
Use $xflie to turn this X post's core content into a vertical motion card
with natural Simplified Chinese narration. Ask me to approve the bilingual
title and full narration script before producing any media.
Post URL: <paste URL>
```

如需代发，另行明确后台入口、分类、作者、AI内容标记和是否公开发布。不要把凭据写进共享文件。

For assisted publishing, specify the admin site, category, author, AI-content disclosure, and whether to publish publicly. Never place credentials in shared files.

## 交付规格 · Deliverables

| 项目 / Item | 默认规格 / Default |
| --- | --- |
| 视频 / Video | 1080×1920 · 9:16 · 30fps · H.264/AAC MP4 |
| 封面 / Cover | 同尺寸PNG，大标题中英文混合、真实案例为主体 / Matching PNG with a bilingual headline and prominent real examples |
| 安全区 / Safe area | 居中3:4，重要内容进一步内缩 / Centered 3:4 area with additional inner padding |
| 口播 / Narration | 自然中文女性声线 / Natural female voice in Simplified Chinese |
| 字幕 / Subtitles | 白字黑边，最多两行，按语义分段 / White text with a black outline, at most two lines, semantic segmentation |
| 工程 / Source | 可编辑HTML/CSS工程及SRT字幕 / Editable HTML/CSS project and SRT subtitles |

- 主题色跟随案例；有视频则嵌入真实视频，有图片则使用真实图片。 / Use the example's visual palette; include actual videos or images rather than unrelated substitutes.
- 去除头像、作者、点赞数等无关社交信息。 / Exclude avatars, social author metadata, engagement counts, and unrelated platform UI.
- 后台来源字段填“网络”或社交媒体名称，不填具体链接。 / Use “Web” or the social platform name in the publishing source field, not a specific post URL.

## 运行前提 · Requirements

这是供代理执行的工作流技能，**不是独立的一键视频生成软件**。仓库不含原帖媒体或完整渲染项目。

This is an agent workflow skill, **not a standalone one-click video generator**. It does not bundle source-post media or a complete rendering project.

- 可用的浏览器及访问权限；使用ego-browser时先安装并读取配套技能。 / A browser tool and legitimate access; install and read the companion skill if using ego-browser.
- HTML/CSS渲染与视频导出环境；使用HyperFrames时读取其技能和当前CLI合同。 / An HTML/CSS rendering and video export environment; read the current HyperFrames skill and CLI contract if using it.
- 中文语音合成工具及相应授权，密钥由使用者自行配置。 / A Chinese text-to-speech tool with appropriate authorization and user-configured credentials.
- Python 3、FFmpeg/ffprobe。 / Python 3 and FFmpeg/ffprobe.
- 发布后台是可选项，无授权时仅交付文件。 / Publishing is optional; without authorization, deliver local files only.

## 参数检查 · Media verification

```bash
python3 scripts/verify_media.py /path/to/video.mp4 /path/to/cover.png
```

脚本检查基础媒体参数。视觉、安全区、字幕、声音自然度及发布结果仍需按技能核验。

The script checks basic media parameters. Visual quality, safe areas, subtitle segmentation, voice quality, and publishing outcomes still require the workflow's additional checks.

使用原帖媒体前确认版权、许可和使用范围；不绕过登录或访问限制。

Check copyright, licensing, and permitted use before reusing media. Do not bypass login or access restrictions.

## 结构 · Layout

```text
SKILL.md                   代理工作流 / Agent workflow
agents/openai.yaml         展示信息 / UI metadata
references/publishing.md   通用后台经验 / Generic publishing guidance
scripts/verify_media.py    媒体参数检查 / Media parameter checker
```

## 隐私与脱敏 · Privacy and sanitization

公开版已移除个人称呼、指定作者、私人后台域名、个人分类/AI标记偏好、案例发布记录及本机路径。未打包账号密码、会话资料、后台截图、原帖媒体或私人项目。本地个人版不受影响。

The public edition removes personal names, assigned authors, private admin domains, personal category/AI-label defaults, publication records, and local machine paths. It excludes credentials, session data, admin screenshots, original post media, and private projects. The local personalized edition is unchanged.
