# 取证运行记录模板

# Evidence Collection Run Record Template

- 运行编号：`RUN-<TYPE>-<NNN>`
- 计划编号：`PLAN-<YYYYMMDD>-<NNN>`
- 开始时间：`<TIMESTAMP_WITH_TIMEZONE>`
- 结束时间：`<TIMESTAMP_WITH_TIMEZONE>`
- 执行状态：`COMPLETED / STOPPED / PARTIAL / FAILED`

> 本文件是运行记录，不是证据原件。真实页面地址、截图和文件应保存在私有工作区。

> This is a run record, not an evidence original. Real page locations, screenshots, and files belong in the private workspace.

## 一、授权与通道

## 1. Authorization and Channel

- 用户明确授权：`YES / NO`
- 用户本人完成登录：`YES / NO`
- AI 是否接触密码、验证码或 Cookie：`NO`
- 通道：`in_app_browser / system_chrome / manual_export / local_file`
- 浏览器或工具版本：`<TOOL_VERSION>`
- 授权范围：`<PAGES_FILES_AND_TIME_RANGE>`
- 未授权动作：`REFUND / CONFIRM_RECEIPT / SEND / SUBMIT / DELETE / CHANGE_SETTINGS / BYPASS_ACCESS_CONTROL`

- Explicit user authorization: `YES / NO`
- User completed sign-in personally: `YES / NO`
- Did the AI receive a password, verification code, or cookie: `NO`
- Channel: `in_app_browser / system_chrome / manual_export / local_file`
- Browser or tool version: `<TOOL_VERSION>`
- Authorized scope: `<PAGES_FILES_AND_TIME_RANGE>`
- Unauthorized actions: `REFUND / CONFIRM_RECEIPT / SEND / SUBMIT / DELETE / CHANGE_SETTINGS / BYPASS_ACCESS_CONTROL`

## 二、访问轨迹

## 2. Access Trail

| 步骤 | 时间 | 页面或文件 | 标题 | 最终位置 | 可见状态 | 操作 |
| --- | --- | --- | --- | --- | --- | --- |
| `1` | `<TIMESTAMP>` | `<PUBLIC_PLACEHOLDER_URL_OR_FILE>` | `<PAGE_TITLE>` | `<FINAL_URL_OR_FILE>` | `<LOADED_PARTIAL_BLANK_ERROR>` | `<NAVIGATE_SCROLL_READ_SCREENSHOT>` |
| `2` | `<TIMESTAMP>` | `<PUBLIC_PLACEHOLDER_URL_OR_FILE>` | `<PAGE_TITLE>` | `<FINAL_URL_OR_FILE>` | `<LOADED_PARTIAL_BLANK_ERROR>` | `<NAVIGATE_SCROLL_READ_SCREENSHOT>` |

| Step | Time | Page or file | Title | Final location | Visible state | Action |
| --- | --- | --- | --- | --- | --- | --- |
| `1` | `<TIMESTAMP>` | `<PUBLIC_PLACEHOLDER_URL_OR_FILE>` | `<PAGE_TITLE>` | `<FINAL_URL_OR_FILE>` | `<LOADED_PARTIAL_BLANK_ERROR>` | `<NAVIGATE_SCROLL_READ_SCREENSHOT>` |
| `2` | `<TIMESTAMP>` | `<PUBLIC_PLACEHOLDER_URL_OR_FILE>` | `<PAGE_TITLE>` | `<FINAL_URL_OR_FILE>` | `<LOADED_PARTIAL_BLANK_ERROR>` | `<NAVIGATE_SCROLL_READ_SCREENSHOT>` |

## 三、固定件与哈希

## 3. Captures and Hashes

| 固定件编号 | 类型 | 文件名 | 取得方式 | SHA-256 | 备注 |
| --- | --- | --- | --- | --- | --- |
| `CAP-001` | `screenshot` | `<SCREENSHOT_FILENAME>` | `browser_capture` | `<64_LOWERCASE_HEX>` | `<NOTE>` |
| `CAP-002` | `html` | `<HTML_FILENAME>` | `dom_export` | `<64_LOWERCASE_HEX>` | `<NOTE>` |
| `CAP-003` | `json` | `<JSON_FILENAME>` | `page_data_capture` | `<64_LOWERCASE_HEX>` | `<NOTE>` |
| `CAP-004` | `audio` | `<AUDIO_FILENAME>` | `user_provided` | `<64_LOWERCASE_HEX>` | `<ORIGINAL_NOT_MODIFIED>` |

| Capture ID | Type | Filename | Acquisition method | SHA-256 | Note |
| --- | --- | --- | --- | --- | --- |
| `CAP-001` | `screenshot` | `<SCREENSHOT_FILENAME>` | `browser_capture` | `<64_LOWERCASE_HEX>` | `<NOTE>` |
| `CAP-002` | `html` | `<HTML_FILENAME>` | `dom_export` | `<64_LOWERCASE_HEX>` | `<NOTE>` |
| `CAP-003` | `json` | `<JSON_FILENAME>` | `page_data_capture` | `<64_LOWERCASE_HEX>` | `<NOTE>` |
| `CAP-004` | `audio` | `<AUDIO_FILENAME>` | `user_provided` | `<64_LOWERCASE_HEX>` | `<ORIGINAL_NOT_MODIFIED>` |

## 四、数字化派生物

## 4. Digital Derivatives

| 派生物编号 | 类型 | 文件名 | 来源固定件 | SHA-256 | 复核状态 |
| --- | --- | --- | --- | --- | --- |
| `DER-001` | `markdown` | `<MARKDOWN_FILENAME>` | `CAP-001` | `<64_LOWERCASE_HEX>` | `HUMAN_REVIEWED` |
| `DER-002` | `ocr` | `<OCR_FILENAME>` | `CAP-001` | `<64_LOWERCASE_HEX>` | `OCR_UNVERIFIED` |
| `DER-003` | `transcript` | `<TRANSCRIPT_FILENAME>` | `CAP-004` | `<64_LOWERCASE_HEX>` | `KEY_PASSAGES_AUDIO_CHECKED` |

| Derivative ID | Type | Filename | Source capture | SHA-256 | Review state |
| --- | --- | --- | --- | --- | --- |
| `DER-001` | `markdown` | `<MARKDOWN_FILENAME>` | `CAP-001` | `<64_LOWERCASE_HEX>` | `HUMAN_REVIEWED` |
| `DER-002` | `ocr` | `<OCR_FILENAME>` | `CAP-001` | `<64_LOWERCASE_HEX>` | `OCR_UNVERIFIED` |
| `DER-003` | `transcript` | `<TRANSCRIPT_FILENAME>` | `CAP-004` | `<64_LOWERCASE_HEX>` | `KEY_PASSAGES_AUDIO_CHECKED` |

## 五、观察、提取、推断与待核

## 5. Observed, Extracted, Inferred, and Unverified

### `observed`

- `<WHAT_WAS_VISIBLE_ON_THE_PAGE_OR_FILE>`

### `extracted`

- `<WHAT_THE_TOOL_EXTRACTED>`

### `inferred`

- `<WHAT_MAY_BE_INFERRED_AND_FROM_WHICH_CAPTURES>`

### `unverified`

- `<WHAT_STILL_REQUIRES_HUMAN_OR_SOURCE_VERIFICATION>`

### `observed`

- `<WHAT_WAS_VISIBLE_ON_THE_PAGE_OR_FILE>`

### `extracted`

- `<WHAT_THE_TOOL_EXTRACTED>`

### `inferred`

- `<WHAT_MAY_BE_INFERRED_AND_FROM_WHICH_CAPTURES>`

### `unverified`

- `<WHAT_STILL_REQUIRES_HUMAN_OR_SOURCE_VERIFICATION>`

## 六、冲突与证明边界

## 6. Conflicts and Limits of Proof

| 冲突编号 | 来源 A | 来源 B | 冲突内容 | 当前处理 | 是否已解决 |
| --- | --- | --- | --- | --- | --- |
| `CONFLICT-001` | `<CAP_OR_EVIDENCE_ID>` | `<CAP_OR_EVIDENCE_ID>` | `<FIELD_OR_FACT_CONFLICT>` | `<CROSS_CHECK_OR_HOLD>` | `YES / NO` |

| Conflict ID | Source A | Source B | Conflict | Current treatment | Resolved |
| --- | --- | --- | --- | --- | --- |
| `CONFLICT-001` | `<CAP_OR_EVIDENCE_ID>` | `<CAP_OR_EVIDENCE_ID>` | `<FIELD_OR_FACT_CONFLICT>` | `<CROSS_CHECK_OR_HOLD>` | `YES / NO` |

证明边界：

- 页面截图只证明截图时点的显示状态；
- 页面数据快照不是平台后台日志；
- 支付回单只证明回单所记载的支付行为；
- 工单截图没有显示结论，不等于平台从未处理；
- 机器转写和 OCR 必须回到原始材料复核。

Limits of proof:

- a page screenshot proves only the state displayed at capture time;
- a page-data snapshot is not a platform back-office log;
- a payment receipt proves only the payment recorded in that receipt;
- a work-order screenshot showing no conclusion does not mean the platform never processed it;
- machine transcripts and OCR must be checked against the original.

## 七、停止与未覆盖

## 7. Stop and Uncovered Scope

- 停止代码：`<NONE_OR_STOP_CODE>`
- 停止原因：`<REASON>`
- 未覆盖页面或文件：`<UNCOVERED_SCOPE>`
- 是否存在截断或空白：`YES / NO`
- 未采取的动作：`<ACTIONS_NOT_TAKEN>`
- 待用户处理：`<USER_ACTION>`
- 待法律复核：`<LEGAL_REVIEW_ITEM>`
- 待调查取证或责令提交：`<INVESTIGATION_OR_PRODUCTION_REQUEST>`

- Stop code: `<NONE_OR_STOP_CODE>`
- Reason: `<REASON>`
- Uncovered pages or files: `<UNCOVERED_SCOPE>`
- Truncated or blank content: `YES / NO`
- Actions not taken: `<ACTIONS_NOT_TAKEN>`
- User action required: `<USER_ACTION>`
- Legal review required: `<LEGAL_REVIEW_ITEM>`
- Investigation or production request: `<INVESTIGATION_OR_PRODUCTION_REQUEST>`

## 八、复核

## 8. Review

- 复核人：`<USER_OR_SYNTHETIC_REVIEWER>`
- 复核时间：`<TIMESTAMP_WITH_TIMEZONE>`
- 复核结论：`ACCEPTED / PARTIAL / REJECTED`
- 复核备注：`<NOTE>`

- Reviewer: `<USER_OR_SYNTHETIC_REVIEWER>`
- Review time: `<TIMESTAMP_WITH_TIMEZONE>`
- Result: `ACCEPTED / PARTIAL / REJECTED`
- Note: `<NOTE>`
