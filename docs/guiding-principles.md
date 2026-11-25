# AI 私人律师项目的指导原则

## 让 AI 扩大能力，但不转移责任

> 这不是一份抽象伦理宣言，而是一组从真实纠纷、错误、退回和版本审计中提炼出来的工作规则。它适用于法律研究、证据整理、文书起草、程序状态维护和公开传播。

这个项目相信，AI 在个人维权中真正有价值的地方，不是“像一个无所不知的律师”，而是：

- 把一个模糊诉求拆成可以回答的问题；
- 持续整理大量分散材料；
- 扩大检索范围；
- 对同一个结论反复寻找反例；
- 发现主体、金额、日期、证据和版本之间的矛盾；
- 在任何外部动作之前，把需要本人确认的事项明确列出来。

这也不是“AI 比律师更好”的结论。更准确的说法是：

> 在大量整理、检索和一致性检查这类任务上，AI 可以显著扩展一个人的工作能力；在复杂法律判断、策略取舍、庭审应对和责任承担上，AI 不能替代执业律师，也不能替代当事人。

## 十六项指导原则

### 1. 证据先于结论

先问“哪份材料证明什么”，再问“因此谁应负责”。没有证据编号的事实只能标为待核实，不能用更流畅的语言升级为结论。

**检查问题：** 这项事实的原件在哪里？

### 2. 法律判断先于文书润色

起诉状不是作文。法律关系、主体、请求和构成要件没有理清时，增加篇幅可能只是扩大错误。

**检查问题：** 这段文字背后是哪一项关系和构成要件？

### 3. 法律关系先于被告选择

先确认谁对谁负有什么义务，再确定告谁。品牌名、App 名、收款方和服务商不当然属于同一法律主体。

**检查问题：** 这项请求基于哪一份合同、哪一项法定义务或哪一种法定责任？

### 4. 被告与管辖先于提交

原告的直觉通常是“先写状纸”。可提交性还取决于被告是否适格、法院是否有管辖权、材料是否符合程序要求。

**检查问题：** 如果今天提交，主体和管辖能否分别用官方来源解释？

### 5. 官方原文先于模型记忆和搜索摘要

法律、司法解释、行政法规、地方规则和法院公告必须记录名称、条号、版本、施行日期、官方 URL、访问时间和适用范围。

**检查问题：** 这条规则现在仍有效吗？我能打开官方原文吗？

### 6. 每项诉请必须走完四段链路

一项可复核的诉请应当能够从“事实”走到“证据”，再到“法律依据”，最后落到“具体请求和计算方式”。

**检查问题：** 任何一段断开时，我是否愿意删除、改写或暂缓这项请求？

### 7. 主动审查己方弱点

AI 不能只负责把己方论证写强，还要扮演反方，寻找主体错误、关系混合、证据不足、金额不可计算、期限风险和不必要的法律定性。

**检查问题：** 如果对方只指出一个最致命的问题，可能是什么？

### 8. 不确定必须显式保留

“不确定”“来源冲突”“页面过期”“等待正式通知”不是失败文案，而是必须进入状态记录的真实信息。无法核验时应失败关闭。

**检查问题：** 我是在记录事实，还是为了让材料看起来完整而猜了一个答案？

### 9. 原件只读，派生件可追溯

截图、录音、付款记录、聊天和程序通知不因命名、裁剪、OCR、转写或整理而被覆盖。每份派生件应能回到原件、处理方法和时间。

**检查问题：** 如果明天有人质疑这份 Markdown，我能否找到原件和处理链？

### 10. 最小权限、最少披露和公开前再脱敏

AI 只处理完成任务所需的最少材料。用户本人负责登录和授权，采集保持在只读或明确范围内。公开稿必须在私有稿之外重新制作，不把“内部可见”误当成“可以公开”。

**检查问题：** 这份材料真的需要交给 AI、上传平台或进入公开仓库吗？

### 11. AI 生成的是待审草稿，不是法律行为

AI 不签字、不缴费、不点击提交、不发送投诉、不处分程序权利，也不替本人接受调解。有效批准必须对应具体版本、具体用途和具体动作。

**检查问题：** 这一步是谁在承担法律后果？是否已有明确授权记录？

### 12. 程序节点不等于实体结果

提交成功、立案、缴费、证据接收、程序转换和开庭通知都只代表程序向前推进，不代表法院支持请求。案件未决时不得宣称胜诉。

**检查问题：** 这条表述是在描述程序，还是在暗示实体裁判？

### 13. 状态必须带来源和时间

法院短信、平台页面、银行扣款、系统入账和正式文书可能不同步。状态记录应包含来源、显示时间、证明范围和下一份待核实来源。

**检查问题：** 两个来源冲突时，哪一个更正式、更新、更接近正式通知？

### 14. 重要事项设置专业帮助阈值

案件复杂、金额较大、涉及人身权益、刑事风险、复杂主体结构、重大期限或当事人明显无法理解程序时，应引入执业律师。AI 可以准备材料和问题清单，但不能取消专业帮助。

**检查问题：** 继续自行处理的风险是否已经超过节省成本的价值？

### 15. 人是价值判断和责任的最终节点

AI 可以列出方案、概率、风险和后果，但“是否起诉、告谁、请求什么、是否调解、是否公开”必须由本人作决定。AI 不应通过强势语气替本人制造决定。

**检查问题：** 我是否真正理解这个选择的代价，而不是因为 AI 说“建议”就点了同意？

### 16. 公开传播不得破坏正在进行的程序

公开内容只写有证据支持的事实，避免侮辱、诽谤、未经裁判确认的严重违法定性、真实身份、案号和可反查细节。传播不是证明责任的方式。

**检查问题：** 这篇内容是在帮助他人理解方法，还是在用舆论替代法院判断？

## AI 与人的分工

| 环节 | AI 更适合 | 人必须负责 |
| --- | --- | --- |
| 发现问题 | 扩展问题树、追问缺口 | 确认哪些问题与自己有关 |
| 整理材料 | 转写、分类、索引、比对 | 确认真实性、完整性和隐私边界 |
| 研究法律 | 检索、对照、提取构成要件 | 确认适用、选择策略和承担后果 |
| 识别主体 | 阅读协议、提出候选、核验线索 | 决定被告和诉讼结构 |
| 判断管辖 | 比较规则、整理官方来源 | 确认并完成提交 |
| 起草文书 | 生成、审计、比较版本 | 逐项批准、签署和提交 |
| 维护状态 | 提醒冲突、记录来源 | 核对正式通知和处分期限 |
| 公开表达 | 检查敏感信息和表达风险 | 决定是否、何时、以何种方式发布 |

## 项目的七个“不”

1. 不把 AI 的流畅表达当作法律正确。
2. 不把品牌名当作法律主体。
3. 不把搜索摘要当作官方原文。
4. 不把截图当作完整后台记录。
5. 不把程序节点当作胜诉结果。
6. 不把本人未确认的草稿用于外部动作。
7. 不为了传播效果牺牲隐私、人格权和正在进行的程序。

## 最低交付标准

任何准备进入下一步的成果，至少应满足：

- 关键事实有来源，未知项有标记；
- 法律结论有官方原文和版本；
- 被告、管辖、请求与案由能相互解释；
- 证据目录与文书属于同一版本；
- 重要金额和期间可以独立复算；
- 失败条件和待确认事项已经写明；
- 外部动作有本人明确批准；
- 公开版本已经重新脱敏。

当以上任一项无法满足时，正确动作通常不是“让 AI 再写一版”，而是暂停、补证、核对来源或引入专业帮助。

## 相关文档

- [七道校准关口](decision-workflow.md)
- [自诉工作协议](../PROTOCOL.md)
- [证据协议](evidence-protocol.md)
- [来源核验协议](citation-protocol.md)
- [威胁模型](threat-model.md)
- [人工批准 Schema](../schemas/approval.schema.json)

---

# Guiding Principles for the AI Private Counsel Project

## Expand Capability with AI Without Transferring Responsibility

> This is not an abstract ethics statement. It is a set of working rules derived from a real dispute, errors, filing returns, and version audits. It applies to legal research, evidence organization, drafting, procedural-state tracking, and public communication.

The project's central claim is not that AI should act like an omniscient lawyer. AI is valuable because it can:

- turn a vague claim into answerable questions;
- keep large, scattered collections organized;
- expand the search surface;
- look repeatedly for counterexamples;
- detect contradictions across parties, amounts, dates, evidence, and versions;
- identify exactly what a human must confirm before any external act.

This also does not establish that "AI is better than a lawyer." A more accurate statement is:

> AI can materially expand a person's capacity for organization, research, and consistency checking. It cannot replace a qualified lawyer in complex legal judgment, strategy, hearing preparation, or responsibility, and it cannot replace the party.

## Sixteen Guiding Principles

### 1. Evidence Before Conclusion

Ask what a file proves before asking who should be liable. A fact without an evidence identifier remains unverified and cannot become a conclusion through better prose.

**Test:** Where is the original source for this fact?

### 2. Legal Analysis Before Polishing

A complaint is not an essay. If the relationship, party, claim, and legal elements are unclear, adding length may only enlarge the error.

**Test:** Which relationship and element support this paragraph?

### 3. Legal Relationship Before Defendant

Determine who owed what duty to whom before deciding whom to sue. A brand, app, payment recipient, and service provider are not automatically the same legal entity.

**Test:** Is this claim based on a contract, a statutory duty, or another statutory form of liability?

### 4. Party and Jurisdiction Before Filing

The instinct is often to draft first. Whether a case can be filed also depends on the proper defendant, jurisdiction, and procedural materials.

**Test:** If I filed today, could I explain both the defendant and the court through official sources?

### 5. Official Text Before Model Memory and Search Snippets

Statutes, judicial interpretations, regulations, local rules, and court announcements require title, article, version, effective date, official URL, access time, and scope.

**Test:** Is this rule still effective, and can I open the official text?

### 6. Every Claim Must Complete a Four-Part Chain

A reviewable claim must connect fact to evidence, then to legal basis, then to specific relief and calculation.

**Test:** If one link is missing, am I willing to delete, revise, or pause the claim?

### 7. Attack Your Own Case

AI must do more than strengthen the user's argument. It should act as opposing counsel and look for wrong parties, mixed relationships, insufficient evidence, unreproducible amounts, deadline risk, and unnecessary legal characterizations.

**Test:** If the other side could identify only one fatal problem, what would it be?

### 8. Make Uncertainty Explicit

"Uncertain," "source conflict," "stale page," and "awaiting formal notice" are not failures in presentation. They are real state that must be recorded. When verification fails, the process should fail closed.

**Test:** Am I recording a fact, or guessing to make the file look complete?

### 9. Originals Are Read-Only and Derivatives Are Traceable

Screenshots, recordings, payment records, chats, and notices are never overwritten by renaming, cropping, OCR, transcription, or organization. Every derivative should trace to its original, processing method, and time.

**Test:** If this Markdown file is challenged tomorrow, can I recover the original and the processing chain?

### 10. Least Privilege, Minimum Disclosure, Redact Again Before Publication

AI receives only the material necessary for the task. The user controls sign-in and authorization, and capture remains read-only or explicitly bounded. Public content is produced as a separate, newly redacted artifact; internal visibility does not imply permission to publish.

**Test:** Does this material really need to be given to AI, uploaded, or committed publicly?

### 11. AI Output Is a Draft for Review, Not a Legal Act

AI does not sign, pay, click submit, send a complaint, waive procedural rights, or accept mediation. Valid approval must identify a specific version, purpose, and action.

**Test:** Who bears the legal consequence of this step, and is the authorization recorded?

### 12. Procedural Events Are Not Substantive Outcomes

Submission, acceptance, fee payment, evidence receipt, procedural conversion, and hearing notice only advance the process. They do not mean the court supports the claim. No unresolved case may be described as won.

**Test:** Does this language describe a procedure or imply a merits ruling?

### 13. Every Status Needs a Source and Time

Court messages, portal pages, bank debits, system reconciliation, and formal documents may be out of sync. A status record includes source, display time, scope of proof, and the next formal source to verify.

**Test:** When sources conflict, which is more formal, newer, and closer to an official notice?

### 14. Set a Professional-Help Threshold

Obtain qualified counsel when the matter is complex, high-value, affects personal rights, raises criminal risk, involves complicated entities, contains a material deadline, or exceeds the person's ability to understand the procedure. AI may prepare materials and questions; it does not eliminate professional help.

**Test:** Has the risk of proceeding alone exceeded the value of the cost saved?

### 15. The Human Is the Final Node for Values and Responsibility

AI may list options, probabilities, risks, and consequences. The human decides whether to sue, whom to sue, what relief to seek, whether to mediate, and whether to publish. AI must not manufacture consent through an authoritative tone.

**Test:** Do I genuinely understand the cost of this choice, rather than agreeing because AI called it "recommended"?

### 16. Public Communication Must Not Damage an Active Proceeding

Public content should rely on supported facts and avoid insults, defamation, serious legal characterizations not confirmed by a court, real identities, case numbers, and reverse-identifying details. Public attention is not a substitute for proof.

**Test:** Does this content help others understand a method, or use publicity to replace judicial determination?

## AI and Human Roles

| Stage | AI Is Better Suited To | The Human Must Own |
| --- | --- | --- |
| Problem discovery | Expand the issue tree and ask about gaps | Confirm which issues are personally relevant |
| Material organization | Transcribe, classify, index, and compare | Authenticity, completeness, and privacy boundaries |
| Legal research | Search, compare, and extract elements | Applicability, strategy, and consequences |
| Party identification | Read agreements, propose candidates, verify leads | Defendant and proceeding structure |
| Jurisdiction | Compare rules and organize official sources | Confirmation and filing |
| Drafting | Generate, audit, and compare versions | Item approval, signature, and submission |
| State tracking | Flag conflicts and preserve sources | Check formal notices and exercise deadlines |
| Public expression | Check sensitive data and expression risk | Decide whether, when, and how to publish |

## Seven Prohibitions

1. Do not treat fluent AI output as legal correctness.
2. Do not treat a brand name as a legal entity.
3. Do not treat a search snippet as official text.
4. Do not treat a screenshot as a complete back-office record.
5. Do not treat a procedural event as a favorable judgment.
6. Do not use an unapproved draft for an external act.
7. Do not sacrifice privacy, personality rights, or an active proceeding for publicity.

## Minimum Delivery Standard

Before any output moves to the next step:

- key facts have sources and unknowns are marked;
- legal conclusions have official text and version records;
- defendant, jurisdiction, claims, and cause of action can explain one another;
- evidence index and pleading belong to the same reviewed version;
- material amounts and periods can be independently recalculated;
- failure conditions and pending human decisions are explicit;
- external acts have clear human approval;
- public versions have been redacted independently.

If any item fails, the correct next move is usually not "ask AI for another draft." Pause, preserve evidence, verify the source, or obtain professional help.

## Related Documents

- [Seven Calibration Gates](decision-workflow.md)
- [Self-Litigation Protocol](../PROTOCOL.md)
- [Evidence Protocol](evidence-protocol.md)
- [Citation Protocol](citation-protocol.md)
- [Threat Model](threat-model.md)
- [Approval Schema](../schemas/approval.schema.json)
