imoprt cv2
import socket

vid = cv2.VideoCapture(0)

if (not vid.isOpened()):
    return

# TODO: define user and server ports and address
# TODO: Compress video

# using UDP for streaming
sock = socket.Socket(AF_INET, SOCK_DGRAM)

serv_addr = (serv_ip, serv_port)
user_addr = (user_ip, user_port)

while True:
    val, frame = vid.read()
    if val:
        sock.sendto(frame, user_addr)
        sock.sendto(frame, serv_addr)
    else:
        break
