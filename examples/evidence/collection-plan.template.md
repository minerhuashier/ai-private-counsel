# 取证计划模板

# Evidence Collection Plan Template

- 计划编号：`PLAN-<YYYYMMDD>-<NNN>`
- 案件代号：`<SYNTHETIC_CASE_CODE>`
- 制定时间：`<TIMESTAMP_WITH_TIMEZONE>`
- 状态：`DRAFT / USER_REVIEWED / APPROVED_FOR_READ_ONLY_COLLECTION`

> 只填写公开或完全虚构信息。真实材料不得进入本模板实例。

> Use only public or entirely fictional information. Real material must not enter an instance of this template.

## 一、本轮要回答的问题

## 1. Questions for This Run

1. `<QUESTION_ONE>`
2. `<QUESTION_TWO>`
3. `<QUESTION_THREE>`

限制：一轮最多三个问题。超过三个时拆成多个运行。

Limit: no more than three questions per run. Split additional questions into another run.

## 二、用户叙述摘要

## 2. User Narrative Summary

- 时间：`<DATE_OR_DATE_RANGE>`
- 主体：`<ROLE_OR_ALIAS>`
- 行为：`<WHAT_HAPPENED>`
- 当前材料：`<MATERIAL_ALREADY_HELD>`
- 尚不清楚的事实：`<UNKNOWN_FACTS>`

- Time: `<DATE_OR_DATE_RANGE>`
- Actors: `<ROLE_OR_ALIAS>`
- Conduct: `<WHAT_HAPPENED>`
- Material already held: `<MATERIAL_ALREADY_HELD>`
- Facts still unknown: `<UNKNOWN_FACTS>`

不要在本节写“诈骗”“故意不处理”等未经证明的结论。

Do not write conclusions such as "fraud" or "deliberately ignored" in this section without proof.

## 三、建议证据清单

## 3. Proposed Evidence List

| 编号 | 待证事实 | 建议材料 | 来源/控制方 | 证明边界 | 优先级 | 缺失风险 |
| --- | --- | --- | --- | --- | --- | --- |
| `EV-PLAN-001` | `<FACT_TO_PROVE>` | `<DOCUMENT_OR_PAGE>` | `<SOURCE_OR_CONTROLLER>` | `<WHAT_IT_CAN_AND_CANNOT_PROVE>` | `P1` | `<RISK_IF_MISSING>` |
| `EV-PLAN-002` | `<FACT_TO_PROVE>` | `<DOCUMENT_OR_PAGE>` | `<SOURCE_OR_CONTROLLER>` | `<WHAT_IT_CAN_AND_CANNOT_PROVE>` | `P2` | `<RISK_IF_MISSING>` |

建议覆盖：合同、付款、沟通、履行、平台知情、平台措施、订单状态、退款/结算、主体、损失与费用。

Suggested coverage: contract, payment, communication, performance, platform knowledge, platform action, order state, refund/settlement, entity, loss, and expense.

## 四、用户配合方式

## 4. Required User Cooperation

- 使用的通道：`in_app_browser / system_chrome / manual_export / local_file`
- 用户是否自行登录：`YES / NO`
- 登录由谁完成：`USER_ONLY`
- 需要打开的页面：`<PUBLIC_PLACEHOLDER_URL>`
- 起始位置：`<START_POSITION>`
- 结束位置：`<END_POSITION>`
- 时间范围：`<DATE_OR_TIME_RANGE>`
- 允许的操作：`NAVIGATE / SCROLL / READ / SCREENSHOT / EXPORT_PUBLIC_PAGE`
- 禁止的操作：`REFUND / CONFIRM_RECEIPT / WITHDRAW / SEND / SUBMIT / DELETE / CHANGE_SETTINGS / BYPASS_ACCESS_CONTROL`
- 禁止操作代码：`PROHIBITED_ACTIONS`

- Channel: `in_app_browser / system_chrome / manual_export / local_file`
- Does the user sign in personally: `YES / NO`
- Who completes sign-in: `USER_ONLY`
- Page to open: `<PUBLIC_PLACEHOLDER_URL>`
- Start position: `<START_POSITION>`
- End position: `<END_POSITION>`
- Time range: `<DATE_OR_TIME_RANGE>`
- Allowed actions: `NAVIGATE / SCROLL / READ / SCREENSHOT / EXPORT_PUBLIC_PAGE`
- Prohibited actions: `REFUND / CONFIRM_RECEIPT / WITHDRAW / SEND / SUBMIT / DELETE / CHANGE_SETTINGS / BYPASS_ACCESS_CONTROL`
- Prohibited-action code: `PROHIBITED_ACTIONS`

用户不得向 AI 提供密码、短信验证码、扫码确认、Cookie、支付密码或恢复码。

The user must not provide passwords, SMS verification codes, QR-code confirmation, cookies, payment passwords, or recovery codes to the AI.

## 五、固定与数字化输出

## 5. Preservation and Digitization Outputs

- 原始文件：`<ORIGINAL_FILE_NAMES>`
- 页面固定件：`<SCREENSHOT_HTML_JSON_NAMES>`
- 文本派生物：`<MARKDOWN_NAMES>`
- OCR：`<OCR_NAMES_OR_NA>`
- 录音转写：`<TRANSCRIPT_NAMES_OR_NA>`
- 哈希算法：`SHA-256`
- 哈希清单：`<SHA256_MANIFEST_NAME>`
- 证据台账：`<EVIDENCE_REGISTER_NAME>`

- Originals: `<ORIGINAL_FILE_NAMES>`
- Page captures: `<SCREENSHOT_HTML_JSON_NAMES>`
- Text derivatives: `<MARKDOWN_NAMES>`
- OCR: `<OCR_NAMES_OR_NA>`
- Audio transcript: `<TRANSCRIPT_NAMES_OR_NA>`
- Hash algorithm: `SHA-256`
- Hash manifest: `<SHA256_MANIFEST_NAME>`
- Evidence register: `<EVIDENCE_REGISTER_NAME>`

## 六、停止条件

## 6. Stop Conditions

出现下列任一情况时停止并报告：

- `login_required`
- `blocked_captcha`
- `permission_denied`
- `unexpected_state_change_control`
- `download_requires_confirmation`
- `page_truncated_or_blank`
- `source_conflict`
- `session_expired`
- `uncertain_whether_action_has_external_effect`

Stop and report on any of these conditions:

- `login_required`
- `blocked_captcha`
- `permission_denied`
- `unexpected_state_change_control`
- `download_requires_confirmation`
- `page_truncated_or_blank`
- `source_conflict`
- `session_expired`
- `uncertain_whether_action_has_external_effect`

## 七、人工批准

## 7. Human Approval

- 批准人：`<USER_OR_SYNTHETIC_REVIEWER>`
- 批准时间：`<TIMESTAMP_WITH_TIMEZONE>`
- 批准范围：`<EXACT_PAGES_FILES_AND_ACTIONS>`
- 明确未批准的事项：`<EXCLUDED_ACTIONS_AND_MATERIAL>`

- Approver: `<USER_OR_SYNTHETIC_REVIEWER>`
- Approval time: `<TIMESTAMP_WITH_TIMEZONE>`
- Approved scope: `<EXACT_PAGES_FILES_AND_ACTIONS>`
- Explicitly not approved: `<EXCLUDED_ACTIONS_AND_MATERIAL>`
