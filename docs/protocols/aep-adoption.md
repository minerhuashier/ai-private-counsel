# AEP 3.1 采用说明

版本：`0.1.0`  
状态：`ADOPTED / 外部执行协议`  
来源：用户全局 Agent 工作体系  
适用方式：仅采用与本项目安全边界兼容的执行纪律

## 为什么单独说明

AEP 3.1 全称为 Agentic Evolution Protocol 3.1。它是一套面向 Agent 的执行治理协议，不是本项目原创，也不是法律、司法解释、诉讼规则或律师执业规范。

项目公开文档必须避免两种错误：

1. 把 AEP 写成项目自制的法律协议；
2. 把 AEP 写成高于证据、官方法律来源或本人授权的强制依据。

准确表述是：

> 本项目参考并采用 AEP 3.1 中适合自诉辅助的执行纪律，但所有法律、证据、隐私和人工批准边界仍以本项目专门协议为准。

## 采用的四个 Node

### Node 1：Pre-Execution Alignment

执行前说明：

- 要完成什么；
- 为什么做；
- 影响等级；
- 准备怎么做；
- 是否需要读取历史状态或记忆。

在法律任务中，这一 Node 还要求先确认：

- 当前程序阶段；
- 是否存在期限；
- 是否需要加载领域角色；
- 是否涉及对外动作。

### Node 2：Truth Protocol

采用的核心原则是：

- 结论必须有依据；
- 不确定内容标记为 `UNVERIFIED`；
- 修改核心配置、记忆或注册表前需要明确授权。

在本项目中，该原则被具体化为：

- 事实必须关联证据；
- 法律判断必须关联官方法律来源；
- 搜索结果只是线索；
- 模型记忆不能替代原始来源；
- 无法核验时失败关闭。

### Node 3：Execution Feedback

每次关键工具操作后报告：

- `SUCCESS`；
- `FAILURE`；
- 结果是否符合预期；
- 是否需要重新规划。

若连续两次偏离目标，停止并重新说明问题，而不是继续堆叠操作。

### Node 4：Evolution Consolidation

将错误、纠正和里程碑沉淀到项目状态与日志。

在本项目中，长期事实以项目工作区和审计记录为准，不以模型“记住”为准。全局记忆当前没有可用于本项目的案件事实，不能成为证据来源。

## 本项目中的优先级

采用 AEP 后，优先级仍然是：

1. 法律和正式程序要求；
2. 用户本人对事实和外部动作的授权；
3. 项目证据、来源、隐私和批准协议；
4. AEP 执行纪律；
5. 通知和格式偏好。

AEP 不能：

- 证明事实；
- 替代法律来源；
- 让模型成为律师；
- 授权自动签署、缴费、提交或发布；
- 推翻法院正式通知；
- 把“执行成功”写成“法律结论正确”。

## 已知差异

AEP 面向通用业务 Agent，本项目的核心是证据密集、程序敏感的自诉辅助。因此：

- AEP 的“技术条款引用”在本项目中扩展为法律、司法解释、平台规则和程序来源；
- AEP 的“执行反馈”不能把文件写入成功等同于事实核验成功；
- AEP 的“演进固化”不得把私密案件材料写入公开仓库；
- AEP 的记忆能力不能替代原始证据和正式文书。

## 最低采用清单

- [ ] 执行前说明目标和影响；
- [ ] 读取当前项目状态；
- [ ] 标记不确定内容；
- [ ] 报告关键操作结果；
- [ ] 发生偏离时重新规划；
- [ ] 将结论写入项目记录，而不是只留在对话中；
- [ ] 不把 AEP 当成法律依据。

---

# AEP 3.1 Adoption Note

Version: `0.1.0`  
Status: `ADOPTED / external execution protocol`  
Origin: the user's global agent workflow  
Application: only the execution discipline compatible with this project's safety boundaries

## Why This Note Exists

AEP 3.1 stands for Agentic Evolution Protocol 3.1. It is an agent execution-governance protocol. It is not project-authored and is not a statute, judicial interpretation, procedural rule, or professional legal standard.

This public document avoids two errors:

1. describing AEP as a project-authored legal protocol;
2. treating AEP as authority superior to evidence, official legal sources, or human authorization.

The accurate statement is:

> This project references and adopts the parts of AEP 3.1 that fit self-litigation support as execution discipline. All legal, evidentiary, privacy, and human-approval boundaries remain governed by the project's dedicated protocols.

## Adopted Nodes

### Node 1: Pre-Execution Alignment

Before execution, state:

- what will be done;
- why;
- impact level;
- how;
- whether prior state or memory must be consulted.

For legal work, this also requires checking:

- the current procedural stage;
- whether a deadline exists;
- which domain role should be loaded;
- whether an external action is involved.

### Node 2: Truth Protocol

Adopted principles:

- conclusions require support;
- uncertain data must be marked `UNVERIFIED`;
- changing core configuration, memory, or registries requires explicit authorization.

In this project:

- facts must reference evidence;
- legal conclusions must reference official legal sources;
- search results are leads, not authority;
- model memory cannot replace original sources;
- failure to verify requires fail-closed handling.

### Node 3: Execution Feedback

After every critical tool action, report:

- `SUCCESS`;
- `FAILURE`;
- whether the result matched the plan;
- whether re-planning is required.

After two consecutive deviations, stop and restate the problem instead of piling on more actions.

### Node 4: Evolution Consolidation

Record errors, corrections, and milestones in project state and logs.

For this project, durable facts belong in the working workspace and audit records, not in model memory. The current global memory contains no case facts and cannot serve as evidence.

## Priority Within This Project

After adopting AEP, priority remains:

1. law and formal procedural requirements;
2. the user's authorization for facts and external actions;
3. project evidence, source, privacy, and approval protocols;
4. AEP execution discipline;
5. notification and formatting preferences.

AEP cannot:

- prove a fact;
- replace a legal source;
- turn the model into a lawyer;
- authorize automatic signing, payment, filing, or publication;
- override a formal court notice;
- turn "execution succeeded" into "the legal conclusion is correct."

## Known Differences

AEP is designed for general business agents. This project is evidence-intensive and sensitive to procedure. Therefore:

- AEP's "technical clause citation" expands here to statutes, judicial interpretations, platform rules, and procedural sources;
- successful execution feedback does not mean successful factual verification;
- evolution records must not move private case material into the public repository;
- memory cannot replace original evidence and formal documents.

## Minimum Adoption Checklist

- [ ] State objective and impact before execution;
- [ ] Read current project state;
- [ ] Mark uncertain content;
- [ ] Report critical action results;
- [ ] Re-plan when results deviate;
- [ ] Write conclusions into project records rather than leaving them in chat;
- [ ] Never treat AEP as legal authority.
