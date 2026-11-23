# 法律要件与证据矩阵模板

# Legal-Elements and Evidence Matrix Template

- 矩阵编号：`MATRIX-<YYYYMMDD>-<NNN>`
- 案件代号：`<SYNTHETIC_CASE_CODE>`
- 规范核验日期：`<YYYY-MM-DD>`
- 状态：`DRAFT / HUMAN_REVIEWED`

> 本模板不构成法律意见。每个规范名称、条号、版本和施行时间都必须回到官方来源核验。

> This template is not legal advice. Every instrument name, article, version, and effective date must be verified against an official source.

## 一、争议问题

## 1. Disputed Issues

1. `<DISPUTED_ISSUE_ONE>`
2. `<DISPUTED_ISSUE_TWO>`
3. `<DISPUTED_ISSUE_THREE>`

## 二、矩阵

## 2. Matrix

| 编号 | 法律问题 | 规范与要件 | 待证事实 | 证据 | 证据能证明什么 | 缺口/冲突 | 下一步 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `LE-001` | `<LEGAL_ISSUE>` | `<INSTRUMENT_AND_ARTICLE>; <ELEMENTS>` | `<FACT_TO_PROVE>` | `<EVIDENCE_IDS>` | `<LIMIT_OF_PROOF>` | `<GAP_OR_CONFLICT>` | `<COLLECT_OR_INVESTIGATE_OR_DROP>` | `SUFFICIENT / INDIRECT / GAP / HOLD` |
| `LE-002` | `<LEGAL_ISSUE>` | `<INSTRUMENT_AND_ARTICLE>; <ELEMENTS>` | `<FACT_TO_PROVE>` | `<EVIDENCE_IDS>` | `<LIMIT_OF_PROOF>` | `<GAP_OR_CONFLICT>` | `<COLLECT_OR_INVESTIGATE_OR_DROP>` | `SUFFICIENT / INDIRECT / GAP / HOLD` |

| ID | Legal issue | Norm and elements | Fact to prove | Evidence | What the evidence proves | Gap/conflict | Next step | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `LE-001` | `<LEGAL_ISSUE>` | `<INSTRUMENT_AND_ARTICLE>; <ELEMENTS>` | `<FACT_TO_PROVE>` | `<EVIDENCE_IDS>` | `<LIMIT_OF_PROOF>` | `<GAP_OR_CONFLICT>` | `<COLLECT_OR_INVESTIGATE_OR_DROP>` | `SUFFICIENT / INDIRECT / GAP / HOLD` |
| `LE-002` | `<LEGAL_ISSUE>` | `<INSTRUMENT_AND_ARTICLE>; <ELEMENTS>` | `<FACT_TO_PROVE>` | `<EVIDENCE_IDS>` | `<LIMIT_OF_PROOF>` | `<GAP_OR_CONFLICT>` | `<COLLECT_OR_INVESTIGATE_OR_DROP>` | `SUFFICIENT / INDIRECT / GAP / HOLD` |

## 三、常用检查维度

## 3. Common Review Dimensions

| 维度 | 需要回答的问题 | 可能证据 |
| --- | --- | --- |
| 合同关系 | 谁与谁形成何种关系，内容是什么 | 商品页、订单、聊天、合同、付款记录 |
| 履行 | 应履行什么、何时履行、实际履行了什么 | 聊天、录音、现场材料、第三方材料 |
| 平台知情 | 何时知道了什么，信息来源是什么 | 投诉、客服记录、工单、录音 |
| 平台措施 | 收到何种请求，采取何种措施，结果是什么 | 请求原文、页面状态、工单结论、结算记录 |
| 损失 | 损失范围、金额、因果关系和减损 | 付款凭证、发票、替代服务记录、计算表 |
| 程序 | 主体、管辖、期限和请求是否匹配 | 主体登记、合同履行地、程序通知 |

| Dimension | Questions | Possible evidence |
| --- | --- | --- |
| Contract | Who formed what relationship, and on what terms? | product page, order, chat, contract, payment record |
| Performance | What was due, when, and what was actually performed? | chat, audio, on-site material, third-party material |
| Platform knowledge | When did it know what, and from which source? | complaint, customer-service record, work order, audio |
| Platform action | What request was received, what action was taken, and what was the result? | original request, page state, work-order result, settlement record |
| Loss | Scope, amount, causation, and mitigation | payment proof, invoice, replacement record, calculation |
| Procedure | Do the parties, jurisdiction, deadlines, and requests match? | entity record, place of performance, procedural notice |

## 四、缺口清单

## 4. Gap List

| 缺口编号 | 缺失事实或材料 | 为什么重要 | 由谁控制 | 补证方式 | 不能补证时的处理 |
| --- | --- | --- | --- | --- | --- |
| `GAP-001` | `<MISSING_FACT_OR_MATERIAL>` | `<WHY_MATERIAL>` | `<CONTROLLER>` | `<USER_EXPORT / PUBLIC_SOURCE / INVESTIGATION / PRODUCTION_ORDER>` | `<NARROW_CLAIM / MARK_UNPROVED / HOLD>` |

| Gap ID | Missing fact or material | Why it matters | Controller | Collection route | Fallback |
| --- | --- | --- | --- | --- | --- |
| `GAP-001` | `<MISSING_FACT_OR_MATERIAL>` | `<WHY_MATERIAL>` | `<CONTROLLER>` | `<USER_EXPORT / PUBLIC_SOURCE / INVESTIGATION / PRODUCTION_ORDER>` | `<NARROW_CLAIM / MARK_UNPROVED / HOLD>` |

## 五、来源核验

## 5. Source Verification

| 规范编号 | 正式名称 | 条号 | 版本/施行时间 | 官方来源 | 取得时间 | SHA-256 | 复核状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SRC-001` | `<OFFICIAL_TITLE>` | `<ARTICLE>` | `<VERSION_OR_EFFECTIVE_DATE>` | `<OFFICIAL_URL>` | `<TIMESTAMP>` | `<64_LOWERCASE_HEX>` | `VERIFIED / HOLD` |

| Source ID | Official title | Article | Version/effective date | Official source | Acquired at | SHA-256 | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SRC-001` | `<OFFICIAL_TITLE>` | `<ARTICLE>` | `<VERSION_OR_EFFECTIVE_DATE>` | `<OFFICIAL_URL>` | `<TIMESTAMP>` | `<64_LOWERCASE_HEX>` | `VERIFIED / HOLD` |

## 六、人工结论

## 6. Human Conclusion

- 已足够支持的事项：`<SUFFICIENT_ITEMS>`
- 只有间接证据的事项：`<INDIRECT_ITEMS>`
- 暂不主张或待补证的事项：`<HOLD_ITEMS>`
- 需要调查取证或责令提交：`<INVESTIGATION_ITEMS>`
- 复核人：`<USER_OR_SYNTHETIC_REVIEWER>`
- 复核时间：`<TIMESTAMP_WITH_TIMEZONE>`

- Supported as sufficient: `<SUFFICIENT_ITEMS>`
- Supported only indirectly: `<INDIRECT_ITEMS>`
- Not asserted yet or awaiting evidence: `<HOLD_ITEMS>`
- Requires investigation or production: `<INVESTIGATION_ITEMS>`
- Reviewer: `<USER_OR_SYNTHETIC_REVIEWER>`
- Review time: `<TIMESTAMP_WITH_TIMEZONE>`
