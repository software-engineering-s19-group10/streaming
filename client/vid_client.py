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

global video_writer
print("Creating Video Writer")
video_writer = cv2.VideoWriter("stream.avi", cv2.VideoWriter_fourcc(*'MJPG'), 4, (640, 480), True)
global count
count = 0

def on_message(ws, message):
    # global video_writer
    global count

    im_bytes = binascii.a2b_base64(message)
    pil_bytes = io.BytesIO(im_bytes)
    pil_image = Image.open(pil_bytes)
    cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGBA2RGB)
    cv2.imshow('frame', cv_image)

    print("Writing Frame to Video File.")
    video_writer.write(cv_image)
    count += 1

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("Connected")
    return


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://8f02b0c0.ngrok.io",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()