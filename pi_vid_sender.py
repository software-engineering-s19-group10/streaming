import cv2
import socket, sys
from threading import Thread

class VideoSender:

    def __init__(self, address, bind_port):
        # Start the video capture
        self.vid = cv2.VideoCapture(0)

        # Set address to send to
        self.address = address

        # using UDP for streaming
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to a port to receive termination command
        self.sock.bind(('',bind_port))

    # TODO: Compress video
    def send_video(self):

        # Keep sending forever until we receive a STOP signal
        while True:
            try:
                # Set timeout to be 0.1 seconds
                self.sock.settimeout(0.1)

                # Receive a message in 0.1 seconds
                recv_mess, addr = self.sock.recvfrom()

                # If the message is to stop, we exit
                if recv_mess == "STOP":
                    sys.exit(0)
                else:
                    # Otherwise, set timeout to None, and send the frame
                    self.sock.settimeout(None)

                    # Get the frame
                    val, frame = self.vid.read()

                    if val:
                        # Send the frame
                        self.sock.sendto(frame, self.address)
                    else:
                        continue

            except socket.timeout:
                # Set timeout to None in case of timeout meaning
                # we did not receive a termination command.
                self.sock.settimeout(None)

                # Get the frame
                val, frame = self.vid.read()

                if val:
                    # Send the frame
                    self.sock.sendto(frame, self.address)
                else:
                    continue


def start_sending(address, bind_port):
    # Create a VideoSender and start sending video
    vid_sender = VideoSender(address, bind_port)
    vid_sender.send_video()


# Program will take one command line argument which will be the auth key
if __name__=="__main__":
    # Set port to receive requests
    recv_port = 51342

    # Create list of all threads that are sending data
    thread_list = []

    # Get the auth key
    auth_key = sys.argv[1]

    # Create a socket to receive requests for video
    recv_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # Bind to port 51342
    recv_sock.bind(('', recv_port))

    # Keep receiving requests forever
    while True:
        (auth_attempt, address) = recv_sock.recvfrom()

        if auth_attempt == auth_key:
            # Create and start thread
            send_thread = Thread(target=start_sending,args=(address, recv_port))

            # Set daemon to true so we can kill all threads with termination
            send_thread.daemon = True
            send_thread.start()

            # Append to list
            thread_list.append(send_thread)
        else:
            # If we get wrong auth key, send a message back
            recv_sock.sendto("Wrong Auth Key",address)