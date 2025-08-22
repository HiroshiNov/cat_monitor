import cv2
from . import __init__ as _


def open_capture(backend: str, device, w: int, h: int, fps: int = 30):
    print(backend,device,w,h,fps)
    if backend == 'gstreamer':
        pipeline = (
        f"v4l2src device={device} ! video/x-raw, width={w}, height={h}, framerate={fps}/1 "
        f"! videoconvert ! appsink"
        )
        cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    else:
        cap = cv2.VideoCapture(int(device))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        cap.set(cv2.CAP_PROP_FPS, fps)
    if not cap.isOpened():
        raise RuntimeError(f'Camera open failed: backend={backend} device={device}')
    return cap