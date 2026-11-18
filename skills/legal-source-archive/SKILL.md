# 法律法规来源存档与数字化

## 用途

把公开法律、行政法规、司法解释、部门规章和平台规则整理成可追溯、可检索、可引用的来源链。它解决的是“这条法条从哪里来、是不是现行版本、原文是否真的这样写、转换后有没有丢字”，而不是替用户决定案件策略。

## 适用场景

- 需要从官方来源下载法律法规；
- 需要把 PDF、DOCX 或官方网页转换为 Markdown；
- 需要核对法律版本、文号、条号和施行日期；
- 需要为研究备忘录、证据分析或待审文书建立来源台账；
- 需要比较多份法规或同一法规的不同版本。

## 不适用场景

- 把搜索摘要当作法律依据；
- 凭模型记忆回答法条；
- 代替律师给出个案法律意见；
- 代替用户签署、缴费、提交法院或公开发布；
- 绕过 PDF、网站或平台的访问限制。

## 输入

- 争议问题和待判断的法律关系；
- 法域、争议事实时间和程序阶段；
- 现有官方法律来源或候选 URL；
- 工作目录和文件命名规则；
- 允许使用的联网、浏览器、PDF 和文档工具。

## 输出

- 未经修改的官方原件；
- 可全文检索的 Markdown 或纯文本；
- 来源登记表；
- 版本和效力核对记录；
- 关键条文摘录；
- “问题—要件—规范—事实—证据”矩阵；
- 未核实项、冲突和失败关闭说明。

## 执行流程

### 1. 建立问题清单

先把争议拆成具体问题，不要直接要求“找所有有利法条”。对每项问题记录：

- 争议事实发生时间；
- 当前程序阶段；
- 可能适用的规范层级；
- 需要证明的构成要件；
- 需要排除的例外或时间效力问题。

### 2. 建立来源候选表

为每个候选规范记录：

- 完整名称；
- 发布机关；
- 文号；
- 版本；
- 官方候选 URL；
- 初步适用理由；
- 当前核验状态。

找不到官方来源时标记 `UNVERIFIED`。

### 3. 下载原件

优先顺序：

1. 发布机关官网的 PDF、DOCX 或 HTML；
2. 国家法律法规数据库、最高人民法院公报等官方平台；
3. 政府公报或官方报刊全文；
4. 平台官方规则页或公开接口。

下载后：

- 保留原始扩展名；
- 不覆盖同名旧版本，改用版本号或日期区分；
- 记录官方 URL 和取得时间；
- 计算 SHA-256；
- 记录页数或字符数；
- 检查是否真的是全文，而不是登录页、错误页、摘要页或验证码页。

### 4. 判断数字化分支

先检查 PDF 文本层：

```bash
pdfinfo "input.pdf"
pdftotext -f 1 -l 1 "input.pdf" -
```

分支：

- 文本层可靠：提取文本并规范为 Markdown；
- 有官方 DOCX：优先使用官方 DOCX 转换；
- 扫描 PDF 但官网有 HTML 全文：保留扫描件，用官方 HTML 生成检索文本；
- 只能 OCR：标记 `OCR_UNVERIFIED`，逐段对照原 PDF；
- 动态网页：保存原始 HTML 或 JSON，再提取正文。

### 5. 规范 Markdown

每份文本至少包含：

- 标题；
- 发布机关；
- 文号；
- 公布日期；
- 施行日期；
- 版本或修正信息；
- 官方 URL；
- 取得时间；
- 原件哈希；
- 正文；
- 附则；
- 数字化限制。

保持原始条号，不让转换工具自动重编号。

### 6. 复核

必须检查：

- 标题、发布机关、文号；
- 第一条和最后一条；
- 条号连续性；
- 附则和施行日期；
- 关键条文与原件逐字一致；
- 数字、期限、百分比和“条/款/项”；
- 缺页、重复、乱码、截断和双栏交错；
- UTF-8 编码；
- 原件和派生文本分别有 SHA-256。

### 7. 建立适用矩阵

每一行至少包含：

| 问题 | 规范 | 版本 | 条号 | 要件 | 已证事实 | 证据 | 缺口 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `issue` | `title` | `version` | `article` | `elements` | `facts` | `evidence IDs` | `gap` | `verified/unverified` |

### 8. 输出引用

内部记录至少包含：

```text
法律全称 + 版本 + 条号
source_id
官方 URL
取得时间
原件 SHA-256
派生文本 SHA-256
核验状态
适用范围和限制
```

## 失败关闭

出现下列任一情况时停止：

- 找不到官方来源；
- 同一名称存在多个版本且无法确定适用版本；
- PDF、DOCX、HTML 和 Markdown 关键条文不一致；
- PDF 缺页、乱码或无法确认全文；
- OCR 文本未经原 PDF 复核；
- 页面只显示摘要或登录墙；
- 规范尚未生效、已经废止或只是草案；
- 需要模型凭常识补全文号、条号或内容。

## 工具

- 联网检索：`anysearch` 或浏览器；
- 网页正文提取：`defuddle`、浏览器或公开接口；
- PDF：`pdfinfo`、`pdftotext`，或 PDF 处理技能；
- DOCX：`pandoc` 或文档处理技能；
- 哈希：`shasum -a 256`；
- 检索：`rg`；
- 矩阵：Markdown 表格或电子表格技能。

工具只是执行手段。任何工具的输出都必须回到官方原件核对。

## 红线

- 原件只读；
- 不使用搜索摘要替代原文；
- 不把草案当成现行法；
- 不编造文号、条号、案例或裁判观点；
- 不把 OCR 结果直接当作正式引文；
- 不把平台规则自动提升为法律；
- 不替用户决定诉讼策略或执行外部动作。

完整方法见 [从官方文本到可引用法律](../../docs/legal-source-pipeline.md)。

---

# Legal Source Archival and Digitization

## Purpose

Build a traceable, searchable, citable source chain for public statutes, administrative regulations, judicial interpretations, departmental rules, and platform rules. The skill answers: where did this rule come from, is it the effective version, does the original text really say this, and did conversion lose any content? It does not decide case strategy.

## Use When

- official legal sources must be downloaded;
- PDF, DOCX, or official web pages must be converted to Markdown;
- versions, document numbers, articles, and effective dates must be checked;
- a source register is needed for a research memo, evidence analysis, or review draft;
- multiple instruments or versions must be compared.

## Do Not Use To

- treat search snippets as authority;
- answer from model memory;
- replace a lawyer's case-specific advice;
- sign, pay, file, or publish for the user;
- bypass access controls.

## Inputs

- disputed issues and legal relationships;
- jurisdiction, fact date, and procedural stage;
- existing official sources or candidate URLs;
- working directory and naming rules;
- permitted web, browser, PDF, and document tools.

## Outputs

- unmodified official originals;
- searchable Markdown or plain text;
- source register;
- version and validity checks;
- key-article excerpts;
- issue-element-authority-fact-evidence matrix;
- unverified items, conflicts, and fail-closed notes.

## Workflow

1. Turn the dispute into specific legal questions with a fact cutoff date.
2. Build a candidate source table with title, issuer, document number, version, official URL, reason for possible application, and verification status.
3. Prefer official PDF, DOCX, or HTML from the issuing authority, a statutory database, an official gazette, or an official platform page.
4. Preserve the original, retrieval time, URL, page count, and SHA-256. Verify that the file is the complete text rather than a login page, error page, snippet, or CAPTCHA page.
5. Test the PDF text layer with `pdfinfo` and `pdftotext`.
6. Choose the correct branch:
   - usable PDF text layer;
   - official DOCX;
   - scanned PDF plus official HTML;
   - OCR as a last resort;
   - raw HTML or JSON for dynamic platform rules.
7. Normalize into Markdown while retaining title, issuer, document number, publication date, effective date, version, official URL, retrieval time, original hash, body, supplementary provisions, and limitations.
8. Check first and last articles, article continuity, key articles, figures, deadlines, paragraph/item numbers, missing pages, duplication, garbling, columns, and encoding.
9. Hash the original and the derived text separately.
10. Build an issue-element-authority-fact-evidence matrix.
11. Mark unsupported propositions `unverified` and stop when source versions conflict.

## Fail-Closed Conditions

- No official source is available;
- several versions exist and the applicable one cannot be identified;
- the PDF, DOCX, HTML, and Markdown conflict on key language;
- the PDF is incomplete, garbled, or unreadable;
- OCR has not been checked against the original;
- the page shows only a snippet or login wall;
- the instrument is not yet effective, has been repealed, or is only a draft;
- completing the record would require model memory or invention.

## Tools

- web retrieval: `anysearch`, browser;
- page extraction: `defuddle`, browser, or public API;
- PDF: `pdfinfo`, `pdftotext`, or a PDF processing skill;
- DOCX: `pandoc` or a document processing skill;
- hashing: `shasum -a 256`;
- local search: `rg`;
- matrix: Markdown table or spreadsheet skill.

Tools do not replace comparison with the official original.

## Red Lines

- Keep originals read-only;
- never use a search snippet as final authority;
- never treat a draft as effective law;
- never invent document numbers, articles, cases, or judicial reasoning;
- never use unchecked OCR as a formal citation;
- never elevate a platform rule to a statute;
- never decide strategy or perform external actions for the user.

See [From Official Text to Citable Law](../../docs/legal-source-pipeline.md).
