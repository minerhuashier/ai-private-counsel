# 程序状态登记模板

> 只使用占位符或完全虚构内容。真实案号、日期、金额、法院材料、证据和个人信息必须留在私有工作区。
>
> Use placeholders or entirely fictional content only. Keep real case numbers, dates, amounts, court materials, evidence, and personal information in a private workspace.

## 0. 登记摘要

| 字段 | 内容 |
| --- | --- |
| 内部案件代号 | `CASE-CODE` |
| 当前登记版本 | `v0.0` |
| 登记生成时间（含时区） | `YYYY-MM-DD HH:MM:SS TIMEZONE` |
| 最近人工复核时间 | `YYYY-MM-DD HH:MM:SS TIMEZONE` |
| 责任人 | `PERSON` |
| 当前是否有冲突 | `yes` / `no` |
| 当前禁止执行的动作 | `NONE` |

## 1. 八条状态轴总表

| 状态轴 | 当前可确认结论 | 状态 | 最新来源 | 抓取时间 | 下一步核实 | 责任人 |
| --- | --- | --- | --- | --- | --- | --- |
| 案件身份 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| 程序类型 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| 费用 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| 送达 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| 期限 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| 证据 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| 审理 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| 文书与批准 | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |

允许的状态值：

- `observed`
- `corroborated`
- `conflict`
- `stale`
- `unverified`
- `closed`

## 2. 来源登记

每个来源单独登记，不覆盖旧来源。

| 来源 ID | 来源类型 | 事件时间 | 来源时间 | 抓取时间 | 原始载体 | SHA-256 | 可证明范围 | 不能证明什么 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SOURCE-001` | `formal-document` / `court-platform` / `message` / `email` / `bank-receipt` / `call-record` / `human-action` | `DATE TIME` | `DATE TIME` | `DATE TIME` | `PRIVATE-PATH-OR-PLACEHOLDER` | `HASH-OR-NONE` | `SCOPE` | `LIMITS` |

## 3. 费用节点

| 节点 | 是否发生 | 来源 ID | 时间 | 可确认事项 | 尚不能确认事项 |
| --- | --- | --- | --- | --- | --- |
| 存在缴费义务 | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| 已收到缴费通知 | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| 本人发起支付 | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| 银行或支付机构显示成功 | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| 法院账单或正式渠道确认入账 | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |

费用冲突时的固定写法：

```text
银行侧支付成功；法院侧入账状态待核实；核实前不重复缴纳。
```

## 4. 期限登记

| 期限 ID | 对应行为 | 正式截止时间 | 时区 | 来源 ID | 来源是否明确调整旧期限 | 内部操作缓冲 | 当前处理 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DEADLINE-001` | `ACT` | `YYYY-MM-DD HH:MM` | `TIMEZONE` | `SOURCE-ID` | `yes` / `no` / `unclear` | `EARLIER-DATE-OR-NONE` | `continue-preparing` / `closed` |

内部操作缓冲不改变正式期限。

## 5. 审理阶段

| 阶段 | 来源 ID | 窗口或阶段开放时间 | 正式截止时间 | 当前入口 | 待提交内容 | 本人是否已批准 | 提交回执 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `STAGE-NAME` | `SOURCE-ID` | `DATE TIME` | `DATE TIME` | `PLACEHOLDER` | `DRAFT-ID` | `none` / `approved` | `RECEIPT-ID-OR-NONE` |

异步审理窗口、阶段开放时间和单项截止时间必须分开登记。

## 6. 证据状态

| 证据 ID | 原件是否存在 | 是否已提交 | 系统是否接收 | 是否要求补正或重传 | 是否进入质证 | 证明目的 | 版本冲突 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXHIBIT-001` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `PURPOSE` | `yes` / `no` / `unknown` |

## 7. 外部动作与批准

| 动作 ID | 动作类型 | 使用的文档版本 | 本人是否明确批准 | 批准时间 | 执行人 | 执行时间 | 回执 | 结果核实 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ACTION-001` | `pay` / `sign` / `file` / `upload` / `respond` / `withdraw` / `settle` / `publish` | `DOC-ID` | `none` / `approved` | `DATE TIME OR NONE` | `PERSON` | `DATE TIME OR NONE` | `RECEIPT-ID-OR-NONE` | `UNVERIFIED` |

没有明确批准时写 `none`。AI 草稿、口头讨论或“看起来可以”都不等于批准。

## 8. 冲突记录

来源冲突时暂停确定性结论，保留冲突双方及其证明范围，等待正式来源或人工核实。

| 冲突 ID | 状态轴 | 来源 A | 来源 B | 冲突点 | 可确认事项 | 不能确认事项 | 暂停的动作 | 关闭依据 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CONFLICT-001` | `AXIS` | `SOURCE-A` | `SOURCE-B` | `DIFFERENCE` | `CONFIRMED` | `UNCONFIRMED` | `PROHIBITED-ACTION` | `none` |

## 9. 每日事件日志

追加记录，不覆盖旧记录。

```text
TIMESTAMP TIMEZONE
Source:
Capture:
State axes affected:
What changed:
What remains uncertain:
Conflict:
Human decision required:
External act performed by human:
Receipt:
Next verification:
```

## 10. 人工关闭检查

关闭任何事项前，逐项确认：

- [ ] 有可回链的来源；
- [ ] 事件时间、来源时间和抓取时间分开记录；
- [ ] 证明范围和限制都已写明；
- [ ] 与其他来源没有未解决冲突；
- [ ] 需要外部动作的事项已经由本人明确批准；
- [ ] 已经保存执行回执；
- [ ] 已重新读取结果，未把“提交成功”写成“法院已采信”；
- [ ] 公开版本不包含真实案件信息。

---

# Procedural State Register Template

## 0. Register Summary

| Field | Value |
| --- | --- |
| Internal case code | `CASE-CODE` |
| Register version | `v0.0` |
| Register created at (with time zone) | `YYYY-MM-DD HH:MM:SS TIMEZONE` |
| Last human review | `YYYY-MM-DD HH:MM:SS TIMEZONE` |
| Responsible person | `PERSON` |
| Any current conflict | `yes` / `no` |
| Actions currently prohibited | `NONE` |

## 1. Eight State Axes

| State axis | Confirmed conclusion | State | Latest source | Capture time | Next verification | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| Case identity | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| Procedure type | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| Fees | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| Service | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| Deadlines | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| Evidence | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| Hearing | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |
| Documents and approval | `UNKNOWN` | `unverified` | `SOURCE-ID` | `DATE TIME` | `NEXT-STEP` | `PERSON` |

Allowed state values:

- `observed`
- `corroborated`
- `conflict`
- `stale`
- `unverified`
- `closed`

## 2. Source Register

Register each source separately. Do not overwrite older sources.

| Source ID | Source type | Event time | Source time | Capture time | Original medium | SHA-256 | Proven scope | Cannot prove |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SOURCE-001` | `formal-document` / `court-platform` / `message` / `email` / `bank-receipt` / `call-record` / `human-action` | `DATE TIME` | `DATE TIME` | `DATE TIME` | `PRIVATE-PATH-OR-PLACEHOLDER` | `HASH-OR-NONE` | `SCOPE` | `LIMITS` |

## 3. Fee Nodes

| Node | Occurred | Source ID | Time | Confirmed | Not yet confirmed |
| --- | --- | --- | --- | --- | --- |
| Fee obligation exists | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| Fee notice received | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| Person initiated payment | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| Bank or payment provider reports success | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |
| Court bill or formal channel confirms receipt | `yes` / `no` / `unknown` | `SOURCE-ID` | `DATE TIME` | `CONFIRMED` | `UNCONFIRMED` |

Use this fixed wording when fee status conflicts:

```text
The bank-side payment succeeded; court-side reconciliation remains unverified; do not pay again before verification.
```

## 4. Deadline Register

| Deadline ID | Required act | Formal deadline | Time zone | Source ID | Source explicitly adjusts older deadline | Internal buffer | Current treatment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DEADLINE-001` | `ACT` | `YYYY-MM-DD HH:MM` | `TIMEZONE` | `SOURCE-ID` | `yes` / `no` / `unclear` | `EARLIER-DATE-OR-NONE` | `continue-preparing` / `closed` |

An internal buffer does not change the formal deadline.

## 5. Hearing Stages

| Stage | Source ID | Window or opening time | Formal deadline | Current entrance | Content to submit | Human-approved | Submission receipt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `STAGE-NAME` | `SOURCE-ID` | `DATE TIME` | `DATE TIME` | `PLACEHOLDER` | `DRAFT-ID` | `none` / `approved` | `RECEIPT-ID-OR-NONE` |

Record the asynchronous hearing window, stage opening time, and item-specific deadline separately.

## 6. Evidence Status

| Exhibit ID | Original exists | Submitted | Received by system | Correction or re-upload requested | Cross-examination opened | Proven purpose | Version conflict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXHIBIT-001` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `yes` / `no` / `unknown` | `PURPOSE` | `yes` / `no` / `unknown` |

## 7. External Acts and Approval

| Action ID | Action type | Document version used | Explicitly approved by person | Approval time | Executed by | Execution time | Receipt | Result verification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ACTION-001` | `pay` / `sign` / `file` / `upload` / `respond` / `withdraw` / `settle` / `publish` | `DOC-ID` | `none` / `approved` | `DATE TIME OR NONE` | `PERSON` | `DATE TIME OR NONE` | `RECEIPT-ID-OR-NONE` | `UNVERIFIED` |

Write `none` when no explicit approval exists. An AI draft, informal discussion, or "looks fine" is not approval.

## 8. Conflict Record

| Conflict ID | State axis | Source A | Source B | Difference | Confirmed | Unconfirmed | Paused action | Closing basis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CONFLICT-001` | `AXIS` | `SOURCE-A` | `SOURCE-B` | `DIFFERENCE` | `CONFIRMED` | `UNCONFIRMED` | `PROHIBITED-ACTION` | `none` |

## 9. Daily Event Log

Append entries. Do not overwrite old records.

```text
TIMESTAMP TIMEZONE
Source:
Capture:
State axes affected:
What changed:
What remains uncertain:
Conflict:
Human decision required:
External act performed by human:
Receipt:
Next verification:
```

## 10. Human Closure Checklist

Before closing any item, confirm:

- [ ] A linkable source exists;
- [ ] Event time, source time, and capture time are recorded separately;
- [ ] Proven scope and limits are stated;
- [ ] No unresolved conflict remains;
- [ ] Any external act was explicitly approved by the person;
- [ ] An execution receipt was saved;
- [ ] The result was read again; "submitted" was not rewritten as "accepted on the merits";
- [ ] The public version contains no real case information.
