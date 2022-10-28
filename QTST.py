# This is a Python example script for a QT slot definition function.

import time
from PyQt5 import QtGui


def toFace(self):
    global log_s
    face_err, face_name, face_id, face_score = Face()
    time.sleep(0.5)
    if face_err == 0:
        self.label_2.setText("Face ID:" + str(face_id))
        self.label_3.setText("Name:" + str(face_name))
        self.Face_pic.setPixmap(QtGui.QPixmap("setFace.jpg"))
        print("good")
        self.face_info.setText("识别成功")
        log_s = 1
    else:
        self.label_2.setText("Face ID:")
        self.label_3.setText("Name:")
        self.Face_pic.setPixmap(QtGui.QPixmap("Face.jpg"))
        print("bad")
        self.face_info.setText("识别失败")
        log_s = 0