####################################################
# Modificat de Iascerinschi Ion                    #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 pentru procesarea imgaginilor
# Import os pentru calea spre fisiere
import cv2, os

# Import numpy pentru calcularea matricilor
import numpy as np

# Import Python Image Library (PIL) clar pentru ce
from PIL import Image

# Cream Patternuri(Histograme) Locale Pentru Recunoasterea Fetei
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Folosim Algoritmi De Recunoastere a Fetei folosind biblioteca
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Cream metoda pentru preluarea imaginilor si datelor
def getImagesAndLabels(path):

    # Caile spre toate folderele/fisierele
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    # Initializam un prototip a fetei fara informatii
    faceSamples=[]

    # Initializam id gol
    ids = []

    # Iteram toate caile
    for imagePath in imagePaths:

        # Primim imaginiea si o convertim in albnegru
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image => numpy array
        img_numpy = np.array(PIL_img,'uint8')

        # Primim ID-ul imaginei
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        # Primim fata din modelele antrenate anterior
        faces = detector.detectMultiScale(img_numpy)

        # Iteram fiecare fata, adaugam ID-ul respectiv
        for (x,y,w,h) in faces:

            # Adaugam imaginea din date
            faceSamples.append(img_numpy[y:y+h,x:x+w])

            # Adaugam ID-ul la lista de ID-uri
            ids.append(id)

    # Returnam fata si array-ul de ID-uri
    return faceSamples,ids

# Get fete si ID-uri
faces,ids = getImagesAndLabels('dataset')

# Antrenam modelul folosind fete si ID-urile
recognizer.train(faces, np.array(ids))

# Salvam modelul in trainer.yml
recognizer.write('trainer/trainer.yml')
