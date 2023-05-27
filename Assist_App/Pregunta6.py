# IMPORTACIONES
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Pregunta7 import  Ui_Pregunta7
from Funciones_Auxiliares import  suma_vectorial

class Ui_Pregunta6(object):
    def setupUi(self, Pregunta6,lista_sustancias_escogidas,lista_puntajes_pregunta_anterior):
        self.puntajes_recibidos = lista_puntajes_pregunta_anterior
        Pregunta6.setObjectName("Pregunta6")
        Pregunta6.resize(1924, 1089)
        self.BannerLabel = QtWidgets.QLabel(Pregunta6)
        self.BannerLabel.setGeometry(QtCore.QRect(10, 10, 1901, 131))
        pixmap = QtGui.QPixmap("imagenes/Banner.png")
        self.BannerLabel.setPixmap(pixmap)
        self.BannerLabel.setObjectName("BannerLabel")
        self.LabelInstruccion = QtWidgets.QLabel(Pregunta6)
        self.LabelInstruccion.setGeometry(QtCore.QRect(100, 156, 1831, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LabelInstruccion.setFont(font)
        self.LabelInstruccion.setObjectName("LabelInstruccion")
        self.LabelInstruccion.setText(
            "6. ¿Un amigo, un familiar o alguien más, alguna vez ha mostrado preocupación por su consumo de las siguientes sustancias?")
        self.progressBar = QtWidgets.QProgressBar(Pregunta6)
        self.progressBar.setGeometry(QtCore.QRect(40, 1000, 1841, 23))
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"  background-color: #FA9300;\n"
"}\n"
"QProgressBar {\n"
"  border: 2px solid black;\n"
"  border-radius: 20px;\n"
"}")
        self.progressBar.setProperty("value", 72)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Pregunta6)
        self.pushButton.setGeometry(QtCore.QRect(1580, 932, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"  border: 3px solid black;\n"
"  border-radius: 20px;\n"
"  background-color: #FA9300;\n"
"  color: white;\n"
"  font-weight: bold;\n"
"  padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #FFB347;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.abrir_pregunta7)

        self.canitdad_sustancias = len(lista_sustancias_escogidas)
        self.Lista_sustancias = lista_sustancias_escogidas

        if self.canitdad_sustancias == 1:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame.setGeometry(QtCore.QRect(410, 460, 1081, 101))
            self.SustanciaFrame.setStyleSheet("QFrame {\n"
    "  border: 3px solid black;\n"
    "  border-radius: 20px;\n"
    "}\n"
    "\n"
    "QFrame > QLabel {\n"
    "\n"
    "}")
            self.SustanciaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame.setObjectName("SustanciaFrame")
            self.LabelSustancia = QtWidgets.QLabel(self.SustanciaFrame)
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia.setFont(font)
            self.LabelSustancia.setStyleSheet("QFrame > QLabel {\n"
    "  border: none;\n"
    "  border-radius: 0; \n"
    "}")
            self.LabelSustancia.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia.setObjectName("LabelSustancia")
            self.SeleccionNoNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNoNunca.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca.setFont(font)
            self.SeleccionNoNunca.setObjectName("SeleccionNoNunca")
            self.SeleccionSiEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiEnLosUltimos3Meses.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses.setObjectName("SeleccionSiEnLosUltimos3Meses")
            self.SeleccionSiPeroNoEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses")


            QtCore.QMetaObject.connectSlotsByName(Pregunta6)


            _translate = QtCore.QCoreApplication.translate
            Pregunta6.setWindowTitle(_translate("Pregunta6", "Pregunta6"))
            self.pushButton.setText(_translate("Pregunta6", "SIGUIENTE PREGUNTA"))
            self.LabelSustancia.setText(_translate("Pregunta6", "Cannabis"))
            self.SeleccionNoNunca.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

        if self.canitdad_sustancias == 2:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame.setGeometry(QtCore.QRect(410, 420, 1081, 101))
            self.SustanciaFrame.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame.setObjectName("SustanciaFrame")

            self.LabelSustancia = QtWidgets.QLabel(self.SustanciaFrame)
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia.setFont(font)
            self.LabelSustancia.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia.setObjectName("LabelSustancia")

            self.SeleccionNoNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNoNunca.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca.setFont(font)
            self.SeleccionNoNunca.setObjectName("SeleccionNoNunca")
            self.SeleccionSiEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiEnLosUltimos3Meses.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses.setObjectName("SeleccionSiEnLosUltimos3Meses")
            self.SeleccionSiPeroNoEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses")

            self.SustanciaFrame2 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame2.setGeometry(QtCore.QRect(410, 530, 1081, 101))
            self.SustanciaFrame2.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame2.setObjectName("SustanciaFrame2")
            self.LabelSustancia2 = QtWidgets.QLabel(self.SustanciaFrame2)
            self.LabelSustancia2.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia2.setFont(font)
            self.LabelSustancia2.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia2.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia2.setObjectName("LabelSustancia2")
            self.SeleccionNoNunca2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionNoNunca2.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca2.setFont(font)
            self.SeleccionNoNunca2.setObjectName("SeleccionNoNunca2")
            self.SeleccionSiEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiEnLosUltimos3Meses2.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses2.setObjectName("SeleccionSiEnLosUltimos3Meses2")
            self.SeleccionSiPeroNoEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses2")

            QtCore.QMetaObject.connectSlotsByName(Pregunta6)

            _translate = QtCore.QCoreApplication.translate
            Pregunta6.setWindowTitle(_translate("Pregunta6", "Pregunta6"))
            self.pushButton.setText(_translate("Pregunta6", "SIGUIENTE PREGUNTA"))
            self.LabelSustancia.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNoNunca.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setText(
                _translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            _translate = QtCore.QCoreApplication.translate
            Pregunta6.setWindowTitle(_translate("Pregunta6", "Pregunta6"))
            self.pushButton.setText(_translate("Pregunta6", "SIGUIENTE PREGUNTA"))
            self.LabelSustancia2.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNoNunca2.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setText(
                _translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

        if self.canitdad_sustancias == 3:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame.setGeometry(QtCore.QRect(410, 330, 1081, 101))
            self.SustanciaFrame.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame.setObjectName("SustanciaFrame")

            self.LabelSustancia = QtWidgets.QLabel(self.SustanciaFrame)
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia.setFont(font)
            self.LabelSustancia.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia.setObjectName("LabelSustancia")

            self.SeleccionNoNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNoNunca.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca.setFont(font)
            self.SeleccionNoNunca.setObjectName("SeleccionNoNunca")
            self.SeleccionSiEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiEnLosUltimos3Meses.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses.setObjectName("SeleccionSiEnLosUltimos3Meses")
            self.SeleccionSiPeroNoEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses")

            self.SustanciaFrame2 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame2.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.SustanciaFrame2.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame2.setObjectName("SustanciaFrame2")
            self.LabelSustancia2 = QtWidgets.QLabel(self.SustanciaFrame2)
            self.LabelSustancia2.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia2.setFont(font)
            self.LabelSustancia2.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia2.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia2.setObjectName("LabelSustancia2")
            self.SeleccionNoNunca2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionNoNunca2.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca2.setFont(font)
            self.SeleccionNoNunca2.setObjectName("SeleccionNoNunca2")
            self.SeleccionSiEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiEnLosUltimos3Meses2.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses2.setObjectName("SeleccionSiEnLosUltimos3Meses2")
            self.SeleccionSiPeroNoEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses2")

            self.SustanciaFrame3 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame3.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.SustanciaFrame3.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame3.setObjectName("SustanciaFrame3")
            self.LabelSustancia3 = QtWidgets.QLabel(self.SustanciaFrame3)
            self.LabelSustancia3.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia3.setFont(font)
            self.LabelSustancia3.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia3.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia3.setObjectName("LabelSustancia3")
            self.SeleccionNoNunca3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionNoNunca3.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca3.setFont(font)
            self.SeleccionNoNunca3.setObjectName("SeleccionNoNunca3")
            self.SeleccionSiEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiEnLosUltimos3Meses3.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses3.setObjectName("SeleccionSiEnLosUltimos3Meses3")
            self.SeleccionSiPeroNoEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses3")

            QtCore.QMetaObject.connectSlotsByName(Pregunta6)

            _translate = QtCore.QCoreApplication.translate
            Pregunta6.setWindowTitle(_translate("Pregunta6", "Pregunta6"))
            self.pushButton.setText(_translate("Pregunta6", "SIGUIENTE PREGUNTA"))
            self.LabelSustancia.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNoNunca.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setText(
                _translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia2.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNoNunca2.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia3.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNoNunca3.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

        if self.canitdad_sustancias == 4:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame.setGeometry(QtCore.QRect(410, 330, 1081, 101))
            self.SustanciaFrame.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame.setObjectName("SustanciaFrame")

            self.LabelSustancia = QtWidgets.QLabel(self.SustanciaFrame)
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia.setFont(font)
            self.LabelSustancia.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia.setObjectName("LabelSustancia")

            self.SeleccionNoNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNoNunca.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca.setFont(font)
            self.SeleccionNoNunca.setObjectName("SeleccionNoNunca")
            self.SeleccionSiEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiEnLosUltimos3Meses.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses.setObjectName("SeleccionSiEnLosUltimos3Meses")
            self.SeleccionSiPeroNoEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses")

            self.SustanciaFrame2 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame2.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.SustanciaFrame2.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame2.setObjectName("SustanciaFrame2")
            self.LabelSustancia2 = QtWidgets.QLabel(self.SustanciaFrame2)
            self.LabelSustancia2.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia2.setFont(font)
            self.LabelSustancia2.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia2.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia2.setObjectName("LabelSustancia2")
            self.SeleccionNoNunca2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionNoNunca2.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca2.setFont(font)
            self.SeleccionNoNunca2.setObjectName("SeleccionNoNunca2")
            self.SeleccionSiEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiEnLosUltimos3Meses2.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses2.setObjectName("SeleccionSiEnLosUltimos3Meses2")
            self.SeleccionSiPeroNoEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses2")

            self.SustanciaFrame3 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame3.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.SustanciaFrame3.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame3.setObjectName("SustanciaFrame3")
            self.LabelSustancia3 = QtWidgets.QLabel(self.SustanciaFrame3)
            self.LabelSustancia3.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia3.setFont(font)
            self.LabelSustancia3.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia3.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia3.setObjectName("LabelSustancia3")
            self.SeleccionNoNunca3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionNoNunca3.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca3.setFont(font)
            self.SeleccionNoNunca3.setObjectName("SeleccionNoNunca3")
            self.SeleccionSiEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiEnLosUltimos3Meses3.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses3.setObjectName("SeleccionSiEnLosUltimos3Meses3")
            self.SeleccionSiPeroNoEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses3")

            self.SustanciaFrame4 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame4.setGeometry(QtCore.QRect(410, 660, 1081, 101))
            self.SustanciaFrame4.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame4.setObjectName("SustanciaFrame4")
            self.LabelSustancia4 = QtWidgets.QLabel(self.SustanciaFrame4)
            self.LabelSustancia4.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia4.setFont(font)
            self.LabelSustancia4.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia4.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia4.setObjectName("LabelSustancia4")
            self.SeleccionNoNunca4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionNoNunca4.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca4.setFont(font)
            self.SeleccionNoNunca4.setObjectName("SeleccionNoNunca4")
            self.SeleccionSiEnLosUltimos3Meses4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionSiEnLosUltimos3Meses4.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses4.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses4.setObjectName("SeleccionSiEnLosUltimos3Meses4")
            self.SeleccionSiPeroNoEnLosUltimos3Meses4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses4")

            QtCore.QMetaObject.connectSlotsByName(Pregunta6)

            _translate = QtCore.QCoreApplication.translate
            Pregunta6.setWindowTitle(_translate("Pregunta6", "Pregunta6"))
            self.pushButton.setText(_translate("Pregunta6", "SIGUIENTE PREGUNTA"))
            self.LabelSustancia.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNoNunca.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setText(
                _translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia2.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNoNunca2.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia3.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNoNunca3.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia4.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[3]}"))
            self.SeleccionNoNunca4.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses4.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

        if self.canitdad_sustancias == 5:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame.setGeometry(QtCore.QRect(410, 220, 1081, 101))
            self.SustanciaFrame.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame.setObjectName("SustanciaFrame")

            self.LabelSustancia = QtWidgets.QLabel(self.SustanciaFrame)
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia.setFont(font)
            self.LabelSustancia.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia.setObjectName("LabelSustancia")

            self.SeleccionNoNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNoNunca.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca.setFont(font)
            self.SeleccionNoNunca.setObjectName("SeleccionNoNunca")
            self.SeleccionSiEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiEnLosUltimos3Meses.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses.setObjectName("SeleccionSiEnLosUltimos3Meses")
            self.SeleccionSiPeroNoEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses")

            self.SustanciaFrame2 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame2.setGeometry(QtCore.QRect(410, 330, 1081, 101))
            self.SustanciaFrame2.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame2.setObjectName("SustanciaFrame2")
            self.LabelSustancia2 = QtWidgets.QLabel(self.SustanciaFrame2)
            self.LabelSustancia2.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia2.setFont(font)
            self.LabelSustancia2.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia2.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia2.setObjectName("LabelSustancia2")
            self.SeleccionNoNunca2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionNoNunca2.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca2.setFont(font)
            self.SeleccionNoNunca2.setObjectName("SeleccionNoNunca2")
            self.SeleccionSiEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiEnLosUltimos3Meses2.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses2.setObjectName("SeleccionSiEnLosUltimos3Meses2")
            self.SeleccionSiPeroNoEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses2")

            self.SustanciaFrame3 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame3.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.SustanciaFrame3.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame3.setObjectName("SustanciaFrame3")
            self.LabelSustancia3 = QtWidgets.QLabel(self.SustanciaFrame3)
            self.LabelSustancia3.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia3.setFont(font)
            self.LabelSustancia3.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia3.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia3.setObjectName("LabelSustancia3")
            self.SeleccionNoNunca3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionNoNunca3.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca3.setFont(font)
            self.SeleccionNoNunca3.setObjectName("SeleccionNoNunca3")
            self.SeleccionSiEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiEnLosUltimos3Meses3.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses3.setObjectName("SeleccionSiEnLosUltimos3Meses3")
            self.SeleccionSiPeroNoEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses3")

            self.SustanciaFrame4 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame4.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.SustanciaFrame4.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame4.setObjectName("SustanciaFrame4")
            self.LabelSustancia4 = QtWidgets.QLabel(self.SustanciaFrame4)
            self.LabelSustancia4.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia4.setFont(font)
            self.LabelSustancia4.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia4.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia4.setObjectName("LabelSustancia4")
            self.SeleccionNoNunca4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionNoNunca4.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca4.setFont(font)
            self.SeleccionNoNunca4.setObjectName("SeleccionNoNunca4")
            self.SeleccionSiEnLosUltimos3Meses4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionSiEnLosUltimos3Meses4.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses4.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses4.setObjectName("SeleccionSiEnLosUltimos3Meses4")
            self.SeleccionSiPeroNoEnLosUltimos3Meses4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses4")

            self.SustanciaFrame5 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame5.setGeometry(QtCore.QRect(410, 660, 1081, 101))
            self.SustanciaFrame5.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame5.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame5.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame5.setObjectName("SustanciaFrame5")
            self.LabelSustancia5 = QtWidgets.QLabel(self.SustanciaFrame5)
            self.LabelSustancia5.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia5.setFont(font)
            self.LabelSustancia5.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia5.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia5.setObjectName("LabelSustancia5")
            self.SeleccionNoNunca5 = QtWidgets.QRadioButton(self.SustanciaFrame5)
            self.SeleccionNoNunca5.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca5.setFont(font)
            self.SeleccionNoNunca5.setObjectName("SeleccionNoNunca5")
            self.SeleccionSiEnLosUltimos3Meses5 = QtWidgets.QRadioButton(self.SustanciaFrame5)
            self.SeleccionSiEnLosUltimos3Meses5.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses5.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses5.setObjectName("SeleccionSiEnLosUltimos3Meses5")
            self.SeleccionSiPeroNoEnLosUltimos3Meses5 = QtWidgets.QRadioButton(self.SustanciaFrame5)
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses5")

            QtCore.QMetaObject.connectSlotsByName(Pregunta6)

            _translate = QtCore.QCoreApplication.translate
            Pregunta6.setWindowTitle(_translate("Pregunta6", "Pregunta6"))
            self.pushButton.setText(_translate("Pregunta6", "SIGUIENTE PREGUNTA"))
            self.LabelSustancia.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNoNunca.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setText(
                _translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia2.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNoNunca2.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia3.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNoNunca3.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia4.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[3]}"))
            self.SeleccionNoNunca4.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses4.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia5.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[4]}"))
            self.SeleccionNoNunca5.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses5.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

        if self.canitdad_sustancias == 6:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame.setGeometry(QtCore.QRect(410, 220, 1081, 101))
            self.SustanciaFrame.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame.setObjectName("SustanciaFrame")

            self.LabelSustancia = QtWidgets.QLabel(self.SustanciaFrame)
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia.setFont(font)
            self.LabelSustancia.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia.setObjectName("LabelSustancia")

            self.SeleccionNoNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNoNunca.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca.setFont(font)
            self.SeleccionNoNunca.setObjectName("SeleccionNoNunca")
            self.SeleccionSiEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiEnLosUltimos3Meses.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses.setObjectName("SeleccionSiEnLosUltimos3Meses")
            self.SeleccionSiPeroNoEnLosUltimos3Meses = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses")

            self.SustanciaFrame2 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame2.setGeometry(QtCore.QRect(410, 330, 1081, 101))
            self.SustanciaFrame2.setStyleSheet("QFrame {\n"
                                              "  border: 3px solid black;\n"
                                              "  border-radius: 20px;\n"
                                              "}\n"
                                              "\n"
                                              "QFrame > QLabel {\n"
                                              "\n"
                                              "}")
            self.SustanciaFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame2.setObjectName("SustanciaFrame2")
            self.LabelSustancia2 = QtWidgets.QLabel(self.SustanciaFrame2)
            self.LabelSustancia2.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia2.setFont(font)
            self.LabelSustancia2.setStyleSheet("QFrame > QLabel {\n"
                                              "  border: none;\n"
                                              "  border-radius: 0; \n"
                                              "}")
            self.LabelSustancia2.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia2.setObjectName("LabelSustancia2")
            self.SeleccionNoNunca2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionNoNunca2.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca2.setFont(font)
            self.SeleccionNoNunca2.setObjectName("SeleccionNoNunca2")
            self.SeleccionSiEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiEnLosUltimos3Meses2.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses2.setObjectName("SeleccionSiEnLosUltimos3Meses2")
            self.SeleccionSiPeroNoEnLosUltimos3Meses2 = QtWidgets.QRadioButton(self.SustanciaFrame2)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses2")

            self.SustanciaFrame3 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame3.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.SustanciaFrame3.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame3.setObjectName("SustanciaFrame3")
            self.LabelSustancia3 = QtWidgets.QLabel(self.SustanciaFrame3)
            self.LabelSustancia3.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia3.setFont(font)
            self.LabelSustancia3.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia3.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia3.setObjectName("LabelSustancia3")
            self.SeleccionNoNunca3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionNoNunca3.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca3.setFont(font)
            self.SeleccionNoNunca3.setObjectName("SeleccionNoNunca3")
            self.SeleccionSiEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiEnLosUltimos3Meses3.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses3.setObjectName("SeleccionSiEnLosUltimos3Meses3")
            self.SeleccionSiPeroNoEnLosUltimos3Meses3 = QtWidgets.QRadioButton(self.SustanciaFrame3)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses3")

            self.SustanciaFrame4 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame4.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.SustanciaFrame4.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame4.setObjectName("SustanciaFrame4")
            self.LabelSustancia4 = QtWidgets.QLabel(self.SustanciaFrame4)
            self.LabelSustancia4.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia4.setFont(font)
            self.LabelSustancia4.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia4.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia4.setObjectName("LabelSustancia4")
            self.SeleccionNoNunca4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionNoNunca4.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca4.setFont(font)
            self.SeleccionNoNunca4.setObjectName("SeleccionNoNunca4")
            self.SeleccionSiEnLosUltimos3Meses4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionSiEnLosUltimos3Meses4.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses4.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses4.setObjectName("SeleccionSiEnLosUltimos3Meses4")
            self.SeleccionSiPeroNoEnLosUltimos3Meses4 = QtWidgets.QRadioButton(self.SustanciaFrame4)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses4")

            self.SustanciaFrame5 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame5.setGeometry(QtCore.QRect(410, 660, 1081, 101))
            self.SustanciaFrame5.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame5.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame5.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame5.setObjectName("SustanciaFrame5")
            self.LabelSustancia5 = QtWidgets.QLabel(self.SustanciaFrame5)
            self.LabelSustancia5.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia5.setFont(font)
            self.LabelSustancia5.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia5.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia5.setObjectName("LabelSustancia5")
            self.SeleccionNoNunca5 = QtWidgets.QRadioButton(self.SustanciaFrame5)
            self.SeleccionNoNunca5.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca5.setFont(font)
            self.SeleccionNoNunca5.setObjectName("SeleccionNoNunca5")
            self.SeleccionSiEnLosUltimos3Meses5 = QtWidgets.QRadioButton(self.SustanciaFrame5)
            self.SeleccionSiEnLosUltimos3Meses5.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses5.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses5.setObjectName("SeleccionSiEnLosUltimos3Meses5")
            self.SeleccionSiPeroNoEnLosUltimos3Meses5 = QtWidgets.QRadioButton(self.SustanciaFrame5)
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses5")

            self.SustanciaFrame6 = QtWidgets.QFrame(Pregunta6)
            self.SustanciaFrame6.setGeometry(QtCore.QRect(410, 770, 1081, 101))
            self.SustanciaFrame6.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")
            self.SustanciaFrame6.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.SustanciaFrame6.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SustanciaFrame6.setObjectName("SustanciaFrame6")
            self.LabelSustancia6 = QtWidgets.QLabel(self.SustanciaFrame6)
            self.LabelSustancia6.setGeometry(QtCore.QRect(30, 30, 161, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.LabelSustancia6.setFont(font)
            self.LabelSustancia6.setStyleSheet("QFrame > QLabel {\n"
                                               "  border: none;\n"
                                               "  border-radius: 0; \n"
                                               "}")
            self.LabelSustancia6.setAlignment(QtCore.Qt.AlignCenter)
            self.LabelSustancia6.setObjectName("LabelSustancia6")
            self.SeleccionNoNunca6 = QtWidgets.QRadioButton(self.SustanciaFrame6)
            self.SeleccionNoNunca6.setGeometry(QtCore.QRect(240, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNoNunca6.setFont(font)
            self.SeleccionNoNunca6.setObjectName("SeleccionNoNunca6")
            self.SeleccionSiEnLosUltimos3Meses6 = QtWidgets.QRadioButton(self.SustanciaFrame6)
            self.SeleccionSiEnLosUltimos3Meses6.setGeometry(QtCore.QRect(380, 40, 261, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiEnLosUltimos3Meses6.setFont(font)
            self.SeleccionSiEnLosUltimos3Meses6.setObjectName("SeleccionSiEnLosUltimos3Meses6")
            self.SeleccionSiPeroNoEnLosUltimos3Meses6 = QtWidgets.QRadioButton(self.SustanciaFrame6)
            self.SeleccionSiPeroNoEnLosUltimos3Meses6.setGeometry(QtCore.QRect(660, 40, 331, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionSiPeroNoEnLosUltimos3Meses6.setFont(font)
            self.SeleccionSiPeroNoEnLosUltimos3Meses6.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses6")

            QtCore.QMetaObject.connectSlotsByName(Pregunta6)

            _translate = QtCore.QCoreApplication.translate
            Pregunta6.setWindowTitle(_translate("Pregunta6", "Pregunta6"))
            self.pushButton.setText(_translate("Pregunta6", "SIGUIENTE PREGUNTA"))
            self.LabelSustancia.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNoNunca.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses.setText(
                _translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia2.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNoNunca2.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses2.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia3.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNoNunca3.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses3.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia4.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[3]}"))
            self.SeleccionNoNunca4.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses4.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses4.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia5.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[4]}"))
            self.SeleccionNoNunca5.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses5.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses5.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))

            self.LabelSustancia6.setText(_translate("Pregunta6", f"{lista_sustancias_escogidas[5]}"))
            self.SeleccionNoNunca6.setText(_translate("Pregunta6", "No,Nunca"))
            self.SeleccionSiEnLosUltimos3Meses6.setText(_translate("Pregunta6", "Si, en los ultimos 3 meses"))
            self.SeleccionSiPeroNoEnLosUltimos3Meses6.setText(_translate("Pregunta6", "Si, pero no en los ultimos 3 meses"))


    def abrir_pregunta7(self):
        puntajes_pregunta_actual = []

        if self.canitdad_sustancias == 1:
            if self.SeleccionNoNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(3)
        elif self.canitdad_sustancias == 2:
            if self.SeleccionNoNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(3)
        elif self.canitdad_sustancias == 3:
            if self.SeleccionNoNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(3)
        elif self.canitdad_sustancias == 4:
            if self.SeleccionNoNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca4.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses4.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses4.isChecked():
                puntajes_pregunta_actual.append(3)
        elif self.canitdad_sustancias == 5:
            if self.SeleccionNoNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca4.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses4.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses4.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca5.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses5.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses5.isChecked():
                puntajes_pregunta_actual.append(3)
        elif self.canitdad_sustancias == 6:
            if self.SeleccionNoNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses2.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses3.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca4.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses4.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses4.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca5.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses5.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses5.isChecked():
                puntajes_pregunta_actual.append(3)
            if self.SeleccionNoNunca6.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.SeleccionSiEnLosUltimos3Meses6.isChecked():
                puntajes_pregunta_actual.append(6)
            elif self.SeleccionSiPeroNoEnLosUltimos3Meses6.isChecked():
                puntajes_pregunta_actual.append(3)

        lista_puntajes_a_pasar = suma_vectorial(puntajes_pregunta_actual, self.puntajes_recibidos)

        print("El puntaje que lleva hasta la pregunta 6 es: ",lista_puntajes_a_pasar)

        self.pregunta7 = QMainWindow()
        self.ui = Ui_Pregunta7()
        self.ui.setupUi(self.pregunta7, self.Lista_sustancias,lista_puntajes_a_pasar)
        self.pregunta7.showFullScreen()
