import cv2

def get_frame(cap):

    ret, frame = cap.read()

    if ret:
        return frame
    return None

def set_up_cap():
    # Create a VideoSender and start sending video
    vid = cv2.VideoCapture(0)

    if not vid.isOpened():
        print("Could not open video feed.")
        exit(-1)

    print("Connected.")
    return vid