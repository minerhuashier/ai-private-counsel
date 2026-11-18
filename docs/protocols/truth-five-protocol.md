# “真实五问”协议

版本：`0.1.0-draft`  
状态：`PROPOSED / 本次首次书面提出`  
首次记录：`2026-11-18`  
提出者：本项目用户  
定位：事实、证据、来源、不确定性和批准的五道发布前门槛

## 来源说明

“真实五问”此前没有对应的正式项目文件，也没有在公开仓库、全局记忆或 AEP 3.1 中找到同名规则。

本文件是首次书面固化，用于公开讨论和测试。它不是法律要求、行业标准、执业规范或已经长期运行的项目制度。

## 五个问题

任何事实性说明、法律分析、公开发布内容或对外文书草稿，在转为“可执行候选”前，必须依次回答：

### 1. 这句话属于什么？

它是：

- 可定位的客观事实；
- 本人的主观感受；
- 对方或第三方作出的陈述；
- 本方的法律主张或评价；
- 某个系统在特定时间显示的程序状态；
- 尚未核实的假设；
- AI 的表达或策略建议。

不允许把感受写成事实，把对方陈述写成已被证明的事实，把法律主张写成法院结论，或把页面状态写成客观全貌。

### 2. 它由哪份原始材料支持？

必须回答：

- 证据编号是什么？
- 原始文件在哪里？
- 来源和取得时间是什么？
- 文件哈希是否匹配？
- 证据能证明到哪一步？
- 是否存在反向证据？

没有证据编号的事实句，状态只能是 `UNVERIFIED`。

### 3. 适用的法律、规则或程序依据是什么？

必须回答：

- 法律、司法解释、法院规则或平台规则的完整名称；
- 发布机关和文号；
- 条号；
- 公布日期和生效日期；
- 官方原文 URL 或原始文件；
- 当前是否有效；
- 原文是否直接支持该结论。

如果没有法律问题，应明确写“本句不包含法律判断”，而不是用空白假装已经核验。

### 4. 哪些内容仍不确定、存在冲突或只是假设？

必须列出：

- 未核实事实；
- 来源冲突；
- 版本冲突；
- 缺失材料；
- 合理反证；
- 对己方不利的可能性；
- 需要法院、平台、行政机关或专业人士确认的问题。

不能只列有利解释。无法回答时必须保留空白，不得补全。

### 5. 谁有权确认，批准覆盖什么？

必须回答：

- 谁确认了事实和表达？
- 用户批准的是哪个版本？
- 批准的用途是什么？
- 是否覆盖当前动作？
- 输出修改后，原批准是否失效？
- 实际外部动作由谁执行？

AI 不能批准自己，也不能把笼统的“可以”解释为对签署、缴费、提交、发送或发布的授权。

## 判定规则

五问中任一项失败，输出状态只能是以下之一：

```yaml
status: blocked_missing_evidence
status: blocked_missing_source
status: blocked_unresolved_conflict
status: draft_for_human_review
```

只有五问全部得到明确回答，且不存在阻断项时，输出才可标记为：

```yaml
status: ready_for_human_action
```

`ready_for_human_action` 仍不等于 AI 可以自动执行。它只表示材料已具备提交给本人做最终决定的条件。

## 简化记录表

| 问题 | 记录 |
| --- | --- |
| 内容类型 | `fact / feeling / statement / legal_claim / procedural_status / hypothesis` |
| 证据支持 | `EVD-...` 或 `none` |
| 官方来源 | `SRC-...` 或 `none` |
| 未确定与冲突 | 逐项列出 |
| 批准范围 | 动作、版本、用途、批准人、时间 |

## 示例

### 示例 1：“对方没有提供服务”

- 类型：需要事实基础的主张；
- 支持材料：订单、聊天、录音、退款记录和平台处理记录；
- 边界：材料最多证明特定时间、特定服务内容未履行，不能自动证明对方主观恶意；
- 不确定性：是否存在部分履行、替代履行或双方变更，需要逐项核对；
- 批准：由本人确认事实、措辞和用途。

### 示例 2：“平台明知并应承担责任”

- 类型：事实主张与法律主张的组合；
- 支持材料：需要分别证明平台何时知道什么，以及知道后采取了什么动作；
- 法律依据：必须逐条核对官方法律文本和适用条件；
- 不确定性：平台是否只提供信息、是否已处理、是否达到法律要求的责任门槛；
- 批准：事实和法律结构均由本人复核，必要时另行取得专业意见。

### 示例 3：“我很失望”

- 类型：感受；
- 支持材料：无需外部证据，但必须明确写成感受；
- 法律边界：感受不能替代违约、欺诈、过错或责任结论；
- 批准：本人确认公开表达方式。

## 防止形式化

“真实五问”不能退化为在表格中机械填“是”。

有效回答必须包含可定位材料、具体来源和可复核理由。以下内容视为未回答：

- “已核实”但不写来源；
- “有证据”但不写证据编号；
- “法律有规定”但不写法规名称和条号；
- “用户同意”但不写版本和动作；
- “应该没问题”但不列风险和反证。

## 与防止幻觉协议的关系

- 防止幻觉协议定义内容分类、来源规则、状态标记和失败处理；
- “真实五问”提供一份可以在每个输出前快速执行的最低检查表；
- 两者不能替代官方法律核验、证据审查或本人责任；
- 若两者冲突，以更严格、要求更多人工确认的规则为准。

## 状态与演进

本协议目前为 `PROPOSED`。出现以下任一情况后再考虑升级为正式项目协议：

- 至少在多个完全虚构案例中完成测试；
- 每个问题都有明确记录格式；
- 能够区分“可核验”“可提交”和“已获批准”；
- 公开审查没有发现会鼓励形式化填表的问题；
- Pull Request 记录采用理由和剩余风险。

---

# Truth Five Protocol

Version: `0.1.0-draft`  
Status: `PROPOSED / first written in this document`  
First recorded: `2026-11-18`  
Proposer: the user of this project  
Purpose: five pre-release gates for facts, evidence, sources, uncertainty, and approval

## Provenance

No formal project document named "Truth Five" existed before this proposal. The research also found no same-named rule in the public repository, global memory, or AEP 3.1.

This is the first written version, intended for public review and testing. It is not a statutory requirement, industry standard, professional regulation, or long-running project practice.

## The Five Questions

Before any factual statement, legal analysis, public post, or external-document draft becomes an "action candidate," answer these five questions in order.

### 1. What kind of statement is this?

Is it:

- a locatable objective fact;
- the user's subjective experience;
- a statement by another person or institution;
- the user's legal claim or characterization;
- a procedural status displayed by a system at a particular time;
- an unverified hypothesis;
- an AI suggestion about wording or strategy?

Never write a feeling as a fact, another person's statement as proven fact, a legal claim as a court holding, or a page state as the whole objective reality.

### 2. Which original material supports it?

Answer:

- What is the evidence ID?
- Where is the original file?
- What are the source and acquisition time?
- Does the hash match?
- What exactly can the evidence prove?
- Is there contrary evidence?

A factual sentence without an evidence reference can only have `UNVERIFIED` status.

### 3. What law, rule, or procedural authority applies?

Answer:

- full name of the statute, judicial interpretation, court rule, or platform rule;
- issuing authority and document number;
- article number;
- publication and effective dates;
- official URL or original file;
- whether it remains in force;
- whether the original text directly supports the proposition.

If a sentence contains no legal issue, state that explicitly. Do not hide the absence of verification behind a blank field.

### 4. What remains uncertain, disputed, or hypothetical?

List:

- unverified facts;
- conflicting sources;
- conflicting versions;
- missing materials;
- credible contrary evidence;
- unfavorable possibilities;
- questions requiring confirmation by a court, platform, agency, or qualified professional.

Do not list only favorable explanations. If an answer is unknown, preserve the gap rather than filling it.

### 5. Who may confirm it, and what does the approval cover?

Answer:

- Who confirmed the fact and wording?
- Which exact version did the user approve?
- What is the approved purpose?
- Does the approval cover the current action?
- Does the approval expire after the output changes?
- Who will perform the external action?

AI cannot approve itself and cannot interpret a general "okay" as authorization to sign, pay, file, send, or publish.

## Decision Rules

If any question fails, use one of these statuses:

```yaml
status: blocked_missing_evidence
status: blocked_missing_source
status: blocked_unresolved_conflict
status: draft_for_human_review
```

Only when all five questions are answered and no blocker remains may the output be marked:

```yaml
status: ready_for_human_action
```

`ready_for_human_action` still does not permit AI to execute. It means only that the material is ready for the human's final decision.

## Compact Record

| Question | Record |
| --- | --- |
| Content type | `fact / feeling / statement / legal_claim / procedural_status / hypothesis` |
| Evidentiary support | `EVD-...` or `none` |
| Official source | `SRC-...` or `none` |
| Uncertainty and conflicts | List each item |
| Approval scope | Action, version, purpose, approver, and time |

## Examples

### Example 1: "The provider did not perform"

- Type: a claim requiring factual support;
- Materials: order, chats, recordings, refund records, and platform-handling records;
- Boundary: the materials may prove non-performance of specific content at a specific time, not subjective malice;
- Uncertainty: partial performance, substitute performance, or mutual changes require item-by-item review;
- Approval: the user confirms the facts, wording, and purpose.

### Example 2: "The platform knew and should be liable"

- Type: a combination of factual and legal claims;
- Materials: prove separately what the platform knew, when it knew it, and what it did afterward;
- Authority: verify each element against official legal texts;
- Uncertainty: whether the platform was merely an information channel, whether it acted, and whether the legal threshold is met;
- Approval: the user reviews both fact and legal structure, with qualified advice where needed.

### Example 3: "I was disappointed"

- Type: feeling;
- Materials: no external proof required, but the statement must remain a feeling;
- Legal boundary: disappointment does not itself establish breach, fraud, fault, or liability;
- Approval: the user approves the public wording.

## Anti-Formalism Rule

Truth Five must not become a table of mechanical "yes" answers.

A valid answer needs locatable material, a specific source, and a reviewable reason. The following count as unanswered:

- "verified" with no source;
- "there is evidence" with no evidence ID;
- "the law says" with no statute and article;
- "the user agreed" with no version or action;
- "should be fine" with no listed risk or contrary evidence.

## Relationship to the Anti-Hallucination Protocol

- The Anti-Hallucination Protocol defines classifications, source rules, status tokens, and failure handling;
- Truth Five provides a compact minimum checklist before each output;
- neither replaces official legal verification, evidence review, or human responsibility;
- if they conflict, follow the stricter rule requiring more human confirmation.

## Status and Evolution

This protocol remains `PROPOSED`. Consider upgrading it only after:

- testing against multiple entirely synthetic cases;
- defining a record format for every question;
- distinguishing "verified," "ready to file," and "approved";
- public review finds no incentive toward mechanical box-checking;
- a Pull Request records the adoption rationale and residual risk.
