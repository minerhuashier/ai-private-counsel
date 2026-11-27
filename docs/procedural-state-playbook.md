# 立案之后：用 AI 维护程序状态与准备线上异步审理

## 当“已经立案”不再是终点

把材料提交给法院，只完成了从争议整理到程序入口的一次转换。案件随后会出现许多彼此独立、更新时间也不一致的状态：程序类型、费用、送达、期限、证据、审理方式和文书。一个页面显示“审理中”，不能同时回答这些状态是否已经更新；一条短信提到新程序，也不能证明法院系统内部的每一项记录都已完成同步。

AI 在这里的价值，不是替当事人宣布“案件进展到哪一步”，而是把互相冲突的状态拆开，记录每个状态来自哪里、能证明什么、还有什么没有确认，并把下一步整理成由本人核实的清单。

> **程序状态不是一个字段，而是一组带来源和时间的状态轴。**
>
> **A procedural status is not one field. It is a set of source-bound, time-stamped state axes.**

本文是一套公开的操作方法，不是对任何具体法院、案件或平台的程序规则作概括。涉及具体期限、缴费、送达、审理方式和诉讼权利时，必须以当时有效的正式通知、法院平台和法院工作人员答复为准。

## 为什么要单独维护程序状态

普通人在自行诉讼中经常遇到四类“看起来已经同步”的误解：

1. **一件事只有一个状态**：实际上，案件状态、程序类型、费用、送达、期限和证据状态可能分别更新；
2. **最新页面一定覆盖旧通知**：实际上，平台可能滞后、缓存或只显示部分信息；
3. **银行扣款成功等于法院入账完成**：实际上，付款义务、支付动作、银行扣款、法院收款确认和内部账单核销是不同节点；
4. **程序转换当然改变所有期限**：实际上，一项新通知没有写到的内容，不能由 AI 自行推定已经失效、延长或重新起算。

因此，程序台账的最小单位不应是“案件当前状态：某四个字”，而应是一条条可追溯的事件记录。

## 八条状态轴

| 状态轴 | 需要回答的问题 | 常见来源 | 典型错误 |
| --- | --- | --- | --- |
| 案件身份 | 当前适用哪个程序、哪个案号阶段？ | 正式受理通知、法院平台 | 把前序调解编号当成当前诉讼编号 |
| 程序类型 | 简易、普通或其他程序是否已经由正式文书变更？ | 裁定书、传票、法院平台 | 看到旧页面后继续使用历史程序结论 |
| 费用 | 是否存在缴费义务、是否已支付、是否已入账？ | 缴费通知、银行回单、法院账单 | 银行已扣款就写成法院已完成入账 |
| 送达 | 哪份文书、何时、通过何种方式送达？ | 送达回证、短信、电子邮件、正式文书 | “网页未打开”就写成“未送达” |
| 期限 | 哪个行为应在何时之前完成？ | 正式文书、传票、法院平台 | 把页面抓取时间当成期限起算时间 |
| 证据 | 哪些材料已提交、接收、补充或被要求说明？ | 证据页、上传回执、法院通知 | 系统可预览就写成法院已采信 |
| 审理 | 是否线下、在线同步或线上异步？各阶段何时开放？ | 传票、审理告知、法院平台 | 把异步窗口写成必须全程实时在线 |
| 文书与批准 | 哪一版文书已由本人确认并用于外部动作？ | 批准记录、提交回执、正式文书 | 把 AI 草稿当成已提交版本 |

台账应逐轴登记，不应为了让页面“看起来整齐”而把不同来源强行合并成一个确定结论。

## 一条状态记录必须写什么

每条记录至少包含：

- **事件时间**：法院或来源声称事件发生的时间；
- **来源时间**：文书日期、短信时间、页面显示时间或回单时间；
- **抓取时间**：本人或 AI 实际看到、下载、截图或登记的时间；
- **来源类型**：正式文书、法院平台、短信、电子邮件、银行回单、电话记录或本人操作；
- **原始载体与哈希**：原件路径、文件名、SHA-256 或私有台账编号；
- **可证明范围**：这条来源能证明什么，不能证明什么；
- **当前状态**：`observed`、`corroborated`、`conflict`、`stale`、`unverified` 或 `closed`；
- **下一步核实来源**：需要查看哪份正式文书、哪个页面或向谁核实；
- **责任人**：谁负责核实、批准和执行；
- **批准记录**：没有明确批准时写 `none`。

状态词不是法律结论：

- `observed`：只在某一来源中看到；
- `corroborated`：至少两个相互独立的来源在相同范围内一致；
- `conflict`：来源之间不一致，暂停推定；
- `stale`：曾经有效或曾经显示，但已被更晚的正式来源取代；
- `unverified`：尚未取得足够来源；
- `closed`：该事项已经完成，并有可回链的回执或正式记录。

## 来源不能互相替代

程序材料通常来自五层来源，每层回答的问题不同：

1. **页面观察**：抓取时页面显示了什么；
2. **通知到达**：短信、邮件或平台消息何时到达；
3. **正式文书**：文书正文作出了什么程序处理；
4. **外部动作回执**：本人是否完成支付、签署、上传或提交；
5. **权威确认**：法院账单、送达记录、案件系统或工作人员是否确认该动作已进入法院流程。

更高层来源并不自动推翻低层来源。正确做法是记录它们各自证明的范围。例如：

- 页面显示“待缴费”，银行回单显示“已扣款”，只能先得出“银行侧已支付、法院侧状态尚待核对”；
- 短信通知转为普通程序，法院页面仍显示旧程序，不能因为页面滞后就否定短信，也不能因为短信存在就宣称平台所有阶段入口已经同步；
- 正式文书未提到某个旧期限，不等于该期限当然改变；应把旧期限标为“继续准备、等待正式确认”，直到取得新的正式依据。

## `SOURCE_CONFLICT`：状态冲突处理协议

发现冲突时，AI 必须暂停生成确定性结论，并按以下顺序处理：

1. **停止**：不输出“已经完成”“已经变更”“无需再做”等结论；
2. **并列保存**：保留每个来源的原文、时间、抓取时间和证明范围；
3. **比较范围**：确认冲突是两个来源真的矛盾，还是只是回答不同问题；
4. **寻找最新正式来源**：优先查看正式文书、传票、法院平台最新记录或法院明确答复；
5. **人工核实**：由本人登录、致电或现场确认，AI 只准备核对清单；
6. **记录冲突关闭理由**：写清哪一个来源在何时解决了哪一个问题，不能只把旧记录删掉；
7. **如需外部动作**：重新生成待审草稿，等待本人逐项批准。

冲突记录示例：

```text
状态轴：费用
来源 A：法院页面在某一时点仍只显示历史账单
来源 B：银行回单显示已向法院收款户名支付
当前状态：conflict
可以确认：银行侧交易成功
不能确认：法院内部账单已核销
下一步：本人查看法院最新账单；如长期未同步，再由本人联系法院
禁止动作：不重复支付，不宣称法院已确认收款
```

## 费用状态：五个节点不能合并

费用问题至少应拆成五个节点：

1. 是否存在缴费义务；
2. 缴费通知要求的金额、期限和收款方式；
3. 本人是否发起支付；
4. 银行或支付机构是否显示成功；
5. 法院账单或正式渠道是否确认入账。

AI 可以帮助核对金额、日期、收款户名和通知版本，也可以比较银行回单与法院页面。但 AI 不得：

- 根据旧页面断定无需缴费；
- 根据银行扣款断定法院内部已经入账；
- 为避免“逾期”建议重复支付；
- 代替本人向任何账户付款。

遇到“已扣款但平台未显示”时，正确结论是：

> **银行侧支付成功，法院侧入账状态待核实；在核实前不得重复缴纳。**

## 期限状态：宁可保留，不擅自宣布失效

期限管理应同时保存四种时间：

- 事件发生时间；
- 来源生成或显示时间；
- 本人实际看到或抓取的时间；
- 正式行为截止时间及其所在时区。

当新的程序通知没有明确处理旧期限时，不要把“程序变化”自动解释成“旧期限延长”或“旧期限取消”。更稳妥的记录方式是：

```text
旧期限：仍按原记录准备
新来源：已记录，但未明确调整该期限
状态：待正式核实
行动：本人核对传票、法院平台或法院答复后再决定
```

可以设置早于正式截止的内部操作缓冲，但必须标注“内部缓冲不改变正式期限”。不要把 AI 设置的提醒时间冒充法院期限，也不要在未确认时删除旧截止日。

## 线上异步审理不是“整段时间实时在线”

线上异步审理通常意味着法院在规定的窗口或阶段中开放询问、举证、质证、辩论、最后陈述等操作，具体安排仍应以传票、审理告知和法院平台为准。一个审理窗口不等于要求当事人从开始到结束一直在线，也不等于任何时点提交都会立即得到实时回应。

准备时应把“窗口”“阶段开放时间”“单项提交截止时间”和“法院回复时间”分开登记。

### 异步审理准备流程

1. **收齐入口材料**：传票、审理告知、平台消息、身份验证要求和操作说明；
2. **核对案件与身份**：确认案号阶段、当事人信息和当前程序类型；
3. **拆出阶段表**：列出询问、补充材料、质证、辩论、最后陈述等阶段及各自来源；
4. **提前离线起草**：在阶段开放前准备事实摘要、证据索引和待审发言，不把写作压到提交时；
5. **逐项人工确认**：本人确认事实、金额、法律表述、证据版本和是否提交；
6. **留出操作缓冲**：不要等到正式截止前才上传或填写；
7. **保存提交回执**：截图、页面文本、文件哈希、提交时间和平台提示全部留档；
8. **持续检查新通知**：阶段变化、法院追问和对方材料可能在不同时间出现；
9. **未经批准不处分权利**：承认、放弃、变更请求、和解、撤诉等事项必须由本人明确决定。

### 每个阶段的检查表

- 当前阶段名称是什么，来源在哪里？
- 正式开放与截止时间是什么，时区是什么？
- 这个阶段要求“阅读”“回答”“上传”还是“确认”？
- 已有材料是否已经在案，是否真的需要重复上传？
- 本次提交对应哪一项事实、证据和法律主张？
- 是否存在法院新通知、对方新证据或来源冲突？
- 提交版本是否由本人确认？
- 提交后是否取得回执，页面是否出现成功或待处理状态？

## 质证与证据状态

“系统里能看到证据”只说明材料在某个页面中可见，不等于法院已经完成实体审查或采信。质证准备应把证据状态拆成：

- 原件是否保存；
- 是否已经提交；
- 系统是否接收；
- 是否收到补正、退回或重传要求；
- 是否进入质证；
- 对方是否发表意见；
- 法院是否在正式文书中处理。

准备质证时，优先核对：

1. 已提交证据的编号、文件名、页数和证明目的是否一致；
2. 是否存在新增证据、补充原件或法院要求说明；
3. 对方证据是否出现，是否需要核对真实性、合法性、关联性和证明目的；
4. 现有材料是否被重复上传、错传或覆盖；
5. 每项意见是否能回链到具体证据、原始载体和正式期限。

AI 可以生成“证据—事实—争点—法律要件—对方可能反驳”的对照表，也可以检查重复上传和版本冲突。是否提交、如何质证以及是否作出程序处分，仍由本人决定。

## AI 能做什么，不能做什么

AI 适合做：

- 把页面、短信、正式文书和回执整理成状态轴；
- 比较多个版本的日期、金额、案号阶段和程序用语；
- 发现“来源已变化但台账未更新”的冲突；
- 生成期限核对表、阶段准备表和待审草稿；
- 检查同一项事实在不同文书中的矛盾；
- 保存操作前后的审计记录。

AI 不能做：

- 代替法院确认送达、入账、立案、排期或裁判结果；
- 根据常识推定某个期限已经变化；
- 代替本人签署、缴费、提交、质证、和解、撤诉或处分权利；
- 把异步窗口解释为实时庭审；
- 把程序节点写成实体胜负；
- 把“未显示”写成“从未发生”。

## 每日与每个节点的工作循环

```text
读取最新来源
    -> 记录抓取时间与原始载体
    -> 更新状态轴
    -> 检测冲突和过期状态
    -> 生成待办与核实清单
    -> 本人确认事实和选择
    -> 本人执行外部动作
    -> 保存回执
    -> 重新读取并核对结果
```

每次循环只关闭能够被来源证明的事项。不能因为任务列表想变短，就把未知状态改成“已完成”。

## 必须停止的情况

出现以下任一情况时，AI 应停止输出确定性结论：

- 正式文书、短信、平台页面和银行回单互相冲突；
- 无法确认当前有效期限或程序类型；
- 页面要求输入验证码、密码或进行身份验证；
- 需要缴费、签署、提交、和解、撤诉或处分权利；
- 证据版本、金额、主体或案号阶段无法对应；
- 平台上出现新的法院通知或对方材料但尚未阅读；
- 公开内容可能暴露真实案件信息。

停止不是失败，而是把不可逆动作留给有来源、有批准、有责任人的节点。

## 最小落地方式

建议建立三类文件：

1. **程序状态总表**：按八条状态轴记录当前结论、来源、时间和待核实项；
2. **事件日志**：按时间追加，不覆盖旧记录；
3. **阶段准备包**：每个审理阶段单独保存待审稿、证据索引、提交回执和批准记录。

可直接从 [程序状态登记模板](../examples/procedural-state/state-register.template.md) 开始。模板只使用占位符；真实案号、金额、日期、法院材料和个人信息应留在私有工作区。

## 结语

立案后的 AI 辅助，不是让模型替案件“自动推进”，而是让每一个程序节点都有来源、有时间、有证明边界、有责任人。真正重要的不是把状态写得多确定，而是在状态不确定时仍然知道下一步该核实什么、哪些动作不能做，以及什么时候必须停下来等待本人决定。

> **不确定时保留状态，冲突时回到来源，不可逆动作交还本人。**
>
> **Preserve uncertainty, return to sources when records conflict, and leave irreversible acts to the human.**

---

# After Filing: Using AI to Maintain Procedural State and Prepare for Asynchronous Online Proceedings

## "The Case Has Been Filed" Is Not the End

Submitting materials to a court only completes one transition from dispute organization to a procedural entrance. The case then develops many independent states that may update at different times: procedure type, fees, service, deadlines, evidence, hearing mode, and documents. A page saying "under review" does not answer whether every one of those states has been synchronized; a message announcing a new procedure does not prove that every internal court record has changed.

The value of AI here is not to announce on the person's behalf that "the case has reached a certain stage." It is to separate conflicting states, record where each state came from, what it can prove, and what remains unconfirmed, then turn the next step into a checklist for the person to verify.

This is a public operating method, not a summary of the procedural rules of any particular court, case, or platform. For a specific deadline, fee, service event, hearing mode, or procedural right, the effective formal notice, court platform, and answer from court staff control.

## Why Procedural State Needs Its Own Record

People handling their own cases often encounter four false assumptions:

1. **One event has one status**: case status, procedure type, fees, service, deadlines, and evidence may update separately;
2. **The newest page always supersedes an older notice**: a platform may lag, cache data, or display only part of the record;
3. **A successful bank debit means the court has completed reconciliation**: the obligation, payment action, bank debit, court receipt, and internal accounting record are different nodes;
4. **A procedural change automatically changes every deadline**: if a new notice is silent about a deadline, AI cannot infer that the deadline was cancelled, extended, or restarted.

The smallest unit in a procedural register should therefore be a traceable event record, not a single field reading "current status: four words."

## Eight State Axes

| State axis | Question | Common sources | Typical error |
| --- | --- | --- | --- |
| Case identity | Which case-number stage and proceeding currently apply? | Formal acceptance notice, court platform | Treating an earlier mediation number as the current litigation number |
| Procedure type | Has a formal document changed the procedure type? | Ruling, summons, court platform | Continuing to use a historical procedure label from an old page |
| Fees | Is there an obligation, a payment, and a court-side receipt? | Fee notice, bank receipt, court bill | Equating a bank debit with completed court reconciliation |
| Service | Which document was served, when, and by what method? | Service record, message, email, formal document | Treating an unopened web page as proof of non-service |
| Deadlines | Which act must be completed by what time? | Formal document, summons, court platform | Confusing capture time with the legal start time |
| Evidence | What was submitted, received, supplemented, or challenged? | Evidence page, upload receipt, court notice | Treating a previewable document as evidence accepted on the merits |
| Hearing | Is the hearing offline, synchronous online, or asynchronous online? When do stages open? | Summons, hearing notice, court platform | Treating an asynchronous window as a requirement to remain online throughout |
| Documents and approval | Which document version was approved and used for an external act? | Approval record, filing receipt, formal document | Treating an AI draft as a filed version |

Record each axis separately. Do not force different sources into one definite conclusion merely to make a dashboard look tidy.

## Fields in Every State Record

Every record should include:

- **Event time**: when the source says the event occurred;
- **Source time**: the date on the document, message, page display, or receipt;
- **Capture time**: when the person or AI actually saw, downloaded, captured, or registered it;
- **Source type**: formal document, court platform, message, email, bank receipt, call record, or human action;
- **Original and hash**: original path, filename, SHA-256, or private register ID;
- **Proven scope**: what this source can and cannot prove;
- **Current state**: `observed`, `corroborated`, `conflict`, `stale`, `unverified`, or `closed`;
- **Next verification source**: which formal document, page, or person must be checked;
- **Responsible person**: who verifies, approves, and acts;
- **Approval record**: write `none` when no explicit approval exists.

The state labels are not legal conclusions:

- `observed`: seen in one source only;
- `corroborated`: at least two independent sources agree within the same scope;
- `conflict`: sources disagree; inference stops;
- `stale`: previously valid or visible, but superseded by a later formal source;
- `unverified`: insufficient sources have been obtained;
- `closed`: completed, with a linked receipt or formal record.

## Sources Are Not Interchangeable

Procedural records commonly come from five layers:

1. **Page observation**: what the page displayed at capture time;
2. **Notice arrival**: when a message, email, or platform notice arrived;
3. **Formal document**: what the document itself decided or required;
4. **External-action receipt**: whether the person paid, signed, uploaded, or filed;
5. **Authoritative confirmation**: whether a court bill, service record, case system, or staff member confirms that the act entered the court process.

A higher layer does not automatically erase a lower layer. Record what each source proves. For example:

- A page says "payment pending," while a bank receipt says "debited." The supported conclusion is "paid on the bank side; court-side status remains to be checked."
- A message announces a change of procedure while the court page still shows the old procedure. Neither source should be discarded: one may be newer, while the platform may not yet have synchronized every stage.
- A formal document does not mention an older deadline. That silence does not prove the deadline changed; keep preparing under the older deadline until a formal source resolves the issue.

## `SOURCE_CONFLICT`: Conflict-Handling Protocol

When records conflict, AI must stop producing a definite conclusion and proceed in this order:

1. **Stop**: do not say "completed," "changed," or "no further action required";
2. **Preserve side by side**: keep each source text, time, capture time, and proven scope;
3. **Compare scope**: decide whether the sources truly contradict each other or answer different questions;
4. **Find the latest formal source**: check formal documents, summons, the current court platform record, or an explicit answer from court staff;
5. **Human verification**: the person signs in, calls, or attends; AI prepares only the checklist;
6. **Record why the conflict closed**: identify which source resolved which issue and when; do not simply delete the old record;
7. **Re-draft before action**: if an external act is needed, prepare a review draft and wait for item-by-item human approval.

Example conflict record:

```text
State axis: fees
Source A: at a given time, the court page still showed only a historical bill
Source B: a bank receipt showed payment to the court collection account
Current state: conflict
Can confirm: the bank-side transaction succeeded
Cannot confirm: the court's internal bill has been reconciled
Next step: the person checks the latest court bill; if it remains unsynchronized, the person contacts the court
Prohibited action: do not pay twice; do not state that the court has confirmed receipt
```

## Fee Status: Do Not Merge Five Nodes

A fee issue has at least five nodes:

1. whether an obligation exists;
2. the amount, deadline, and payment channel in the notice;
3. whether the person initiated payment;
4. whether the bank or payment provider reports success;
5. whether a court bill or formal channel confirms receipt.

AI may compare amounts, dates, payee names, notice versions, bank receipts, and court pages. It must not:

- infer from an old page that no payment is due;
- turn a bank debit into proof of court-side reconciliation;
- recommend duplicate payment merely to avoid a possible delay;
- pay any account on the person's behalf.

When payment has been debited but the platform does not display it, the correct conclusion is:

> **The bank-side payment succeeded; court-side reconciliation remains unverified; do not pay again before verification.**

## Deadline Status: Preserve Before Declaring Expiry

Record four times together:

- event time;
- source generation or display time;
- actual capture or observation time;
- the formal act deadline and its time zone.

When a new procedural notice does not explicitly address an older deadline, do not automatically convert "procedure changed" into "deadline extended" or "deadline cancelled." A safer record is:

```text
Older deadline: continue preparing under the existing record
New source: recorded, but does not explicitly adjust this deadline
State: pending formal verification
Action: the person checks the summons, court platform, or court answer before deciding
```

An internal buffer may be set earlier than the formal deadline, but it must be labeled as an internal buffer and must not be presented as a court deadline. Do not delete an old deadline merely because AI generated a new reminder.

## Asynchronous Online Proceedings Are Not "Stay Online for the Whole Window"

Asynchronous online proceedings generally involve a court opening stages or actions such as questions, evidence, cross-examination, argument, and final statements during a defined period. The summons, hearing notice, and court platform control the specific arrangements. A hearing window is not a requirement to remain online from start to finish, and it does not mean that a submission will receive an immediate real-time response.

Record the **window**, **stage opening time**, **item-specific deadline**, and **court response time** separately.

### Preparation Workflow

1. **Collect entrance materials**: summons, hearing notice, platform message, identity-verification requirement, and instructions;
2. **Verify case and identity**: confirm the case-number stage, party details, and current procedure type;
3. **Build a stage table**: list questions, supplemental materials, cross-examination, argument, final statement, and the source for each stage;
4. **Draft offline in advance**: prepare fact summaries, evidence indexes, and review drafts before a stage opens;
5. **Obtain item-by-item human approval**: the person confirms facts, amounts, legal wording, evidence versions, and whether to submit;
6. **Leave an operational buffer**: do not wait until the formal cut-off to upload or complete a form;
7. **Save submission receipts**: capture screenshots, page text, file hashes, submission time, and platform messages;
8. **Keep checking for new notices**: stages, court questions, and opposing materials may appear at different times;
9. **Do not dispose of rights without approval**: admissions, waivers, claim changes, settlement, and withdrawal remain human decisions.

### Checklist for Each Stage

- What is the stage name, and where is the source?
- What are the formal opening and closing times, including the time zone?
- Does the stage require reading, answering, uploading, or confirming?
- Are the materials already on file, and is re-upload genuinely required?
- Which fact, exhibit, and legal proposition does this submission address?
- Is there a new court notice, new opposing evidence, or unresolved source conflict?
- Has the person approved the exact submission version?
- After submission, is there a receipt or a success/pending indicator?

## Cross-Examination and Evidence Status

"The evidence is visible in the system" means only that a document is visible on a page. It does not mean that the court has completed substantive review or accepted the evidence. Record evidence status in separate layers:

- original preserved;
- submitted;
- received by the system;
- correction, return, or re-upload requested;
- cross-examination opened;
- opposing comments made;
- addressed in a formal court document.

For cross-examination preparation, verify:

1. whether exhibit numbers, filenames, page counts, and stated purposes match;
2. whether new evidence, original documents, or explanations have been requested;
3. whether opposing evidence appeared and requires review of authenticity, legality, relevance, and purpose;
4. whether existing materials were duplicated, misuploaded, or overwritten;
5. whether every comment links to a specific exhibit, original medium, and formal deadline.

AI may build an exhibit-fact-issue-legal-element-counterargument matrix and detect duplicates or version conflicts. The person still decides what to file, how to cross-examine, and whether to exercise a procedural right.

## What AI Can and Cannot Do

AI can:

- organize pages, messages, formal documents, and receipts into state axes;
- compare dates, amounts, case-number stages, and procedural language across versions;
- detect when a source changed but the register did not;
- generate deadline and stage-preparation checklists and review drafts;
- identify inconsistencies in the same fact across documents;
- preserve an audit trail before and after an external act.

AI cannot:

- confirm service, payment reconciliation, acceptance, scheduling, or judgment on behalf of a court;
- infer that a deadline changed merely from general knowledge;
- sign, pay, file, cross-examine, settle, withdraw, or dispose of rights for the person;
- describe an asynchronous window as a real-time hearing;
- convert a procedural event into a substantive outcome;
- convert "not displayed" into "never happened."

## Daily and Event-Driven Loop

```text
Read the latest source
    -> record capture time and original medium
    -> update the state axis
    -> detect conflict and stale records
    -> generate a verification checklist
    -> human confirms facts and chooses a path
    -> human performs the external act
    -> save the receipt
    -> read again and verify the result
```

Close only the items that a source can prove. Do not change an unknown state to "completed" just to shorten the task list.

## Mandatory Stop Conditions

AI must stop producing definite conclusions when:

- formal documents, messages, platform pages, and bank receipts conflict;
- the effective deadline or current procedure type cannot be verified;
- a page requests a verification code, password, or identity verification;
- an act involves payment, signing, filing, settlement, withdrawal, or disposition of rights;
- exhibit versions, amounts, parties, or case-number stages do not match;
- a new court notice or opposing material appears but has not been read;
- public content could expose real case information.

Stopping is not failure. It reserves irreversible acts for a node with a source, approval, and accountable person.

## Minimum Implementation

Create three kinds of files:

1. **Procedural state register**: record the conclusion, source, time, and verification task for each of the eight axes;
2. **Event log**: append chronologically without overwriting old records;
3. **Stage preparation package**: keep the review draft, evidence index, submission receipt, and approval record for each hearing stage.

Start with the [procedural-state register template](../examples/procedural-state/state-register.template.md). It uses placeholders only. Real case numbers, amounts, dates, court materials, and personal information belong in a private workspace.

## Conclusion

AI assistance after filing is not about letting a model "automatically move a case forward." It is about giving every procedural node a source, a time, a limit of proof, and an accountable person. The goal is not to make every status sound certain. The goal is to know what must be checked next, which actions must not be taken while the record is uncertain, and when to stop for a human decision.

> **Preserve uncertainty, return to sources when records conflict, and leave irreversible acts to the human.**
