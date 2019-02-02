####################################################
# Modified by Sacha Arbonel                        #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Pentru folosirea parametrului (ip)
import sys

from urllib.request import urlopen

from ssl import SSLContext,PROTOCOL_TLSv1

# Import numpy pentru calcularea matricilor
import numpy as np

# Import OpenCV2 pentru procesarea imgaginilor
import cv2

# Detectam obiectul din video stream folosind Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Pentru fiecare persoana, id aparte
face_id = 1

# Initializam prototip de fata ca imagine
count = 0

# Aici primim parametrul din linia de comanda pentru IP webcam server (Pe telefon).
# Telefonul si calculatorul trebuie sa fie conectat la aceiasi retea (LAN sau WiFi).
url = 'https://'+ sys.argv[1] +':8080/shot.jpg'

# Iteram pana nu tastam ESC/q/Ctrl+C
while(True):

    # Citeste 1 cadru din URL
    gcontext = SSLContext(PROTOCOL_TLSv1)  # Securizam
    info = urlopen(url, context=gcontext).read()

    imgNp=np.array(bytearray(info),dtype=np.uint8)
    image_frame=cv2.imdecode(imgNp,-1)

    # Convertim imaginea in albnegru
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detectam imaginile de diferite marimi, lista de fete in patrate
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Iteram pentru fiecare fata
    for (x,y,w,h) in faces:

        # Taiem imaginea(frame) in imagini unde este doar fata
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)

        # Incrementam numarul pozei ca prototip
        count += 1

        # Salvam imaginea capturata in dataset folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        print(count)
        # Arata frame-ul video, cu patratul pus deja peste fata
        cv2.imshow('frame', image_frame)

    k = cv2.waitKey(33)
    if k==27:    # Esc key pentru Stop
        break

    # Daca numarul de imagini depaseste 30 oprim ca e destul
    elif count>30:
        break
