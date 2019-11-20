import socket, subprocess, picamera

camera = picamera.PiCamera()

#socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.connect(("192.168.0.11",8585))

while True:

    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect(("ec2-52-78-103-22.ap-northeast-2.compute.amazonaws.com", 8585))

    abc = socket1.recv(1024)
    abc = abc.decode()
    print("-------------------")
    print("connect to server")
    if abc == '1':
        camera.resolution = (768, 768)
        camera.capture("input.jpg")

        f = open('input.jpg', 'rb')
        l = f.read(1024)
        while(l):
            socket1.send(l)
            l = f.read(1024)

        socket1.close()
#        socket.send(b'end')


    f.close()
    print("send sucess")
