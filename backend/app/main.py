from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes import router
import os

app = FastAPI(title="Automated PR Review Agent")

app.include_router(router, prefix="/api/v1")


static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(static_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
