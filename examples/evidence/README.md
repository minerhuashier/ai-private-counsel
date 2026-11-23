# 证据取证模板

# Evidence Collection Templates

本目录只提供公开、通用、可复用的取证记录模板。所有案件字段均为占位符或完全虚构内容。

This directory contains public, generic, reusable templates for evidence collection. Every case field is a placeholder or entirely fictional.

## 文件

## Files

- [取证计划模板](collection-plan.template.md)：先确定待证事实、建议材料、控制方、用户配合方式和停止条件；
- [运行记录模板](collection-run.template.md)：记录一次浏览器读取或文件固定过程；
- [法律要件与证据矩阵模板](legal-evidence-matrix.template.md)：用规范要件反查事实、证据和缺口。

- [Collection plan](collection-plan.template.md): define facts to prove, proposed material, controller, user cooperation, and stop conditions;
- [Run record](collection-run.template.md): document one browser-read or file-preservation run;
- [Legal-elements and evidence matrix](legal-evidence-matrix.template.md): test facts, evidence, and gaps against legal elements.

## 使用顺序

## Sequence

```text
collection-plan
  -> user authorization
  -> collection-run
  -> originals and SHA-256
  -> Markdown/OCR/transcript derivatives
  -> legal-evidence-matrix
  -> gap list / investigation list
  -> human review
```

## 公开边界

## Public Boundary

不要在提交到公开仓库的模板实例中包含：

- 真实姓名、联系方式和身份证件；
- 订单号、交易号、账号、工单号和案号；
- 金额、真实商家、法院和具体地址；
- 聊天原文、录音、截图、合同附件或法院文书；
- 浏览器 Cookie、密码、验证码、Local Storage 或会话导出。

Do not include any of the following in an instance committed to the public repository:

- real names, contact details, or identity documents;
- order numbers, transaction identifiers, accounts, work-order numbers, or case numbers;
- amounts, a real merchant, a court, or a specific address;
- original chat text, audio, screenshots, contract attachments, or court documents;
- browser cookies, passwords, verification codes, local storage, or session exports.

真实材料应保存在用户的私有、加密和受控工作区。公开仓库只保留方法、模板和虚构示例。

Real material belongs in the user's private, encrypted, and controlled workspace. The public repository contains only methods, templates, and synthetic examples.
