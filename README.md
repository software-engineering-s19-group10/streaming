# Video Streaming for Smart Lock 
## How to use
The program for streaming will run continuously on the Pi
and will receive a request for the video at port 51342. To request streaming,
send the authorization key (see the docs for the server and database) only to 
port 51342 on the Pi. The Pi should start immediately sending the video to the port and IP
address that the request was received from. 

To terminate the video feed, send the string "STOP" to port 51342 on the Pi and the Pi should
stop sending video. 