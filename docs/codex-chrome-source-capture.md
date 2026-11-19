# 用系统 Chrome 检索、下载与固定法律法规：`codex-chrome-ops` 实操记录

版本：`0.1.0`
状态：公开技术说明
整理日期：`2026-11-18`

## 结论先行

法律法规下载不是“打开网页，点一下 PDF”这么简单。一个可复核的下载任务至少要同时回答五个问题：

1. **找到的是不是发布机关或其正式公开平台？**
2. **浏览器最终停在哪个 URL，页面是否完整显示目标文本？**
3. **下载到的是 PDF、DOCX、HTML、JSON，还是伪装成文件的错误页？**
4. **文件是否完整，原始文件和派生文本的哈希是否已经登记？**
5. **遇到登录、验证码、重定向、证书异常或服务错误时，是否停止而不是绕过？**

本项目早期实际混合使用了联网搜索、内置浏览器、HTTP 抓取和公开详情接口。后来的 `codex-chrome-ops` Skill 把这些经验固化成系统 Chrome 的操作契约：先预检，再连接；只操作明确页面；从最终页面、下载文件或业务状态验证结果；连接失败时不静默切换浏览器。

> 历史记录是什么通道，就登记什么通道。
> 不能把早期操作追溯改写成系统 Chrome：记录当时真实使用的通道，再单独说明后来形成的系统 Chrome 操作契约。

## 一、这套方法从哪里来

项目早期的资料下载经历形成了四类可复用经验。

### 1. 先有来源队列，再打开浏览器

浏览器不会替人决定一份规范是否可能适用。正确顺序是：

```text
争议问题
  -> 待核规范清单
  -> 可能的发布机关
  -> 官方站点或正式公开平台
  -> 检索与下载
  -> 来源核验
```

如果先随意搜索关键词，再把搜索结果拼成“法律依据”，后续很难证明检索范围、版本和遗漏。

### 2. 网页搜索负责发现，不负责定稿

联网搜索适合找到发布机关、正式标题、文号和可能的官方入口。搜索摘要、页面卡片和二次转载只能用于发现线索。

以下内容都不能直接进入正式引用：

- 搜索摘要；
- 社交媒体转述；
- 无发布机关的转载；
- 只显示部分条文的页面；
- 模型根据常识补出的条号或文号。

### 3. 静态页面用可重复抓取，动态页面才交给浏览器

内容稳定的官方 HTML、PDF 或 DOCX，有时可以用 HTTP 请求保存并通过哈希复核。JavaScript 动态加载、分页、公开详情响应、原生下载按钮或登录后的公开页面，则更适合用浏览器完成。

选择通道的标准不是“哪个工具更自动”，而是：

- 页面是否需要 JavaScript；
- 是否需要点击公开下载控件；
- 是否能从最终 URL 和页面状态确认来源；
- 是否能保留下载文件或公开响应；
- 是否涉及登录、验证码、Cookie 或其他访问控制。

### 4. 浏览器操作与文件处理分开

浏览器负责导航、读取公开页面、触发公开下载和确认最终页面。文件下载后，再由本地工具完成：

```text
文件类型识别
  -> 页数或字符数
  -> 文本层抽查
  -> SHA-256
  -> 正文转换
  -> 版本与条号核对
```

浏览器显示“下载完成”不等于文件已经可引用。真正的验证对象是磁盘上的文件。

### 5. 与历史记录的边界

项目早期资料下载阶段实际出现过：

- 联网搜索定位官方来源；
- 内置浏览器读取页面并检查 DOM；
- HTTP 请求保存官方 HTML；
- 从国家法律法规数据库的公开页面和前端资源中发现公开详情或下载入口；
- 通过公开响应取得动态规则正文；
- 使用 `pdfinfo`、`pdftotext` 和 `pandoc` 处理文件；
- 在没有可靠文本层时优先补取官方 HTML 或 DOCX。

后来形成的 `codex-chrome-ops` 是面向系统 Chrome 的强化操作契约。它继承的是这些任务经验、失败处理和验证原则，不代表早期每一步都由系统 Chrome 执行。

### 6. 从 `02-资料下载` 到自研 `codex-chrome-ops`

`02-资料下载` 阶段的真实工作不是单一工具完成的，而是一条逐步收敛的技术链：

```text
联网搜索发现候选来源
  -> 打开官方页面
  -> 用内置浏览器检查 DOM、动态加载和页面公开状态
  -> 从官方页面、公开详情响应或下载入口取得正文或原件
  -> 必要时用 HTTP 保存静态官方文件
  -> 用 pdfinfo、pdftotext、pandoc、shasum 完成验证和数字化
```

这一阶段暴露出几个需要长期固化的问题：

- 搜索结果页、详情页和最终下载 URL 经常不是同一个地址；
- 页面可能先显示空壳，正文由公开响应或 `window.__INITIAL_STATE__` 一类的页面公开状态补全；
- 原生下载控件、公开 HTML 和 HTTP 抓取适用于不同页面，不能混在一个“下载成功”结论里；
- 浏览器提示下载完成，并不等于文件类型、页数、正文和版本都正确；
- 登录、验证码、证书异常或扩展连接失败时，如果没有停止规则，很容易误用其他通道或错误材料。

因此，后来把这些一次性的处理经验整理成了用户自研的 `codex-chrome-ops` Skill。它的定位不是替代官方浏览器插件，也不是自研 Chrome 扩展，而是建立在官方 `control-chrome` 传输层上的**操作契约层**：

| 组成 | 作用 |
| --- | --- |
| `SKILL.md` | 规定系统 Chrome 的选择、预检、授权边界、验证和禁止静默换通道 |
| `scripts/preflight.mjs` | 检查插件路径、Chrome 安装与进程、扩展、Native Host 和浏览器客户端 |
| `references/query-playbook.md` | 定义检索范围、稳定页面信号、结构化提取、分页和覆盖限制 |
| `references/form-playbook.md` | 规定表单、上传和外部副作用发生前的检查与结果验证 |
| `references/recovery.md` | 处理连接失败、旧标签页、定位器失败、权限和结果不确定状态 |

这套 Skill 把“我当时是怎么点开的”提升为“下一次仍然能重复、能停下来、能证明结果”的流程。对于法律法规下载，最重要的变化不是多了一个按钮操作，而是每次都能回答：用了哪个通道、最终到了哪里、取得了什么文件、如何验证、哪里没有覆盖。

## 二、浏览器通道如何分工

| 通道 | 适用任务 | 能得到什么 | 不能宣称什么 |
| --- | --- | --- | --- |
| 联网搜索 | 发现问题、定位正式标题和发布机关 | 候选官方入口和检索线索 | 不能把摘要当作法律原文 |
| `codex-chrome-ops` 控制的本机系统 Chrome | 动态页面、公开下载、用户已明确要求的 Chrome 操作 | 页面状态、最终 URL、公开下载文件、公开响应摘要 | 不得绕过登录、验证码或访问控制 |
| 内置浏览器 | 不要求系统 Chrome 的页面阅读、DOM 检查和可视化核验 | 页面文本、结构、截图或公开网络响应 | 不能登记成“系统 Chrome 下载” |
| HTTP 抓取 | 不需要浏览器交互的静态官方页面或公开文件 | 原始 HTML、PDF、DOCX、JSON 及状态码 | 不能绕过证书、鉴权或反爬限制 |
| 本地文件工具 | 下载后的完整性、数字化和哈希验证 | 页数、文本层、转换文本和哈希 | 不能替代官方来源真实性核验 |

同一任务可以组合多个通道，但运行记录必须逐项写清楚。例如：

```text
system Chrome -> 点击官方 PDF 下载
local shell   -> file / pdfinfo / pdftotext / shasum
manual review -> 核对标题、版本、首尾条号和关键条文
```

这不是三个“下载来源”，而是一条下载、验证和引用链的三个步骤。

## 三、`codex-chrome-ops` 的启动契约

### 1. 先运行预检

在全新会话、浏览器重连、插件更新或怀疑扩展桥接失效时，先运行：

```bash
node "$HOME/.codex/skills/codex-chrome-ops/scripts/preflight.mjs" --json
```

预检用于确认：

- Chrome 插件脚本路径存在；
- 本机安装了受支持的 Chrome；
- Chrome 正在运行；
- 官方扩展已安装并启用；
- Native Host manifest 可用；
- 浏览器客户端脚本存在。

只有结果中的 `ready: true` 才表示可以继续。

如果 `ready` 不是 `true`：

1. 根据失败项修复环境；
2. 如果只是 Chrome 未运行，请用户打开 Chrome；
3. 重新执行同一个预检；
4. 不得用内置浏览器、Computer Use 或独立 Playwright 静默替代明确要求的系统 Chrome 任务。

### 2. 动态加载当前浏览器客户端

系统 Chrome 插件可能升级。公开脚本不能硬编码缓存版本号，也不应保存易过期的数字浏览器 ID。

```js
const fs = await import("node:fs/promises");
const path = await import("node:path");
const { pathToFileURL } = await import("node:url");

const cacheRoot = path.join(
  nodeRepl.homeDir,
  ".codex",
  "plugins",
  "cache",
  "openai-bundled",
  "chrome",
);
const versions = (await fs.readdir(cacheRoot, { withFileTypes: true }))
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name)
  .sort((a, b) => b.localeCompare(a, undefined, { numeric: true }));

const clientPath = path.join(
  cacheRoot,
  versions[0],
  "scripts",
  "browser-client.mjs",
);
const { setupBrowserRuntime } = await import(pathToFileURL(clientPath).href);
const agent = await setupBrowserRuntime({ environment: "codex-app" });
const chrome = await agent.browsers.get("chrome");
```

首次操作前必须读取当前运行时返回的 browser documentation，并以实时文档为准，而不是复制旧版本 API。

如果 `agent.browsers.get("chrome")` 失败：

1. 短暂等待；
2. 只尝试一次 `agent.browsers.get("extension")`；
3. 仍然失败时，记录 `chrome_channel_unavailable` 并停止；
4. 未经用户明确同意，不得切换浏览器通道。

### 3. 导航不等于授权提交或下载

打开页面、滚动、读取标题和检查公开链接属于导航与观察。以下动作需要任务本身已经明确授权：

- 点击上传；
- 登录或提交表单；
- 点击会改变账户状态的按钮；
- 向外部发送数据；
- 下载并保存可能包含个人信息的内容。

法律法规的公开下载通常在“获取公开原文”的任务范围内，但仍应验证目标站点、文件名和最终 URL。

## 四、检索任务契约

打开浏览器前，先把一个模糊目标改写成检索契约：

```json
{
  "run_id": "RUN-<TYPE>-<NNN>",
  "legal_question": "<LEGAL_QUESTION>",
  "target_instrument": "<OFFICIAL_TITLE_OR_UNKNOWN>",
  "issuing_authority": "<AUTHORITY_OR_UNKNOWN>",
  "start_url": "<OFFICIAL_SITE_OR_SEARCH_ENTRY>",
  "query": "<SEARCH_TERMS>",
  "requested_fields": [
    "title",
    "issuer",
    "document_number",
    "publication_date",
    "effective_date",
    "version",
    "official_download_or_full_text"
  ],
  "maximum_pages": 3,
  "expected_result": "complete_official_text",
  "write_actions": "none"
}
```

其中 `maximum_pages` 用来防止无限翻页。法律法规通常不需要无边界遍历；如果站点有大量同名或历史版本，应记录筛选条件并分批处理。

### 1. 检索步骤

1. 从发布机关官网、国家法律法规数据库或正式公开平台开始；
2. 使用正式标题、文号、年份或修正信息缩小范围；
3. 记录起始 URL、检索词、筛选条件和翻页范围；
4. 打开候选结果，核对页面标题、发布机关、文号和版本；
5. 优先进入官方详情页，而不是长期停留在搜索结果页；
6. 保存最终 URL、页面标题和取得时间；
7. 只有完整正文或官方原件才进入下载分支。

### 2. 官方来源识别

来源判断至少要检查：

- 页面是否明确显示发布机关；
- 标题是否与待核规范完全一致；
- 是否有正式文号或通过、修正、修订信息；
- 是否能看到完整正文、附则和施行日期；
- 下载文件是否由同一官方页面提供；
- 页面是否只是政策解读、新闻稿、搜索摘要或转载。

域名可以辅助判断，但不能只凭域名。页面内容、发布机关、标题和文件元数据必须相互对应。

### 3. 查询结果契约

检索结束后，至少返回：

```json
{
  "run_id": "RUN-<TYPE>-<NNN>",
  "start_url": "<START_URL>",
  "final_url": "<FINAL_URL>",
  "page_title": "<PAGE_TITLE>",
  "captured_at": "YYYY-MM-DDTHH:MM:SS+08:00",
  "issuer_observed": "<ISSUER>",
  "candidate_rows_seen": 0,
  "pages_checked": 0,
  "selected_result": {
    "title": "<OFFICIAL_TITLE>",
    "document_number": "<DOCUMENT_NUMBER_OR_NONE>",
    "version_marker": "<VERSION_MARKER>"
  },
  "coverage_limits": [
    "<PAGINATION_OR_FILTER_LIMIT>"
  ],
  "warnings": []
}
```

缺失字段写 `null` 或明确警告，不从标题、摘要或模型记忆补值。

## 五、下载分支

### 分支 A：官方页面提供原生下载按钮

适用于官方详情页直接提供 PDF、DOCX 或其他公开文件。

操作顺序：

1. 记录详情页 URL 和页面标题；
2. 确认下载按钮对应的正式标题和版本；
3. 触发一次下载；
4. 等待浏览器显示明确的下载完成状态；
5. 在本地定位新文件；
6. 用 `file`、扩展名和内容共同判断文件类型；
7. 记录文件名、字节数、页数和 SHA-256；
8. 回到详情页确认标题、发布机关和文件一致。

不能只凭文件名判断内容。一个名为 `.pdf` 的文件可能是：

- HTML 错误页；
- 登录页；
- 验证码页；
- 被截断的响应；
- 与页面版本不一致的旧文件。

### 分支 B：官方 HTML 全文

当 PDF 是扫描件、下载不稳定，或发布机关同时提供官方 HTML 全文时，可以保留 HTML 作为来源层。

要求：

- 保存页面标题、发布机关、文号和最终 URL；
- 保存原始 HTML；
- 只从正文容器提取文本；
- 去除导航、页脚和相关推荐，但保留附则和施行信息；
- 对关键条文与 PDF 或其他官方版本抽样对照；
- 派生 Markdown 单独计算 SHA-256。

如果 HTML 只是摘要或缺少附则，不能替代完整官方文本。

### 分支 C：动态页面的公开响应

某些规则页先加载空壳，再通过公开详情响应渲染正文。可以用浏览器观察页面实际请求的公开响应，但必须满足：

- 响应由当前公开页面自身发起；
- 不读取 Cookie、Authorization、Storage 或账号数据；
- 不构造越权请求；
- 不绕过登录、验证码或访问控制；
- 保存响应 URL 模式时去除会话参数和令牌；
- 只保留正文、标题、版本、规则 ID 等完成任务所需字段；
- 记录页面路由与响应之间的对应关系。

如果当前浏览器运行时没有稳定的公开响应捕获接口，应停止该分支，改用页面可见正文、官方下载文件或用户人工保存。不要为了“抓接口”而复制浏览器会话凭据。

### 分支 D：本地 HTML 转阅读用 PDF

把官方 HTML 打印为 PDF，只生成便于阅读的派生副本，不把该 PDF 说成发布机关提供的原件。

应登记：

```text
official_source = HTML
derived_rendering = local print-to-PDF
original_hash = HTML SHA-256
derived_hash = PDF SHA-256
```

派生 PDF 不能替代官方 HTML 或官方 PDF 的来源地位。

### 分支 E：用户人工接管

出现登录、验证码、设备验证、下载确认或浏览器权限问题时：

1. AI 停止与该控件交互；
2. 说明卡在哪一步；
3. 由用户本人决定是否登录、继续或保存；
4. AI 只处理用户已经取得并明确允许处理的公开文件；
5. 不要求用户提供密码、Cookie 或令牌。

人工接管不是失败后的“绕路”，而是访问控制的正确边界。

## 六、下载后的文件验证

### 1. 先验证文件身份

```bash
file "$DOWNLOAD_FILE"
ls -l "$DOWNLOAD_FILE"
wc -c "$DOWNLOAD_FILE"
```

根据结果判断：

- 是否为真实 PDF、DOCX、HTML 或 JSON；
- 是否为零字节或明显过小；
- 是否是服务器错误页；
- 是否与预期格式不一致。

### 2. PDF 检查

```bash
pdfinfo "$DOWNLOAD_FILE"
pdftotext -f 1 -l 1 "$DOWNLOAD_FILE" -
```

记录页数、标题、生成工具（如有）和文本层抽查结果。扫描件没有可靠文本层时，不因此判定文件无效；应转用官方 DOCX、官方 HTML 或受控 OCR 分支。

### 3. DOCX 检查

```bash
file "$DOWNLOAD_FILE"
pandoc "$DOWNLOAD_FILE" -t gfm --wrap=none -o "$DERIVED_MARKDOWN"
```

随后检查标题层级、条号、表格、附则、脚注和施行日期是否完整。

### 4. 哈希与派生文本

```bash
shasum -a 256 "$DOWNLOAD_FILE"
shasum -a 256 "$DERIVED_MARKDOWN"
```

原始文件与派生文本必须分开哈希。派生文本更新后，原哈希不变，派生哈希重新计算。

### 5. 内容完整性检查

至少核对：

- 正式标题；
- 发布机关；
- 文号；
- 公布、修正和施行日期；
- 第一条和最后一条；
- 附则；
- 争议涉及的关键条文；
- 数字、期限和“条、款、项”编号；
- 是否存在缺页、截断、乱码、双栏交错或重复。

浏览器成功下载只说明文件到达磁盘；完成上述检查后，来源才进入待引用或已核验状态。

## 七、重定向、验证码和服务错误

| 现象 | 正确处理 | 禁止做法 |
| --- | --- | --- |
| 搜索页跳到另一官方详情页 | 记录起始和最终 URL，重新核对发布机关与标题 | 不记录重定向，直接沿用旧标题 |
| 跳到登录页 | 标记 `login_required`，由用户本人决定是否登录 | 读取 Cookie 或伪造会话 |
| 出现滑块或图形验证码 | 标记 `captcha_blocked` 并停止自动交互 | 自动识别、绕过或反复刷新轰炸 |
| 页面返回 502/503 | 保留失败时间、URL 和状态；寻找另一官方全文入口 | 把缓存页或非官方转载当作原件 |
| 证书警告 | 停止；检查系统时间、证书链和官方入口 | 在正常流程中使用 `curl -k` 关闭验证 |
| 下载文件实为 HTML | 检查状态码和正文，重新定位下载链接 | 仅改扩展名继续使用 |
| 下载后同名文件冲突 | 使用版本号或日期命名副本，保留原文件 | 覆盖旧版本 |
| 页面只显示摘要 | 继续寻找完整正文或标记 `incomplete_text` | 用摘要扩写成完整条文 |

历史上为排查特定站点的证书问题曾出现关闭证书验证的异常操作。公开方法不把这种做法推荐为常规路径。任何绕过证书验证取得的材料都必须视为高风险，并通过独立官方入口、可信网络或其他正式文本交叉复核后才能使用。

## 八、可审计的下载运行记录

每次重要下载至少生成一条运行记录，模板见：

[法律法规下载运行记录模板](../examples/legal-sources/download-run.template.md)

记录应区分三件事：

1. **观察事实**：页面显示了什么、最终 URL 是什么、下载到了哪个文件；
2. **机器结果**：文件类型、页数、字节数、哈希、转换输出；
3. **人工结论**：来源是否完整、版本是否匹配、能否进入引用层。

不要让模型在一条摘要里同时替代这三层记录。

### 1. 浏览器侧最小证据

- `run_id`；
- 浏览器通道；
- 预检结果；
- 起始 URL；
- 最终 URL；
- 页面标题；
- 取得时间；
- 检索词和筛选条件；
- 分页或覆盖限制；
- 公开下载按钮或完整正文的可见标识；
- 下载文件名；
- 成功、失败或需要人工接管的状态。

浏览器截图可能包含账号、历史记录、书签栏或其他个人信息，不应默认进入公开仓库。确需保存时，只保留完成任务所需的页面区域并脱敏。

### 2. 本地文件侧最小证据

- 原始文件哈希；
- 文件格式和字节数；
- PDF 页数或文本字符数；
- 派生文本哈希；
- 使用的转换工具和版本；
- 已检查的首尾条号与关键条文；
- 已知转换限制。

### 3. 状态词

建议统一使用：

- `captured`：已取得文件或公开正文；
- `captured_unverified`：已取得，但尚未完成版本和完整性核验；
- `verified`：已完成来源、版本、原文和完整性检查；
- `blocked_login`：被登录页阻断；
- `blocked_captcha`：被验证码阻断；
- `blocked_access`：被其他访问控制阻断；
- `incomplete_text`：页面或文件不完整；
- `source_conflict`：多个官方版本冲突；
- `chrome_channel_unavailable`：系统 Chrome 通道不可用。

状态只描述证据状态，不描述案件胜负或法律结论。

## 九、最小可复制流程

```text
1. 从争议问题生成待核来源队列；
2. 写明发布机关、正式标题和官方站点；
3. 运行 codex-chrome-ops 预检，只在 ready: true 后继续；
4. 连接系统 Chrome，读取实时 browser documentation；
5. 导航、检索并记录起始 URL、最终 URL、范围和限制；
6. 选择原生下载、官方 HTML 或公开响应分支；
7. 遇登录、验证码或访问控制时停止并交给用户；
8. 下载后验证文件类型、页数或字节数、首尾内容和 SHA-256；
9. 选择 PDF/DOCX/HTML/OCR 数字化分支；
10. 核对版本、条号、原文和事实适用；
11. 写下载运行记录和来源登记；
12. 人工复核后才进入正式引用层。
```

## 十、公开仓库的隐私边界

公开运行记录只使用占位符或完全虚构的标识。不得提交：

- 真实姓名、手机号、地址或身份证件；
- 案号、法院具体案件信息或程序通知；
- 订单号、支付号、账号 ID 或会话标识；
- Cookie、Authorization、令牌、浏览器 profile；
- 含个人信息的原始截图；
- 真实案件文件或私密下载链接；
- 带签名参数的临时公开接口 URL。

法律、行政法规和司法解释的正式名称可以公开；与具体纠纷有关的平台名称按本仓库规则使用 `F猪` 和 `T宝`。

---

# Retrieving and Preserving Legal Sources with System Chrome: A `codex-chrome-ops` Practice Note

Version: `0.1.0`
Status: public technical note
Consolidated: `2026-11-18`

## Conclusion First

Downloading a legal source is not merely opening a page and clicking a PDF. An auditable retrieval task must answer five questions:

1. Is the page an issuing authority or its official publication platform?
2. What final URL did the browser reach, and did the page display the complete target text?
3. Is the downloaded object a PDF, DOCX, HTML, JSON file, or an error page disguised as a document?
4. Is the file complete, and have the original and derived-text hashes been recorded?
5. Did the workflow stop at a login, CAPTCHA, redirect, certificate warning, or service error instead of bypassing it?

The project's early retrieval work combined web search, the in-app browser, HTTP retrieval, and public detail responses. The later `codex-chrome-ops` Skill turned those lessons into a system-Chrome operating contract: preflight first; connect only when ready; operate only on the specified page; verify through the final page, downloaded file, or business state; and never silently switch browser channels.

> Record the channel that actually performed the work.
> A later system-Chrome workflow does not retroactively turn an in-app browser or HTTP capture into a Chrome download.

## 1. Where the Method Came From

### Start with a source queue

The browser does not decide whether an instrument may apply. The sequence is:

```text
Disputed issue
  -> candidate legal instruments
  -> possible issuing authority
  -> official site or formal publication platform
  -> search and download
  -> source verification
```

Searching keywords first and assembling a legal argument from result cards destroys the audit trail for scope, version, and omissions.

### Search discovers; it does not finalize

Web search is suitable for finding the issuing authority, official title, document number, and possible official entry point. Search snippets, result cards, and secondary reposts are discovery aids only.

They cannot become final authority merely because their wording appears complete.

### Prefer repeatable retrieval for static sources and a browser for dynamic pages

Stable official HTML, PDF, and DOCX files can sometimes be retrieved by HTTP and verified by hash. JavaScript-rendered pages, pagination, public detail responses, native download controls, and user-authorized Chrome tasks are better handled through a browser.

The choice should depend on:

- whether the page needs JavaScript;
- whether a public download control must be clicked;
- whether the final URL and visible page state identify the source;
- whether the original file or public response can be preserved;
- whether login, CAPTCHA, cookies, or other access controls are involved.

### Separate browser operation from file processing

The browser navigates, reads public pages, triggers public downloads, and confirms the final page. Local tools then identify the file, count pages, test the text layer, hash, convert, and compare the text.

A browser message that a download completed is not proof that the file is citable. The object on disk is the verification target.

### Boundary between history and the current contract

The early retrieval stage used:

- web search to locate official sources;
- the in-app browser for page reading and DOM inspection;
- HTTP requests to preserve official HTML;
- public detail and download entry points discovered through official pages and public front-end resources;
- public responses to recover dynamically rendered rule text;
- `pdfinfo`, `pdftotext`, and `pandoc` for document processing;
- official HTML or DOCX alternatives when a PDF lacked a reliable text layer.

`codex-chrome-ops` is the later, stronger contract for system Chrome. It inherits those retrieval and failure-handling lessons. It does not mean that every early step was performed in system Chrome.

### From `02-Legal-Source-Download` to the self-developed `codex-chrome-ops`

The historical `02-Legal-Source-Download` work was not a one-tool operation. It converged through a technical chain:

```text
web search to discover candidate sources
  -> open the official page
  -> inspect DOM, dynamic loading, and public page state in the in-app browser
  -> obtain text or originals from an official page, public detail response, or download entry
  -> use HTTP retrieval for static official files when appropriate
  -> use pdfinfo, pdftotext, pandoc, and shasum for verification and digitization
```

That stage exposed recurring failure modes:

- search results, detail pages, and final download URLs are often different addresses;
- a page may begin as an empty shell and receive its body from a public response or public page state such as `window.__INITIAL_STATE__`;
- native download controls, official HTML, and HTTP retrieval fit different pages and cannot be collapsed into one undifferentiated claim of a successful download;
- a browser's download-complete message does not prove file type, page count, body completeness, or version;
- login, CAPTCHA, certificate errors, and extension failures require explicit stop rules to prevent accidental channel switching or use of the wrong material.

The user-developed `codex-chrome-ops` Skill later consolidated those one-off lessons. It is neither a replacement for the official browser plugin nor a custom Chrome extension. It is an **operating-contract layer** built on the official `control-chrome` transport:

| Component | Purpose |
| --- | --- |
| `SKILL.md` | Defines system-Chrome selection, preflight, authorization boundaries, verification, and the prohibition on silent channel changes |
| `scripts/preflight.mjs` | Checks the plugin path, Chrome installation and process, extension, native host, and browser client |
| `references/query-playbook.md` | Defines search scope, stable page signals, structured extraction, pagination, and coverage limits |
| `references/form-playbook.md` | Requires checks before forms, uploads, and external side effects, followed by result verification |
| `references/recovery.md` | Handles connection failures, stale tabs, locator failures, permissions, and ambiguous results |

The Skill turns “how I opened it once” into “how the next run can repeat the work, stop safely, and prove the result.” For legal-source retrieval, the key improvement is not merely another button action. Every run should state which channel was used, where it ended, what object was obtained, how it was verified, and what remained uncovered.

## 2. Browser-Channel Responsibilities

| Channel | Suitable work | Evidence produced | Claim it cannot support |
| --- | --- | --- | --- |
| Web search | Issue discovery and official-entry identification | Candidate official sources and query leads | Search snippets are not statutory text |
| System Chrome through `codex-chrome-ops` | Dynamic pages, public downloads, user-requested Chrome work | Page state, final URL, downloaded public file, public-response summary | Bypassing login, CAPTCHA, or access controls |
| In-app browser | Page reading, DOM inspection, and visual checks that do not require system Chrome | Page text, structure, screenshot, or public network response | Calling the operation a system-Chrome download |
| HTTP retrieval | Static official pages or public files that need no browser interaction | Original HTML, PDF, DOCX, JSON, and status codes | Bypassing certificates, authentication, or anti-bot controls |
| Local file tools | Integrity checks, digitization, and hashing after download | Page count, text layer, derived text, and hashes | Proving that the official source itself is authentic |

Channels may be combined, but the run record must state each step:

```text
system Chrome -> click public PDF download
local shell   -> file / pdfinfo / pdftotext / shasum
manual review -> title, version, first and last articles, key text
```

These are not three source authorities. They are three stages of one retrieval, preservation, and verification chain.

## 3. `codex-chrome-ops` Startup Contract

### Run preflight

For a fresh session, reconnect, plugin update, or suspected extension failure:

```bash
node "$HOME/.codex/skills/codex-chrome-ops/scripts/preflight.mjs" --json
```

Preflight checks the plugin path, supported Chrome installation, running process, extension, native host manifest, and browser client.

Continue only when the result contains `ready: true`. If it does not:

1. fix the failed prerequisite;
2. ask the user to open Chrome if it is installed but not running;
3. rerun the same preflight;
4. do not silently replace an explicit system-Chrome task with the in-app browser, Computer Use, or standalone Playwright.

### Load the current browser client dynamically

Do not hard-code a plugin cache version or a numeric browser ID. Resolve the current plugin directory, import its `browser-client.mjs`, call `setupBrowserRuntime({ environment: "codex-app" })`, and acquire `agent.browsers.get("chrome")`.

Read the live browser documentation before the first tab operation. Current runtime documentation overrides old examples.

If `get("chrome")` fails:

1. wait briefly;
2. try `get("extension")` once;
3. if that also fails, record `chrome_channel_unavailable` and stop;
4. do not switch channels without explicit user approval.

Navigation is not submission or download authorization. Uploading, logging in, changing account state, sending data, or saving potentially personal content requires a task that clearly authorized that action.

## 4. Search-Task Contract

Turn the request into a compact contract before opening the browser:

```json
{
  "run_id": "RUN-<TYPE>-<NNN>",
  "legal_question": "<LEGAL_QUESTION>",
  "target_instrument": "<OFFICIAL_TITLE_OR_UNKNOWN>",
  "issuing_authority": "<AUTHORITY_OR_UNKNOWN>",
  "start_url": "<OFFICIAL_SITE_OR_SEARCH_ENTRY>",
  "query": "<SEARCH_TERMS>",
  "maximum_pages": 3,
  "expected_result": "complete_official_text",
  "write_actions": "none"
}
```

Record the query, filters, pages checked, candidate count, selected title, and any coverage limits. Open candidate detail pages and verify the title, issuer, document number, and version. Domain names help but are not sufficient by themselves.

Search ends with a result contract containing at least:

- `run_id`;
- start and final URLs;
- page title and retrieval time;
- observed issuing authority;
- selected official title;
- document number and version marker;
- pagination or filtering limits;
- explicit warnings and missing fields.

Use `null` or an explicit warning for unknown values. Do not infer a document number, article, or version from a snippet or model memory.

## 5. Download Branches

### A. Native public download control

1. Record the detail-page URL and title.
2. Confirm that the control corresponds to the expected official title and version.
3. Trigger one download.
4. Wait for a visible completed-download state.
5. Locate the new local file.
6. Check the extension, `file` output, and content together.
7. Record filename, byte count, page count, and SHA-256.
8. Return to the detail page and confirm that title, issuer, and file match.

A `.pdf` filename can still contain an HTML error page, login page, CAPTCHA page, truncated response, or a different version.

### B. Official HTML full text

Preserve the page title, issuer, document number, final URL, and raw HTML. Extract only the main text container, retain supplementary provisions and effective-date language, compare key articles with another official version, and hash the derived Markdown separately.

An official HTML page that contains only a summary cannot replace the complete text.

### C. Public response of a dynamic page

Capture only a public response initiated by the visible page. Do not inspect cookies, authorization headers, storage, or account data; do not construct privileged requests; do not bypass login, CAPTCHA, or access controls; remove session parameters and tokens from URL patterns; retain only the title, body, version, rule ID, and other required fields.

If the current browser runtime has no stable public-response interface, stop this branch and use visible page text, an official download, or user-assisted saving. Never copy browser credentials to make an endpoint work.

### D. Local HTML-to-PDF rendering

A local print-to-PDF copy is a derived reading artifact. Record the official HTML as the source, the local PDF as a derived rendering, and hash both separately. The derived PDF does not become an authority-issued original.

### E. User takeover

At login, CAPTCHA, device verification, a download confirmation, or a browser-permission issue, the agent stops interacting with the control, states where it is blocked, and lets the user decide whether to authenticate or save. Never request passwords, cookies, or tokens.

## 6. Post-Download Verification

```bash
file "$DOWNLOAD_FILE"
ls -l "$DOWNLOAD_FILE"
wc -c "$DOWNLOAD_FILE"
pdfinfo "$DOWNLOAD_FILE"
pdftotext -f 1 -l 1 "$DOWNLOAD_FILE" -
shasum -a 256 "$DOWNLOAD_FILE"
```

For DOCX, verify the container and convert with:

```bash
file "$DOWNLOAD_FILE"
pandoc "$DOWNLOAD_FILE" -t gfm --wrap=none -o "$DERIVED_MARKDOWN"
```

Then check the formal title, issuer, document number, publication and effective dates, first and last articles, supplementary provisions, key disputed articles, figures, deadlines, and article/paragraph/item numbering. Look for missing pages, truncation, garbling, column interleaving, and duplication.

Hash the original and derived text separately. A successful browser download proves only that a file reached disk. The source enters the citation layer only after identity, completeness, version, and content checks.

## 7. Redirects, CAPTCHAs, and Service Errors

| Event | Correct handling | Prohibited shortcut |
| --- | --- | --- |
| Redirect to another official detail page | Record both URLs and recheck issuer and title | Carrying over the old title without review |
| Login page | Mark `login_required` and let the user decide | Reading cookies or forging a session |
| CAPTCHA | Mark `captcha_blocked` and stop | Automated bypass or request flooding |
| 502/503 | Preserve time, URL, and status; find another official full-text entry | Treating a cache or unofficial repost as the original |
| Certificate warning | Stop and check system time, certificate chain, and official entry | Using `curl -k` as a normal workflow |
| Downloaded HTML masquerading as a document | Inspect status and body; relocate the official link | Renaming the extension and continuing |
| Filename collision | Use a dated or versioned copy | Overwriting the previous original |
| Summary-only page | Find the full text or mark `incomplete_text` | Expanding a summary into “statutory text” |

A historical certificate workaround used during site diagnosis is not a recommended public workflow. Any material obtained while verification was disabled is high risk and requires independent comparison through a trusted official entry.

## 8. Auditable Download Run Record

Use [the legal-source download run template](../examples/legal-sources/download-run.template.md).

Keep three layers distinct:

1. **Observed facts**: visible page, final URL, and downloaded object;
2. **Machine results**: file type, byte/page count, hashes, and conversion output;
3. **Human conclusion**: completeness, version match, and permission to enter the citation layer.

Recommended status values are `captured`, `captured_unverified`, `verified`, `blocked_login`, `blocked_captcha`, `blocked_access`, `incomplete_text`, `source_conflict`, and `chrome_channel_unavailable`.

Do not commit browser screenshots by default. They may expose accounts, history, bookmarks, or other personal information. If a private capture is necessary, crop it to the relevant page area and redact it.

## 9. Minimum Reproducible Workflow

```text
1. Build a source queue from the disputed issues.
2. State the issuer, official title, and official site.
3. Run codex-chrome-ops preflight and continue only on ready: true.
4. Connect to system Chrome and read the live browser documentation.
5. Search and record start URL, final URL, scope, and limits.
6. Choose a native download, official HTML, or public-response branch.
7. Stop at login, CAPTCHA, or access-control boundaries.
8. Verify file type, page/byte count, first and last content, and SHA-256.
9. Use the appropriate PDF/DOCX/HTML/OCR digitization branch.
10. Verify version, article, original language, and factual application.
11. Complete the download run record and source register.
12. Enter the citation layer only after human review.
```

## 10. Public-Repository Privacy Boundary

Public run records use placeholders or entirely fictional identifiers. Never submit real names, contact details, case numbers, court-specific case information, order or payment identifiers, account IDs, cookies, authorization values, tokens, browser profiles, personal screenshots, case files, private download links, or temporary signed URLs.

Official statute, administrative-regulation, and judicial-interpretation names may remain public. Platform names tied to the underlying dispute use the repository aliases `F猪` and `T宝`.
