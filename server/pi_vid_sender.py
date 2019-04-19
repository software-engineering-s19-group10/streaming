import cv2, numpy, base64, io, binascii
from websocket_server import WebsocketServer
from time import sleep
from PIL import Image
import api_handler
from video_api import set_up_cap, get_frame



global vid

vid = set_up_cap()


def start_sending(client, server):

    print("Sending Data Now")
    
    # Keep sending forever until connection terminated
    while True:

        frame = get_frame(vid)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if not frame is None:
            
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


# TODO: Program will take one command line argument which will be the auth key
if __name__=="__main__":
    # api_handler.post_ip_address()
    create_server()