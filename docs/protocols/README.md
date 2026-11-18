# 协议总表

版本：`0.1.0`  
整理日期：`2026-11-18`  
状态：公开说明与索引

本目录回答两个问题：

1. 这个项目实际使用了哪些协议或规则？
2. 哪些由本项目制定，哪些是项目内嵌规则，哪些来自外部工作体系，哪些只是本次首次提出？

这里的“协议”不是合同，也不是法律意见。它指一套可执行的人机协作规则：规定输入、输出、证据要求、停止条件、批准边界和审计记录。

## 数量口径

当前公开仓库共整理 **13 个协议条目**：

| 状态 | 数量 | 含义 |
| --- | ---: | --- |
| `FORMAL` | 5 | 已有独立项目文件的正式规则 |
| `EMBEDDED` | 4 | 已写入项目配置、角色或技能，但此前没有独立协议文件 |
| `CONSOLIDATED` | 1 | 已有控制分散在多个文件中，本次首次整理为独立协议 |
| `ADOPTED` | 2 | 来自用户全局 Agent 环境的外部协议或规则 |
| `PROPOSED` | 1 | 本次首次书面提出，尚待公开讨论与实际检验 |

其中：

- 项目此前已经形成或内嵌的协议条目为 9 个；
- 本次首次显式整理 1 个，即防止幻觉协议；
- 本次首次提出 1 个，即“真实五问”；
- 从外部工作体系采用 2 个，即 AEP 3.1 与重要任务通知规则。

## 协议清单

| ID | 协议 | 状态 | 来源 | 公开入口 |
| --- | --- | --- | --- | --- |
| P-01 | AI 自诉工作协议 | `FORMAL` | 项目自有 | [PROTOCOL.md](../../PROTOCOL.md) |
| P-02 | 证据固定协议 | `FORMAL` | 项目自有 | [evidence-protocol.md](../evidence-protocol.md) |
| P-03 | 法律来源核验协议 | `FORMAL` | 项目自有 | [citation-protocol.md](../citation-protocol.md) |
| P-04 | 隐私最小化协议 | `FORMAL` | 项目自有 | [PRIVACY.md](../../PRIVACY.md) |
| P-05 | 公开安全与事件响应协议 | `FORMAL` | 项目自有 | [SECURITY.md](../../SECURITY.md)、[threat-model.md](../threat-model.md) |
| P-06 | 人工批准与外部动作边界 | `EMBEDDED` | 项目根 `AGENTS.md` 与 P-01 | 本文第“协议边界”节 |
| P-07 | 媒体发布合规协议 | `EMBEDDED` | 私有工作区发布技能 | 本文第“协议边界”节 |
| P-08 | Agent 角色加载协议 | `EMBEDDED` | 项目根 `AGENTS.md`、项目配置和角色库 | [agent-configuration.md](agent-configuration.md)、[agent-architecture.md](../agent-architecture.md) |
| P-09 | 项目状态、决策与审计协议 | `EMBEDDED` | 私有工作区项目管理目录 | [agent-configuration.md](agent-configuration.md) |
| P-10 | 重要任务通知协议 | `ADOPTED` | 用户全局 Agent 配置 | 本文第“外部规则”节 |
| P-11 | 防止幻觉协议 | `CONSOLIDATED` | 由 P-01 至 P-05 及项目红线整理 | [anti-hallucination-protocol.md](anti-hallucination-protocol.md) |
| P-12 | “真实五问”协议 | `PROPOSED` | 用户本次提出，本次首次书面固化 | [truth-five-protocol.md](truth-five-protocol.md) |
| P-13 | AEP 3.1 | `ADOPTED` | 用户全局 Agent 工作体系 | [aep-adoption.md](aep-adoption.md) |

## 哪些是项目自己制定的

项目自有或项目内嵌的条目为 P-01 至 P-09，以及基于这些规则整理的 P-11。

它们覆盖五条主线：

1. **证据真实性**：原件只读、哈希、来源、时间和证明目的；
2. **来源真实性**：官方法律文本、版本、条号和失败关闭；
3. **事实与主张分离**：事实、感受、对方陈述、法律主张和待核实信息不得混写；
4. **人工责任**：AI 只生成待审材料，签署、缴费、提交和发布由本人完成；
5. **可审计性**：状态、决策、批准、工作日志和输出版本可追溯。

## 哪些来自外部

### P-10 重要任务通知协议

来源是用户全局 Agent 配置，不是本项目原创。它只负责在重要或耗时任务完成、失败时发送一次简洁通知，不参与法律判断，也不构成对外发布授权。

### P-13 AEP 3.1

AEP 是用户全局 Agent 工作体系中的执行治理协议，不是本项目原创，也不是法律规范。本项目只采用与自诉辅助兼容的部分：

- 执行前说明目标、原因、影响和步骤；
- 技术或事实结论必须有依据，不确定内容标记为 `UNVERIFIED`；
- 执行过程必须反馈成功、失败和偏离；
- 错误和里程碑需要沉淀到状态记录。

当 AEP 与本项目的证据、来源、隐私或人工批准规则冲突时，本项目规则优先。

## “防止幻觉”与“真实五问”的准确来源

### 防止幻觉协议

此前没有一个名为“防止幻觉协议”的独立历史文件。但项目已经持续执行以下控制：

- 不虚构法条、案号、判例、裁判观点、政府答复或送达事实；
- 没有证据的事实只能标记为待核实；
- 没有官方来源的法律结论不得进入正式草稿；
- 搜索摘要、模型记忆和转载不能替代原文；
- 状态冲突或无法核验时必须停止。

因此，P-11 是将既有要求显式整理成独立协议，不是声称项目过去已经存在同名文件。

### “真实五问”

本次调查没有在项目历史文件、全局记忆、公开仓库或 AEP 3.1 中找到名为“真实五问”的正式协议。

因此，P-12 的状态是：

- `PROPOSED`，不是 `FORMAL`；
- 由用户本次提出；
- 本次首次书面固化；
- 可以用于公开讨论、测试和后续 PR；
- 不得宣传为项目早已制定、行业标准或法律要求。

## 协议优先级

发生冲突时，按以下顺序处理：

1. 现行法律、法院正式通知、期限和个人安全要求；
2. 用户本人对事实、版本、范围和外部动作的明确授权；
3. P-01 至 P-05 的强制边界；
4. P-11 防止幻觉协议与 P-12“真实五问”的核验门槛；
5. AEP 等执行层协议；
6. 通知、格式和平台适配规则。

任何内部协议都不能授权 AI 代替本人签署、缴费、提交法院、处分程序权利或对外发布。

## 协议边界

### P-06 人工批准与外部动作边界

AI 可以：

- 整理材料；
- 建立索引；
- 比较版本；
- 检索官方来源；
- 生成待审草稿；
- 列出风险和待确认事项。

AI 不得：

- 代替本人确认事实或金额；
- 伪造批准；
- 自动签署；
- 自动缴费；
- 自动向法院提交；
- 自动发送投诉；
- 自动发布社交媒体内容。

有效批准必须同时对应：具体动作、具体版本、具体用途、批准人和时间。任何一项变化都可能使原批准失效。

### P-07 媒体发布合规协议

发布前依次完成：

1. 事实底稿；
2. 事实、感受、对方陈述和法律主张分离；
3. 隐私脱敏；
4. 名誉权与传播风险审查；
5. 平台规则和 AI 内容标识检查；
6. 本人对最终标题、正文、图片、视频、平台和时间逐项确认；
7. 实际点击发布仍由本人完成。

### P-08 角色加载协议

每个会话先读取项目配置和当前状态，再按任务加载一个或多个领域角色。角色只提供专业工作边界，不产生执业律师身份，也不能绕过红线。

### P-09 状态、决策与审计协议

项目必须持续记录：

- 当前阶段；
- 已知期限；
- 来源冲突；
- 用户决策；
- 待确认事项；
- 产物版本和哈希；
- 已完成与未完成动作。

旧截图、旧状态和旧批准不得自动延续为当前事实。

## 标准执行链

```text
输入材料
  -> 分类为事实、感受、陈述、主张、状态或假设
  -> 关联证据编号与原件状态
  -> 关联官方法律来源与版本
  -> 执行防止幻觉检查
  -> 执行“真实五问”
  -> 生成待审草稿
  -> 本人逐项复核并批准
  -> 本人执行外部动作
  -> 记录结果、哈希和审计日志
```

任何一步失败，输出应停留在草稿或问题清单，不得被包装为确定结论。

## 维护规则

新增或修改协议必须通过 Pull Request，并说明：

- 修改原因；
- 影响的文件和数据字段；
- 新增或移除的停止条件；
- 与现有协议的冲突；
- 对应测试；
- 是否需要迁移旧记录。

---

# Protocol Registry

Version: `0.1.0`  
Consolidated: `2026-11-18`  
Status: public explanation and index

This directory answers two questions:

1. Which protocols or rules does this project actually use?
2. Which are project-authored, embedded in project configuration, adopted from an external workflow, or merely proposed here for the first time?

"Protocol" here does not mean a contract or legal advice. It means an executable human-AI rule set that defines inputs, outputs, evidence requirements, stop conditions, approval boundaries, and audit records.

## Counting Standard

This public repository currently consolidates **13 protocol entries**:

| Status | Count | Meaning |
| --- | ---: | --- |
| `FORMAL` | 5 | A formal rule with a dedicated project document |
| `EMBEDDED` | 4 | A rule already embedded in project configuration, roles, or skills without a standalone document |
| `CONSOLIDATED` | 1 | Controls previously distributed across files and explicitly consolidated here for the first time |
| `ADOPTED` | 2 | An external protocol or rule from the user's global agent environment |
| `PROPOSED` | 1 | First written proposal in this repository, pending public review and testing |

Specifically:

- Nine protocol entries already existed in or were embedded in the project;
- One protocol, the anti-hallucination protocol, is explicitly consolidated for the first time;
- One protocol, Truth Five, is proposed for the first time;
- Two protocols, AEP 3.1 and the important-task notification rule, are adopted from the user's external global environment.

## Protocol List

| ID | Protocol | Status | Origin | Public entry |
| --- | --- | --- | --- | --- |
| P-01 | AI Self-Litigation Work Protocol | `FORMAL` | Project-authored | [PROTOCOL.md](../../PROTOCOL.md) |
| P-02 | Evidence Preservation Protocol | `FORMAL` | Project-authored | [evidence-protocol.md](../evidence-protocol.md) |
| P-03 | Legal Source Verification Protocol | `FORMAL` | Project-authored | [citation-protocol.md](../citation-protocol.md) |
| P-04 | Privacy Minimization Protocol | `FORMAL` | Project-authored | [PRIVACY.md](../../PRIVACY.md) |
| P-05 | Public Safety and Incident Response Protocol | `FORMAL` | Project-authored | [SECURITY.md](../../SECURITY.md), [threat-model.md](../threat-model.md) |
| P-06 | Human Approval and External Action Boundary | `EMBEDDED` | Private project `AGENTS.md` and P-01 | The "Protocol Boundaries" section below |
| P-07 | Media Publication Compliance Protocol | `EMBEDDED` | Private-workspace publishing skill | The "Protocol Boundaries" section below |
| P-08 | Agent Role Loading Protocol | `EMBEDDED` | Private project `AGENTS.md`, configuration, and role registry | [agent-configuration.md](agent-configuration.md), [agent-architecture.md](../agent-architecture.md) |
| P-09 | Project State, Decision, and Audit Protocol | `EMBEDDED` | Private-workspace project-management directory | [agent-configuration.md](agent-configuration.md) |
| P-10 | Important Task Notification Protocol | `ADOPTED` | User's global agent configuration | The "External Rules" section below |
| P-11 | Anti-Hallucination Protocol | `CONSOLIDATED` | Consolidated from P-01 through P-05 and project red lines | [anti-hallucination-protocol.md](anti-hallucination-protocol.md) |
| P-12 | Truth Five Protocol | `PROPOSED` | Proposed by the user and first written here | [truth-five-protocol.md](truth-five-protocol.md) |
| P-13 | AEP 3.1 | `ADOPTED` | User's global agent workflow | [aep-adoption.md](aep-adoption.md) |

## What the Project Authored

P-01 through P-09 and the consolidated P-11 are project-authored or project-embedded.

They cover five main lines of control:

1. **Evidence integrity**: read-only originals, hashes, source, time, and evidentiary purpose;
2. **Source integrity**: official legal texts, versions, article numbers, and fail-closed handling;
3. **Fact-claim separation**: facts, feelings, statements by others, legal claims, and unverified information must not be merged;
4. **Human responsibility**: AI produces review drafts only; signing, payment, filing, and publication remain human actions;
5. **Auditability**: status, decisions, approvals, work logs, and output versions remain traceable.

## External Rules

### P-10 Important Task Notification Protocol

This rule comes from the user's global agent configuration, not this project. It only sends a concise notification after an important or long-running task succeeds or fails. It does not make legal judgments and does not authorize publication.

### P-13 AEP 3.1

AEP is an execution-governance protocol in the user's global agent workflow. It is neither project-authored nor a legal standard.

This project adopts the compatible parts:

- state the objective, reason, impact, and steps before execution;
- require support for technical or factual claims and mark uncertainty as `UNVERIFIED`;
- report success, failure, and deviation;
- consolidate errors and milestones into state records.

Where AEP conflicts with this project's evidence, source, privacy, or human-approval rules, the project rules prevail.

## Accurate Provenance of Anti-Hallucination and Truth Five

### Anti-Hallucination Protocol

No standalone historical file named "Anti-Hallucination Protocol" existed before this consolidation. The project already enforced these controls:

- Do not invent statutes, case numbers, judicial opinions, government replies, or service facts;
- A fact without evidence must remain unverified;
- A legal conclusion without an official source must not enter a formal draft;
- Search snippets, model memory, and reposts cannot replace original texts;
- Stop when a critical source or status conflicts.

P-11 therefore consolidates existing requirements into an explicit protocol. It does not claim that the same standalone file existed in the past.

### Truth Five

The investigation for this version found no formal "Truth Five" protocol in project history, global memory, the public repository, or AEP 3.1.

P-12 is therefore:

- `PROPOSED`, not `FORMAL`;
- introduced by the user in the current task;
- written down explicitly for the first time;
- available for public review, testing, and later Pull Requests;
- not to be described as a long-established project rule, industry standard, or legal requirement.

## Protocol Priority

When rules conflict, use this order:

1. Applicable law, formal court notices, deadlines, and personal safety;
2. The user's explicit authorization concerning facts, versions, scope, and external actions;
3. Mandatory boundaries in P-01 through P-05;
4. Verification gates in P-11 and P-12;
5. Execution-layer protocols such as AEP;
6. Notification, formatting, and platform-adaptation rules.

No internal protocol authorizes AI to sign, pay, file with a court, waive procedural rights, or publish on the user's behalf.

## Protocol Boundaries

### P-06 Human Approval and External Action Boundary

AI may:

- organize materials;
- build indexes;
- compare versions;
- retrieve official sources;
- create review drafts;
- list risks and items requiring confirmation.

AI may not:

- confirm facts or amounts for the user;
- forge approval;
- sign documents;
- make payments;
- file with a court;
- send complaints;
- publish social-media content.

Valid approval must identify the exact action, version, purpose, approving person, and time. A change to any one of them may invalidate the earlier approval.

### P-07 Media Publication Compliance Protocol

Before publication:

1. Build a factual record;
2. Separate facts, feelings, statements by others, and legal claims;
3. Redact private information;
4. Review defamation and publicity risk;
5. Check platform rules and AI-content labeling requirements;
6. Obtain human approval for the exact title, text, images, video, platform, and time;
7. Leave the final publishing click to the user.

### P-08 Agent Role Loading Protocol

Each session reads project configuration and current status first, then loads one or more domain roles required by the task. A role supplies a professional working boundary. It does not make the model a licensed lawyer and cannot bypass project red lines.

### P-09 State, Decision, and Audit Protocol

The project records:

- current stage;
- known deadlines;
- source conflicts;
- user decisions;
- open questions;
- artifact versions and hashes;
- completed and uncompleted actions.

An old screenshot, status, or approval never automatically becomes a current fact.

## Standard Execution Chain

```text
Input material
  -> classify as fact, feeling, statement, claim, status, or hypothesis
  -> attach evidence IDs and original-file status
  -> attach official legal source and version
  -> run anti-hallucination checks
  -> run Truth Five
  -> produce a review draft
  -> obtain item-by-item human approval
  -> human performs the external action
  -> record outcome, hash, and audit log
```

If any step fails, the output must remain a draft or an issue list. It must not be presented as a settled conclusion.

## Change Control

New or amended protocols require a Pull Request explaining:

- why the change is needed;
- affected files and data fields;
- new or removed stop conditions;
- conflicts with existing protocols;
- corresponding tests;
- whether old records require migration.
