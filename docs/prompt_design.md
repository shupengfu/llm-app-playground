# Prompt Design Notes

This document explains how prompts are designed in this LLM App Playground project.

The goal of prompt design is to convert raw user input into clear instructions that the language model can understand and follow.

In this project, prompt construction is handled by:

```text
backend/prompts.py
```

The core function is:

```python
def build_prompt(task_type: str, user_input: str) -> str:
```

It receives:

```text
task_type
user_input
```

and returns a complete prompt for the language model.

---

## 1. Why Prompt Templates Are Needed

A user usually provides raw input, for example:

```text
今天我学习了 FastAPI、fetch 请求和 Ollama 模型调用。
```

This input alone does not clearly tell the model what to do.

So the backend needs to convert it into a task-specific prompt, such as:

```text
你是一个专业的文本总结助手。

请总结下面的内容，要求：
1. 保留核心信息
2. 语言简洁清晰
3. 不要添加原文没有的信息
4. 输出分点总结

原文：
今天我学习了 FastAPI、fetch 请求和 Ollama 模型调用。
```

This makes the task clearer and helps the model produce more stable results.

---

## 2. Prompt Construction Flow

The prompt construction process is:

```text
User Input
    ↓
Task Type
    ↓
Prompt Template
    ↓
Final Prompt
    ↓
LLM
```

For example:

```text
task_type = summary
user_input = 用户输入内容
```

The backend selects the summarization prompt template and inserts the user input into it.

---

## 3. Current Task Types

This project currently supports four task types:

```text
summary
code_explain
daily_report
polish_translate
```

Each task type has a different prompt template.

---

## 4. Summary Prompt

The summary prompt is used for text summarization.

It tells the model to:

```text
1. 保留核心信息
2. 语言简洁清晰
3. 不要添加原文没有的信息
4. 输出分点总结
```

This is important because summarization should not invent new facts.

The prompt is designed to make the model focus on extracting and organizing the original information.

---

## 5. Code Explanation Prompt

The code explanation prompt is used for explaining code.

It tells the model to:

```text
1. 先说明代码整体作用
2. 再分模块解释关键代码
3. 说明关键变量和函数的作用
4. 最后总结这段代码适合用在什么场景
```

This structure is useful because code explanation should not only explain syntax, but also explain purpose, logic, and usage.

---

## 6. Daily Report Prompt

The daily report prompt is used for generating work reports.

It tells the model to organize the content into:

```text
1. 今日主要工作
2. 具体完成内容
3. 遇到的问题和解决方式
4. 下一步计划
```

This makes the output more suitable for reporting to a mentor, team leader, or manager.

---

## 7. Polish and Translation Prompt

The polish and translation prompt is used for writing improvement.

It tells the model to:

```text
1. If the input is Chinese, polish it into more natural and formal Chinese
2. If the input is English, polish it into more natural and professional English
3. Preserve the original meaning
4. Do not add unsupported facts
```

This prompt is useful for improving writing while keeping the original meaning unchanged.

---

## 8. Why Different Tasks Need Different Prompts

Different tasks require different output formats and reasoning styles.

For example:

```text
Text summarization
    ↓
Needs concise key points

Code explanation
    ↓
Needs logical structure and technical details

Daily report
    ↓
Needs formal work-report format

Writing polish
    ↓
Needs natural language improvement
```

If all tasks use the same prompt, the model output may become unstable or unclear.

Task-specific prompts make the application easier to control.

---

## 9. Why Prompt Logic Is Separated into prompts.py

Prompt construction is separated from `api_server.py`.

This makes the project structure clearer:

```text
api_server.py
    ↓
Receives requests and controls the backend workflow

prompts.py
    ↓
Builds task-specific prompts
```

This separation has several benefits:

```text
1. The backend API code stays clean
2. Prompt templates are easier to modify
3. New task types can be added more easily
4. The project structure becomes closer to real LLM applications
```

---

## 10. How to Add a New Task Type

To add a new task type, two files need to be modified.

First, add a new option in:

```text
frontend/index.html
```

For example:

```html
<option value="email_reply">邮件回复</option>
```

Second, add a new branch in:

```text
backend/prompts.py
```

For example:

```python
if task_type == "email_reply":
    return f"""
你是一个专业的邮件写作助手。

请根据下面的内容写一封礼貌、清晰、正式的邮件回复。

用户输入：
{user_input}
"""
```

After this, the frontend can send:

```json
{
  "task_type": "email_reply",
  "user_input": "用户输入内容"
}
```

and the backend will build the corresponding prompt.

---

## 11. Summary

Prompt design is a core part of LLM application development.

In this project, prompt templates convert user input into clear task instructions.

The current prompt system supports summarization, code explanation, daily report generation, and writing polish or translation.

This structure makes the application easier to understand, easier to extend, and closer to real-world LLM application design.
