# 安全政策

## 报告安全问题

请勿通过公开 Issue 提交以下内容：

- 密钥或访问令牌；
- 真实案件材料；
- 可识别个人的信息；
- 可直接利用的隐私绕过方式。

优先使用 GitHub 的私密漏洞报告功能。若仓库尚未启用该功能，请通过维护者公开资料中的私密联系方式联系，并只提供最少必要信息。

## 公开仓库安全设置

维护者应启用：

- Secret scanning；
- Push protection；
- Dependabot alerts；
- Code scanning；
- 分支保护；
- 必要时代码所有者审查。

## 凭据处理

一旦凭据进入提交历史，应立即视为泄露并撤销或轮换。仅从最新文件中删除不能消除风险。

## 支持范围

当前项目处于设计阶段。安全问题重点包括：

- 敏感文件误入仓库；
- 脱敏不完整；
- 引用核验被绕过；
- 人工批准状态被伪造；
- 自动执行未经授权的对外动作。

---

# Security Policy

## Reporting Security Issues

Do not use a public Issue to submit:

- secrets or access tokens;
- real case material;
- personally identifiable information;
- directly exploitable privacy bypasses.

Prefer GitHub's private vulnerability reporting. If unavailable, use a private contact method listed in the maintainer's public profile and provide only the minimum information necessary.

## Public Repository Settings

Maintainers should enable:

- Secret scanning;
- Push protection;
- Dependabot alerts;
- Code scanning;
- Branch protection;
- Code-owner review where needed.

## Credential Handling

Once a credential enters commit history, treat it as compromised and revoke or rotate it immediately. Deleting it from the latest file does not remove the risk.

## Scope

This project is currently in a design stage. Security priorities include:

- sensitive files entering the repository;
- incomplete redaction;
- bypassed source verification;
- forged human approval;
- unauthorized automated external actions.

