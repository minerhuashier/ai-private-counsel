# Agent 配置示例

本目录把当前项目的 Agent 配置提炼为可复用的脱敏模板。  
它保留架构、字段、停止条件和批准门，不包含真实案件信息。

## 文件

| 文件 | 用途 |
| --- | --- |
| `AGENTS.template.md` | 项目根总控规则与每次会话的启动顺序 |
| `project.example.yaml` | 项目元数据、阶段、角色与技能注册表 |
| `roles.example.yaml` | 七个角色的最小契约 |
| `role-contract.template.md` | 新增单独角色文件时使用的结构 |
| `STATUS.template.md` | 当前状态、期限、风险和下一步模板 |
| `decisions.template.md` | 用户关键决定模板 |
| `worklog.template.md` | 阶段或工作日审计记录模板 |

## 使用顺序

1. 复制 `AGENTS.template.md` 到自己的项目根目录，并改名为 `AGENTS.md`；
2. 建立 `00-项目配置/project.yaml`，参考 `project.example.yaml`；
3. 为当前争议选择角色，参考 [Agent 构成与设计理由](../../docs/agent-architecture.md)；
4. 如有必要，为每个角色建立单独文件，使用 `role-contract.template.md`；
5. 建立 `STATUS.md`、`decisions.md` 与 `worklog/`；
6. 把真实案件工作区与公开代码仓库分开；
7. 在允许任何外部动作前，核对批准门。

## 不得放入模板的真实内容

- 姓名、电话、地址、身份证件、银行卡或账号；
- 法院、法官、案号、对方主体、交易相对方或平台账号；
- 订单号、交易号、支付凭证、金额和与案件绑定的日期；
- 证据原文、聊天记录、录音、截图、法院文书或内部链接；
- 密钥、Token、Cookie、登录状态或浏览器配置。

模板中的 `<...>` 和 `example.*` 都必须替换为本地私密值；公开仓库中的示例应继续保持占位符。

## 设计边界

这些模板不是法律意见，不会自动建立律师关系，也不授权 AI 签署、缴费、提交、发送投诉或公开发布。实际动作仍由用户本人完成或逐项明确授权。

---

# Agent Configuration Examples

This directory distills the project's Agent configuration into reusable, de-identified templates.  
It preserves the architecture, fields, stop conditions, and approval gates without including real case information.

## Files

| File | Purpose |
| --- | --- |
| `AGENTS.template.md` | Root control rules and session-start sequence |
| `project.example.yaml` | Project metadata, stage, role registry, and skill registry |
| `roles.example.yaml` | Minimum contracts for the seven roles |
| `role-contract.template.md` | Structure for a separate role file |
| `STATUS.template.md` | Current state, deadlines, risks, and next actions |
| `decisions.template.md` | Record of key user decisions |
| `worklog.template.md` | Audit record for a stage or workday |

## Adoption Order

1. Copy `AGENTS.template.md` to the project root as `AGENTS.md`;
2. create `00-project-config/project.yaml` based on `project.example.yaml`;
3. select roles for the dispute with [Agent Composition and Design Rationale](../../docs/agent-architecture.md);
4. create separate role files only when useful, using `role-contract.template.md`;
5. create `STATUS.md`, `decisions.md`, and `worklog/`;
6. separate the private case workspace from the public code repository;
7. check the approval gate before permitting any external action.

## Never Put Real Content in a Public Template

- names, phone numbers, addresses, identity documents, bank cards, or accounts;
- courts, judges, case numbers, opposing entities, counterparties, or platform accounts;
- order numbers, transaction numbers, payment records, amounts, or case-specific dates;
- evidence text, chats, recordings, screenshots, court documents, or private links;
- secrets, tokens, cookies, login state, or browser configuration.

Replace every `<...>` and `example.*` value in a private workspace. Public examples must remain placeholders.

## Design Boundary

These templates are not legal advice, do not create a lawyer-client relationship, and do not authorize AI to sign, pay, file, send complaints, or publish. External actions remain human actions or require explicit item-by-item authorization.
