# 隐私规范

## 公开仓库禁止的数据

以下内容不得提交到本仓库，包括 Issue、Pull Request、Discussion、Wiki 和测试夹具：

- 真实姓名、身份证件、手机号、住址、邮箱和银行卡；
- 订单号、支付流水号、账号、Cookie、访问令牌和密钥；
- 法院案号与可识别当事人的法院文书；
- 聊天记录、录音、视频、人脸、头像和签名；
- 未公开的合同、投诉材料、证据目录和代理意见；
- 任何能够通过组合信息识别个人的材料。

## 本地优先

工具设计优先采用本地文件和本地数据库。需要调用外部模型时：

1. 先脱敏；
2. 只发送完成任务所需的最小内容；
3. 不上传原件；
4. 记录发送范围和目的；
5. 遵守所用服务的隐私与数据保留条款。

## 公开副本

真实材料只有经过人工脱敏并重新制作成公开副本后才能展示。公开副本必须：

- 去除直接和间接标识；
- 裁掉二维码、条形码、账号信息；
- 清除文档元数据；
- 使用虚构或概括性文字替代敏感细节；
- 保留脱敏记录，但不公开原始值。

## 数据删除

如果敏感数据误入公开仓库，仅删除最新文件不够，因为 Git 历史仍可能保留。应立即停止公开传播、撤销相关凭据，并按照 Git 历史清理流程处理。

---

# Privacy Standard

## Data Prohibited from the Public Repository

Never submit the following to this repository, including Issues, Pull Requests, Discussions, Wikis, or test fixtures:

- real names, identity documents, phone numbers, addresses, email addresses, or bank cards;
- order numbers, payment references, account IDs, cookies, access tokens, or secrets;
- court case numbers and court documents that identify a party;
- chats, recordings, videos, faces, avatars, or signatures;
- unpublished contracts, complaints, evidence indexes, or advocacy materials;
- any material that can identify an individual through combined information.

## Local First

Prefer local files and local databases. When an external model is required:

1. redact first;
2. send only the minimum content necessary;
3. never upload originals;
4. record the purpose and scope of transmission;
5. follow the provider's privacy and retention terms.

## Public Copies

Real material may be shown only after human redaction and the creation of a new public copy. A public copy must:

- remove direct and indirect identifiers;
- crop QR codes, barcodes, and account information;
- remove document metadata;
- replace sensitive details with fictional or generalized wording;
- retain a redaction record without publishing the original values.

## Data Deletion

If sensitive data enters a public repository, deleting the latest file is not enough because Git history may retain it. Stop publication, revoke affected credentials, and follow a Git-history cleanup procedure immediately.

