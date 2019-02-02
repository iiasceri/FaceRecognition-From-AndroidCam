####################################################
# Modificat de Iascerinschi Ion                    #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Pentru folosirea parametrului (ip)
import sys

# Import OpenCV2 pentru image processing
import cv2

# Import numpy for calcularea matricilor
import numpy as np

# Import ssl for erori ssl
from ssl import SSLContext,PROTOCOL_TLSv1

# Import urlopen pentru a deschide url catre ip webcam
from urllib.request import urlopen

# Cream paternuri locale pentru recunoasterea fetei
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Incarca modelul antrenat
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Cream clasificator pentru modelul preconstruit
faceCascade = cv2.CascadeClassifier(cascadePath);

# Setam stilul la text
font = cv2.FONT_HERSHEY_SIMPLEX

# Aici primim parametrul din linia de comanda pentru IP webcam server (Pe telefon).
# Telefonul si calculatorul trebuie sa fie conectat la aceiasi retea (LAN sau WiFi).
url = 'https://'+ sys.argv[1] +':8080/shot.jpg'

# Iteratie
while True:
    # Citeste video cadru din url
    gcontext = SSLContext(PROTOCOL_TLSv1)  # Only for gangstars
    info = urlopen(url, context=gcontext).read()


    imgNp=np.array(bytearray(info),dtype=np.uint8)
    im=cv2.imdecode(imgNp,-1)

    # Convertim imaginea citita in albnegru
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Primeste toate fetele din stream-ul video(din imagini)
    faces = faceCascade.detectMultiScale(gray, 1.3,5)

    # Iteram pentru fiecare fata
    for(x,y,w,h) in faces:

        # Cream patrat in jurul fetei
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Vedem fata la ce ID apartine
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])

        # Verificam daca Id-ul exista
        if(Id == 1):
            Id = "Nicu"
        # # Scoate acest comentariu daca ai mai multi oameni, si schimbal cu ID din 'datasets'
        # elif(Id == 2):
        #     Id = "Vasea" # # Numele urmatoarei persoane
        # #Daca nu exista atunci e Unknown
        # else:
        #     Id = "Unknown"

        # Pune textul cu descriere cine e in imagine
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Deja punem patratul cu text peste fata in frame
    cv2.imshow('im',im)

    # Daca a fost tastat 'q' iesim din program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
