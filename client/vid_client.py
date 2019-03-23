import websocket, binascii
import cv2
from PIL import Image
import base64
import numpy as np
import io
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    im_bytes = binascii.a2b_base64(message)
    pil_bytes = io.BytesIO(im_bytes)
    pil_image = Image.open(pil_bytes)
    cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGBA2RGB)
    cv2.imshow('frame',cv_image)

    ws.close()
    

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("connected")
    return


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8080/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()