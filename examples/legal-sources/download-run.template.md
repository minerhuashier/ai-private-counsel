# 法律法规下载运行记录模板

> 仅使用占位符或完全虚构的信息。公开仓库不得写入真实账号、案号、案件材料、订单号、Cookie、令牌、私密 URL 或含个人信息的浏览器截图。

## 运行标识

| 字段 | 填写内容 |
| --- | --- |
| `run_id` | `RUN-<TYPE>-<NNN>` |
| 任务目标 | `<RETRIEVAL_OBJECTIVE>` |
| 法律问题 ID | `ISSUE-<NNN>` |
| `source_id` | `SRC-<TYPE>-<NNN>` |
| 操作者 | `agent / user / user_assisted` |
| 开始时间 | `YYYY-MM-DDTHH:MM:SS+08:00` |
| 完成时间 | `YYYY-MM-DDTHH:MM:SS+08:00` |
| 最终状态 | `captured / captured_unverified / verified / blocked_login / blocked_captcha / blocked_access / incomplete_text / source_conflict / chrome_channel_unavailable` |

## 通道与预检

| 字段 | 填写内容 |
| --- | --- |
| 浏览器通道 | `system_chrome / in_app_browser / web_search / http / user_supplied_file` |
| 操作契约 | `codex-chrome-ops / other_public_method / manual` |
| 预检命令 | `node "$HOME/.codex/skills/codex-chrome-ops/scripts/preflight.mjs" --json` |
| `ready` | `true / false / not_applicable` |
| Chrome 选择器 | `chrome / extension / not_applicable` |
| 实时文档已读 | `yes / no / not_applicable` |
| 通道限制 | `<CHANNEL_LIMITATIONS>` |

## 检索范围

| 字段 | 填写内容 |
| --- | --- |
| 目标规范名称 | `<OFFICIAL_TITLE_OR_UNKNOWN>` |
| 发布机关候选 | `<ISSUING_AUTHORITY>` |
| 起始 URL | `<START_URL>` |
| 最终 URL | `<FINAL_URL>` |
| 页面标题 | `<PAGE_TITLE>` |
| 检索词 | `<SEARCH_TERMS>` |
| 筛选条件 | `<FILTERS>` |
| 检查页数 | `<PAGES_CHECKED>` |
| 候选结果数 | `<CANDIDATE_COUNT>` |
| 分页或覆盖限制 | `<COVERAGE_LIMITS>` |
| 取得时间 | `YYYY-MM-DDTHH:MM:SS+08:00` |

## 页面观察

| 检查项 | 结果 |
| --- | --- |
| 页面显示正式标题 | `yes / no` |
| 页面显示发布机关 | `yes / no` |
| 页面显示文号 | `yes / no / not_applicable` |
| 页面显示公布或修正日期 | `yes / no` |
| 页面显示施行日期 | `yes / no` |
| 页面显示完整正文和附则 | `yes / no / partial` |
| 存在公开下载控件 | `yes / no / not_applicable` |
| 可见验证证据 | `<VISIBLE_MARKER_WITHOUT_PERSONAL_DATA>` |

## 执行动作

| 顺序 | 动作 | 结果 |
| --- | --- | --- |
| 1 | `navigate / search / click_public_download / read_html / observe_public_response / user_saved_file` | `<RESULT>` |
| 2 | `<ACTION>` | `<RESULT>` |
| 3 | `<ACTION>` | `<RESULT>` |

不得在此表填写 Cookie、Authorization、令牌、密码或会话值。

## 下载文件

| 字段 | 填写内容 |
| --- | --- |
| 公开标识 | `ART-<NNN>` |
| 原始文件名 | `<ORIGINAL_FILENAME>` |
| 原始格式 | `PDF / DOCX / HTML / JSON / other` |
| 文件类型检查 | `<FILE_COMMAND_RESULT>` |
| 字节数 | `<BYTE_COUNT>` |
| PDF 页数 | `<PAGE_COUNT_OR_NOT_APPLICABLE>` |
| 字符数 | `<CHARACTER_COUNT_OR_NOT_APPLICABLE>` |
| 原件 SHA-256 | `<64_LOWERCASE_HEX>` |
| 下载完成证据 | `<BROWSER_STATE_OR_USER_CONFIRMATION>` |
| 下载后页面复核 | `passed / failed / not_applicable` |

公开模板不记录本机绝对路径。私有工作区可以使用内部制品编号定位文件。

## 数字化

| 字段 | 填写内容 |
| --- | --- |
| 数字化分支 | `pdf-text / official-docx / official-html / ocr / raw-html-json / derived-rendering` |
| 转换工具和版本 | `<TOOL_AND_VERSION>` |
| 派生文本标识 | `TEXT-<NNN>` |
| 派生文本 SHA-256 | `<64_LOWERCASE_HEX>` |
| 首尾和附则已核对 | `yes / no` |
| 条号连续性已核对 | `yes / no / not_checked` |
| 关键条文已对照 | `yes / no` |
| OCR 已人工复核 | `yes / no / not_applicable` |
| 数字化限制 | `<LIMITATIONS>` |

## 异常与人工接管

| 字段 | 填写内容 |
| --- | --- |
| 是否遇到登录 | `yes / no` |
| 是否遇到验证码 | `yes / no` |
| 是否遇到重定向 | `yes / no` |
| 是否遇到证书异常 | `yes / no` |
| 是否遇到 4xx 或 5xx | `yes / no` |
| 失败原因 | `<FAILURE_REASON_OR_NONE>` |
| 人工接管事项 | `<USER_ACTION_OR_NONE>` |
| 是否发生通道切换 | `yes / no` |
| 通道切换授权 | `<USER_APPROVAL_OR_NOT_APPLICABLE>` |

## 核验结论

| 字段 | 填写内容 |
| --- | --- |
| 来源身份 | `confirmed / conflict / unverified` |
| 完整性 | `complete / partial / unavailable` |
| 版本匹配 | `confirmed / conflict / unverified` |
| 允许进入引用层 | `yes / no` |
| 未解决事项 | `<OPEN_ITEMS>` |
| 复核人 | `<USER_OR_REVIEWER>` |
| 复核时间 | `YYYY-MM-DDTHH:MM:SS+08:00` |

---

# Legal-Source Download Run Record Template

> Use placeholders or entirely fictional information only. The public repository must not contain real accounts, case numbers, case materials, order identifiers, cookies, tokens, private URLs, or personal browser screenshots.

## Run Identity

| Field | Value |
| --- | --- |
| `run_id` | `RUN-<TYPE>-<NNN>` |
| Retrieval objective | `<RETRIEVAL_OBJECTIVE>` |
| Legal issue ID | `ISSUE-<NNN>` |
| `source_id` | `SRC-<TYPE>-<NNN>` |
| Operator | `agent / user / user_assisted` |
| Started at | `YYYY-MM-DDTHH:MM:SS+08:00` |
| Completed at | `YYYY-MM-DDTHH:MM:SS+08:00` |
| Final status | `captured / captured_unverified / verified / blocked_login / blocked_captcha / blocked_access / incomplete_text / source_conflict / chrome_channel_unavailable` |

## Channel and Preflight

| Field | Value |
| --- | --- |
| Browser channel | `system_chrome / in_app_browser / web_search / http / user_supplied_file` |
| Operating contract | `codex-chrome-ops / other_public_method / manual` |
| Preflight command | `node "$HOME/.codex/skills/codex-chrome-ops/scripts/preflight.mjs" --json` |
| `ready` | `true / false / not_applicable` |
| Chrome selector | `chrome / extension / not_applicable` |
| Live documentation read | `yes / no / not_applicable` |
| Channel limitations | `<CHANNEL_LIMITATIONS>` |

## Search Scope

| Field | Value |
| --- | --- |
| Target title | `<OFFICIAL_TITLE_OR_UNKNOWN>` |
| Candidate issuer | `<ISSUING_AUTHORITY>` |
| Start URL | `<START_URL>` |
| Final URL | `<FINAL_URL>` |
| Page title | `<PAGE_TITLE>` |
| Query | `<SEARCH_TERMS>` |
| Filters | `<FILTERS>` |
| Pages checked | `<PAGES_CHECKED>` |
| Candidate count | `<CANDIDATE_COUNT>` |
| Pagination or coverage limits | `<COVERAGE_LIMITS>` |
| Captured at | `YYYY-MM-DDTHH:MM:SS+08:00` |

## Page Observation

| Check | Result |
| --- | --- |
| Formal title displayed | `yes / no` |
| Issuer displayed | `yes / no` |
| Document number displayed | `yes / no / not_applicable` |
| Publication or amendment date displayed | `yes / no` |
| Effective date displayed | `yes / no` |
| Complete body and supplementary provisions displayed | `yes / no / partial` |
| Public download control present | `yes / no / not_applicable` |
| Visible verification marker | `<VISIBLE_MARKER_WITHOUT_PERSONAL_DATA>` |

## Actions

| Order | Action | Result |
| --- | --- | --- |
| 1 | `navigate / search / click_public_download / read_html / observe_public_response / user_saved_file` | `<RESULT>` |
| 2 | `<ACTION>` | `<RESULT>` |
| 3 | `<ACTION>` | `<RESULT>` |

Do not record cookies, authorization headers, tokens, passwords, or session values.

## Downloaded File

| Field | Value |
| --- | --- |
| Public artifact token | `ART-<NNN>` |
| Original filename | `<ORIGINAL_FILENAME_OR_PLACEHOLDER>` |
| Original format | `PDF / DOCX / HTML / JSON / other` |
| File-type check | `<FILE_COMMAND_RESULT>` |
| Byte count | `<BYTE_COUNT>` |
| PDF page count | `<PAGE_COUNT_OR_NOT_APPLICABLE>` |
| Character count | `<CHARACTER_COUNT_OR_NOT_APPLICABLE>` |
| Original SHA-256 | `<64_LOWERCASE_HEX>` |
| Download-completion evidence | `<BROWSER_STATE_OR_USER_CONFIRMATION>` |
| Post-download page check | `passed / failed / not_applicable` |

The public template does not record absolute local paths. A private workspace may use an internal artifact token.

## Digitization

| Field | Value |
| --- | --- |
| Digitization branch | `pdf-text / official-docx / official-html / ocr / raw-html-json / derived-rendering` |
| Conversion tool and version | `<TOOL_AND_VERSION>` |
| Derived-text token | `TEXT-<NNN>` |
| Derived-text SHA-256 | `<64_LOWERCASE_HEX>` |
| First, last, and supplementary provisions checked | `yes / no` |
| Article continuity checked | `yes / no / not_checked` |
| Key articles compared | `yes / no` |
| OCR manually reviewed | `yes / no / not_applicable` |
| Digitization limitations | `<LIMITATIONS>` |

## Exceptions and User Takeover

| Field | Value |
| --- | --- |
| Login encountered | `yes / no` |
| CAPTCHA encountered | `yes / no` |
| Redirect encountered | `yes / no` |
| Certificate anomaly encountered | `yes / no` |
| HTTP 4xx or 5xx encountered | `yes / no` |
| Failure reason | `<FAILURE_REASON_OR_NONE>` |
| User takeover required | `<USER_ACTION_OR_NONE>` |
| Channel changed | `yes / no` |
| User approval for channel change | `<USER_APPROVAL_OR_NOT_APPLICABLE>` |

## Verification Conclusion

| Field | Value |
| --- | --- |
| Source identity | `confirmed / conflict / unverified` |
| Completeness | `complete / partial / unavailable` |
| Version match | `confirmed / conflict / unverified` |
| May enter citation layer | `yes / no` |
| Open items | `<OPEN_ITEMS>` |
| Reviewer | `<USER_OR_REVIEWER>` |
| Reviewed at | `YYYY-MM-DDTHH:MM:SS+08:00` |
