# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webcam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, cv2

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Declare Main Window / Size
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        #Check windows and labels
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelWebcam = QtWidgets.QLabel(self.centralwidget)
        self.labelWebcam.setGeometry(QtCore.QRect(570, 10, 211, 141))
        self.labelWebcam.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWebcam.setObjectName("labelWebcam")
        self.labelPlate = QtWidgets.QLabel(self.centralwidget)
        self.labelPlate.setGeometry(QtCore.QRect(10, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelPlate.setFont(font)
        self.labelPlate.setObjectName("labelPlate")
        self.textEdit_plate = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_plate.setGeometry(QtCore.QRect(110, 60, 201, 31))
        self.textEdit_plate.setObjectName("textEdit_plate")
        self.labelMotive = QtWidgets.QLabel(self.centralwidget)
        self.labelMotive.setGeometry(QtCore.QRect(10, 110, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelMotive.setFont(font)
        self.labelMotive.setObjectName("labelMotive")
        self.textEdit_motive = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_motive.setGeometry(QtCore.QRect(110, 110, 201, 31))
        self.textEdit_motive.setObjectName("textEdit_motive")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(470, 340, 281, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAccept = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonAccept.setMinimumSize(QtCore.QSize(70, 40))
        self.buttonAccept.setObjectName("buttonAccept")
        self.horizontalLayout.addWidget(self.buttonAccept)
        self.buttonCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonCancel.setMinimumSize(QtCore.QSize(70, 40))
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(10, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Webcam
        self.webcam = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.video_feed)
        self.timer.start(1)

    def video_feed(self):
        ok, img = self.webcam.read()
 
        if not ok:
            return

        image = QtGui.QImage(img, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QtGui.QImage.Format_RGB888)
 
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
 
        self.labelWebcam.setPixmap(pixmap)

    #Sets labels and such
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelWebcam.setText(_translate("MainWindow", "WEBCAM NO AVAILABLE"))
        self.labelPlate.setText(_translate("MainWindow", "Matrícula"))
        self.labelMotive.setText(_translate("MainWindow", "Motivo"))
        self.buttonAccept.setText(_translate("MainWindow", "Aceptar"))
        self.buttonCancel.setText(_translate("MainWindow", "Cancelar"))
        self.labelTitle.setText(_translate("MainWindow", "CIIoT Parking v0.01"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
