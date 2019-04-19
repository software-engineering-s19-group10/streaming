import pi_vid_sender

# import cv below
from multiprocessing import Process

streamer = Process(target=pi_vid_sender.create_server, args=())
streamer.start()




