# 威胁模型

## 主要风险

| 风险 | 示例 | 控制 |
| --- | --- | --- |
| 虚构权威 | 生成不存在的法条、案号或判例 | 来源白名单、外部核验、失败关闭 |
| 事实污染 | 把模型推测写成确定事实 | 事实分类、证据编号、人工确认 |
| 隐私泄露 | 真实材料进入公开仓库或外部模型 | 双仓库隔离、最小化、公开检查器 |
| 误执行 | 自动提交错误文书或重复缴费 | 动作分级、批准令牌、禁止自动化 |
| 版本漂移 | 修改了错误草稿或使用失效规则 | 哈希、版本号、时间戳、审计日志 |
| 过度依赖 | 用户把模型输出当作律师意见 | 显式声明、不确定性展示、人工复核 |
| 公开传播反噬 | 公开发言与诉讼陈述不一致 | 事实底稿、延迟发布、发布审批 |

## 信任边界

- 本地文件：默认私密；
- 外部模型：默认不可信，不做长期私密存储；
- 网页搜索结果：只作为线索，不作为最终来源；
- 模型输出：默认错误，直到完成核验；
- 用户批准：只对明确版本和明确动作有效。

## 不在本版本内解决

- 完整电子签名；
- 法院系统自动提交；
- 多租户账户和权限系统；
- 大规模法律知识库；
- 各法域的全面合规认证。

---

# Threat Model

## Main Risks

| Risk | Example | Control |
| --- | --- | --- |
| Fabricated authority | Generating a nonexistent statute, case number, or case | Source allowlist, external verification, fail closed |
| Fact contamination | Turning model speculation into a definite fact | Fact classification, evidence IDs, human confirmation |
| Privacy leak | Real material entering a public repository or external model | Private/public separation, minimization, public-safety checker |
| Unauthorized action | Automatically filing a wrong document or paying twice | Action levels, approval records, automation prohibition |
| Version drift | Editing the wrong draft or using an obsolete rule | Hashes, version IDs, timestamps, audit logs |
| Overreliance | Treating model output as legal advice | Explicit disclaimer, uncertainty display, human review |
| Public-post backlash | A public statement conflicts with a litigation position | Factual record, delayed publication, publication approval |

## Trust Boundaries

- Local files: private by default;
- External models: untrusted by default and unsuitable for long-term private storage;
- Web search results: leads only, not final authority;
- Model output: presumed erroneous until verified;
- User approval: valid only for the exact version and action specified.

## Out of Scope for This Version

- Full electronic signatures;
- Automated court filing;
- Multi-tenant accounts and permissions;
- A large-scale legal knowledge base;
- Comprehensive compliance certification across jurisdictions.

