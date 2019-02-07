# Recunoasterea fetei folosind Haar-Cascade Classifier, OpenCV, Python si aplicatia Ip Camera

## Cerinte
- Python 3.4+
- OpenCV 3.1.0
- Numpy
- Android aplicatie: "[IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en)
   Din aplicatie rulez Start Server (cel mai jos)

## Pentru a instala OpenCV 3.1 pe SO Unix si avand Pyton 3.4+
`pip install opencv-contrib-python`

## Continut
Acest proiect este divizat in 3 parti:
1. Crearea datelor/poze (creare_poze.py ip)
   [exemplu de rulare: creare_poze.py 192.168.100.100]
2. Antrenam modelul din poze (model_din_poze.py)
3. Recunoasterea fetei (rec_fata.py ip)
   [exemplu de rulare: rec_fata.py 192.168.100.100]

## Cum sa rulez ?
1. Fiti atenti sa aveti folderul 'dataset' si 'trainer' in acelasi directoriu
2. Rulati in linia de comanda creare_poze.py pentru a crea date in urma detectarilor. Pentru a adauga o persoana noua va rog schimbati ID-ul(Din cod de fiecare data, sau schimbati chiar denumirea pozelor xx_1_xx => xx_2_xx etc)
3. Create modelul antrenat din date ruland model_din_poze.py
4. Si deja pentru a folosi aplicatia rulati rec_fata.py

## Bibliografie
1. Object Detection using Haar-like features, link: http://www.cs.utexas.edu/~grauman/courses/spring2008/slides/Faces_demo.pdf
2. Face Detection using Haar Cascades, link: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
3. Haar-like Features, link: https://en.wikipedia.org/wiki/Haar-like_features
4. Object Detection using Haar-cascades Classifier, link: http://ds.cs.ut.ee/Members/artjom85/2014dss-course-media/Object%20detection%20using%20Haar-final.pdf
5. OpenCV Documentation, link: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html

## Sugestii
- Daca nu intelegi ce face aplicatia, codul este comentat rand cu rand
- Puteti da niste cautari pe google cu sintaxele folosite, sau din OpenCV Documentation.
- Sau puteti sa va adresati la mine prin e-mail: ion.iascerinschi@gmail.com

## Multumesc lui:
#### Anirban de la TheCodacus. Link: http://thecodacus.com/
#### All rights reserved to the respective owner
