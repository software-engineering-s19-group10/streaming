import cv2, numpy, logging, base64
from websocket_server import WebsocketServer
from time import sleep

PORT = 8080

# Testing purposes
def cap():
    cap = cv2.VideoCapture(0)
    print (2)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        print(3)

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)

def start_sending(client, server):
    # Create a VideoSender and start sending video
    vid = cv2.VideoCapture(0)

    i = 0
    # Keep sending forever until ???
    while True:
        # Get the frame
        # Capture frame-by-frame
        ret, frame = vid.read()

        if ret:
            # Convert to bytes
            retval, buffer = cv2.imencode('.jpg', frame)
            img_str = base64.b64encode(buffer)

            # Send the frame
            server.send_message(client, img_str.decode("utf-8"))
            print("Sending following data" + img_str.decode("utf-8"))

            # Throttling to 10 FPS
            sleep(0.1)
        else:
            continue


# TODO: Program will take one command line argument which will be the auth key
if __name__=="__main__":
    # cap()
    server = WebsocketServer(PORT)
    server.set_fn_new_client(start_sending)
    server.run_forever()
