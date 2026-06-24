const taskType = document.getElementById("taskType");
const userInput = document.getElementById("userInput");
const generateBtn = document.getElementById("generateBtn");
const promptBox = document.getElementById("promptBox");
const answerBox = document.getElementById("answerBox");
const statusText = document.getElementById("status");


async function checkHealth() {
    try {
        const response = await fetch("/health");
        const data = await response.json();

        statusText.textContent =
    `后端状态：${data.status}，${data.message}`;
    } catch (error) {
        statusText.textContent = "后端连接失败，请检查 FastAPI 服务是否启动。";
    }
}


async function generate() {
    const input = userInput.value.trim();

    if (!input) {
        alert("请输入内容");
        return;
    }

    generateBtn.disabled = true;
    generateBtn.textContent = "生成中...";

    promptBox.textContent = "正在构造 Prompt...";
    answerBox.textContent = "后端正在生成回答...";

    try {
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

        if (!response.ok) {
    	    const errorData = await response.json();
  	    throw new Error(errorData.detail || "请求失败，请检查后端服务。");
	}

        const data = await response.json();

        promptBox.textContent = data.prompt;
        answerBox.textContent = data.answer;
	statusText.textContent =
    `当前后端：${data.backend_info.backend} | 模型：${data.backend_info.model} | 地址：${data.backend_info.base_url}`;
    } catch (error) {
        promptBox.textContent = "请求失败";
        answerBox.textContent = error.message;
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = "生成";
    }
}


generateBtn.addEventListener("click", generate);

checkHealth();