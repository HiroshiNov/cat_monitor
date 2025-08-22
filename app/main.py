import os, time, json, cv2
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape
from .config import settings
from .capture.cam_abstraction import open_capture
from .pipeline import CatPipeline
from .postproc import EventLatch, decide_event


app = FastAPI(title="cat-watch")


env = Environment(
loader=FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), "../ui")),
autoescape=select_autoescape()
)


# Camera & pipeline (lazy init)
_cap = None
_pipe: CatPipeline | None = None
_latch = EventLatch(cooldown_sec=30)


def get_cap():
    global _cap
    if _cap is None:
        _cap = open_capture(settings.CAMERA_BACKEND, settings.CAMERA_DEVICE,
        settings.FRAME_WIDTH, settings.FRAME_HEIGHT, settings.FPS)
    return _cap


def get_pipe():
    global _pipe
    if _pipe is None:
        _pipe = CatPipeline(models_dir=settings.MODELS_DIR, infer_device=settings.INFER_DEVICE)
    return _pipe


@app.get("/health")
def health():
    return {"status": "ok", "env": settings.ENV}


@app.get("/")
async def index(request: Request):
    template = env.get_template("index.html")
    return HTMLResponse(template.render(env=settings.ENV))


@app.get("/config")
async def get_config():
    d = settings.model_dump() if hasattr(settings, 'model_dump') else settings.__dict__
    return JSONResponse(d)


@app.get("/events/stream")
async def video_stream():
    cap = get_cap()
    pipe = get_pipe()


    def gen():
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            res = pipe.infer_frame(frame)
            action = decide_event(res)
            now_ts = int(time.time())
            if action and _latch.should_emit(now_ts):
                # ここでクリップ保存や通知に繋ぐ
                pass
            # 表示用（軽量に）
            ret, jpg = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + jpg.tobytes() + b"\r\n")
    return StreamingResponse(gen(), media_type='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)