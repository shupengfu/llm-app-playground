# LLM App Playground Application Flow

This document explains the basic workflow of this LLM web application.

The goal of this project is to help understand the core process of building a basic large language model application:

```text
User Input
    ↓
Frontend JavaScript
    ↓
HTTP Request
    ↓
FastAPI Backend
    ↓
Prompt Construction
    ↓
LLM Client
    ↓
Ollama / vLLM / OpenAI-compatible API
    ↓
Model Answer
    ↓
Frontend Display
```

---

## 1. Project Structure

```text
llm-app-playground/
├── backend/
│   ├── api_server.py
│   ├── config.py
│   ├── llm_client.py
│   └── prompts.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── docs/
│   └── app_flow.md
└── requirements.txt
```

---

## 2. Frontend Layer

The frontend is responsible for the user interface.

Main files:

```text
frontend/index.html
frontend/style.css
frontend/app.js
```

### `index.html`

This file defines the page structure.

It provides:

* Task type selection
* User input box
* Generate button
* Prompt display area
* Answer display area
* Backend status area

Important elements:

```html
<select id="taskType"></select>
<textarea id="userInput"></textarea>
<button id="generateBtn">生成</button>
<pre id="promptBox"></pre>
<pre id="answerBox"></pre>
```

These elements are later accessed and controlled by JavaScript.

---

### `style.css`

This file controls the page appearance.

It defines:

* Page layout
* Card style
* Button style
* Input box style
* Two-column result display

This file does not handle application logic.

---

### `app.js`

This file controls the frontend logic.

It does three important things:

1. Reads user input from the page
2. Sends a POST request to the backend
3. Displays the returned prompt and answer

Core request logic:

```javascript
const response = await fetch("/api/generate", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        task_type: taskType.value,
        user_input: input,
    }),
});
```

The frontend sends data in this format:

```json
{
  "task_type": "summary",
  "user_input": "User input text"
}
```

---

## 3. Backend Layer

The backend is responsible for receiving requests, constructing prompts, calling the LLM, and returning results.

Main files:

```text
backend/api_server.py
backend/prompts.py
backend/llm_client.py
backend/config.py
```

---

### `api_server.py`

This is the main FastAPI backend file.

It provides three main routes:

```text
GET  /
GET  /health
POST /api/generate
```

#### `GET /`

This route returns the frontend page:

```python
@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")
```

When the browser opens:

```text
http://127.0.0.1:8000
```

FastAPI returns:

```text
frontend/index.html
```

---

#### `GET /health`

This route checks whether the backend is running.

It also returns current backend model information.

Example response:

```json
{
  "status": "ok",
  "message": "LLM App Playground backend is running.",
  "backend_info": {
    "backend": "ollama",
    "base_url": "http://localhost:11434/v1",
    "model": "qwen2.5:0.5b",
    "timeout": 180.0
  }
}
```

---

#### `POST /api/generate`

This is the core generation API.

It receives:

```json
{
  "task_type": "summary",
  "user_input": "User input text"
}
```

Then it performs the following steps:

```text
Receive user input
    ↓
Validate input
    ↓
Call build_prompt()
    ↓
Call chat_with_llm()
    ↓
Return prompt, answer, and backend_info
```

---

### `prompts.py`

This file is responsible for prompt construction.

Core function:

```python
def build_prompt(task_type: str, user_input: str) -> str:
```

It receives:

```text
task_type
user_input
```

Then returns a prompt for the selected task.

For example, if `task_type == "summary"`, it builds a text summarization prompt.

If `task_type == "code_explain"`, it builds a code explanation prompt.

This separates prompt design from backend API logic.

---

### `llm_client.py`

This file is responsible for calling the language model.

Core function:

```python
def chat_with_llm(prompt: str, temperature: float = 0.7, max_tokens: int = 800) -> str:
```

It uses the OpenAI SDK with an OpenAI-compatible API endpoint.

This means the same code can call:

```text
Ollama
vLLM
SGLang
OpenAI API
Other OpenAI-compatible services
```

The model call follows this structure:

```python
response = client.chat.completions.create(
    model=LLM_MODEL,
    messages=[
        {
            "role": "system",
            "content": "你是一个严谨、清晰、实用的大模型应用助手。",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ],
    temperature=temperature,
    max_tokens=max_tokens,
)
```

---

### `config.py`

This file stores model backend configuration.

It reads environment variables:

```python
LLM_BACKEND = os.getenv("LLM_BACKEND", "ollama")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "ollama")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen2.5:0.5b")
LLM_REQUEST_TIMEOUT = float(os.getenv("LLM_REQUEST_TIMEOUT", "180"))
```

This makes it easy to switch between Ollama and vLLM without changing application logic.

Example Ollama configuration:

```powershell
$env:LLM_BACKEND="ollama"
$env:LLM_BASE_URL="http://localhost:11434/v1"
$env:LLM_API_KEY="ollama"
$env:LLM_MODEL="qwen2.5:0.5b"
```

Example vLLM configuration:

```powershell
$env:LLM_BACKEND="vllm"
$env:LLM_BASE_URL="http://127.0.0.1:8000/v1"
$env:LLM_API_KEY="EMPTY"
$env:LLM_MODEL="Qwen/Qwen2.5-7B-Instruct"
```

---

## 4. Full Request Flow

When the user clicks the generate button, the application runs the following process:

```text
1. User enters text in the browser
        ↓
2. frontend/index.html provides input elements
        ↓
3. frontend/app.js reads task_type and user_input
        ↓
4. frontend/app.js sends POST /api/generate
        ↓
5. backend/api_server.py receives the request
        ↓
6. backend/api_server.py validates user_input
        ↓
7. backend/prompts.py builds the prompt
        ↓
8. backend/llm_client.py sends the prompt to Ollama or vLLM
        ↓
9. The model generates an answer
        ↓
10. backend/api_server.py returns prompt, answer, and backend_info
        ↓
11. frontend/app.js displays prompt and answer on the page
```

---

## 5. Current Features

The current version supports four task types:

```text
summary
code_explain
daily_report
polish_translate
```

Corresponding frontend options:

```text
文本总结
代码解释
日报生成
翻译润色
```

---

## 6. Why This Structure Is Useful

This project separates the LLM application into clear layers:

```text
Frontend UI
    ↓
Backend API
    ↓
Prompt Construction
    ↓
LLM Client
    ↓
Model Backend Configuration
```

This structure makes the project easier to understand, debug, and extend.

For example:

* To change the page, modify `frontend/index.html` and `frontend/style.css`
* To change frontend behavior, modify `frontend/app.js`
* To add a new task type, modify `backend/prompts.py`
* To switch from Ollama to vLLM, modify environment variables
* To change model calling logic, modify `backend/llm_client.py`

---

## 7. Summary

This project implements a basic LLM web application workflow.

It shows how a user input is passed from the browser to the backend, converted into a prompt, sent to a language model, and displayed back on the webpage.

This workflow is the foundation of many LLM applications, including chatbots, writing assistants, document summarizers, code explanation tools, and RAG systems.
