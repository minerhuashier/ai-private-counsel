# 证据收集的技术、方法与指导原则：从页面到可核验证据链

# Technology, Methods, and Guiding Principles for Evidence Collection: From Page Capture to a Verifiable Evidence Chain

- 版本：`0.1.0`
- 状态：公开方法总览
- 配套文档：[《从一段叙述到可核验证据链：AI 协助取证的五个关口》](evidence-collection-playbook.md)

> 技术回答“怎样采集、保存、数字化和复核”；原则回答“什么可以做、什么时候必须停下来”。
>
> Technology answers how to capture, preserve, digitize, and review. Principles answer what may be done and when the process must stop.

本文不是法律意见，也不主张任何截图、OCR、录音转写、哈希或 AI 整理结果具有公证、司法鉴定、证据保全或当然可采的效力。本文只总结项目实际采用的技术组合、操作方法和安全边界。

This document is not legal advice. It does not claim that screenshots, OCR, audio transcripts, hashes, or AI-organized material have the effect of notarization, forensic examination, judicial evidence preservation, or automatic admissibility. It summarizes the technical combination, operating methods, and safety boundaries actually used in this project.

---

## 中文

## 结论先行

AI 辅助取证不是“让 AI 自动找到证据”，而是一条由多种技术共同支撑的可核验链条：

- 先用 AI 把争议叙述拆成待证事实和建议证据清单；
- 由用户本人完成登录、身份验证和明确授权；
- 在只读范围内使用浏览器连续查看、截图并保存页面状态；
- 保存原件、页面固定件和导出文件，计算 SHA-256；
- 使用 OCR、本地转写和 Markdown 建立可检索派生物；
- 通过索引、时间线和交叉核对连接多份材料；
- 最后回到官方法律文本，用构成要件反查事实、证据、冲突和缺口。

任何一个环节只能解决一个问题。截图不等于完整后台记录，哈希不等于内容真实，OCR 不等于原文，转写不等于录音，AI 摘要更不等于证据。技术的价值是提高可追溯性，而不是制造“看起来很确定”的结论。

## 一、技术清单

项目实际使用的技术可以分为四层。

### 1. 访问与抓取层

| 技术或工具 | 实际作用 | 主要产出 | 证明边界 |
| --- | --- | --- | --- |
| 大语言模型辅助拆解叙述 | 把“发生了什么”转成待证事实、材料来源、控制方和缺口 | 建议证据清单、取证问题、优先级 | 只是计划，不是事实认定，也不是证据 |
| 用户本人登录的应用内浏览器或系统浏览器 | 在用户已有会话中打开订单、聊天、工单和规则页面 | 可观察的页面、导航路径和操作记录 | AI 不接触密码、验证码或 Cookie；登录成功本身不证明页面内容真实 |
| 连续截图与页序记录 | 固定某一时间范围内页面实际显示的内容 | 截图、页码、消息序、时间范围 | 只能证明截图时点的显示状态，不能替代平台数据库导出 |
| 页面标题、最终位置和页面数据快照 | 保留页面上下文、文本结构和当时状态 | HTML、JSON、文本快照、最终 URL 或脱敏占位符 | 页面快照不是后台日志，也不能证明未显示事件从未发生 |
| 原始文件读取与导出 | 保留用户已有的 PDF、图片、录音、付款凭证和导出材料 | 未经修改的原始文件副本 | 文件存在不等于来源真实；仍需核验取得过程和原始载体 |

### 2. 完整性与保管层

| 技术或工具 | 实际作用 | 主要产出 | 证明边界 |
| --- | --- | --- | --- |
| 原件只读保存 | 防止裁剪、转码、改名或格式转换覆盖源文件 | 原始文件、只读备份、保管位置 | 备份不能替代对原始载体和取得过程的说明 |
| 稳定编号与命名 | 把证据、页面、文件和派生物建立稳定关系 | `evidence_id`、`capture_id`、文件编号 | 文件名不是证据本身，必须与台账和哈希共同使用 |
| SHA-256 哈希 | 检查两个文件是否在字节层面一致，发现后续替换或损坏 | 文件哈希清单、校验结果 | 哈希只能证明文件一致，不能证明内容真实、来源合法或陈述正确 |
| 操作日志 | 记录谁在何时、通过什么通道、读取或处理了什么 | 运行记录、时间、通道、范围、停止原因 | AI 生成的日志仍需用户核对，不能自动成为事实 |
| 私有区与公开区隔离 | 防止真实材料、个人信息和案件附件进入公开仓库 | 私有原件、脱敏公开副本、安全检查结果 | 自动扫描不能代替人工脱敏和法律判断 |

### 3. 数字化与结构化层

| 技术或工具 | 实际作用 | 主要产出 | 证明边界 |
| --- | --- | --- | --- |
| Markdown 规范化 | 把聊天、页面、文件和转写整理成可检索、可版本比较的文本 | 带来源链接和稳定编号的 Markdown | Markdown 是派生物，不是新原件，不能覆盖原文中的错误和缺失 |
| OCR 加逐张视觉复核 | 从截图中提取文字，再由人回看重要字段 | OCR 文本、复核标记、差异记录 | OCR 存在误识别；未经复核的文本不能当作截图原文 |
| 本地离线录音转写 | 在不把原始录音上传外部服务的情况下生成带时间戳文本 | 转写稿、时间戳、关键片段索引 | 机器转写可能有同音字、漏字和语序错误；正式引用前必须回听 |
| 分页索引与时间线 | 把多条消息、截图和事件按顺序组织 | 页码索引、消息序号、事件时间线 | 时间线帮助理解，不自动证明因果关系或责任 |
| 字段化与证据矩阵 | 把金额、时间、主体、页面状态、证明目的和缺口结构化 | 结构化清单、法律要件与证据矩阵 | 字段完整不等于事实成立，仍需原件和规范双重核验 |
| 冲突登记 | 保留不同页面或文件之间的不一致，禁止靠猜测消除 | `SOURCE_CONFLICT` 记录、待核实事项 | 冲突记录本身不解决冲突，可能需要原始记录或调查取证 |

### 4. 核验与法律映射层

| 技术或工具 | 实际作用 | 主要产出 | 证明边界 |
| --- | --- | --- | --- |
| 官方法律来源登记 | 核对法规名称、条号、版本、施行时间和官方文本 | 来源登记、官方链接、存档文件和哈希 | 搜索摘要、二手文章和模型记忆不能替代官方文本 |
| 法律要件反查 | 从争议问题和规范要件反查待证事实与证据 | “问题—规范—要件—事实—证据—缺口”矩阵 | 矩阵是研究工具，不是法院裁判，也不保证证明力 |
| AI 辅助一致性检查 | 比较多个版本、日期、主体、金额和引用，定位前后矛盾 | 矛盾清单、待确认问题、复核任务 | 发现矛盾不等于判断哪一方正确，必须回到来源 |
| 公开安全检查器与人工复核 | 检查敏感文件、号码、密钥和平台主体名称 | 扫描结果、脱敏副本、发布清单 | 工具通过不代表内容天然适合公开，仍需逐段人工审核 |

## 二、实际方法链

项目的取证方法不是一次“抓取”，而是十二个可停止的步骤。

| 步骤 | 输入 | 动作 | 输出 |
| --- | --- | --- | --- |
| 1. 限定问题 | 纠纷叙述、当前目标 | 每轮只保留最重要的三个以内问题 | 本轮取证问题清单 |
| 2. 建立证据地图 | 待证事实、现有材料 | 标注材料来源、控制方、形式和缺失风险 | 建议证据清单 |
| 3. 划定范围 | 页面、文件、时间和目的 | 明确“只看什么、从哪里开始、到哪里结束” | 授权范围与停止条件 |
| 4. 用户本人登录 | 用户账号和必要验证 | 用户自己完成登录、扫码或验证码 | 有效会话，不记录凭据 |
| 5. 只读采集 | 已授权页面或文件 | 导航、滚动、截图、保存页面状态 | 原始固定件与页序 |
| 6. 固定完整性 | 采集到的全部文件 | 只读保存、编号、计算 SHA-256 | 哈希清单和保管记录 |
| 7. 数字化 | 截图、录音、页面和原件 | OCR、本地转写、Markdown、结构化字段 | 可检索派生物 |
| 8. 标记状态 | 每条事实和提取结果 | 标注 `observed`、`extracted`、`inferred` 或 `unverified` | 可区分的证据状态 |
| 9. 关键字段交叉核对 | 金额、主体、时间、交易标识、页面状态 | 至少使用两个独立来源比对 | 一致点、冲突点和缺口 |
| 10. 法律映射 | 官方法律文本、证据矩阵 | 用构成要件反查事实和证据 | 支持、间接支持、缺口或暂缓 |
| 11. 补证或收口 | 缺口清单 | 补取材料、申请调查取证、请求提交或暂不主张 | 下一步责任人与期限 |
| 12. 归档与公开审查 | 本轮全部记录 | 关闭运行记录，二次脱敏和安全扫描 | 可复核归档与必要的公开副本 |

这套方法最重要的不是“步骤多”，而是每一步都有明确输入、输出、责任人和停止点。无法完成某一步时，应记录缺口，而不是让 AI 用文字补全。

## 三、证据状态必须分开

| 状态 | 含义 | 示例 |
| --- | --- | --- |
| `observed` | 用户在指定时点直接看到了页面或文件内容 | 页面在采集时显示“处理中” |
| `extracted` | 工具从截图、页面或文件中提取出某项内容 | OCR 识别出一个日期 |
| `inferred` | 根据多份材料作出的解释或推论 | 两份记录共同支持某个时间顺序 |
| `unverified` | 尚未回到原件、人工或官方法律来源确认 | 聊天摘要中的金额尚未核对 |
| `SOURCE_CONFLICT` | 两个来源对同一字段记载不一致 | 新页面显示的交易标识与付款回单不同 |
| `blocked_captcha` | 验证码阻止继续采集 | 页面要求滑块验证，采集停止 |
| `login_required` | 登录失效，当前授权范围无法继续 | 会话过期，等待用户本人处理 |
| `OCR_UNVERIFIED` | OCR 文本尚未经过人工视觉复核 | 客服截图刚完成机器识别 |

状态标记不是形式要求。它决定某条内容能否进入事实底稿、证据目录、法律论证或公开发布。

## 四、十二项指导原则

1. **原件优先**：原始文件、录音和截图永不修改；裁剪、OCR、转写和脱敏都生成新文件。
2. **本人认证**：登录、扫码、短信验证码、支付密码和恢复码只能由用户本人完成。
3. **只读和最小权限**：只访问解决当前问题所必需的页面、时间范围和数据类型。
4. **遇到访问控制即停止**：验证码、权限弹窗、登录失效、下载确认或状态改变按钮出现时，停止并报告。
5. **截图必须带上下文**：记录页面、时间、通道、页序、可见状态和未覆盖范围。
6. **派生物必须回链**：每份 Markdown、OCR 和转写都要链接到原件、截图或录音。
7. **不确定性原样保留**：错字、乱码、遮挡、听不清和字段冲突不能被“润色”掉。
8. **事实、评价和法律结论分开**：用户陈述、对方陈述、客观材料、AI 推论和规范适用分别登记。
9. **关键字段双源核对**：金额、主体、时间和交易标识尽量用页面、回单、导出或原始文件交叉验证。
10. **法律判断回到官方文本**：法规名称、条号、版本和施行时间必须核验，不能使用模型记忆或搜索摘要。
11. **证明边界与材料同时登记**：每份证据都要写明能支持什么，以及不能证明什么。
12. **对外动作由人负责**：签字、缴费、提交、发送、修改订单和公开发布由用户本人完成或逐项明确授权。

## 五、必须停下来的情形

| 情形 | 处理方式 | 禁止做法 |
| --- | --- | --- |
| 登录失效或需要多因素验证 | 记录 `login_required`，交还用户本人处理 | 索取密码、Cookie、验证码或恢复码 |
| 出现验证码、滑块或人机验证 | 记录 `blocked_captcha`，停止采集 | 绕过、破解或使用第三方代过 |
| 页面被截断、空白或持续加载 | 记录可见范围、时间和异常，必要时由用户重新打开 | 把未加载内容写成未发生 |
| 两份材料字段冲突 | 建立 `SOURCE_CONFLICT`，保留各来源原文 | 选择更符合叙事的版本直接采用 |
| OCR 或转写不确定 | 标记 `OCR_UNVERIFIED` 或保留 `[?]`，回看原件 | 把机器文本当成截图或录音原文 |
| 原件缺失或只有转发副本 | 标记来源和保管链缺口 | 用 AI 摘要替代原件 |
| 官方法律文本无法核验 | 暂缓法律引用或换用可核验官方来源 | 编造条号、版本、案例或裁判观点 |
| 出现签署、付款、发送或提交按钮 | 停止自动化，说明后果，由用户决定 | 把“取证”扩大为代理操作 |

任何情况下都不得绕过验证码、登录限制或访问控制。需要人工操作时，由用户本人处理并重新授权。

## 六、每份证据的最小技术记录

一份可复核的记录至少应回答：

- 证据编号和固定件编号是什么；
- 原件文件名、格式和 SHA-256 是什么；
- 材料来自哪个页面、文件、录音或公开来源；
- 通过什么通道取得，是否由用户本人登录和授权；
- 何时开始、何时结束，使用哪个时区；
- 页序、消息序或音频时间戳是什么；
- 当时实际看到了什么，哪些内容没有加载或无法访问；
- 使用过哪些 OCR、转写或格式转换方法；
- 哪些内容经过人工复核，复核人是谁；
- 与哪份材料存在冲突；
- 该材料用于证明什么，证明边界是什么；
- 是否允许形成公开副本，脱敏规则是什么。

结构化字段可参考 [证据 Schema](../schemas/evidence.schema.json)，运行过程可记录在 [取证运行记录模板](../examples/evidence/collection-run.template.md) 中。

## 七、推荐的最小目录结构

```text
case-private/
├── 00_originals/       # 用户提供的原始文件，只读保存
├── 10_captures/        # 截图、HTML、页面数据和页序
├── 20_derived/         # Markdown、OCR、转写和结构化派生物
├── 30_index/           # 证据台账、时间线、冲突清单
├── 40_legal/           # 官方文本、来源登记和法律要件矩阵
├── 50_public_copies/   # 二次脱敏后的公开候选文件
└── manifest.json       # 文件、哈希、来源和状态索引
```

真实目录和清单应保留在私有工作区。公开仓库只放方法、模板、Schema 和完全虚构示例。

## 八、使用前的质量闸门

一项材料进入正式研究或文书前，逐项确认：

- [ ] 能回到原件或明确的页面固定件；
- [ ] 有取得时间、通道、范围和页序；
- [ ] SHA-256 已计算并登记；
- [ ] OCR 和转写中的重要字段已经人工复核；
- [ ] 所有冲突都已保留，没有擅自选择有利版本；
- [ ] 事实、推论和法律评价已经分开；
- [ ] 对应法律规范已经回到官方文本核对；
- [ ] 证明目的和证明边界都已写明；
- [ ] 无法取得的材料已经列入补证、调查取证或暂缓事项；
- [ ] 公开前已完成二次脱敏、人工复核和安全扫描。

## 九、常见误区

| 误区 | 为什么错误 | 正确做法 |
| --- | --- | --- |
| 截图越多越有证明力 | 重复截图不增加独立性，可能遗漏关键上下文 | 记录范围、页序、来源和证明目的 |
| 页面没显示结果，就说明没有处理 | 页面只反映某一时点的前台状态 | 写“该页当时未显示”，另行寻找后台或正式记录 |
| OCR 文本就是截图原文 | OCR 会产生误识别和漏字 | 保留 OCR，同时逐张回看重要字段 |
| 录音转写可以直接引用 | 机器转写存在同音字和语序错误 | 关键片段回听并标注时间戳 |
| 哈希可以证明证据真实 | 哈希只检查文件是否一致 | 同时核验来源、取得过程和原始载体 |
| AI 摘要可以替代材料 | 摘要丢失上下文且可能引入错误 | 摘要只作导航，结论必须回到原件 |
| 搜到法条就可以引用 | 搜索摘要可能过期、删改或错配 | 回到官方全文核对条号、版本和施行时间 |

## 十、一句话记住

> 好的取证技术，不是让材料看起来更多，而是让每份材料都能回答：从哪里来、何时取得、是否完整、由谁复核、能证明什么、还缺什么。
>
> Good evidence technology does not make the record look larger. It makes every item answer: where it came from, when it was obtained, whether it is intact, who reviewed it, what it can prove, and what is still missing.

---

## English

## Conclusion First

AI-assisted evidence collection is not "letting AI find evidence automatically." It is a verifiable chain supported by several technologies:

- use AI to turn the dispute narrative into facts to prove and a proposed evidence list;
- have the user personally complete sign-in, identity verification, and explicit authorization;
- view pages consecutively and preserve screenshots and page states within a read-only scope;
- preserve originals, page captures, and exports and compute SHA-256;
- use OCR, local transcription, and Markdown to create searchable derivatives;
- connect materials through an index, timeline, and cross-source checks;
- return to official legal texts and test facts, evidence, conflicts, and gaps against legal elements.

Each layer solves a different problem. A screenshot is not a complete back-office record. A hash does not prove that content is true. OCR is not the original text. A transcript is not the recording. An AI summary is not evidence. The purpose of the technology is traceability, not manufactured certainty.

## 1. Technology Inventory

The technologies used in the project fall into four layers.

### 1.1 Access and Capture

| Technology or tool | Actual role | Main output | Limit of proof |
| --- | --- | --- | --- |
| Large language model assisting narrative decomposition | Converts "what happened" into facts to prove, material sources, controllers, and gaps | Proposed evidence list, collection questions, priorities | A plan, not a finding of fact and not evidence |
| In-app or system browser with user-controlled login | Opens order, chat, work-order, and rule pages within the user's existing session | Observable pages, navigation path, operation record | AI never receives passwords, verification codes, or cookies; login alone does not prove page content is true |
| Consecutive screenshots and page-order records | Preserves what a page displayed during a defined time range | Screenshots, page numbers, message order, time range | Proves only the displayed state at capture time, not the platform's database export |
| Page title, final location, and page-data snapshots | Preserves context, text structure, and state at the time | HTML, JSON, text snapshot, final URL or de-identified placeholder | A page snapshot is not a back-office log and does not prove an event never happened merely because it was not displayed |
| Original-file access and export | Preserves existing PDFs, images, audio, payment receipts, and exports | Unmodified copy of the original file | File existence does not prove source authenticity; acquisition and original medium still require verification |

### 1.2 Integrity and Custody

| Technology or tool | Actual role | Main output | Limit of proof |
| --- | --- | --- | --- |
| Read-only preservation of originals | Prevents cropping, transcoding, renaming, or conversion from overwriting the source | Original files, read-only backups, custody location | A backup does not replace an account of the original medium and acquisition process |
| Stable IDs and naming | Creates stable relationships among evidence, captures, files, and derivatives | `evidence_id`, `capture_id`, file IDs | A filename is not evidence; use it with the register and hash |
| SHA-256 hashing | Checks whether two files are byte-for-byte identical and detects later replacement or corruption | Hash manifest, verification result | A hash proves file consistency, not truthful content, lawful origin, or correct interpretation |
| Operation log | Records who read or processed what, when, and through which channel | Run record, time, channel, scope, stop reason | An AI-generated log still requires human review and is not automatically a fact |
| Private/public separation | Keeps real material, personal information, and case attachments out of the public repository | Private originals, de-identified public copies, safety-check results | Automated scanning does not replace manual redaction and legal judgment |

### 1.3 Digitization and Structure

| Technology or tool | Actual role | Main output | Limit of proof |
| --- | --- | --- | --- |
| Markdown normalization | Converts chats, pages, files, and transcripts into searchable and version-comparable text | Markdown with source links and stable IDs | Markdown is a derivative, not a new original; it must not erase errors or omissions |
| OCR followed by image-by-image visual review | Extracts text from screenshots and has a human check important fields | OCR text, review markers, difference record | OCR makes mistakes; unreviewed text is not the screenshot's original text |
| Local offline audio transcription | Produces timestamped text without uploading the original recording to an external service | Transcript, timestamps, key-segment index | Machine transcription may contain homophones, omissions, and word-order errors; key passages must be replayed before formal use |
| Page index and timeline | Organizes messages, screenshots, and events in sequence | Page index, message order, event timeline | A timeline aids understanding but does not automatically prove causation or responsibility |
| Field extraction and evidence matrix | Structures time, actors, amounts, page states, purposes, and gaps | Structured list, legal-elements and evidence matrix | Complete fields do not establish a fact; originals and legal sources still require verification |
| Conflict register | Preserves disagreement among pages or files instead of guessing it away | `SOURCE_CONFLICT` record, verification task | Recording a conflict does not resolve it; original records or further investigation may be needed |

### 1.4 Verification and Legal Mapping

| Technology or tool | Actual role | Main output | Limit of proof |
| --- | --- | --- | --- |
| Official legal-source register | Verifies instrument name, article, version, effective date, and official text | Source register, official link, archived file, hash | Search snippets, secondary articles, and model memory cannot replace official text |
| Reverse check against legal elements | Starts from the legal issue and required elements, then checks facts and evidence | "Issue, norm, element, fact, evidence, gap" matrix | The matrix is a research tool, not a court ruling, and does not guarantee probative weight |
| AI-assisted consistency review | Compares versions, dates, actors, amounts, and citations for contradictions | Conflict list, questions for confirmation, review tasks | Finding a conflict does not decide which version is correct; return to the sources |
| Public-safety checker and human review | Checks sensitive files, numbers, secrets, and platform entity names | Scan result, redacted copies, publication checklist | Passing the tool does not make content suitable for publication; section-by-section human review is still required |

## 2. The Operating Method

The project does not treat collection as a single capture action. It uses twelve stoppable steps.

| Step | Input | Action | Output |
| --- | --- | --- | --- |
| 1. Limit the question | Dispute narrative and current objective | Keep no more than three high-priority questions for the run | Collection question list |
| 2. Build an evidence map | Facts to prove and existing material | Record source, controller, form, and risk if missing | Proposed evidence list |
| 3. Define scope | Page, file, time, and purpose | Specify what may be viewed, where to start, and where to stop | Authorization scope and stop conditions |
| 4. User signs in | User account and required verification | The user completes sign-in, QR confirmation, or CAPTCHA | Active session without recording credentials |
| 5. Read-only capture | Authorized page or file | Navigate, scroll, screenshot, and save page state | Original captures and page order |
| 6. Fix integrity | All captured files | Preserve read-only, assign IDs, compute SHA-256 | Hash manifest and custody record |
| 7. Digitize | Screenshots, audio, pages, and originals | OCR, local transcription, Markdown, structured fields | Searchable derivatives |
| 8. Mark status | Every fact and extracted result | Label as `observed`, `extracted`, `inferred`, or `unverified` | Distinguishable evidence status |
| 9. Cross-check critical fields | Amounts, actors, time, transaction IDs, page states | Compare at least two independent sources | Agreements, conflicts, and gaps |
| 10. Map to law | Official legal text and evidence matrix | Test facts and evidence against legal elements | Supported, indirectly supported, gap, or hold |
| 11. Fill or close the gap | Gap list | Collect more material, seek court investigation, request production, or defer the assertion | Next actor and deadline |
| 12. Archive and review for publication | All records from the run | Close the run record, redact again, run safety checks | Reviewable archive and necessary public copy |

The number of steps is not the important part. Each step has an input, output, responsible actor, and stop point. If a step cannot be completed, record the gap instead of filling it with generated prose.

## 3. Evidence Statuses Must Remain Separate

| Status | Meaning | Example |
| --- | --- | --- |
| `observed` | The user directly saw the content on a page or file at a specified time | A page displayed "processing" during capture |
| `extracted` | A tool extracted content from a screenshot, page, or file | OCR recognized a date |
| `inferred` | An explanation or inference drawn from multiple materials | Two records jointly support a sequence of events |
| `unverified` | Not yet checked against the original, human review, or an official legal source | An amount in a chat summary has not been checked |
| `SOURCE_CONFLICT` | Two sources disagree on the same field | A new page shows a different transaction ID from a payment receipt |
| `blocked_captcha` | A CAPTCHA prevented further capture | A slider challenge appeared and collection stopped |
| `login_required` | The login expired and the authorized scope cannot continue | The session expired while awaiting the user |
| `OCR_UNVERIFIED` | OCR text has not received image-by-image human review | A customer-service screenshot has only machine recognition |

Status labels are not decoration. They determine whether content may enter the factual record, evidence index, legal analysis, or public release.

## 4. Twelve Guiding Principles

1. **Originals first**: original files, recordings, and screenshots are never modified; cropping, OCR, transcription, and redaction create new files.
2. **User-controlled authentication**: sign-in, QR confirmation, SMS codes, payment passwords, and recovery codes are completed only by the user.
3. **Read-only and least privilege**: access only the pages, time range, and data types necessary for the current question.
4. **Stop at access controls**: stop and report when a CAPTCHA, permission prompt, expired session, download confirmation, or state-changing control appears.
5. **Screenshots need context**: record page, time, channel, page order, visible state, and what was not covered.
6. **Derivatives must link back**: every Markdown file, OCR result, and transcript links to its original, screenshot, or recording.
7. **Preserve uncertainty**: typos, garbled text, occlusion, unclear audio, and field conflicts must not be polished away.
8. **Separate facts, opinions, and legal conclusions**: user statements, opposing statements, objective material, AI inferences, and legal application remain distinct.
9. **Cross-check critical fields**: amounts, actors, time, and transaction identifiers should be compared across pages, receipts, exports, or original files.
10. **Legal conclusions return to official texts**: verify instrument name, article, version, and effective date; do not rely on model memory or search snippets.
11. **Record the limit of proof with the material**: state what each item can support and what it cannot prove.
12. **Humans own external actions**: signatures, payments, filings, messages, order changes, and public release are performed by the user or explicitly authorized item by item.

## 5. Mandatory Stop Conditions

| Situation | Required handling | Prohibited response |
| --- | --- | --- |
| Login expired or multi-factor verification required | Record `login_required` and return control to the user | Request passwords, cookies, verification codes, or recovery codes |
| CAPTCHA, slider, or human-verification challenge appears | Record `blocked_captcha` and stop | Bypass, defeat, or use a third-party solver |
| Page is truncated, blank, or stuck loading | Record visible scope, time, and anomaly; have the user reopen it if needed | Treat unloaded content as something that never happened |
| Two materials conflict on a field | Create `SOURCE_CONFLICT` and preserve each source | Select the version that better fits the narrative |
| OCR or transcription is uncertain | Mark `OCR_UNVERIFIED` or use `[?]` and review the original | Treat machine text as the screenshot or recording's original language |
| Original is missing or only a forwarded copy exists | Record the gap in source and custody | Replace the original with an AI summary |
| Official legal text cannot be verified | Defer the citation or use a verifiable official source | Invent an article, version, case, or judicial statement |
| A sign, payment, send, or submit control appears | Stop automation, explain the consequence, and leave the decision to the user | Expand "evidence collection" into acting on the user's behalf |

Never bypass a CAPTCHA, login restriction, or access control. When human action is required, the user handles it personally and authorizes any continuation.

## 6. Minimum Technical Record for Each Item

A reviewable record should answer:

- What are the evidence ID and capture ID?
- What are the original filename, format, and SHA-256?
- Which page, file, recording, or public source produced the material?
- Through which channel was it obtained, and did the user personally sign in and authorize it?
- When did collection start and end, and in which time zone?
- What are the page order, message order, or audio timestamps?
- What was actually visible, and what failed to load or remained inaccessible?
- Which OCR, transcription, or conversion methods were used?
- Which content received human review, and who performed it?
- Which other material conflicts with it?
- What is the item intended to prove, and what is its limit of proof?
- Is a public copy permitted, and what redaction rule applies?

For structured fields, see the [evidence schema](../schemas/evidence.schema.json). For the run record, use the [collection run template](../examples/evidence/collection-run.template.md).

## 7. Recommended Minimal Directory Structure

```text
case-private/
├── 00_originals/       # user-provided originals, preserved read-only
├── 10_captures/        # screenshots, HTML, page data, and page order
├── 20_derived/         # Markdown, OCR, transcripts, and structured derivatives
├── 30_index/           # evidence register, timeline, and conflict list
├── 40_legal/           # official texts, source register, and legal-elements matrix
├── 50_public_copies/   # redacted candidates for public release
└── manifest.json       # file, hash, source, and status index
```

The actual directory and register remain in the private workspace. The public repository contains only methods, templates, schemas, and entirely synthetic examples.

## 8. Quality Gate Before Use

Before an item enters formal research or a draft, confirm:

- [ ] It can be traced to an original or an identified page capture;
- [ ] Acquisition time, channel, scope, and page order are recorded;
- [ ] SHA-256 has been computed and registered;
- [ ] Important OCR and transcript fields have been reviewed by a human;
- [ ] All conflicts are preserved without selecting the convenient version;
- [ ] Facts, inferences, and legal characterizations remain separate;
- [ ] The corresponding legal norm has been checked against official text;
- [ ] Evidentiary purpose and limit of proof are explicit;
- [ ] Unavailable material is listed for further collection, investigation, or deferral;
- [ ] Public release has passed redaction, human review, and the safety checker.

## 9. Common Mistakes

| Mistake | Why it is wrong | Correct practice |
| --- | --- | --- |
| More screenshots create more probative force | Repetition does not create independence and may omit critical context | Record scope, page order, source, and purpose |
| No result shown on the page means nothing was processed | A page reflects only a front-end state at one time | State "the page did not display it at the time" and seek back-office or formal records separately |
| OCR text is the original screenshot text | OCR produces misrecognition and omissions | Preserve OCR and visually review important fields |
| A transcript can be quoted directly | Machine transcription may contain homophones and word-order errors | Replay key passages and mark timestamps |
| A hash proves the evidence is true | A hash checks only whether files match | Also verify source, acquisition process, and original medium |
| An AI summary can replace the material | A summary loses context and may introduce errors | Use summaries for navigation; conclusions return to originals |
| A search result for a statute is enough to cite | A snippet may be stale, altered, or mismatched | Check article, version, and effective date against the official full text |

## 10. One-Sentence Rule

> Good evidence technology does not make the record look larger. It makes every item answer: where it came from, when it was obtained, whether it is intact, who reviewed it, what it can prove, and what is still missing.
>
> 好的取证技术，不是让材料看起来更多，而是让每份材料都能回答：从哪里来、何时取得、是否完整、由谁复核、能证明什么、还缺什么。
