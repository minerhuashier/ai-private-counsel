# 法律来源核验协议

本协议规定“什么可以被当作来源”。完整下载、原件存档、PDF 数字化、版本比较和事实适用流程见 [从官方文本到可引用法律](legal-source-pipeline.md) 和 [法律法规来源存档与数字化 Skill](../skills/legal-source-archive/SKILL.md)。

## 可用来源

优先顺序：

1. 法律、行政法规、司法解释发布机关的官方文本；
2. 法院、检察院、政府部门或平台官方规则页面；
3. 官方数据库中的案例全文；
4. 有完整出处和版本信息的二次资料，仅用于发现问题。

搜索摘要、社交媒体帖文、模型记忆和无法打开来源的转载不能作为最终依据。

## 来源登记

每个来源必须记录：

- `source_id`；
- 类型；
- 标题；
- 发布机关；
- 文号；
- 公布日期；
- 生效日期；
- 官方 URL；
- 抓取时间；
- 原文 SHA-256；
- 核验状态；
- 适用范围与限制。

## 核验清单

- 标题和文号是否一致；
- 是否仍在生效；
- 是否已被修订或废止；
- 条号是否存在；
- 原文是否支持所述结论；
- 案例是否真实存在；
- 案例层级、地域和后续历史是否被正确表述。

## 失败处理

任一关键项无法确认时：

- 将来源标记为 `unverified`；
- 从正式草稿中移除该结论；
- 在待办中保留需要核验的问题；
- 不允许模型根据常识补全。

---

# Legal Source Verification Protocol

This protocol defines what may count as a source. See [From Official Text to Citable Law](legal-source-pipeline.md) and the [Legal Source Archival and Digitization Skill](../skills/legal-source-archive/SKILL.md) for the full retrieval, preservation, digitization, version-comparison, and fact-application workflow.

## Permitted Sources

Preferred order:

1. Official texts from the authority that issued the statute, administrative regulation, or judicial interpretation;
2. Official pages from courts, procuratorates, government departments, or platform operators;
3. Full-text cases in official databases;
4. Secondary material with complete provenance and version information, used only to identify issues.

Search snippets, social-media posts, model memory, and inaccessible reposts cannot be final authority.

## Source Record

Each source must record:

- `source_id`;
- type;
- title;
- issuer;
- document number;
- publication date;
- effective date;
- official URL;
- retrieval time;
- SHA-256 of the original text;
- verification status;
- scope and limitations.

## Verification Checklist

- Do the title and document number match?
- Is the source still in force?
- Has it been amended or repealed?
- Does the cited article exist?
- Does the original text support the proposition?
- Does the case actually exist?
- Are court level, jurisdiction, and subsequent history described accurately?

## Failure Handling

If any critical item cannot be confirmed:

- mark the source `unverified`;
- remove the conclusion from the formal draft;
- retain the verification question as an open task;
- do not let the model fill the gap from general knowledge.

