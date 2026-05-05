# claude-api Skill 理解说明

claude-api 是 Anthropic 官方提供的 Claude CLI Skill，用于帮助开发者使用 Anthropic SDK 构建基于 Claude 大语言模型的应用程序。该 Skill 涵盖从简单的单次 API 调用（分类、摘要、提取、问答）到复杂的工作流和 Agent 架构的完整技术栈。其核心设计原则是"从简开始"——能用单次 API 调用解决的问题就不上工作流，能用工作流解决的问题就不上 Agent。Skill 文档详细说明了模型选择（默认使用 claude-opus-4-7）、SDK 初始化、流式响应、Tool Use、Prompt Caching、Structured Outputs、Thinking/Effort 配置等关键功能，并提供各语言（Python、TypeScript、Java、Go、Ruby、C#、PHP）的具体实现指南。对于需要持久化、版本化管理且由 Anthropic 托管运行环境的 Agent 场景，推荐使用 Managed Agents。本次调用中，我利用该 Skill 的 Python 文档生成了一个调用 Claude API 进行中文文本摘要的工作脚本 `claude_summarizer.py`，完整实践了"调用 Skill → 阅读文档 → 产出 artifact"的学习闭环。
