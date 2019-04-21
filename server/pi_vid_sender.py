import cv2, numpy, base64, io, binascii
from websocket_server import WebsocketServer
from time import sleep
from PIL import Image
import api_handler


def start_sending(client, server):
    # Create a VideoSender and start sending video
    vid = cv2.VideoCapture(0)

    if not vid.isOpened():
        print("Could not open video feed.")
        exit(-1)

    print("Connected.")

    print("Sending Data Now")

    # Keep sending forever until connection terminated
    while True:

        ret, frame = vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to bytes
            pil_im = Image.fromarray(frame)
            b = io.BytesIO()

            # convert to jpeg encoding
            pil_im.save(b, 'jpeg')
            im_bytes = b.getvalue()

            # Send the frame
            server.send_message(client, binascii.b2a_base64(im_bytes))


        else:
            continue


def create_server():
    PORT = 8080
    server = WebsocketServer(PORT)
    server.set_fn_new_client(start_sending)
    server.run_forever()


if __name__ == "__main__":
    create_server()