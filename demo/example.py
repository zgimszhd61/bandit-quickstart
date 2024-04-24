from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.post("/run-command")
async def run_command(request: Request):
    data = await request.json()
    command = data.get("command")
    if command:
        os.system(command)  # 不安全的调用

# 运行应用
# uvicorn example:app --reload

