# 法律法规来源登记模板

> 本文件只提供字段和占位符，不包含真实案件材料。法律、法规名称可以完整填写；案件当事人、案号、法院具体案件信息、联系方式、订单号和证据标识不进入公开仓库。

## 来源主记录

| 字段 | 填写内容 |
| --- | --- |
| `source_id` | `SRC-<TYPE>-<NNN>` |
| 完整标题 | `<LEGAL_INSTRUMENT_TITLE>` |
| 发布机关 | `<ISSUING_AUTHORITY>` |
| 文号 | `<DOCUMENT_NUMBER_OR_NONE>` |
| 规范类型 | `statute / administrative_regulation / judicial_interpretation / departmental_rule / platform_rule` |
| 版本 | `<VERSION_OR_AMENDMENT>` |
| 公布日期 | `YYYY-MM-DD` |
| 施行日期 | `YYYY-MM-DD` |
| 事实发生时版本 | `<VERSION_AT_RELEVANT_DATE>` |
| 官方 URL | `<OFFICIAL_URL>` |
| 取得时间 | `YYYY-MM-DDTHH:MM:SS+08:00` |
| 原始格式 | `PDF / DOCX / HTML / JSON` |
| 原始页数或字符数 | `<COUNT>` |
| 原件 SHA-256 | `<64_LOWERCASE_HEX>` |
| 派生文本 SHA-256 | `<64_LOWERCASE_HEX>` |
| 核验状态 | `unverified / verified / superseded / repealed` |
| 已知限制 | `<LIMITATIONS_OR_NONE>` |

## 数字化记录

| 检查项 | 结果 |
| --- | --- |
| PDF 是否带可靠文本层 | `yes / no / not_applicable` |
| 使用的转换分支 | `pdf-text / official-docx / official-html / ocr / raw-html-json` |
| 转换工具和版本 | `<TOOL_AND_VERSION>` |
| 是否逐条检查条号 | `yes / no` |
| 是否核对首尾和附则 | `yes / no` |
| 是否对照关键条文 | `yes / no` |
| OCR 是否人工复核 | `yes / no / not_applicable` |
| 转换限制 | `<LIMITATIONS>` |

## 使用记录

| 法律问题 | 条号 | 要件 | 对应事实 | 对应证据 | 结论状态 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| `<ISSUE>` | `<ARTICLE>` | `<ELEMENTS>` | `<FACTS>` | `<EVIDENCE_IDS>` | `verified / unverified` | `<NOTES>` |

## 复核签字位

- 复核人：`<USER_OR_REVIEWER>`
- 复核时间：`YYYY-MM-DDTHH:MM:SS+08:00`
- 复核范围：`<SCOPE>`
- 未解决事项：`<OPEN_ITEMS>`

---

# Legal Source Register Template

> This file provides fields and placeholders only. Names of statutes and regulations may be written in full. Parties, case numbers, case-specific court information, contact details, order identifiers, and evidence identifiers do not enter the public repository.

## Main Source Record

| Field | Value |
| --- | --- |
| `source_id` | `SRC-<TYPE>-<NNN>` |
| Full title | `<LEGAL_INSTRUMENT_TITLE>` |
| Issuing authority | `<ISSUING_AUTHORITY>` |
| Document number | `<DOCUMENT_NUMBER_OR_NONE>` |
| Source type | `statute / administrative_regulation / judicial_interpretation / departmental_rule / platform_rule` |
| Version | `<VERSION_OR_AMENDMENT>` |
| Publication date | `YYYY-MM-DD` |
| Effective date | `YYYY-MM-DD` |
| Version at relevant date | `<VERSION_AT_RELEVANT_DATE>` |
| Official URL | `<OFFICIAL_URL>` |
| Retrieval time | `YYYY-MM-DDTHH:MM:SS+08:00` |
| Original format | `PDF / DOCX / HTML / JSON` |
| Page or character count | `<COUNT>` |
| Original SHA-256 | `<64_LOWERCASE_HEX>` |
| Derived-text SHA-256 | `<64_LOWERCASE_HEX>` |
| Verification status | `unverified / verified / superseded / repealed` |
| Known limitations | `<LIMITATIONS_OR_NONE>` |

## Digitization Record

| Check | Result |
| --- | --- |
| PDF has a reliable text layer | `yes / no / not_applicable` |
| Conversion branch | `pdf-text / official-docx / official-html / ocr / raw-html-json` |
| Conversion tool and version | `<TOOL_AND_VERSION>` |
| Article numbers checked | `yes / no` |
| First, last, and supplementary provisions checked | `yes / no` |
| Key articles compared | `yes / no` |
| OCR manually reviewed | `yes / no / not_applicable` |
| Conversion limitations | `<LIMITATIONS>` |

## Use Record

| Legal issue | Article | Elements | Facts | Evidence | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `<ISSUE>` | `<ARTICLE>` | `<ELEMENTS>` | `<FACTS>` | `<EVIDENCE_IDS>` | `verified / unverified` | `<NOTES>` |

## Review

- Reviewer: `<USER_OR_REVIEWER>`
- Reviewed at: `YYYY-MM-DDTHH:MM:SS+08:00`
- Scope: `<SCOPE>`
- Open items: `<OPEN_ITEMS>`
