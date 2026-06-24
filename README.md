\# LLM App Playground



This project is a basic web application for learning the core workflow of building large language model applications.



The goal is not only to call an LLM, but also to understand the complete application process:



```text

User Input

&#x20;   ↓

Frontend JavaScript

&#x20;   ↓

FastAPI Backend

&#x20;   ↓

Prompt Construction

&#x20;   ↓

LLM Client

&#x20;   ↓

Ollama / vLLM / OpenAI-compatible API

&#x20;   ↓

Model Answer

&#x20;   ↓

Frontend Display

```



\---



\## 1. Project Motivation



After learning Transformer basics and LLM serving with Ollama and vLLM, this project focuses on building a simple LLM application.



Through this project, I want to understand:



\* How a user input is collected from a web page

\* How frontend JavaScript sends HTTP requests to a backend

\* How FastAPI receives and validates request data

\* How backend code constructs task-specific prompts

\* How to call an LLM through an OpenAI-compatible API

\* How to return model results to the browser

\* How to structure a basic LLM application project



\---



\## 2. Features



The current version supports four task types:



```text

Text Summarization

Code Explanation

Daily Report Generation

Writing Polish / Translation

```



The user can:



1\. Select a task type

2\. Enter text in the browser

3\. Click the generate button

4\. View the constructed prompt

5\. View the model-generated answer

6\. Check the current backend model information



\---



\## 3. Project Structure



```text

llm-app-playground/

├── backend/

│   ├── \_\_init\_\_.py

│   ├── api\_server.py

│   ├── config.py

│   ├── llm\_client.py

│   └── prompts.py

├── frontend/

│   ├── index.html

│   ├── style.css

│   └── app.js

├── docs/

│   ├── app\_flow.md

│   └── prompt\_design.md

├── examples/

├── requirements.txt

└── README.md

```



\---



\## 4. File Descriptions



| File                    | Description                                            |

| ----------------------- | ------------------------------------------------------ |

| `frontend/index.html`   | Defines the web page structure                         |

| `frontend/style.css`    | Defines the page style and layout                      |

| `frontend/app.js`       | Reads user input, sends requests, and displays results |

| `backend/api\_server.py` | Defines the FastAPI backend routes                     |

| `backend/prompts.py`    | Builds task-specific prompts                           |

| `backend/llm\_client.py` | Calls the LLM through an OpenAI-compatible API         |

| `backend/config.py`     | Reads backend configuration from environment variables |

| `docs/app\_flow.md`      | Explains the full application workflow                 |

| `docs/prompt\_design.md` | Explains prompt template design                        |



\---



\## 5. Environment



This project uses:



```text

Python 3.x

FastAPI

Uvicorn

OpenAI Python SDK

Ollama or vLLM

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\## 6. Run with Ollama



First, make sure Ollama is installed and running.



Check available models:



```bash

ollama list

```



If the model is not available, pull it:



```bash

ollama pull qwen2.5:0.5b

```



Set environment variables in PowerShell:



```powershell

$env:LLM\_BACKEND="ollama"

$env:LLM\_BASE\_URL="http://localhost:11434/v1"

$env:LLM\_API\_KEY="ollama"

$env:LLM\_MODEL="qwen2.5:0.5b"

```



Start the FastAPI server:



```powershell

python -m uvicorn backend.api\_server:app --host 127.0.0.1 --port 8000 --reload

```



Open the browser:



```text

http://127.0.0.1:8000

```



\---



\## 7. Run with vLLM



If a vLLM OpenAI-compatible server is running, set:



```powershell

$env:LLM\_BACKEND="vllm"

$env:LLM\_BASE\_URL="http://127.0.0.1:8000/v1"

$env:LLM\_API\_KEY="EMPTY"

$env:LLM\_MODEL="Qwen/Qwen2.5-7B-Instruct"

```



Then start the local FastAPI app on another port to avoid port conflict:



```powershell

python -m uvicorn backend.api\_server:app --host 127.0.0.1 --port 8001 --reload

```



Open:



```text

http://127.0.0.1:8001

```



\---



\## 8. API Endpoints



\### `GET /`



Returns the frontend web page.



\### `GET /health`



Checks whether the backend is running and returns backend model information.



Example response:



```json

{

&#x20; "status": "ok",

&#x20; "message": "LLM App Playground backend is running.",

&#x20; "backend\_info": {

&#x20;   "backend": "ollama",

&#x20;   "base\_url": "http://localhost:11434/v1",

&#x20;   "model": "qwen2.5:0.5b",

&#x20;   "timeout": 180.0

&#x20; }

}

```



\### `POST /api/generate`



Generates an answer based on task type and user input.



Example request:



```json

{

&#x20; "task\_type": "summary",

&#x20; "user\_input": "Today I learned FastAPI and LLM application workflow."

}

```



Example response:



```json

{

&#x20; "task\_type": "summary",

&#x20; "prompt": "Constructed prompt...",

&#x20; "answer": "Generated answer...",

&#x20; "backend\_info": {

&#x20;   "backend": "ollama",

&#x20;   "base\_url": "http://localhost:11434/v1",

&#x20;   "model": "qwen2.5:0.5b",

&#x20;   "timeout": 180.0

&#x20; }

}

```



\---



\## 9. Application Flow



The full request flow is:



```text

1\. User enters text in the browser

&#x20;       ↓

2\. frontend/app.js reads task\_type and user\_input

&#x20;       ↓

3\. frontend/app.js sends POST /api/generate

&#x20;       ↓

4\. backend/api\_server.py receives the request

&#x20;       ↓

5\. backend/prompts.py builds the prompt

&#x20;       ↓

6\. backend/llm\_client.py calls Ollama or vLLM

&#x20;       ↓

7\. The LLM generates an answer

&#x20;       ↓

8\. backend/api\_server.py returns prompt, answer, and backend\_info

&#x20;       ↓

9\. frontend/app.js displays the result on the web page

```



\---



\## 10. What I Learned



Through this project, I learned:



\* How to build a simple frontend page for an LLM application

\* How frontend JavaScript communicates with FastAPI through HTTP requests

\* How to design backend API endpoints

\* How to use Pydantic models for request and response validation

\* How to construct task-specific prompt templates

\* How to call LLMs through OpenAI-compatible APIs

\* How to switch between Ollama and vLLM using environment variables

\* How to structure a basic LLM application project



\---



\## 11. Future Improvements



Possible next steps:



\* Add streaming output

\* Add conversation history

\* Add more task templates

\* Add RAG document question answering

\* Add frontend loading animation

\* Add request logging

\* Add evaluation examples

\* Deploy the app to a cloud server

\* Package the app with Docker



\---



\## 12. Project Summary



This project implements a basic LLM web application workflow.



It connects a browser frontend, a FastAPI backend, prompt construction logic, and an OpenAI-compatible LLM backend.



The project helps me understand the foundation of real LLM applications such as writing assistants, code explanation tools, summarization tools, and RAG systems.



