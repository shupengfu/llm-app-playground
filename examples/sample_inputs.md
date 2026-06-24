\# Sample Inputs for LLM App Playground



This file provides sample inputs for testing different task types in the LLM App Playground.



The current app supports four task types:



```text

summary

code\_explain

daily\_report

polish\_translate

```



\---



\## 1. Text Summarization



Task type:



```text

summary

```



Sample input:



```text

今天我学习了基础大模型应用的构建流程，包括前端页面如何收集用户输入，JavaScript 如何通过 fetch 向后端发送 POST 请求，FastAPI 如何接收和校验请求数据，以及后端如何根据任务类型构造 Prompt。随后，我又学习了如何通过 OpenAI-compatible API 调用本地 Ollama 模型，并将模型生成的结果返回给网页展示。通过这个过程，我对大模型应用从用户输入到模型输出的完整链路有了更清晰的理解。

```



Expected behavior:



```text

The model should summarize the main points in a concise and structured way.

```



\---



\## 2. Code Explanation



Task type:



```text

code\_explain

```



Sample input:



```python

async function generate() {

&#x20;   const input = userInput.value.trim();



&#x20;   if (!input) {

&#x20;       alert("请输入内容");

&#x20;       return;

&#x20;   }



&#x20;   const response = await fetch("/api/generate", {

&#x20;       method: "POST",

&#x20;       headers: {

&#x20;           "Content-Type": "application/json",

&#x20;       },

&#x20;       body: JSON.stringify({

&#x20;           task\_type: taskType.value,

&#x20;           user\_input: input,

&#x20;       }),

&#x20;   });



&#x20;   const data = await response.json();



&#x20;   promptBox.textContent = data.prompt;

&#x20;   answerBox.textContent = data.answer;

}

```



Expected behavior:



```text

The model should explain that this function reads user input, sends a POST request to the backend, receives JSON data, and displays the prompt and answer on the page.

```



\---



\## 3. Daily Report Generation



Task type:



```text

daily\_report

```



Sample input:



```text

今天完成了 LLM App Playground 项目的基础 Web App 构建。首先创建了 frontend、backend、docs 和 examples 等项目目录。然后使用 FastAPI 搭建了后端服务，实现了首页返回、健康检查接口和 /api/generate 生成接口。接着编写了前端 index.html、style.css 和 app.js，实现了任务选择、用户输入、按钮触发和结果展示。随后将 Prompt 构造逻辑拆分到 prompts.py，并通过 llm\_client.py 接入本地 Ollama 模型，实现了真实的大模型调用。最后补充了错误处理和项目文档。

```



Expected behavior:



```text

The model should organize the content into a formal daily report, including completed work, problems, solutions, and next steps.

```



\---



\## 4. Writing Polish / Translation



Task type:



```text

polish\_translate

```



Sample input:



```text

This project help me understand how build a basic LLM web application. It includes frontend page, FastAPI backend, prompt construction and model calling through OpenAI-compatible API.

```



Expected behavior:



```text

The model should polish the English text into more natural and professional English while preserving the original meaning.

```



\---



\## 5. Chinese Writing Polish



Task type:



```text

polish\_translate

```



Sample input:



```text

这个项目主要是为了让我知道大模型应用到底是怎么从网页输入到后端，再到模型回答，最后返回到网页上的。通过这个项目，我对前端、后端、Prompt 和模型调用之间的关系更清楚了。

```



Expected behavior:



```text

The model should polish the Chinese text into more formal and natural Chinese.

```



\---



\## 6. How to Use These Samples



1\. Start the FastAPI server.

2\. Open the web page.

3\. Select the corresponding task type.

4\. Copy one sample input into the input box.

5\. Click the generate button.

6\. Check the constructed prompt and model answer.



\---



\## 7. Notes



These samples are used for functional testing and demonstration.



They help verify that:



```text

Frontend input works

POST /api/generate works

Prompt construction works

LLM calling works

Frontend result display works

```



