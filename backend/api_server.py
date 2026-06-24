from pathlib import Path


from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


from backend.prompts import build_prompt
from backend.llm_client import chat_with_llm, get_backend_info


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FRONTEND_DIR = PROJECT_ROOT / "frontend"


app = FastAPI(
    title="LLM App Playground",
    description="A basic web app for learning LLM application workflow.",
    version="0.1.0",
)


class GenerateRequest(BaseModel):
    task_type: str
    user_input: str


class GenerateResponse(BaseModel):
    task_type: str
    prompt: str
    answer: str
    backend_info: dict


app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "LLM App Playground backend is running.",
        "backend_info": get_backend_info(),
    }


@app.post("/api/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    if not request.user_input.strip():
        raise HTTPException(status_code=400, detail="user_input cannot be empty")

    prompt = build_prompt(
        task_type=request.task_type,
        user_input=request.user_input,
    )

    try:
        answer = chat_with_llm(prompt)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"模型调用失败，请检查模型服务是否启动。错误信息：{str(e)}"
        )

    return GenerateResponse(
        task_type=request.task_type,
        prompt=prompt,
        answer=answer,
        backend_info=get_backend_info(),
    )