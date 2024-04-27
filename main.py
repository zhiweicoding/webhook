from fastapi import FastAPI
from routers import webhook

app = FastAPI()

# 包含具体的路由器
app.include_router(webhook.router, prefix="/webHook", tags=["webHook"])

# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
