# 证据协议

## 原件规则

- 原件永不修改；
- 所有裁剪、转写、OCR 和脱敏都写入新文件；
- 文件名不能替代证据编号和哈希；
- 证据移动、复制和导出应保留操作记录。

## 必备字段

每份证据至少登记：

- `evidence_id`；
- 原始文件名；
- 文件类型；
- SHA-256；
- 来源；
- 取得时间；
- 保管位置；
- 证明目的；
- 保密级别；
- 是否允许生成公开副本。

## 证明目的

证明目的应描述“该材料可以支持哪项事实”，而不是直接写结论。

不推荐：

> 证明平台诈骗。

推荐：

> 用于证明某日某时用户向平台提交了某项材料，以及平台页面显示的受理状态。

## 多份证据

多份材料可以共同证明一个事实，但应分别登记。不得为了形成完整叙事而把不同时间、不同主体的材料拼接成一份“新证据”而不说明处理过程。

## 公开副本

公开副本必须重新命名、脱敏并记录处理规则。公开副本的哈希与原件哈希分别保存。

---

# Evidence Protocol

## Original-File Rule

- Originals are never modified;
- cropping, transcription, OCR, and redaction always produce new files;
- filenames do not replace evidence IDs and hashes;
- moves, copies, and exports should retain an operation record.

## Required Fields

Record at least:

- `evidence_id`;
- original filename;
- file type;
- SHA-256;
- source;
- acquisition time;
- custody location;
- evidentiary purpose;
- confidentiality level;
- whether a public copy is permitted.

## Evidentiary Purpose

Describe the fact the material can support, not the desired legal conclusion.

Avoid:

> Prove that the platform committed fraud.

Prefer:

> Show that the user submitted a specific item to the platform at a specific time and show the status displayed by the platform.

## Multiple Items

Several materials may jointly support one fact, but each must be registered separately. Do not merge materials from different times or actors into a new "evidence item" without documenting the processing method.

## Public Copies

Public copies must be renamed, redacted, and linked to a documented processing rule. Store the public-copy hash separately from the original hash.

