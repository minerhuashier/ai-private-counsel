# 本项目如何初始化 Agent 配置

版本：`0.1.0`  
状态：公开方法说明  
核查日期：`2026-11-18`

## 结论先行

本项目不是靠模型“记得”如何工作，而是靠工作区里的文件和状态启动。

每次会话的最小启动顺序是：

1. 读取项目根 `AGENTS.md`；
2. 读取 `00-项目配置/project.yaml`；
3. 读取 `00-项目配置/roles/README.md`；
4. 根据任务加载领域角色；
5. 涉及法律、传播或视频任务时，重新核对红线；
6. 读取当前 `STATUS.md` 和相关决策、工作日志；
7. 再开始检索、修改或生成。

公开仓库只描述可复用的初始化方法，不包含真实案件字段、角色文件中的案件信息或私密材料。

## 本次核查过哪些配置

| 文件或目录 | 实际作用 | 是否可作为案件事实来源 |
| --- | --- | --- |
| 项目根 `AGENTS.md` | 使命、启动顺序、角色、红线、目录和阶段 | 它是规则，不是证据 |
| `00-项目配置/project.yaml` | 项目元数据、当前状态、角色与技能注册 | 可指路，但事实仍应回到证据 |
| `00-项目配置/roles/README.md` | 角色选择与加载顺序 | 它是规则，不是证据 |
| `00-项目配置/roles/*.md` | 各领域角色边界与工作方法 | 不是证据 |
| `00-项目配置/skills/` | 发布、视频等具体任务技能 | 不是证据 |
| `06-项目管理/STATUS.md` | 当前阶段、期限、风险和待办 | 状态记录，需保留来源 |
| `06-项目管理/decisions.md` | 用户决策与口径 | 决策记录，不等于客观事实 |
| `06-项目管理/worklog/` | 按日期保存工作过程 | 审计线索，不替代原件 |
| 用户全局 `AGENTS.md` | 重要任务通知等跨项目规则 | 不参与法律判断 |
| 全局 `MEMORY.md` 等记忆文件 | 跨会话偏好与经验 | 当前为空，不能提供本案事实 |

## 全局记忆的实际状态

本次读取到：

- `MEMORY.md` 只有初始化占位内容；
- `memory_summary.md` 明确写明尚无已整合记忆；
- `raw_memories.md` 明确写明尚无原始记忆。

因此必须准确表述：

> 本项目的初始化依据是可审计的工作区配置，不是当前为空的全局记忆。

即使未来记忆中有内容，也应按以下规则使用：

- 记忆可用于偏好、流程和已知路径；
- 记忆不能替代原始证据；
- 记忆不能替代官方法律文本；
- 记忆不能证明法院、平台或对方在某个时间做了什么；
- 与当前文件或正式来源冲突时，以当前可核验来源为准。

## 初始化目录

```text
project-root/
├── AGENTS.md
├── 00-项目配置/
│   ├── project.yaml
│   ├── roles/
│   │   ├── README.md
│   │   └── <domain-role>.md
│   └── skills/
│       ├── media-posting/
│       └── video-editing/
├── 01-证据/
├── 02-起诉文书/
├── 03-法律法规/
├── 04-沟通记录/
├── 05-自媒体发布/
├── 06-项目管理/
│   ├── STATUS.md
│   ├── decisions.md
│   └── worklog/
├── 07-参考资料/
└── git-pub/
    └── ai-private-counsel/
```

目录名不是装饰。它把原始材料、法律研究、文书、沟通、传播、项目管理和公开代码分开，减少误把私密材料发布到公共仓库的概率。

## 从零初始化步骤

### 1. 建立私密工作区与公开仓库边界

- 私密工作区保存真实证据、身份信息、案号、法院文书和沟通记录；
- 公开仓库只保存协议、代码、Schema、文档和完全虚构示例；
- 两个仓库不共享提交历史；
- 公开仓库默认不配置远端，直到完成安全检查并取得本人明确授权。

### 2. 编写项目根 `AGENTS.md`

至少包含：

- 项目使命；
- 用户与 Agent 的权限边界；
- 每次会话启动顺序；
- 角色加载规则；
- 红线；
- 目录约定；
- 当前工作阶段；
- 阶段完成后写工作日志的要求。

### 3. 建立 `project.yaml`

至少登记：

- 项目名称和负责人角色；
- 当前程序阶段；
- 已知期限与状态来源；
- 角色注册表；
- 技能注册表；
- 需要下载的法律与平台规则清单；
- 最后更新时间。

敏感字段留在私密工作区。公开方法文档不复制真实值。

### 4. 建立角色库

每个角色至少写明：

- 领域身份；
- 适用任务；
- 必读材料；
- 可以使用的方法或技能；
- 允许输出；
- 禁止输出；
- 失败关闭条件；
- 何时需要用户确认。

`roles/README.md` 负责总表、加载顺序和旧角色归档说明。

### 5. 建立任务技能

媒体发布、视频剪辑等任务单独放在 `skills/`，避免把传播方法误当成法律判断。

涉及对外发布时，至少同时加载：

- 公开传播合规角色；
- 媒体发布技能；
- 隐私和安全规则；
- 当前事实底稿。

### 6. 建立项目管理闭环

- `STATUS.md`：当前状态、期限、风险、待办；
- `decisions.md`：用户关键决策和时间；
- `worklog/`：每个阶段完成后的结论、待确认事项和下一步；
- 交付物单独记录版本、哈希和审批状态。

### 7. 建立公开协议和 Schema

公开仓库应先有：

- 协议总表；
- AI 自诉工作协议；
- 证据、来源、隐私、安全和批准边界；
- 防止幻觉协议；
- 事实、证据、来源和批准 Schema；
- 完全虚构示例；
- 公开安全检查器与测试。

### 8. 建立启动检查清单

```text
[ ] 读取 AGENTS.md
[ ] 读取 project.yaml
[ ] 读取 roles/README.md
[ ] 加载任务角色
[ ] 读取 STATUS.md
[ ] 核对期限和正式来源
[ ] 核对是否涉及外部动作
[ ] 核对公开与私密数据边界
```

### 9. 建立变更治理

协议、角色、Schema 和安全规则变更应记录：

- 修改原因；
- 影响范围；
- 兼容性；
- 新风险；
- 测试结果；
- 是否需要用户重新批准。

### 10. 建立公开前检查

```bash
python3 tools/check_public_safety.py .
python3 -m unittest discover -s tests -v
git diff --check
```

还要人工检查：

- 是否含真实姓名、案号、订单号、电话、地址或法院文书；
- 链接是否存在；
- 示例是否完全虚构；
- 协议是否准确区分历史文件和本次新增；
- 中英文内容是否一致；
- Git 历史是否在获准公开前已经清理。

## 角色加载方法

角色不是越多越好。按任务选择最小集合：

| 任务 | 最小角色集合 |
| --- | --- |
| 合同关系与违约 | 合同律师 + 证据专家 |
| 消费者和平台责任 | 消费者律师 + 平台责任律师 + 证据专家 |
| 起诉状与程序 | 诉讼程序律师 + 相关实体法角色 |
| 证据新增或质证 | 证据专家 + 相关实体法角色 |
| 对外发布 | 传播合规角色 + 媒体发布技能 |
| 视频制作 | 传播合规角色 + 视频技能 |

每次角色加载都要继续遵守同一套红线。角色不能互相授权绕过隐私、来源或人工批准。

## 配置更新原则

1. 状态变化写 `STATUS.md`，不要只留聊天；
2. 用户决策写 `decisions.md`，注明决定和日期；
3. 阶段完成写 `worklog/`，说明结论、待确认事项和下一步；
4. 协议修改走 Pull Request；
5. 对外动作前重新读取具体版本；
6. 旧状态、旧批准和旧截图不自动延续；
7. 全局记忆不是事实数据库；
8. 公开仓库不接收真实案件材料。

## 可直接复用的初始化模板

```text
project/
├── AGENTS.md
├── 00-项目配置/
│   ├── project.yaml
│   ├── roles/README.md
│   └── skills/
├── 01-证据/
├── 02-文书/
├── 03-法律来源/
├── 04-沟通记录/
├── 05-公开传播/
├── 06-项目管理/
│   ├── STATUS.md
│   ├── decisions.md
│   └── worklog/
├── docs/protocols/
├── schemas/
├── examples/synthetic/
├── tools/
└── tests/
```

初始化完成的判断标准不是“文件都建好了”，而是：

- 新会话知道先读什么；
- 当前状态有可追溯来源；
- 每个角色知道何时停止；
- 私密材料不会误入公开仓库；
- 外部动作仍由本人批准和执行。

---

# How This Project Initializes Agent Configuration

Version: `0.1.0`  
Status: public method note  
Checked: `2026-11-18`

## Conclusion First

This project does not depend on model memory for startup. It starts from files and state in the working workspace.

The minimum startup order for every session is:

1. Read the project-root `AGENTS.md`;
2. Read `00-项目配置/project.yaml`;
3. Read `00-项目配置/roles/README.md`;
4. Load role files required by the current task;
5. Recheck red lines before legal, publicity, or video work;
6. Read current `STATUS.md` plus relevant decisions and work logs;
7. Only then begin retrieval, editing, or generation.

The public repository describes only the reusable initialization method. It contains no real case values or private role content.

## Configuration Sources Reviewed

| File or directory | Purpose | Source of case facts? |
| --- | --- | --- |
| Project-root `AGENTS.md` | Mission, startup order, roles, red lines, directories, and phases | No; it contains rules |
| `00-项目配置/project.yaml` | Project metadata, current state, role and skill registry | Points to facts, but facts still require evidence |
| `00-项目配置/roles/README.md` | Role selection and load order | No; it contains rules |
| `00-项目配置/roles/*.md` | Domain role boundaries and methods | No |
| `00-项目配置/skills/` | Publication, video, and task skills | No |
| `06-项目管理/STATUS.md` | Current stage, deadlines, risks, and tasks | A status record that must retain sources |
| `06-项目管理/decisions.md` | User decisions and established positions | A decision record, not objective fact |
| `06-项目管理/worklog/` | Dated work history | Audit lead, not a replacement for originals |
| User-global `AGENTS.md` | Cross-project rules such as important-task notification | Not involved in legal judgment |
| Global `MEMORY.md` and related memory files | Cross-session preferences and experience | Currently empty; cannot supply case facts |

## Actual State of Global Memory

At review time:

- `MEMORY.md` contained only initialization placeholders;
- `memory_summary.md` explicitly stated that no memory had been consolidated;
- `raw_memories.md` explicitly stated that no raw memories existed.

The accurate statement is:

> This project is initialized from auditable workspace configuration, not from the currently empty global memory.

If memory is populated later:

- memory may be used for preferences, workflows, and known paths;
- memory cannot replace original evidence;
- memory cannot replace official legal texts;
- memory cannot prove what a court, platform, or another party did at a specific time;
- current verifiable sources prevail when memory conflicts with files or formal sources.

## Initialized Directory

```text
project-root/
├── AGENTS.md
├── 00-项目配置/
│   ├── project.yaml
│   ├── roles/
│   │   ├── README.md
│   │   └── <domain-role>.md
│   └── skills/
│       ├── media-posting/
│       └── video-editing/
├── 01-证据/
├── 02-起诉文书/
├── 03-法律法规/
├── 04-沟通记录/
├── 05-自媒体发布/
├── 06-项目管理/
│   ├── STATUS.md
│   ├── decisions.md
│   └── worklog/
├── 07-参考资料/
└── git-pub/
    └── ai-private-counsel/
```

The directory names are functional. They separate originals, legal research, documents, communications, publicity, project management, and public code. This reduces the chance of publishing private material by mistake.

## Bootstrap Steps

### 1. Separate Private Workspace and Public Repository

- Keep real evidence, identity data, case numbers, court documents, and communications private;
- Keep only protocols, code, schemas, documentation, and entirely synthetic examples public;
- never share Git history between the two;
- configure no public remote until safety checks pass and the user explicitly authorizes it.

### 2. Write the Project-Root `AGENTS.md`

Include:

- project mission;
- user and agent authority boundaries;
- startup order;
- role-loading rules;
- red lines;
- directory conventions;
- current working phase;
- requirement to write a work log after each phase.

### 3. Create `project.yaml`

Record at minimum:

- project name and owner role;
- current procedural stage;
- known deadlines and their source;
- role registry;
- skill registry;
- laws and platform rules to retrieve;
- last update.

Keep sensitive values private. The public method note does not reproduce real values.

### 4. Build the Role Registry

Each role should state:

- domain identity;
- applicable tasks;
- mandatory reading;
- permitted methods or skills;
- permitted output;
- prohibited output;
- stop conditions;
- cases requiring human confirmation.

`roles/README.md` owns the role table, load order, and archive policy.

### 5. Create Task Skills

Media publication and video editing belong in `skills/`. Publicity methods must not be confused with legal analysis.

For external publication, load:

- the publicity-compliance role;
- the media-posting skill;
- privacy and security rules;
- the current factual record.

### 6. Create the Project-Management Loop

- `STATUS.md`: current state, deadlines, risks, and open tasks;
- `decisions.md`: key user decisions and dates;
- `worklog/`: conclusions, items requiring confirmation, and next actions after each phase;
- deliverable records for version, hash, and approval status.

### 7. Create Public Protocols and Schemas

The public repository should first contain:

- a protocol registry;
- the AI self-litigation work protocol;
- evidence, source, privacy, security, and approval boundaries;
- the anti-hallucination protocol;
- fact, evidence, source, and approval schemas;
- entirely synthetic examples;
- a public-safety checker and tests.

### 8. Create the Startup Checklist

```text
[ ] Read AGENTS.md
[ ] Read project.yaml
[ ] Read roles/README.md
[ ] Load the task role
[ ] Read STATUS.md
[ ] Check deadlines and formal sources
[ ] Check whether an external action is involved
[ ] Check the public/private data boundary
```

### 9. Establish Change Control

Protocol, role, schema, and safety changes should record:

- reason;
- affected scope;
- compatibility;
- new risk;
- test results;
- whether user approval must be renewed.

### 10. Establish the Pre-Publication Checklist

```bash
python3 tools/check_public_safety.py .
python3 -m unittest discover -s tests -v
git diff --check
```

Also inspect manually:

- real names, case numbers, order numbers, phone numbers, addresses, or court documents;
- broken links;
- synthetic examples;
- accurate separation of historical files from new proposals;
- Chinese and English consistency;
- Git history before public release.

## Role Loading

Load the smallest set of roles required:

| Task | Minimum roles |
| --- | --- |
| Contract and breach | Contract lawyer + evidence specialist |
| Consumer and platform liability | Consumer lawyer + platform-liability lawyer + evidence specialist |
| Complaint and procedure | Litigation-procedure lawyer + relevant substantive-law role |
| New evidence or cross-examination | Evidence specialist + relevant substantive-law role |
| Public posting | Publicity-compliance role + media-posting skill |
| Video production | Publicity-compliance role + video skill |

Every loaded role remains subject to the same red lines. No role can authorize another role to bypass privacy, source, or human-approval controls.

## Configuration Update Rules

1. Write status changes to `STATUS.md`, not only in chat;
2. Write user decisions to `decisions.md` with date and scope;
3. Write phase completion to `worklog/` with conclusions and next steps;
4. Change protocols through Pull Requests;
5. Re-read the exact version before any external action;
6. Never carry old status, approval, or screenshots forward automatically;
7. Never treat global memory as a fact database;
8. Never accept real case material into the public repository.

## Reusable Bootstrap Template

```text
project/
├── AGENTS.md
├── 00-项目配置/
│   ├── project.yaml
│   ├── roles/README.md
│   └── skills/
├── 01-证据/
├── 02-文书/
├── 03-法律来源/
├── 04-沟通记录/
├── 05-公开传播/
├── 06-项目管理/
│   ├── STATUS.md
│   ├── decisions.md
│   └── worklog/
├── docs/protocols/
├── schemas/
├── examples/synthetic/
├── tools/
└── tests/
```

Initialization is complete only when:

- a new session knows what to read first;
- current state has traceable sources;
- every role knows when to stop;
- private material cannot flow into the public repository by default;
- external actions still require human approval and human execution.
