import zmq
import os

from time import sleep

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2000')
path = input("What is the path that your folder is in?:")

# for file in os.listdir(path):
#     sleep(2)
#     socket.send_string(os.path.basename(path), "has ", file)

while True:
    folderName = os.path.basename(path)
    for fileName in os.listdir(path):
        message = ("%s has %s" %(folderName, fileName))
        socket.send_string(message)
        print(message)
        sleep(2)

