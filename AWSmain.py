import cv2, time, subprocess, socket, os ,signal, threading
from multiprocessing import Process

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
andoird_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lockFlag = True

r1, w1 = os.pipe()  # for parent -> child writes
r2, w2 = os.pipe()  # for child -> parent writes

proc_face = subprocess.Popen(["/Users/joyeongjae/anaconda3/envs/project/bin/python", "faceDetection.py"], stdin=r1, stdout=w2)
outfile = os.fdopen(w1, 'w', buffering=1)
infile = os.fdopen(r2)

server_socket.bind(('aws 주소', 8585))
android_socket.bind(('aws 주소', 8686))
server_socket.listen(0)

def motion():
    proc_motion = subprocess.Popen(["/Users/joyeongjae/anaconda3/envs/project/bin/python", "motionDetection.py", "--input", "input.jpg"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    motionOut, motionErr = proc_motion.communicate()
    motionFlag = motionOut.decode()[-2]
    print("motion detection : " + motionFlag)


def imgprocess():
    while True:
        
        c, err = server_socket.accept()
        f = open("input.jpg", "wb")
        c.send("1".encode())
        l = c.recv(1)
        if l == b'T':
            print("high Temperture.")
            continue
        while(l):
            lockFlag = True

            f.write(l)
            l = c.recv(1024)

        f.close()
        faceFlag = '0' #0이면 정상, 1이면 비정상
        motionFlag = '0' #0이면 전상, 1이면 비정상

        motionThread = threading.Thread(target=motion)
        motionThread.start()
        print("4", file=outfile) #send start to faceDetection.py
        faceFlag = infile.readline()
        print("face detection : " + faceFlag)
        
        motionThread.join()
        if faceFlag == '1' and motionFlag == '1':
            print("베이비 이스 데인저러스")
            c, err = server_socket.accept()
            c.send("1".encode())
        
        img = cv2.imread('/Users/joyeongjae/Desktop/project/project/jo/result.jpg')
        cv2.startWindowThread()
        cv2.imshow('img', img)
        cv2.waitKey(1)

        print("-------------")
imgprocess()
