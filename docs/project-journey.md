# 一场真实纠纷如何变成一个可核验的 AI 工作流

> 本文是公开版项目历程。具体当事人、平台、商家、法院、日期、金额、案号、证据编号和文书内容均已删除或泛化。它记录方法，不复述可用于识别真实案件的材料。

## 一、缘起：问题不是“不会写一段话”

事情始于一项时间敏感的服务。

付款前，服务方确认可以履约。临近履行时，对方却表示无法按原安排继续，并提出替代方案。替代方案被拒绝后，事情没有回到原约定，也没有因为退款建议而结束。相反，真正复杂的问题开始出现：

- 原约定究竟包含哪些内容？
- 谁作出了承诺，谁应当承担责任？
- 当事人拒绝了什么，又明确要求了什么？
- 平台何时知道服务没有按约发生？
- 平台只是提供信息，还是对交易和资金采取了具体动作？
- 哪些材料能证明事实，哪些只能证明某人在某个时间说过一句话？
- 哪些是情绪上完全真实、却不能直接当作法律事实的表达？

项目一开始把这些问题压缩成“写一份起诉状”。后来发现，起诉状只是把已经完成的证据整理、关系判断和来源核验表达出来。前面的工作没有完成，文书越流畅，风险反而越大。

## 二、第一课：先把材料固定下来

第一项稳定下来的不是观点，而是材料边界。

- 原始材料只读保存，不因命名、裁剪、转写或 OCR 而覆盖；
- 每份材料记录来源、时间、载体、证明目的和哈希；
- 长录音转成文字，但与原始录音分开保存；
- 聊天截图、平台页面和正式通知分别登记，不混成“一个故事”；
- 公开版本如果需要使用材料，必须重新制作脱敏副本。

这一步没有戏剧性，却改变了后续所有工作的质量。因为从这一刻开始，“我记得”“对方说过”和“证据能够支持到什么程度”不再是同一个问题。

## 三、第二课：AI 最早的价值不是生成，而是整理

AI 第一次真正节省时间，不是在几秒钟内写出一份文书，而是把杂乱材料变成可以搜索和核对的中间层：

1. 把录音和聊天记录转成文本；
2. 按日期、主体和行为拆成事件；
3. 把客观事件、个人感受、对方陈述和本方主张分开；
4. 为每项事实寻找证据；
5. 找出“有说法但没有材料”的空白；
6. 标出“有材料但没有进入请求或论证”的遗漏。

这一步之后，AI 的输出仍然不是事实。它只是把需要人来判断的地方变得更清楚。

## 四、第三课：第一次诉讼路径没有通过审查

初期起诉思路没有顺利通过立案审查。

当时最容易产生的误解是：“一定是文书写得不够好。”但实际暴露的问题更基础：

- 所主张的法律关系是否单一、清楚；
- 被告主体是否与所主张的责任基础一致；
- 合同关系、平台关系和侵权评价是否被混在一起；
- 证据结构是否支持所写的请求；
- 金额、利息、责任方式和材料分类是否能够逐项解释。

这次挫折后来被视为项目中最有价值的错误之一。它证明了一件事：

> AI 可以把一个未经澄清的思路写得非常完整，但完整不等于正确。

随后，争议被重新拆解：先确定以哪一类法律关系为核心，再确定责任主体、请求内容、证据组和官方法律来源。起诉状经历多个版本，每个版本都保留修改原因、来源核对和待人工确认事项。

## 五、第四课：法条不是“生成出来”的，而是“核验出来”的

法律文本对准确性的要求很高。标题、条号、版本、生效日期、适用范围和官方来源缺一不可。

在这个项目中，形成了以下规则：

- 优先使用发布机关、法院、政府部门或平台官方的原文；
- 记录文号、公布日期、生效日期、访问时间和原文哈希；
- 不用搜索摘要、模型记忆或二次转载替代原文；
- 区分“法律要求”“本方主张”和“可能的裁判观点”；
- 无法确认时，宁可删除结论，也不让模型自行补全；
- 案例必须能够定位全文，并核对层级、地域和后续历史。

“没有来源就不引用”不是形式主义。它防止的是把一个听起来合理的句子，变成后面所有文书和口头表达的错误基础。

## 六、第五课：程序状态会变化，旧截图会过期

案件从材料准备进入补正、调解和诉讼后，状态开始不断变化：

- 举证期限变化；
- 质证阶段出现；
- 程序类型发生变化；
- 新费用通知出现；
- 法院短信可能比平台页面更新；
- 平台页面可能比正式文书滞后；
- 已缴款、银行扣款和法院系统入账不是同一个状态。

因此，工作流不再问“现在是什么状态”，而会继续追问：

1. 这条状态来自哪里？
2. 它是什么时候显示的？
3. 是否有更晚的正式通知？
4. 它证明的是“页面显示”“本人付款”“法院收到”还是“法院已经完成实体判断”？
5. 如果状态冲突，哪一个来源具有更高层级和更新时间？

这使项目从“生成答案”转向“维护状态”。对一个真实案件来说，后者往往更重要。

## 七、第六课：人工批准不能省略

AI 可以整理、提醒、比较和起草，但不能替当事人承担法律后果。

项目将动作分成两类：

### 可以由 AI 辅助的动作

- 提取材料；
- 建立索引；
- 归纳时间线；
- 发现矛盾；
- 检索官方来源；
- 生成待审草稿；
- 制作核对清单；
- 记录版本差异。

### 必须由本人确认或执行的动作

- 确认事实和金额；
- 决定诉讼请求；
- 决定是否接受调解；
- 签署文书；
- 缴纳费用；
- 向法院提交材料；
- 处分程序权利；
- 对外公开发布；
- 对任何期限作出最终判断。

有效批准不是一句笼统的“可以”。它必须对应具体版本、具体用途和具体动作。只要其中一项改变，批准就可能失效。

## 八、项目工作流

```text
原始材料
  -> 原件固定与哈希
  -> 证据台账
  -> 时间线
  -> 事实、感受、主张分离
  -> 争议问题
  -> 官方法律来源
  -> 来源核验
  -> 事实与规则映射
  -> 待审文书
  -> 本人逐项批准
  -> 本人执行外部动作
  -> 审计记录
```

关键不是流程图画得完整，而是每一步都能回答三个问题：

- 输入是什么？
- 输出了什么？
- 如果无法继续，为什么停止？

## 九、这个项目拒绝怎样宣传

项目仍在法院程序中，因此公开表达必须保持克制：

- 不写“AI 帮我赢了”；
- 不把立案、缴费、接收证据或进入下一程序写成胜诉；
- 不公开真实案号、法院文书、完整时间线和证据细节；
- 不把未经裁判确认的行为定性为诈骗或其他严重违法；
- 不用“斗巨龙”的叙事替代对责任、证据和程序的证明；
- 不把 AI 的流畅表达当作法律能力。

“AI 协助斗巨龙”可以是一句有传播力的社交媒体引子，但不适合作为正式项目标题。法律争议不是童话。对方是谁、责任是什么、证据能证明什么，都需要被具体说明。

## 十、目前沉淀了什么

这次经历最终沉淀为四类资产：

1. **协议**：规定 AI 何时可以工作、何时必须停止；
2. **数据结构**：让证据、事实、来源和批准可以逐项关联；
3. **工具**：优先实现公开安全检查等可验证能力；
4. **叙事**：公开真实的方法和错误，不公开真实案件材料。

这不是一个“自动打官司”的产品。它更像一套个人诉讼操作系统的最小骨架：

> 让事实有出处，让来源有版本，让草稿有审计，让动作有负责人。

## 十一、下一步

项目后续将优先补充：

- 证据台账验证器；
- 官方法律来源登记器；
- 引用与原文一致性检查；
- 文书版本差异比较；
- 人工批准记录；
- 完全虚构的端到端案例；
- 更清晰的中英双语方法文档。

真实的案件继续在私密工作区中处理。公开仓库只负责把可以复用的方法做成可检查、可讨论、可改进的公共基础设施。

---

# How a Real Dispute Became a Verifiable AI Workflow

> This is the public version of the project journey. Specific parties, platforms, merchants, courts, dates, amounts, case numbers, evidence numbers, and document contents have been removed or generalized. It records the method, not material that could identify the underlying case.

## 1. Origin: The Problem Was Not "Writing a Paragraph"

The story began with a time-sensitive service.

Before payment, the provider confirmed that it could perform. Close to performance, the provider said it could no longer follow the original arrangement and proposed a substitute. The substitute was rejected, but the matter did not return to the original agreement, nor did a refund suggestion end it. More difficult questions emerged:

- What exactly did the original arrangement include?
- Who made the promise, and who should bear responsibility?
- What did the user reject, and what did the user explicitly require?
- When did the platform learn that the service had not been performed as agreed?
- Was the platform merely an information channel, or did it take specific actions concerning the transaction and funds?
- Which materials proved an event, and which merely proved that someone said something at a particular time?
- Which statements were emotionally genuine but could not be treated directly as legal facts?

The project initially reduced these questions to "draft a complaint." It later became clear that a complaint only expresses work that should already have been completed: evidence organization, legal-relationship analysis, and source verification. If that earlier work is incomplete, smoother drafting can increase the risk.

## 2. Lesson One: Preserve the Materials First

The first stable object was not an argument, but a boundary around the materials.

- Originals were preserved read-only and never overwritten by renaming, cropping, transcription, or OCR;
- Each item recorded its source, time, medium, evidentiary purpose, and hash;
- Long recordings were transcribed into separate files rather than replacing the originals;
- Chat screenshots, platform pages, and formal notices were indexed separately instead of being merged into "one story";
- Any public-facing use required a newly created, redacted copy.

This step was not dramatic, but it changed the quality of everything that followed. From that point onward, "I remember," "the other side said," and "what the evidence can support" were no longer treated as the same question.

## 3. Lesson Two: AI's First Value Was Organization, Not Generation

The first real time saving did not come from producing a legal document in seconds. It came from turning scattered materials into an intermediate layer that could be searched and checked:

1. Convert recordings and chats into text;
2. Break events down by date, actor, and action;
3. Separate objective events, personal feelings, statements by others, and legal arguments;
4. Associate each factual statement with evidence;
5. Identify gaps where a claim existed but supporting material did not;
6. Identify omissions where evidence existed but had not entered a request or argument.

Even after this step, AI output was not fact. It simply made the points requiring human judgment more visible.

## 4. Lesson Three: The First Litigation Path Did Not Pass Review

The initial filing theory did not pass case-intake review smoothly.

The easiest assumption at the time would have been: "the document simply was not written well enough." The actual problems were more fundamental:

- Whether the asserted legal relationship was clear and coherent;
- Whether the named defendant matched the asserted basis of responsibility;
- Whether contractual, platform, and tort characterizations had been mixed together;
- Whether the evidence structure supported the requested relief;
- Whether the amount, interest, form of liability, and material classification could each be explained.

That setback later became one of the project's most valuable errors. It demonstrated a simple point:

> AI can make an unclarified theory look complete, but completeness is not correctness.

The dispute was then rebuilt: first identify the core legal relationship, then determine the responsible party, requested relief, evidence groups, and official legal sources. The complaint went through multiple versions. Each version retained its reasons for change, source checks, and items requiring human confirmation.

## 5. Lesson Four: Legal Provisions Are Verified, Not Generated

Legal text demands precision. A title, article number, version, effective date, scope, and official source are all necessary.

The project adopted these rules:

- Prefer official texts published by legislatures, courts, government departments, or platform operators;
- Record the document number, publication date, effective date, access time, and source hash;
- Never replace the original text with a search snippet, model memory, or reproduced summary;
- Distinguish legal requirements, party arguments, and possible judicial interpretations;
- If a proposition cannot be verified, remove it rather than allowing the model to fill the gap;
- For cases, locate the full text and verify jurisdiction, court level, and subsequent history.

"No source, no citation" is not formalism. It prevents a plausible-sounding sentence from becoming the erroneous foundation of later documents and oral statements.

## 6. Lesson Five: Procedural Status Changes, and Old Screenshots Expire

After the matter moved from preparation into correction, mediation, and litigation, the status kept changing:

- Evidence deadlines changed;
- A cross-examination stage appeared;
- The type of procedure changed;
- New fee notices appeared;
- Court messages could be newer than a portal page;
- A portal page could lag behind a formal document;
- Payment by the user, a bank debit, and court-system reconciliation were not the same status.

The workflow therefore stopped asking only "what is the status now?" and began asking:

1. Where did this status come from?
2. When was it displayed?
3. Is there a later formal notice?
4. Does it prove that a page displayed something, that the user paid, that the court received materials, or that the court made a substantive determination?
5. If sources conflict, which source has the higher authority and more recent update?

This shifted the project from "generating answers" to "maintaining state." In a real case, state maintenance is often more important.

## 7. Lesson Six: Human Approval Cannot Be Skipped

AI can organize, remind, compare, and draft, but it cannot bear the legal consequences of a person's decisions.

The project divides actions into two groups.

### Actions AI May Support

- Extract materials;
- Build an index;
- Summarize a timeline;
- Identify contradictions;
- Search official sources;
- Generate review drafts;
- Produce checklists;
- Record version differences.

### Actions Requiring Human Confirmation or Execution

- Confirm facts and amounts;
- Decide the requested relief;
- Decide whether to accept mediation;
- Sign documents;
- Pay fees;
- File materials with a court;
- Exercise or waive procedural rights;
- Publish to the public;
- Make final decisions about any deadline.

Valid approval is not a vague "okay." It must correspond to a specific version, a specific use, and a specific action. If any of those changes, the approval may no longer apply.

## 8. The Project Workflow

```text
Original materials
  -> Preserve originals and calculate hashes
  -> Evidence index
  -> Timeline
  -> Separate facts, feelings, and arguments
  -> Define disputed issues
  -> Locate official legal sources
  -> Verify sources
  -> Map facts to rules
  -> Create review drafts
  -> Obtain item-by-item human approval
  -> Human performs external actions
  -> Preserve audit records
```

The important part is not a complete-looking diagram. It is whether every step can answer three questions:

- What was the input?
- What was the output?
- If the workflow cannot continue, why did it stop?

## 9. How This Project Refuses to Market Itself

The case is still in court proceedings, so public statements must remain restrained:

- Do not say "AI won the case for me";
- Do not treat case acceptance, fee payment, receipt of evidence, or movement to another procedural stage as a favorable judgment;
- Do not publish real case numbers, court documents, complete timelines, or evidence details;
- Do not characterize conduct as fraud or another serious violation before a court has made such a finding;
- Do not replace proof of responsibility, evidence, and procedure with a "fighting a giant" narrative;
- Do not mistake fluent AI output for legal competence.

"AI helps you fight the giant" can work as a social-media hook, but it is not suitable as the formal project title. A legal dispute is not a fairy tale. The parties, duties, evidence, and procedural consequences must be stated concretely.

## 10. What the Project Has Produced

The experience has produced four kinds of assets:

1. **A protocol** defining when AI may work and when it must stop;
2. **Data structures** linking evidence, facts, sources, and approval;
3. **Tools** focused on verifiable functions such as public-safety checks;
4. **A narrative** that shares the method and errors while withholding the real case file.

This is not an "automated lawsuit" product. It is a minimal skeleton for a personal litigation operating system:

> Give every fact a source, every source a version, every draft an audit trail, and every external action a responsible human.

## 11. Next Steps

The project will prioritize:

- An evidence-index validator;
- An official-source registry;
- A citation-to-source consistency checker;
- Document-version diffing;
- Human-approval records;
- A complete synthetic end-to-end case;
- Clearer bilingual documentation of the method.

The real case remains in a private workspace. The public repository exists to turn reusable methods into inspectable, discussable, and improvable public infrastructure.
