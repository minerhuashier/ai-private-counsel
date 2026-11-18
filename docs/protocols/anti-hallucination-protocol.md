# 防止幻觉协议

版本：`0.1.0`  
状态：`CONSOLIDATED / 已整理固化`  
首次显式整理：`2026-11-18`  
来源：项目既有红线、AI 自诉工作协议、证据协议、法律来源核验协议、隐私规范和安全政策

## 目的

AI 生成的流畅文字不等于事实、证据或法律结论。本协议规定：在 AI 输出可以进入公共材料、对外沟通或法院文书草稿之前，必须如何区分事实、来源、推断和不确定性。

本协议不是声称项目过去存在完全相同的独立文件。它把此前分散在多个项目文件中的控制统一成可执行的单一门槛。

## 核心规则

1. **没有证据的事实，不写成事实。**  
   事实性陈述必须关联可定位的证据编号；没有证据时标记为 `UNVERIFIED`。

2. **没有官方来源的法律判断，不写成结论。**  
   法条、司法解释、程序规则和平台规则必须回到可追溯的官方原文，并记录版本和生效日期。

3. **不虚构任何权威。**  
   禁止生成不存在的法条、条号、案号、判例、裁判观点、政府答复、送达事实或平台处理结果。

4. **不把“页面状态”扩大为“客观全貌”。**  
   页面未显示、系统未同步、对方未回复，只能描述为对应来源在特定时间显示的状态。

5. **不隐藏不确定性。**  
   不确定、冲突、过期或缺少来源的内容必须显式标记，不能被更流畅的措辞覆盖。

6. **模型不得自行补全。**  
   缺少日期、金额、当事人、条号、证据或程序信息时，保留空缺并列为待确认事项。

7. **失败关闭。**  
   关键证据、来源或状态无法核验时，停止生成确定性结论，转为问题清单。

8. **人工负责。**  
   防止幻觉协议降低错误概率，但不替代本人复核、官方法律文本核对或必要的专业意见。

## 内容分类

每条材料或输出至少归入以下一类：

| 类型 | 定义 | 最低要求 |
| --- | --- | --- |
| `fact` | 可定位的客观事件 | 证据编号、来源、时间范围、本人确认 |
| `feeling` | 本人的感受或体验 | 明确写成感受，不冒充客观事实 |
| `statement` | 他人曾作出的陈述 | 记录原话、说话人、时间和载体 |
| `legal_claim` | 本方的法律评价或请求 | 官方来源、事实基础、适用边界 |
| `procedural_status` | 法院、平台或机构的状态 | 来源、显示时间、是否正式文书、是否可能滞后 |
| `hypothesis` | 尚未验证的解释 | 明确标记为假设，不得进入正式结论 |
| `model_suggestion` | AI 的方案或表达建议 | 不作为事实或法律依据 |
| `unverified` | 当前无法确认的内容 | 写明缺失项、核验路径和责任人 |

## 强制核验链

### 门槛 1：存在性

- 该法条、案例、通知、页面、证据或事实是否真实存在？
- 是否有原始材料或官方 URL？
- 是否只是模型记忆、搜索摘要或他人的二手描述？

### 门槛 2：来源

- 来源发布机关是谁？
- 是否是官方页面、原始文件或可定位载体？
- 是否有抓取时间、文件哈希和获取方式？

### 门槛 3：版本

- 文号、公布日期和生效日期是什么？
- 是否已经修订、废止或被新版本替代？
- 平台规则是否适用于争议发生时的版本？

### 门槛 4：支持关系

- 原文是否真的支持当前结论？
- 条号和引文是否逐字一致？
- 证据是否能够证明所写事实，还是只能证明某个页面曾经显示？

### 门槛 5：边界

- 该来源的适用范围、地域、主体和时间边界是什么？
- 是否把平台规则写成法律义务？
- 是否把法院接收材料写成法院采信？
- 是否把银行扣款写成法院完成入账？

### 门槛 6：冲突

- 同一事实是否存在相反证据？
- 正式文书与平台页面是否不同步？
- 新通知是否改变旧期限、程序或状态？
- 冲突未解决前，不得自行选择更有利的版本。

### 门槛 7：批准

- 谁确认了该事实？
- 谁批准了该版本和用途？
- 批准是否覆盖当前动作？
- 输出修改后，原批准是否仍然有效？

## 状态标记

公开工具和草稿可以使用以下机器可读状态：

```yaml
verification_status: verified | unverified | disputed | superseded | repealed
fact_classification: fact | feeling | statement | legal_claim | procedural_status | hypothesis
human_confirmation: confirmed | pending | rejected
approval_status: none | pending | approved | expired | revoked
```

约束：

- `verified` 只表示来源和原文核验完成，不表示法院已经采信；
- `unverified` 内容不得进入“可直接提交”版本；
- `disputed` 内容必须同时保留冲突来源；
- `superseded` 或 `repealed` 来源不得作为当前法律依据；
- `approved` 必须关联具体版本、动作、批准人和时间。

## 高风险幻觉清单

以下内容最容易被模型“补全”，必须逐项核对：

- 法条条号、修改年份、施行日期；
- 案件名称、案号、法院层级和裁判结果；
- 政府机关、平台客服或法院曾作出某项答复；
- 证据截图中未出现、但模型推测存在的内容；
- 金额、日期、期限、利率和计算过程；
- 送达、立案、缴费、入账、提交或撤回状态；
- 对方的主观故意、明知或承认；
- 用户曾作出某项批准；
- AI 完成了某项外部动作。

## 输出前检查

任何正式草稿输出前必须回答：

1. 哪些句子是事实？
2. 每个事实对应哪个证据编号？
3. 哪些句子是法律主张？
4. 每个法律主张对应哪个官方来源和版本？
5. 哪些内容仍是假设、冲突或空白？
6. 哪些动作需要本人重新批准？

任一问题无法回答时，输出状态只能是：

```yaml
status: draft_for_human_review
unverified_items:
  - "<具体缺失项>"
approval_id: null
```

## 失败处理

触发以下任一条件时，停止确定性输出：

- 找不到原始证据；
- 证据哈希不匹配；
- 找不到官方法律来源；
- 条号、版本或生效日期冲突；
- 正式文书与平台状态冲突；
- 事实陈述包含未被证据支持的推断；
- 输出含未经确认的身份信息；
- 批准范围不明确；
- 模型试图执行或声称已经执行外部动作。

停止后输出：

- 已确认内容；
- 未确认内容；
- 冲突来源；
- 需要补充的材料；
- 下一步核验路径；
- 必须由本人作出的决定。

## 记录模板

```yaml
claim_id: CLM-EXAMPLE-001
statement: ""
classification: fact
evidence_refs: []
source_refs: []
verification_status: unverified
conflicts: []
unverified_reason: ""
human_confirmation: pending
approval_status: none
reviewed_at: ""
reviewer: ""
```

## 边界

本协议不能：

- 保证 AI 永不犯错；
- 代替官方法律文本；
- 代替法院对事实和法律的判断；
- 代替执业律师的专业意见；
- 授权 AI 自动签署、缴费、提交、发送或发布。

它只能让错误更容易被发现，让不确定内容更难以被伪装成确定结论。

---

# Anti-Hallucination Protocol

Version: `0.1.0`  
Status: `CONSOLIDATED`  
First explicit consolidation: `2026-11-18`  
Origin: existing project red lines, AI Self-Litigation Work Protocol, Evidence Preservation Protocol, Legal Source Verification Protocol, Privacy Minimization Protocol, and Security Policy

## Purpose

Fluent AI text is not a fact, evidence, or legal conclusion. This protocol defines how fact, source, inference, and uncertainty must be separated before AI output enters public material, external communication, or a court-document draft.

This document does not claim that an identical standalone file existed in the past. It consolidates controls previously distributed across project files into one executable gate.

## Core Rules

1. **No evidence, no factual assertion.**  
   A factual statement must reference a locatable evidence ID. Without evidence, mark it `UNVERIFIED`.

2. **No official source, no legal conclusion.**  
   Statutes, judicial interpretations, procedural rules, and platform rules must be checked against a traceable official text, including version and effective date.

3. **Invent no authority.**  
   Never generate nonexistent statutes, article numbers, case numbers, judicial opinions, government replies, service facts, or platform outcomes.

4. **Do not expand a page state into the whole truth.**  
   "The page does not show," "the system has not synchronized," and "the other side has not replied" describe only a source state at a particular time.

5. **Do not hide uncertainty.**  
   Uncertain, disputed, outdated, or unsupported content must be marked explicitly and cannot be covered by smoother wording.

6. **The model may not fill gaps.**  
   When a date, amount, party, article number, evidence item, or procedural fact is missing, preserve the gap and list it for confirmation.

7. **Fail closed.**  
   If critical evidence, a source, or a status cannot be verified, stop producing a definitive conclusion and return an issue list.

8. **Humans remain responsible.**  
   This protocol reduces error probability but does not replace human review, official-text checking, or qualified advice when needed.

## Content Classification

Every material item or output must be classified as at least one of:

| Type | Definition | Minimum requirement |
| --- | --- | --- |
| `fact` | A locatable objective event | Evidence ID, source, time range, human confirmation |
| `feeling` | The user's experience or emotion | Clearly labeled as a feeling |
| `statement` | Something another person said | Exact words where possible, speaker, time, and medium |
| `legal_claim` | A legal characterization or request | Official source, factual basis, and scope |
| `procedural_status` | A court, platform, or agency state | Source, display time, formal-document status, synchronization caveat |
| `hypothesis` | An unverified explanation | Explicitly marked and excluded from formal conclusions |
| `model_suggestion` | An AI proposal or wording option | Never treated as fact or legal authority |
| `unverified` | Content that cannot yet be confirmed | Missing item, verification path, and owner |

## Mandatory Verification Chain

### Gate 1: Existence

- Does the statute, case, notice, page, evidence item, or fact actually exist?
- Is there an original file or official URL?
- Is this only model memory, a search snippet, or a secondary description?

### Gate 2: Source

- Who issued the source?
- Is it an official page, an original file, or another locatable medium?
- Are retrieval time, file hash, and acquisition method recorded?

### Gate 3: Version

- What are the document number, publication date, and effective date?
- Has it been amended, repealed, or superseded?
- Did the platform rule version apply at the time of the dispute?

### Gate 4: Support

- Does the original text actually support the proposition?
- Are the article number and quotation exact?
- Does the evidence prove the stated fact, or only that a page displayed something at a specific time?

### Gate 5: Boundary

- What are the source's subject, geographic, temporal, and procedural limits?
- Is a platform rule being misdescribed as a statutory duty?
- Is court receipt being misdescribed as court acceptance?
- Is a bank debit being misdescribed as completed court accounting?

### Gate 6: Conflict

- Is there contrary evidence?
- Do formal documents and platform pages disagree?
- Does a newer notice alter an earlier deadline, procedure, or status?
- Until the conflict is resolved, do not select the more favorable version.

### Gate 7: Approval

- Who confirmed the fact?
- Who approved this version and purpose?
- Does the approval cover the current action?
- Does the approval remain valid after the output changes?

## Status Tokens

```yaml
verification_status: verified | unverified | disputed | superseded | repealed
fact_classification: fact | feeling | statement | legal_claim | procedural_status | hypothesis
human_confirmation: confirmed | pending | rejected
approval_status: none | pending | approved | expired | revoked
```

Constraints:

- `verified` means the source and original text were checked; it does not mean a court accepted the claim;
- `unverified` content must not enter a "ready to file" version;
- `disputed` content must preserve all conflicting sources;
- `superseded` or `repealed` sources are not current authority;
- `approved` must identify the exact version, action, approver, and time.

## High-Risk Hallucination List

Check these items with special care:

- article numbers, amendment years, and effective dates;
- case names, case numbers, court levels, and outcomes;
- alleged replies from governments, platform support, or courts;
- content the model infers but a screenshot does not show;
- amounts, dates, deadlines, interest rates, and calculations;
- service, filing, payment, accounting, submission, or withdrawal status;
- subjective intent, knowledge, or admission by another party;
- an alleged user approval;
- an external action the AI claims to have completed.

## Pre-Output Checklist

Before any formal draft leaves the system:

1. Which sentences are facts?
2. Which evidence ID supports each fact?
3. Which sentences are legal claims?
4. Which official source and version support each legal claim?
5. What remains hypothetical, disputed, or missing?
6. Which actions require fresh human approval?

If any question cannot be answered, the only valid status is:

```yaml
status: draft_for_human_review
unverified_items:
  - "<specific missing item>"
approval_id: null
```

## Failure Handling

Stop definitive output when:

- no original evidence can be found;
- an evidence hash does not match;
- no official legal source can be found;
- article, version, or effective-date conflicts remain;
- formal documents and platform status conflict;
- a factual statement contains unsupported inference;
- output contains unconfirmed identity information;
- approval scope is unclear;
- the model attempts or claims to perform an external action.

After stopping, return:

- confirmed content;
- unconfirmed content;
- conflicting sources;
- missing materials;
- verification steps;
- decisions reserved for the human.

## Record Template

```yaml
claim_id: CLM-EXAMPLE-001
statement: ""
classification: fact
evidence_refs: []
source_refs: []
verification_status: unverified
conflicts: []
unverified_reason: ""
human_confirmation: pending
approval_status: none
reviewed_at: ""
reviewer: ""
```

## Limits

This protocol cannot:

- guarantee that AI never errs;
- replace official legal texts;
- replace a court's determination of fact or law;
- replace qualified legal advice;
- authorize AI to sign, pay, file, send, or publish.

It can only make errors easier to find and make uncertainty harder to disguise as certainty.
