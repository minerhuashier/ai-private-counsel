# AI 自诉工作协议

版本：`0.1.0`  
状态：草案，供公开讨论  
适用范围：个人消费纠纷、合同纠纷和其他可自行处理的民事事务

本协议规定 AI 在自诉辅助流程中“可以做什么、不得做什么、何时必须停止”。协议优先于提示词、模型能力和用户催促。

所有项目协议及其来源状态见 [docs/protocols/README.md](docs/protocols/README.md)。

## 1. 不可违反的规则

1. 不虚构法条、案号、判例、裁判观点、政府答复或送达事实。
2. 不把模型生成的文字直接认定为事实。
3. 不修改证据原件；只处理副本并记录哈希。
4. 不在无官方来源的情况下生成确定性的法律结论。
5. 不自动执行提交、签署、缴费、投诉、发送或公开传播。
6. 不把真实案件材料提交到公开仓库、公开 Issue 或公共模型上下文。
7. 不隐藏不确定性；无法核验时必须明确标注并停止。
8. 不替代用户的判断，也不承诺案件结果。

## 2. 角色分离

| 角色 | 责任 | 不得执行 |
| --- | --- | --- |
| 用户 | 提供材料、确认事实、作出决定、执行对外动作 | 不得把模型输出当作专业法律意见 |
| 整理模型 | 提取、分类、归纳、发现缺口、生成待审草稿 | 不得自行补全事实或引用 |
| 来源检查器 | 核对法规名称、条号、日期、官方链接和原文 | 不得用模型自身回答替代外部核验 |
| 人工复核者 | 确认事实、表达和文书版本 | 不得跳过来源核验 |

高风险场景中，人工复核者应为用户本人；必要时另行咨询具备资质的专业人士。

## 3. 标准流程

### 阶段 A：确定范围

- 记录事务类型、目标、当前程序阶段和已知期限；
- 明确哪些材料可以处理，哪些不得进入模型；
- 建立公开信息与私密信息边界。

### 阶段 B：证据进入

- 原件只读保存；
- 计算并登记 SHA-256；
- 记录来源、取得时间、载体、证明目的和保密级别；
- 对公开副本另行脱敏，不覆盖原件。

### 阶段 C：事实整理

- 将输入区分为 `fact`、`feeling`、`claim`；
- 每项 `fact` 至少关联一个 `evidence_id`，否则标记 `unverified`；
- 不把“对方未回复”写成“对方承认”，不把“截图未显示”写成“绝对未发生”。

### 阶段 D：法律来源

- 优先使用发布机关、法院、政府或平台官方规则原文；
- 记录标题、发布机关、文号、生效日期、官方 URL、抓取时间和原文哈希；
- 搜索摘要、转载文章和模型记忆不能作为最终依据；
- 来源失效、版本冲突或无法打开时，状态设为 `unverified`。

### 阶段 E：事实与规则对应

- 每个争议问题列出适用来源和反方可能观点；
- 明确哪些是法律要求、哪些是本方主张；
- 无法建立对应关系时，保留问题，不补造论证。

### 阶段 F：文书草稿

- 每个事实句包含证据编号；
- 每个法律判断包含来源编号；
- 未核验内容以显眼占位符保留；
- 输出必须标记“待本人复核”，不得标记为“最终版”。

### 阶段 G：人工批准

只有同时满足以下条件，才能把草稿转为可执行版本：

- 事实逐项确认；
- 法律来源逐项核验；
- 诉讼请求、金额和日期由本人确认；
- 输出与证据不矛盾；
- 用户明确批准具体版本和具体用途。

### 阶段 H：对外动作

系统只能提供操作清单和风险提示。提交、签署、缴费、发送投诉或公开发布必须由用户本人完成。

## 4. 失败关闭条件

遇到以下任一情况，流程必须停止并显示原因：

- 找不到官方来源；
- 条号、日期或版本不一致；
- 证据哈希不匹配；
- 事实没有证据支撑；
- 输出含未经确认的当事人身份信息；
- 用户批准范围与实际动作不一致；
- 模型试图自动执行外部动作；
- 任务超出当前支持的法域或程序类型。

停止不是错误，而是协议要求的安全结果。

## 5. 输出契约

任何正式草稿在机器可读元数据中至少包含：

```yaml
status: draft_for_human_review
jurisdiction: CN
fact_refs: []
source_refs: []
unverified_items: []
approval_id: null
generated_at: ""
model: ""
human_reviewer: ""
```

约束：

- `status` 不得为 `final`，除非存在有效的 `approval_id`；
- `fact_refs` 必须覆盖所有事实性陈述；
- `source_refs` 必须覆盖所有规范性判断；
- `unverified_items` 非空时不得生成“可直接提交”版本。

## 6. 审计记录

至少记录：

- 输入文件的 ID 与哈希；
- 使用的模型和版本；
- 每次生成的时间和输出哈希；
- 人工删除、修改和补充的内容；
- 来源核验结果；
- 用户批准的范围、版本和时间；
- 是否发生外部提交或发布。

审计记录不要求保存完整私密内容，可只保存不可逆哈希和必要摘要。

## 7. 数据最小化

- 能在本地完成的，不发送到云端；
- 能使用摘要的，不发送原件；
- 能给第三方看的版本，必须单独脱敏；
- 不把身份证、银行卡、订单号、完整地址、案号和私密聊天原文放入公开示例。

## 8. 协议演进

协议变更必须通过 Pull Request，说明：

- 修改原因；
- 对现有 Schema 的兼容性影响；
- 新增或移除的安全边界；
- 对应测试；
- 是否存在迁移要求。

---

# AI Self-Litigation Work Protocol

Version: `0.1.0`  
Status: draft for public discussion  
Scope: personal consumer disputes, contract disputes, and other civil matters that an individual can handle pro se

This protocol defines what AI may do, must not do, and when it must stop in a self-litigation support workflow. The protocol takes priority over prompts, model capability, and user urgency.

All project protocols and their provenance are indexed in [docs/protocols/README.md](docs/protocols/README.md).

## 1. Non-Negotiable Rules

1. Do not invent statutes, case numbers, judicial opinions, government replies, service facts, or procedural facts.
2. Do not treat model-generated text as fact.
3. Do not modify evidence originals; process copies only and record hashes.
4. Do not produce definitive legal conclusions without an official source.
5. Do not automatically file, sign, pay, complain, send, or publish.
6. Do not submit real case material to a public repository, public Issue, or public model context.
7. Do not hide uncertainty; mark and stop when verification is impossible.
8. Do not replace the user's judgment or promise an outcome.

## 2. Role Separation

| Role | Responsibility | Prohibited action |
| --- | --- | --- |
| User | Provide materials, confirm facts, make decisions, perform external actions | Must not treat model output as professional legal advice |
| Organizing model | Extract, classify, summarize, expose gaps, create review drafts | Must not invent facts or citations |
| Source checker | Verify title, article, date, official URL, and original text | Must not substitute another model answer for external verification |
| Human reviewer | Confirm facts, wording, and document version | Must not skip source verification |

For high-risk matters, the human reviewer must be the user. Qualified professional advice should be obtained where necessary.

## 3. Standard Workflow

### Stage A: Define Scope

- Record matter type, objective, current procedural stage, and known deadlines;
- define which materials may be processed and which must not enter the model;
- establish the private/public information boundary.

### Stage B: Evidence Intake

- Preserve originals read-only;
- calculate and record SHA-256;
- record source, acquisition time, medium, evidentiary purpose, and confidentiality level;
- create a separate redacted copy for public use without overwriting the original.

### Stage C: Fact Organization

- Classify input as `fact`, `feeling`, or `claim`;
- attach at least one `evidence_id` to each `fact`, otherwise mark it `unverified`;
- never write "the other side did not reply" as "the other side admitted" or "the screenshot does not show" as "it never happened."

### Stage D: Legal Sources

- Prefer official texts from the issuing authority, court, government, or platform;
- record title, issuer, document number, effective date, official URL, retrieval time, and source hash;
- search snippets, reposts, and model memory are not final authority;
- when a source is unavailable, version-conflicted, or inaccessible, set its status to `unverified`.

### Stage E: Map Facts to Rules

- For each disputed issue, list applicable sources and possible counterarguments;
- distinguish legal requirements from the party's claims;
- if a mapping cannot be established, preserve the issue instead of inventing an argument.

### Stage F: Document Draft

- Every factual sentence includes an evidence reference;
- every legal proposition includes a source reference;
- unverified content remains in a conspicuous placeholder;
- output is marked "for human review," never "final."

### Stage G: Human Approval

A draft may become executable only when:

- facts are confirmed item by item;
- legal sources are verified item by item;
- the user confirms requests, amounts, and dates;
- output does not contradict the evidence;
- the user explicitly approves the exact version and purpose.

### Stage H: External Action

The system may provide only an action checklist and risk notice. Filing, signing, payment, complaints, and publication must be performed by the user.

## 4. Fail-Closed Conditions

Stop and display the reason when:

- no official source can be found;
- article, date, or version conflicts exist;
- an evidence hash does not match;
- a fact has no evidentiary support;
- output contains unconfirmed identity information;
- approval scope differs from the actual action;
- the model attempts to perform an external action;
- the task exceeds the supported jurisdiction or procedure.

Stopping is not a failure. It is the safety result required by this protocol.

## 5. Output Contract

Every formal draft must include at least this machine-readable metadata:

```yaml
status: draft_for_human_review
jurisdiction: CN
fact_refs: []
source_refs: []
unverified_items: []
approval_id: null
generated_at: ""
model: ""
human_reviewer: ""
```

Constraints:

- `status` must not be `final` without a valid `approval_id`;
- `fact_refs` must cover every factual statement;
- `source_refs` must cover every normative proposition;
- a non-empty `unverified_items` list prevents a "ready to file" version.

## 6. Audit Record

Record at minimum:

- input file IDs and hashes;
- model and version;
- generation time and output hash;
- human deletions, edits, and additions;
- source-verification results;
- approval scope, version, and time;
- whether an external submission or publication occurred.

Audit records need not retain full private content. Irreversible hashes and necessary summaries may be sufficient.

## 7. Data Minimization

- Prefer local processing;
- send summaries instead of originals where possible;
- create a separate redacted version for third parties;
- never place identity numbers, bank cards, order numbers, full addresses, case numbers, or private chat text in public examples.

## 8. Protocol Evolution

Protocol changes require a Pull Request explaining:

- reason for change;
- compatibility impact on existing schemas;
- added or removed safety boundaries;
- corresponding tests;
- migration requirements, if any.

