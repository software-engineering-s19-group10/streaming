import cv2, numpy, logging
from websocket_server import WebsocketServer
from time import sleep

PORT = 51342

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
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, imgencode = cv2.imencode('.jpg', frame, encode_param)
            data = numpy.array(imgencode)
            stringData = data.tostring()

            # Send the frame
            server.send_message(client, stringData)

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
