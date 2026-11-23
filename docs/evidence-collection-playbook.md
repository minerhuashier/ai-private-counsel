# 从一段叙述到可核验证据链：AI 协助取证的五个关口

# From a Narrative to a Verifiable Evidence Chain: Five Gates of AI-Assisted Evidence Collection

- 版本：`0.1.0`
- 状态：公开方法复盘
- 适用范围：仅限用户本人授权的账号页面、已持有文件和公开资料

> 证据不是“AI 找到的一段内容”，而是一条可以回到原件、来源、时间和处理过程的记录。
>
> Evidence is not merely content found by an AI. It is a record that can be traced back to the original file, source, time, and processing history.

本文不是法律意见，也不说明 AI 截图、OCR、转写或整理结果具有公证、司法鉴定或证据保全效力。本文公开的是操作方法、记录字段、停止条件和证明边界。

This document is not legal advice. It does not claim that AI screenshots, OCR, transcripts, or summaries carry the effect of notarization, forensic examination, or judicial evidence preservation. It publishes the operating method, required records, stop conditions, and limits of proof.

---

## 中文

## 结论先行

AI 在取证中的价值，不是替当事人“多找几段材料”，而是把一段混乱叙述转换成五个连续问题：

1. 哪些事实需要证明？
2. 哪些材料可能证明这些事实，材料由谁控制？
3. 用户本人需要怎样登录、打开页面、划定只读范围并授权？
4. 怎样把看到的页面和拿到的文件固定成原件、截图、页面数据、文本与哈希？
5. 怎样回到法律规范，逐项检查“构成要件是否有事实支撑、事实是否有证据支撑、证据是否存在缺口”？

任何一步无法回答时，都应该停下来记录缺口，而不是用更流畅的文字补全。

## 一、这段经历实际发生了什么

### 1. 从“我不知道怎么办”开始

项目开始时只有一段纠纷叙述和少量材料。AI 首先做的不是写起诉状，而是把已经掌握的信息拆成待补材料：

- 订单与商品信息；
- 付款记录；
- 商家承诺与沟通记录；
- 平台投诉、客服反馈和处理结果；
- 未按约履行的客观材料；
- 平台主体、规则版本和管辖信息。

这一步只是“建议证据清单”，不是事实认定。清单中的每一项都要由用户确认是否存在、在哪里、由谁控制。

### 2. 用户先用自然语言说明争议核心

当事人补充了“商家没有退款”“平台已经知道没有履约”“订单后来仍显示交易完成”等关键陈述。AI 没有把这些直接写成已证实事实，而是拆成多个待证命题：

- 商家承诺了什么；
- 是否付款、付给谁、何时付款；
- 商家是否未按约履行；
- 平台何时知道了什么；
- 用户是否要求平台锁定、暂停或采取其他措施；
- 订单是否仍自动完成；
- 是否存在退款、结算或工单最终处理结果；
- 平台主体和管辖信息是否可以核实。

这种拆法的目的，是让“我觉得平台有责任”变成一组能够逐项找证据、逐项承认缺口的问题。

### 3. 用户本人保持登录，AI 只读提取

早期实际操作使用的是**应用内浏览器**，不是后来才形成的系统 Chrome 操作契约。用户本人预先保持账号登录，在浏览器中打开商家聊天和订单页面，并明确要求从最早位置开始逐页读取。

当时的配合方式可以概括为：

- 用户选择页面和账号会话；
- 用户明确授权读取范围；
- 用户把页面定位到起点；
- AI 只做导航、读取、截图和整理；
- AI 不代替用户申请退款、确认收货、删除内容、发送消息或提交工单；
- 遇到登录、验证码、权限或状态不明时停止，不尝试绕过。

日志记录中，聊天提取最终形成 31 页连续截图、105 条带时间的消息、完整 Markdown、分页索引、时间线和逐文件 SHA-256。这里的“连续”表示从用户指定的起点翻到页面终点，不等于已经取得平台后台的全部数据。

### 4. 固定证据，而不是只保存 AI 摘要

真正的证据固定至少保留四层：

| 层级 | 示例 | 作用 |
| --- | --- | --- |
| 原始材料 | 用户提供的 PDF、原始录音、原始截图 | 保留未经修改的来源文件 |
| 页面固定件 | 浏览器截图、HTML、页面数据快照 | 记录某时某页面显示了什么 |
| 派生物 | Markdown、OCR 文本、录音转写、结构化清单 | 方便检索、比对和建立时间线 |
| 台账 | 证据编号、来源、取得时间、SHA-256、证明目的 | 把文件与待证事实连接起来 |

截图和页面数据快照能够证明“当时页面这样显示”，但不能自动证明平台后台日志、资金结算流水或未展示事件从未发生。证明边界必须和材料一起登记。

### 5. 数字化必须保留误差

这段项目里至少出现过三种数字化路径：

- 聊天页：逐页截图，同时提取消息和时间，生成 Markdown 与索引；
- 客服截图：先 OCR，再逐张视觉复核，避免把识别错误当成原文；
- 通话录音：本地离线转写，保留时间戳，并明确机器转写可能存在同音字和语序误差。

数字化结果不是新的“原件”。它是便于检索的派生物，必须链接回原始截图、录音或页面固定件。

### 6. 页面冲突不能靠猜

订单新页面曾把“支付宝交易号”显示成订单编号，与支付回单和旧版页面中的真实交易号不一致。最终没有把单一页面字段直接写成事实，而是采用交叉核对：

- 支付回单证明实际支付行为和回单记载的交易号；
- 旧版页面补充另一组页面状态；
- 订单新页面截图记录当时显示；
- 冲突本身写入运行记录和证据说明。

另一个商品页面触发了滑块验证码。正确处理是停止采集并记录 `blocked_captcha`，由用户决定是否手动查看；不是绕过验证码，也不是用搜索摘要假装已经看过页面。

### 7. 法律反查让证据清单收口

材料并不是越多越好。后来用户明确本案以法院诉讼和法律规定为主，平台规则只作为合同内容、事实背景和主体线索，于是停止扩采无关平台类目。

随后用法律问题反查证据：

- 合同关系是否有订单、商品页面、聊天、合同和付款材料支撑；
- 履行与未履行是否有双方陈述之外的客观材料；
- 平台“知道”是否有投诉、客服记录或工单材料支撑；
- 平台是否采取必要措施，是否有请求、页面状态、处理结论和结算材料；
- 损失、因果关系和请求金额是否有票据、支付记录和计算过程。

这一步会得到三类结论：已有证据足够、只有间接证据、仍缺关键证据。第三类必须进入补证、申请法院调查取证、请求对方提交材料，或者暂时不主张的清单。

## 二、五个关口

### 关口一：从叙述生成建议证据清单

输入不是“帮我找证据”，而是：

- 发生了什么；
- 时间、主体、行为和金额；
- 现在手头有什么；
- 希望证明哪些争议；
- 哪些材料只有对方或平台掌握。

输出应使用“待证事实”而不是“结论”：

| 不推荐 | 推荐 |
| --- | --- |
| 证明平台诈骗 | 证明某日用户向平台提交了何种材料，以及页面显示的受理状态 |
| 证明商家根本没想履约 | 证明商家在何时表示无法提供原服务、提出了什么替代方案、是否退款 |
| 证明平台不作为 | 证明平台何时收到何种请求、页面是否显示处理结果、订单是否继续流转 |

建议清单至少要覆盖：

- 合同与商品内容；
- 付款和收款；
- 双方沟通；
- 履行或未履行；
- 平台知情；
- 平台采取措施或未采取措施；
- 订单状态变化；
- 退款、赔付、结算和工单结果；
- 主体信息；
- 损失与费用。

每项都标注：来源、由谁控制、当前状态、证明边界、优先级和缺失风险。

### 关口二：用户配合与只读授权

AI 不应索取密码、短信验证码、扫码确认、Cookie、支付密码或恢复码。用户应自己完成登录和多因素验证。

推荐操作顺序：

1. 用户说明要查看的页面和目的。
2. 用户自己登录，保持会话。
3. 用户打开目标页面并定位到起点。
4. 用户明确授权“只读、截图、提取、保存”，并说明范围。
5. AI 在范围内导航、滚动、读取和截图。
6. 遇到登录失效、验证码、权限弹窗、下载确认、发送按钮或状态改变按钮时停止并报告。
7. 用户决定是否亲自处理，再重新授权继续。

禁止把下列动作包装成“只是取证”：

- 代为申请退款或售后；
- 确认收货；
- 撤销投诉；
- 修改订单、地址、账号或隐私设置；
- 发送消息、提交表单或上传文件；
- 删除记录；
- 绕过验证码或访问控制。

### 关口三：固定原始材料与页面状态

每一轮采集都要记录：

- 通道：应用内浏览器、系统 Chrome、用户导出、公开网页或本地文件；
- 页面或文件来源；
- 开始时间与结束时间；
- 页面标题、最终 URL 或公开占位符；
- 授权范围；
- 截图、HTML、JSON、PDF、音频或其他固定件；
- 每个固定件的 SHA-256；
- 页面状态和可能的加载限制；
- 是否遇到登录、验证码、截断、空白、重定向或字段冲突；
- 哪些内容看见了，哪些内容没有看见。

建议把“访问事实”和“内容解释”分开记录：

- `observed`：页面当时显示了这段文字；
- `extracted`：工具从页面或文件中提取出这段文字；
- `inferred`：根据多份材料作出的解释；
- `unverified`：仍待人工或原始来源确认。

页面数据快照、HTML 和截图是采集时点的固定件，不是平台数据库导出。若需要平台后台流水、完整工单日志或结算记录，应另行取得，或列入调查取证、责令提交和补充材料清单。

工单页面没有显示处理结论，只能证明该页面当时没有显示该结论，不等于平台从未处理或后台从未留下记录。

### 关口四：数字化为可检索、可回链的 Markdown

一份可用的 Markdown 证据文本至少包含：

- 证据编号和固定件编号；
- 原件文件名和 SHA-256；
- 页面、文件或录音来源；
- 取得时间和操作通道；
- 页序、消息序或音频时间戳；
- 原文与必要的结构化字段；
- 识别不确定处；
- 与另一份材料的冲突；
- 派生物处理规则；
- 复核人、复核时间和复核结论。

聊天记录不要只留一段“剧情摘要”。应保留逐条时间、发送方、原文、附件说明和页序。录音不要只留会议纪要。应保留带时间戳的转写，并在正式引用前回听关键片段。OCR 结果应逐页抽查，重要字段应人工回看截图。

数字化时可以统一格式，但不能悄悄修正原文。错别字、乱码、缺失、遮挡和无法识别处应原样标记，例如：

- `[?]`：可能听错或识别错误；
- `[截断]`：页面或文件在此处缺失；
- `[不可读]`：图像质量不足；
- `OCR_UNVERIFIED`：尚未人工复核；
- `SOURCE_CONFLICT`：两份来源字段不一致。

### 关口五：用法律要件反查证据

不要从“我已经有什么材料”出发拼法律。应从争议问题和规范要件出发，反向检查证据。

建议使用五列表：

| 法律问题 | 规范与要件 | 待证事实 | 证据与证明边界 | 缺口与下一步 |
| --- | --- | --- | --- | --- |
| 合同是否成立、内容是什么 | 规范名称、条号、生效版本；要约、承诺、标的等要件 | 商品描述、订单、聊天承诺、电子合同 | 订单页、聊天、合同、付款记录；各自能证明什么 | 缺少的版本、原件或相互冲突处 |
| 是否付款、付给谁 | 支付事实和收款主体 | 金额、时间、账户、交易号、收款方 | 回单、账单、订单页 | 回单是否能证明后续结算 |
| 是否未按约履行 | 履行义务、履行期限、履行内容 | 原服务内容、变更请求、拒绝替代、实际未提供 | 聊天、录音、现场材料、第三方材料 | 是否存在独立未履行证据 |
| 平台何时知道什么 | 知情事实和信息来源 | 投诉时间、客服答复、工单内容 | 截图、录屏、导出记录、录音 | 是否有完整工单和后台处理日志 |
| 平台采取何种措施 | 必要措施、处理流程和结果 | 用户的请求、平台操作、订单状态、退款或结算 | 请求原文、页面状态、工单结论、资金流水 | 无法取得的材料是否申请调查取证或责令提交 |
| 损失与因果关系 | 损失范围、因果关系、减损情况 | 已付款、未获服务、替代成本、必要费用 | 付款凭证、合同、发票、替代服务记录 | 哪些费用缺少票据或关联性 |

矩阵中的法律规范必须回到官方文本核对名称、条号、版本和施行时间。AI 记忆、搜索摘要和二手文章不能直接成为规范来源。

如果证据只能支持间接推论，应明确写“可结合某证据形成间接证明”，不能写成“已经直接证明”。如果某项事实只有用户陈述，应写“用户陈述，待证”。如果材料由对方控制，应写“补证或申请调查取证”，不能凭空补全。

## 三、成功与失败都要登记

### 成功的部分

- 用户指定起点和读取范围后，聊天记录完成了连续分页截图；
- 消息被整理为带时间的 Markdown，并建立分页索引和时间线；
- 原始录音没有修改，转写文本保留时间戳和不确定标记；
- 订单页面、退改规则、HTML、页面数据和截图分别登记；
- 所有关键固定件计算 SHA-256，能够检查文件是否被替换。

### 失败和限制

- OCR 曾出现识别误差，不能把机器文本直接当作截图原文；
- 商品页面出现滑块验证码，采集停止，没有绕过；
- 新订单页面的交易号字段与支付回单冲突，最终采用交叉核验；
- 平台最终结算流水、完整工单日志和部分规则有效版本无法由普通用户直接取得；
- “页面没有显示结果”不能扩大为“平台绝对从未处理”；
- 支付回单只能证明付款行为，不能单独证明平台后续结算去向；
- 页面数据快照不是平台后台数据库导出，也不是公证文书。

把这些失败写进公开项目，比只展示“AI 成功抓取了 31 页”更有价值。它告诉读者：可信的取证不是从不犯错，而是每个错误都有停止条件、复核记录和证明边界。

## 四、每次取证的最小运行清单

1. 写下本轮要回答的三个以内问题。
2. 列出建议材料、来源、控制方和证明边界。
3. 由用户本人完成登录和必要验证。
4. 明确页面、时间范围和只读权限。
5. 固定页面标题、最终位置、时间和可见状态。
6. 保存原始文件和页面固定件，不覆盖原件。
7. 计算每个文件的 SHA-256。
8. 生成 Markdown、OCR、转写或结构化派生物，并回链原件。
9. 逐项标注 `observed`、`extracted`、`inferred`、`unverified`。
10. 用法律要件矩阵检查证据、冲突和缺口。
11. 记录停止原因、未覆盖范围和下一步责任人。
12. 对外公开前再次脱敏，并确认没有真实案件附件。

## 五、可直接复用的模板

- [取证计划模板](../examples/evidence/collection-plan.template.md)
- [取证运行记录模板](../examples/evidence/collection-run.template.md)
- [法律要件与证据矩阵模板](../examples/evidence/legal-evidence-matrix.template.md)
- [证据示例目录说明](../examples/evidence/README.md)

这些模板只使用占位符和虚构字段。不要把真实姓名、账号、订单号、交易号、金额、聊天原文、录音、截图或法院材料填入公开仓库。

## 六、一句话记住

> AI 可以帮你更快地找到、读取、整理和检查材料；但可信的结论必须回到原件、来源、时间、哈希、人工复核和法律要件。
>
> AI can help find, read, organize, and check material faster. A trustworthy conclusion must still return to the original, source, time, hash, human review, and legal elements.

---

## English

## Conclusion First

The value of AI in evidence collection is not that it finds a few more pieces of material. It converts a messy narrative into five connected questions:

1. Which facts need to be proved?
2. Which materials may prove those facts, and who controls them?
3. How should the user sign in, open the page, define a read-only scope, and authorize access?
4. How should the visible page and obtained files be preserved as originals, screenshots, page data, text, and hashes?
5. How should the legal elements be checked against the facts, the facts against the evidence, and the evidence against its gaps?

If any step cannot be answered, record the gap and stop. Do not fill it with smoother prose.

## 1. What Actually Happened

### 1.1 Starting from uncertainty

The project began with a dispute narrative and a small set of materials. The first AI task was not to draft a complaint. It was to turn the known information into a list of missing material:

- order and product information;
- payment records;
- merchant promises and communications;
- platform complaints, customer-service responses, and handling results;
- objective material about non-performance;
- platform identity, rule versions, and jurisdiction information.

This was only a proposed evidence list, not a finding of fact. The user had to confirm whether each item existed, where it was, and who controlled it.

### 1.2 Turning the dispute into facts to prove

The user then explained the core dispute in natural language, including statements that the merchant had not refunded, the platform knew about the non-performance, and the order later still showed completion.

The AI did not treat those statements as established facts. It separated them into propositions:

- what the merchant promised;
- whether payment was made, to whom, and when;
- whether the merchant failed to perform;
- when the platform knew what;
- whether the user asked the platform to lock, pause, or take other action;
- whether the order still completed automatically;
- whether a refund, settlement, or final work-order result existed;
- whether the platform entity and jurisdiction could be verified.

This converted "I think the platform is responsible" into a set of questions that could be supported, challenged, or marked as missing one by one.

### 1.3 The user stayed signed in; the AI read only

The historical operation used the **in-app browser**, not the later system-Chrome operating contract. The user kept the account signed in, opened the merchant chat and order pages, and explicitly asked the AI to read from the earliest point page by page.

The cooperation pattern was:

- the user selected the page and account session;
- the user authorized a defined reading scope;
- the user positioned the page at the starting point;
- the AI only navigated, read, captured screenshots, and organized content;
- the AI did not apply for a refund, confirm receipt, delete content, send a message, or submit a work order;
- the AI stopped on login, CAPTCHA, permission, or uncertain-state boundaries.

The chat record ultimately produced 31 consecutive screenshots, 105 timestamped messages, complete Markdown, a page index, a timeline, and per-file SHA-256 values. "Consecutive" meant from the user-selected starting point to the visible end of the page. It did not mean that every platform back-office record had been obtained.

### 1.4 Preserving evidence, not just a summary

A complete record kept four layers:

| Layer | Example | Purpose |
| --- | --- | --- |
| Original | user-provided PDF, original audio, original screenshot | preserves the unmodified source file |
| Page capture | browser screenshot, HTML, page-data snapshot | records what a page displayed at a specific time |
| Derivative | Markdown, OCR text, transcript, structured index | supports search, comparison, and timeline work |
| Register | evidence ID, source, acquisition time, SHA-256, purpose | connects a file to a fact to be proved |

A screenshot or page-data snapshot can show that a page displayed a particular state at a particular time. It does not automatically prove back-office logs, fund-settlement records, or that an event never happened merely because the page did not show it. The limit of proof belongs in the record.

### 1.5 Digitization must preserve uncertainty

The project used at least three digitization paths:

- chat pages: page-by-page screenshots plus message and time extraction into Markdown and an index;
- customer-service screenshots: OCR followed by visual review of every image;
- call audio: local offline transcription with timestamps and an explicit warning about homophones and word-order errors.

A derivative is not a new original. It must link back to the source screenshot, audio, or page capture.

### 1.6 Conflicting fields cannot be guessed away

One order page displayed the order number in a field labelled as the payment transaction number. A payment receipt and an older page contained a different value.

The project did not promote either page field to fact without checking. It cross-checked:

- the payment receipt for the payment act and recorded transaction identifier;
- the older page for another page state;
- the new page screenshot for what that page displayed;
- the register and run record for the conflict itself.

Another product page triggered a slider CAPTCHA. The correct response was to stop and record `blocked_captcha`, leaving the user to decide whether to inspect the page manually. The correct response was not to bypass the challenge or pretend that a search snippet proved the page had been read.

### 1.7 Legal review closes the evidence list

More material is not always better. The user later narrowed the matter to court litigation and legal authority. Platform rules remained relevant only as possible contract content, factual background, and entity information, so unrelated platform categories were no longer collected.

The evidence list was then checked from legal questions:

- whether contract formation and content had support in the order, product page, chat, contract, and payment record;
- whether performance or non-performance had evidence beyond the parties' statements;
- whether the platform's knowledge had support in a complaint, customer-service record, or work order;
- whether the platform took necessary measures had support in the request, page state, handling result, and settlement record;
- whether loss, causation, and the requested amount had receipts, payment records, and a calculation trail.

The review produced three outcomes: sufficient evidence, only indirect evidence, or a critical gap. A critical gap belongs in a list for further collection, court investigation, an order to produce documents, or a decision not to assert that point yet.

## 2. The Five Gates

### Gate 1: Generate a proposed evidence list from the narrative

The input is not merely "find evidence." It should include:

- what happened;
- time, actors, conduct, and amount;
- what the user already has;
- which disputes are to be proved;
- which material is controlled only by the other party or the platform.

The output should describe facts to prove rather than conclusions:

| Avoid | Prefer |
| --- | --- |
| Prove that the platform committed fraud | Show what the user submitted to the platform on a given date and what status the page displayed |
| Prove that the merchant never intended to perform | Show when the merchant said the original service was unavailable, what alternative was offered, and whether a refund was made |
| Prove that the platform did nothing | Show when the platform received which request, whether a handling result was displayed, and whether the order continued to move |

The proposed list should cover:

- contract and product content;
- payment and receipt;
- communications;
- performance or non-performance;
- platform knowledge;
- platform action or inaction;
- order-status changes;
- refund, compensation, settlement, and work-order results;
- entity information;
- loss and expense.

Each item should record its source, controller, current status, limit of proof, priority, and risk if missing.

### Gate 2: User cooperation and read-only authorization

An AI should not request passwords, SMS codes, QR-code confirmation, cookies, payment passwords, or recovery codes. The user should complete sign-in and multi-factor verification personally.

Recommended sequence:

1. The user states the page and purpose.
2. The user signs in and keeps the session active.
3. The user opens the target page and positions it at the start.
4. The user expressly authorizes "read, screenshot, extract, and save" within a defined scope.
5. The AI navigates, scrolls, reads, and screenshots within that scope.
6. On login expiry, CAPTCHA, permission prompt, download confirmation, send button, or state-changing control, the AI stops and reports.
7. The user decides whether to handle it personally and then authorizes continuation.

The following must not be described as "just collecting evidence":

- applying for a refund or after-sales process;
- confirming receipt;
- withdrawing a complaint;
- changing an order, address, account, or privacy setting;
- sending a message, submitting a form, or uploading a file;
- deleting a record;
- bypassing a CAPTCHA or access control.

### Gate 3: Preserve originals and page states

Every collection run should record:

- channel: in-app browser, system Chrome, user export, public webpage, or local file;
- page or file source;
- start and end time;
- page title, final URL, or public placeholder;
- authorized scope;
- screenshot, HTML, JSON, PDF, audio, or other capture;
- SHA-256 for every capture;
- page state and possible loading limits;
- whether login, CAPTCHA, truncation, blank content, redirect, or field conflict occurred;
- what was observed and what was not observed.

Keep access facts separate from interpretation:

- `observed`: the page displayed this text at the time;
- `extracted`: the tool extracted this text from a page or file;
- `inferred`: an interpretation supported by multiple materials;
- `unverified`: still awaiting human review or an original source.

A page-data snapshot, HTML file, or screenshot is a capture at a point in time. It is not a platform database export. If back-office fund flow, a complete work-order log, or a settlement record is required, obtain it separately or place it on the list for investigation, production of documents, or further collection.

A work-order page that displays no conclusion proves only that the page did not display that conclusion at that time. It does not prove that the platform never processed the matter or that no back-office record exists.

### Gate 4: Digitize into searchable Markdown with links back to originals

A usable Markdown evidence text should contain:

- evidence ID and capture ID;
- original filename and SHA-256;
- page, file, or audio source;
- acquisition time and channel;
- page order, message order, or audio timestamp;
- original text and necessary structured fields;
- recognition uncertainty;
- conflicts with another source;
- processing rules for the derivative;
- reviewer, review time, and conclusion.

A chat record should not be reduced to a plot summary. It should preserve each time, sender, original text, attachment description, and page location. An audio record should not be only a meeting summary. It should preserve a timestamped transcript and require the key passages to be checked against the audio before formal use.

OCR output must be reviewed. Important fields must be checked visually against the screenshot.

Formatting may be normalized, but the original must not be silently corrected. Typos, garbled text, omissions, redactions, and unreadable sections should be marked, for example:

- `[?]`: possible mishearing or recognition error;
- `[truncated]`: the page or file is missing content here;
- `[unreadable]`: image quality is insufficient;
- `OCR_UNVERIFIED`: not yet reviewed by a human;
- `SOURCE_CONFLICT`: two sources disagree.

### Gate 5: Check the evidence against legal elements

Do not start with the material at hand and search backward for a legal theory. Start with the disputed issue and the required elements, then test the evidence.

Use a five-column matrix:

| Legal issue | Norm and elements | Fact to prove | Evidence and limit of proof | Gap and next step |
| --- | --- | --- | --- | --- |
| Was a contract formed, and what are its terms? | instrument name, article, effective version; offer, acceptance, subject matter, and other elements | product description, order, chat promise, electronic contract | order page, chat, contract, payment record; what each can and cannot prove | missing version, original, or conflict |
| Was payment made, and to whom? | payment act and recipient | amount, time, account, transaction identifier, recipient | receipt, statement, order page | whether the receipt proves later settlement |
| Was performance withheld? | obligation, time, and content of performance | original service, requested change, refused alternative, actual non-performance | chat, audio, on-site material, third-party material | independent evidence of non-performance |
| When did the platform know what? | knowledge and information source | complaint time, customer-service response, work-order content | screenshot, screen recording, export, audio | complete work order or back-office handling log |
| What measures did the platform take? | necessary measures, process, and result | user request, platform action, order state, refund or settlement | original request, page state, work-order result, fund flow | whether unavailable material should be sought by investigation or production order |
| Loss and causation | scope of loss, causation, mitigation | payment, non-receipt, replacement cost, necessary expense | payment proof, contract, invoice, replacement record | expense without receipt or connection |

Every legal instrument in the matrix must be checked against an official text for name, article, version, and effective date. AI memory, search snippets, and secondary articles are not official sources.

If the evidence supports only an inference, write that it may form indirect proof when combined with another item. Do not write that it directly proves the fact. If a fact rests only on the user's statement, mark it as "user statement, to be proved." If material is controlled by the other side, list further collection, investigation, or a production order. Do not fill the gap by invention.

## 3. Record Both Success and Failure

### What worked

- With a user-defined start and scope, the chat record was captured in consecutive pages;
- messages were organized into timestamped Markdown with a page index and timeline;
- the original audio was preserved, while the transcript retained timestamps and uncertainty markers;
- the order page, refund rules, HTML, page data, and screenshots were registered separately;
- key captures received SHA-256 values so replacement could be detected.

### What failed or remained limited

- OCR produced recognition errors and could not be treated as the screenshot's original text;
- a product page triggered a CAPTCHA, and collection stopped without bypassing it;
- a transaction field conflicted between the new order page and the payment receipt, requiring cross-checking;
- the platform's final settlement flow, complete work-order logs, and some effective rule versions were not directly obtainable by an ordinary user;
- "the page did not display a result" could not be expanded into "the platform never processed anything";
- a payment receipt proved payment, not the platform's later settlement destination;
- a page-data snapshot was not a back-office database export or a notarized document.

Publishing those failures is more useful than showing only a successful 31-page extraction. Trustworthy collection is not the absence of errors. It is a process in which every error has a stop condition, a review record, and a limit of proof.

## 4. Minimum Run Checklist

1. Write no more than three questions for the run.
2. List proposed material, source, controller, and limit of proof.
3. Have the user complete sign-in and required verification.
4. Define the page, time range, and read-only permission.
5. Capture page title, final location, time, and visible state.
6. Save originals and page captures without overwriting originals.
7. Compute SHA-256 for every file.
8. Create Markdown, OCR, transcript, or structured derivatives with links back to originals.
9. Mark each item as `observed`, `extracted`, `inferred`, or `unverified`.
10. Check evidence, conflicts, and gaps against the legal-elements matrix.
11. Record the stop reason, uncovered scope, and next responsible actor.
12. Redact again before publication and confirm that no real case attachment is included.

## 5. Reusable Templates

- [Evidence collection plan](../examples/evidence/collection-plan.template.md)
- [Evidence collection run record](../examples/evidence/collection-run.template.md)
- [Legal-elements and evidence matrix](../examples/evidence/legal-evidence-matrix.template.md)
- [Evidence examples directory](../examples/evidence/README.md)

The templates contain only placeholders and fictional fields. Do not place real names, accounts, order numbers, transaction identifiers, amounts, chat text, audio, screenshots, or court documents in the public repository.

## 6. One-Sentence Rule

> AI can help find, read, organize, and check material faster. A trustworthy conclusion must still return to the original, source, time, hash, human review, and legal elements.
