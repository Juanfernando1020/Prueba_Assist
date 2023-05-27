from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Pregunta3 import  Ui_Pregunta3

class Ui_Pregunta2(QWidget):
    def setupUi(self, Pregunta2,lista_sustancias_escogidas):
        Pregunta2.setObjectName("Pregunta2")
        Pregunta2.resize(1924, 1089)
        self.BannerLabel = QtWidgets.QLabel(Pregunta2)
        self.BannerLabel.setGeometry(QtCore.QRect(10, 10, 1901, 131))
        pixmap = QtGui.QPixmap("imagenes/Banner.png")
        self.BannerLabel.setPixmap(pixmap)
        self.BannerLabel.setObjectName("BannerLabel")
        self.LabelInstruccion = QtWidgets.QLabel(Pregunta2)
        self.LabelInstruccion.setGeometry(QtCore.QRect(180, 156, 1831, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LabelInstruccion.setFont(font)
        self.LabelInstruccion.setObjectName("LabelInstruccion")
        self.LabelInstruccion.setText("2. ¿Con qué frecuencia ha consumido las sustancias que ha mencionado en los últimos tres meses?")
        self.progressBar = QtWidgets.QProgressBar(Pregunta2)
        self.progressBar.setGeometry(QtCore.QRect(40, 1000, 1841, 23))
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"  background-color: #FA9300;\n"
"}\n"
"QProgressBar {\n"
"  border: 2px solid black;\n"
"  border-radius: 20px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Pregunta2)
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
        self.pushButton.clicked.connect(self.abrir_pregunta3)

        self.canitdad_sustancias = len(lista_sustancias_escogidas)
        self.Lista_sustancias = lista_sustancias_escogidas

        if self.canitdad_sustancias == 1:
            self.lista_puntajes = []
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta2)
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
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))  # Ajuste de la posición vertical
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

            self.SeleccionNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNunca.setGeometry(QtCore.QRect(240, 40, 95, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca.setFont(font)
            self.SeleccionNunca.setObjectName("SeleccionNunca")

            self.Seleccion1o2Veces = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.Seleccion1o2Veces.setGeometry(QtCore.QRect(350, 40, 131, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces.setFont(font)
            self.Seleccion1o2Veces.setObjectName("Seleccion1o2Veces")

            self.SeleccionCadaMes = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaMes.setGeometry(QtCore.QRect(510, 40, 121, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes.setFont(font)
            self.SeleccionCadaMes.setObjectName("SeleccionCadaMes")

            self.SeleccionCadaSemana = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaSemana.setGeometry(QtCore.QRect(660, 40, 161, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana.setFont(font)
            self.SeleccionCadaSemana.setObjectName("SeleccionCadaSemana")

            self.radioButton = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.radioButton.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName("radioButton")

            _translate = QtCore.QCoreApplication.translate
            Pregunta2.setWindowTitle(_translate("Pregunta2", "Pregunta2"))
            self.LabelSustancia.setText(_translate(f"Pregunta2", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNunca.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton.setText(_translate("Pregunta2", "A diario o casi diario"))
            self.pushButton.setText(_translate("Pregunta2", "SIGUIENTE PREGUNTA"))

        elif self.canitdad_sustancias == 2:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta2)
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
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))  # Ajuste de la posición vertical
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

            self.SeleccionNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNunca.setGeometry(QtCore.QRect(240, 40, 95, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca.setFont(font)
            self.SeleccionNunca.setObjectName("SeleccionNunca")

            self.Seleccion1o2Veces = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.Seleccion1o2Veces.setGeometry(QtCore.QRect(350, 40, 131, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces.setFont(font)
            self.Seleccion1o2Veces.setObjectName("Seleccion1o2Veces")

            self.SeleccionCadaMes = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaMes.setGeometry(QtCore.QRect(510, 40, 121, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes.setFont(font)
            self.SeleccionCadaMes.setObjectName("SeleccionCadaMes")

            self.SeleccionCadaSemana = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaSemana.setGeometry(QtCore.QRect(660, 40, 161, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana.setFont(font)
            self.SeleccionCadaSemana.setObjectName("SeleccionCadaSemana")
            self.radioButton = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.radioButton.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName("radioButton")

            self.Sustancia2Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia2Frame.setGeometry(QtCore.QRect(410, 530, 1081, 101))
            self.Sustancia2Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia2Frame.setObjectName("Sustancia2Frame")

            self.LabelSustancia2 = QtWidgets.QLabel(self.Sustancia2Frame)
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

            self.SeleccionNunca2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionNunca2.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca2.setFont(font)
            self.SeleccionNunca2.setObjectName("SeleccionNunca2")

            self.Seleccion1o2Veces2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.Seleccion1o2Veces2.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces2.setFont(font)
            self.Seleccion1o2Veces2.setObjectName("Seleccion1o2Veces2")

            self.SeleccionCadaMes2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaMes2.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes2.setFont(font)
            self.SeleccionCadaMes2.setObjectName("SeleccionCadaMes2")

            self.SeleccionCadaSemana2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaSemana2.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana2.setFont(font)
            self.SeleccionCadaSemana2.setObjectName("SeleccionCadaSemana2")

            self.radioButton2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.radioButton2.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton2.setFont(font)
            self.radioButton2.setObjectName("radioButton2")

            QtCore.QMetaObject.connectSlotsByName(Pregunta2)

            _translate = QtCore.QCoreApplication.translate
            Pregunta2.setWindowTitle(_translate("Pregunta2", "Pregunta2"))
            self.LabelSustancia.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNunca.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton.setText(_translate("Pregunta2", "A diario o casi diario"))
            self.pushButton.setText(_translate("Pregunta2", "SIGUIENTE PREGUNTA"))

            self.LabelSustancia2.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNunca2.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces2.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes2.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana2.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton2.setText(_translate("Pregunta2", "A diario o casi diario"))

        elif self.canitdad_sustancias == 3:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta2)
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
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))  # Ajuste de la posición vertical
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

            self.SeleccionNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNunca.setGeometry(QtCore.QRect(240, 40, 95, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca.setFont(font)
            self.SeleccionNunca.setObjectName("SeleccionNunca")

            self.Seleccion1o2Veces = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.Seleccion1o2Veces.setGeometry(QtCore.QRect(350, 40, 131, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces.setFont(font)
            self.Seleccion1o2Veces.setObjectName("Seleccion1o2Veces")

            self.SeleccionCadaMes = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaMes.setGeometry(QtCore.QRect(510, 40, 121, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes.setFont(font)
            self.SeleccionCadaMes.setObjectName("SeleccionCadaMes")

            self.SeleccionCadaSemana = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaSemana.setGeometry(QtCore.QRect(660, 40, 161, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana.setFont(font)
            self.SeleccionCadaSemana.setObjectName("SeleccionCadaSemana")
            self.radioButton = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.radioButton.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName("radioButton")

            self.Sustancia2Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia2Frame.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.Sustancia2Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia2Frame.setObjectName("Sustancia2Frame")

            self.LabelSustancia2 = QtWidgets.QLabel(self.Sustancia2Frame)
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

            self.SeleccionNunca2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionNunca2.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca2.setFont(font)
            self.SeleccionNunca2.setObjectName("SeleccionNunca2")

            self.Seleccion1o2Veces2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.Seleccion1o2Veces2.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces2.setFont(font)
            self.Seleccion1o2Veces2.setObjectName("Seleccion1o2Veces2")

            self.SeleccionCadaMes2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaMes2.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes2.setFont(font)
            self.SeleccionCadaMes2.setObjectName("SeleccionCadaMes2")

            self.SeleccionCadaSemana2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaSemana2.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana2.setFont(font)
            self.SeleccionCadaSemana2.setObjectName("SeleccionCadaSemana2")

            self.radioButton2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.radioButton2.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton2.setFont(font)
            self.radioButton2.setObjectName("radioButton2")

            self.Sustancia3Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia3Frame.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.Sustancia3Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia3Frame.setObjectName("Sustancia3Frame")

            self.LabelSustancia3 = QtWidgets.QLabel(self.Sustancia3Frame)
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

            self.SeleccionNunca3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionNunca3.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca3.setFont(font)
            self.SeleccionNunca3.setObjectName("SeleccionNunca3")

            self.Seleccion1o2Veces3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.Seleccion1o2Veces3.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces3.setFont(font)
            self.Seleccion1o2Veces3.setObjectName("Seleccion1o2Veces3")

            self.SeleccionCadaMes3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaMes3.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes3.setFont(font)
            self.SeleccionCadaMes3.setObjectName("SeleccionCadaMes3")

            self.SeleccionCadaSemana3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaSemana3.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana3.setFont(font)
            self.SeleccionCadaSemana3.setObjectName("SeleccionCadaSemana3")

            self.radioButton3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.radioButton3.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton3.setFont(font)
            self.radioButton3.setObjectName("radioButton3")

            QtCore.QMetaObject.connectSlotsByName(Pregunta2)

            _translate = QtCore.QCoreApplication.translate
            Pregunta2.setWindowTitle(_translate("Pregunta2", "Pregunta2"))
            self.LabelSustancia.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNunca.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton.setText(_translate("Pregunta2", "A diario o casi diario"))
            self.pushButton.setText(_translate("Pregunta2", "SIGUIENTE PREGUNTA"))

            self.LabelSustancia2.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNunca2.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces2.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes2.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana2.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton2.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia3.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNunca3.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces3.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes3.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana3.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton3.setText(_translate("Pregunta2", "A diario o casi diario"))

        elif self.canitdad_sustancias == 4:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta2)
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
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))  # Ajuste de la posición vertical
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

            self.SeleccionNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNunca.setGeometry(QtCore.QRect(240, 40, 95, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca.setFont(font)
            self.SeleccionNunca.setObjectName("SeleccionNunca")

            self.Seleccion1o2Veces = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.Seleccion1o2Veces.setGeometry(QtCore.QRect(350, 40, 131, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces.setFont(font)
            self.Seleccion1o2Veces.setObjectName("Seleccion1o2Veces")

            self.SeleccionCadaMes = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaMes.setGeometry(QtCore.QRect(510, 40, 121, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes.setFont(font)
            self.SeleccionCadaMes.setObjectName("SeleccionCadaMes")

            self.SeleccionCadaSemana = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaSemana.setGeometry(QtCore.QRect(660, 40, 161, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana.setFont(font)
            self.SeleccionCadaSemana.setObjectName("SeleccionCadaSemana")
            self.radioButton = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.radioButton.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName("radioButton")

            self.Sustancia2Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia2Frame.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.Sustancia2Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia2Frame.setObjectName("Sustancia2Frame")

            self.LabelSustancia2 = QtWidgets.QLabel(self.Sustancia2Frame)
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

            self.SeleccionNunca2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionNunca2.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca2.setFont(font)
            self.SeleccionNunca2.setObjectName("SeleccionNunca2")

            self.Seleccion1o2Veces2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.Seleccion1o2Veces2.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces2.setFont(font)
            self.Seleccion1o2Veces2.setObjectName("Seleccion1o2Veces2")

            self.SeleccionCadaMes2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaMes2.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes2.setFont(font)
            self.SeleccionCadaMes2.setObjectName("SeleccionCadaMes2")

            self.SeleccionCadaSemana2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaSemana2.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana2.setFont(font)
            self.SeleccionCadaSemana2.setObjectName("SeleccionCadaSemana2")

            self.radioButton2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.radioButton2.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton2.setFont(font)
            self.radioButton2.setObjectName("radioButton2")

            self.Sustancia3Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia3Frame.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.Sustancia3Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia3Frame.setObjectName("Sustancia3Frame")

            self.LabelSustancia3 = QtWidgets.QLabel(self.Sustancia3Frame)
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

            self.SeleccionNunca3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionNunca3.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca3.setFont(font)
            self.SeleccionNunca3.setObjectName("SeleccionNunca3")

            self.Seleccion1o2Veces3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.Seleccion1o2Veces3.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces3.setFont(font)
            self.Seleccion1o2Veces3.setObjectName("Seleccion1o2Veces3")

            self.SeleccionCadaMes3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaMes3.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes3.setFont(font)
            self.SeleccionCadaMes3.setObjectName("SeleccionCadaMes3")

            self.SeleccionCadaSemana3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaSemana3.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana3.setFont(font)
            self.SeleccionCadaSemana3.setObjectName("SeleccionCadaSemana3")

            self.radioButton3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.radioButton3.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton3.setFont(font)
            self.radioButton3.setObjectName("radioButton3")

            self.Sustancia4Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia4Frame.setGeometry(QtCore.QRect(410, 660, 1081, 101))
            self.Sustancia4Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia4Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia4Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia4Frame.setObjectName("Sustancia4Frame")

            self.LabelSustancia4 = QtWidgets.QLabel(self.Sustancia4Frame)
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

            self.SeleccionNunca4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionNunca4.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca4.setFont(font)
            self.SeleccionNunca4.setObjectName("SeleccionNunca4")

            self.Seleccion1o2Veces4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.Seleccion1o2Veces4.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces4.setFont(font)
            self.Seleccion1o2Veces4.setObjectName("Seleccion1o2Veces4")

            self.SeleccionCadaMes4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionCadaMes4.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes4.setFont(font)
            self.SeleccionCadaMes4.setObjectName("SeleccionCadaMes4")

            self.SeleccionCadaSemana4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionCadaSemana4.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana4.setFont(font)
            self.SeleccionCadaSemana4.setObjectName("SeleccionCadaSemana4")

            self.radioButton4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.radioButton4.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton4.setFont(font)
            self.radioButton4.setObjectName("radioButton4")

            QtCore.QMetaObject.connectSlotsByName(Pregunta2)

            _translate = QtCore.QCoreApplication.translate
            Pregunta2.setWindowTitle(_translate("Pregunta2", "Pregunta2"))
            self.LabelSustancia.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNunca.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton.setText(_translate("Pregunta2", "A diario o casi diario"))
            self.pushButton.setText(_translate("Pregunta2", "SIGUIENTE PREGUNTA"))

            self.LabelSustancia2.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNunca2.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces2.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes2.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana2.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton2.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia3.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNunca3.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces3.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes3.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana3.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton3.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia4.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[3]}"))
            self.SeleccionNunca4.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces4.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes4.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana4.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton4.setText(_translate("Pregunta2", "A diario o casi diario"))

        elif self.canitdad_sustancias == 5:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta2)
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
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))  # Ajuste de la posición vertical
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

            self.SeleccionNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNunca.setGeometry(QtCore.QRect(240, 40, 95, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca.setFont(font)
            self.SeleccionNunca.setObjectName("SeleccionNunca")

            self.Seleccion1o2Veces = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.Seleccion1o2Veces.setGeometry(QtCore.QRect(350, 40, 131, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces.setFont(font)
            self.Seleccion1o2Veces.setObjectName("Seleccion1o2Veces")

            self.SeleccionCadaMes = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaMes.setGeometry(QtCore.QRect(510, 40, 121, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes.setFont(font)
            self.SeleccionCadaMes.setObjectName("SeleccionCadaMes")

            self.SeleccionCadaSemana = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaSemana.setGeometry(QtCore.QRect(660, 40, 161, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana.setFont(font)
            self.SeleccionCadaSemana.setObjectName("SeleccionCadaSemana")
            self.radioButton = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.radioButton.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName("radioButton")

            self.Sustancia2Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia2Frame.setGeometry(QtCore.QRect(410, 330, 1081, 101))
            self.Sustancia2Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia2Frame.setObjectName("Sustancia2Frame")

            self.LabelSustancia2 = QtWidgets.QLabel(self.Sustancia2Frame)
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

            self.SeleccionNunca2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionNunca2.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca2.setFont(font)
            self.SeleccionNunca2.setObjectName("SeleccionNunca2")

            self.Seleccion1o2Veces2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.Seleccion1o2Veces2.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces2.setFont(font)
            self.Seleccion1o2Veces2.setObjectName("Seleccion1o2Veces2")

            self.SeleccionCadaMes2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaMes2.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes2.setFont(font)
            self.SeleccionCadaMes2.setObjectName("SeleccionCadaMes2")

            self.SeleccionCadaSemana2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaSemana2.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana2.setFont(font)
            self.SeleccionCadaSemana2.setObjectName("SeleccionCadaSemana2")

            self.radioButton2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.radioButton2.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton2.setFont(font)
            self.radioButton2.setObjectName("radioButton2")

            self.Sustancia3Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia3Frame.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.Sustancia3Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia3Frame.setObjectName("Sustancia3Frame")

            self.LabelSustancia3 = QtWidgets.QLabel(self.Sustancia3Frame)
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

            self.SeleccionNunca3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionNunca3.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca3.setFont(font)
            self.SeleccionNunca3.setObjectName("SeleccionNunca3")

            self.Seleccion1o2Veces3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.Seleccion1o2Veces3.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces3.setFont(font)
            self.Seleccion1o2Veces3.setObjectName("Seleccion1o2Veces3")

            self.SeleccionCadaMes3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaMes3.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes3.setFont(font)
            self.SeleccionCadaMes3.setObjectName("SeleccionCadaMes3")

            self.SeleccionCadaSemana3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaSemana3.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana3.setFont(font)
            self.SeleccionCadaSemana3.setObjectName("SeleccionCadaSemana3")

            self.radioButton3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.radioButton3.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton3.setFont(font)
            self.radioButton3.setObjectName("radioButton3")

            self.Sustancia4Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia4Frame.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.Sustancia4Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia4Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia4Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia4Frame.setObjectName("Sustancia4Frame")

            self.LabelSustancia4 = QtWidgets.QLabel(self.Sustancia4Frame)
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

            self.SeleccionNunca4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionNunca4.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca4.setFont(font)
            self.SeleccionNunca4.setObjectName("SeleccionNunca4")

            self.Seleccion1o2Veces4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.Seleccion1o2Veces4.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces4.setFont(font)
            self.Seleccion1o2Veces4.setObjectName("Seleccion1o2Veces4")

            self.SeleccionCadaMes4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionCadaMes4.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes4.setFont(font)
            self.SeleccionCadaMes4.setObjectName("SeleccionCadaMes4")

            self.SeleccionCadaSemana4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionCadaSemana4.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana4.setFont(font)
            self.SeleccionCadaSemana4.setObjectName("SeleccionCadaSemana4")

            self.radioButton4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.radioButton4.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton4.setFont(font)
            self.radioButton4.setObjectName("radioButton4")

            self.Sustancia5Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia5Frame.setGeometry(QtCore.QRect(410, 660, 1081, 101))
            self.Sustancia5Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia5Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia5Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia5Frame.setObjectName("Sustancia5Frame")

            self.LabelSustancia5 = QtWidgets.QLabel(self.Sustancia5Frame)
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

            self.SeleccionNunca5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.SeleccionNunca5.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca5.setFont(font)
            self.SeleccionNunca5.setObjectName("SeleccionNunca5")

            self.Seleccion1o2Veces5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.Seleccion1o2Veces5.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces5.setFont(font)
            self.Seleccion1o2Veces5.setObjectName("Seleccion1o2Veces5")

            self.SeleccionCadaMes5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.SeleccionCadaMes5.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes5.setFont(font)
            self.SeleccionCadaMes5.setObjectName("SeleccionCadaMes5")

            self.SeleccionCadaSemana5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.SeleccionCadaSemana5.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana5.setFont(font)
            self.SeleccionCadaSemana5.setObjectName("SeleccionCadaSemana5")

            self.radioButton5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.radioButton5.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton5.setFont(font)
            self.radioButton5.setObjectName("radioButton5")

            QtCore.QMetaObject.connectSlotsByName(Pregunta2)

            _translate = QtCore.QCoreApplication.translate
            Pregunta2.setWindowTitle(_translate("Pregunta2", "Pregunta2"))
            self.LabelSustancia.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNunca.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton.setText(_translate("Pregunta2", "A diario o casi diario"))
            self.pushButton.setText(_translate("Pregunta2", "SIGUIENTE PREGUNTA"))

            self.LabelSustancia2.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNunca2.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces2.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes2.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana2.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton2.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia3.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNunca3.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces3.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes3.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana3.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton3.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia4.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[3]}"))
            self.SeleccionNunca4.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces4.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes4.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana4.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton4.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia5.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[4]}"))
            self.SeleccionNunca5.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces5.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes5.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana5.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton5.setText(_translate("Pregunta2", "A diario o casi diario"))

        elif self.canitdad_sustancias ==6:
            self.SustanciaFrame = QtWidgets.QFrame(Pregunta2)
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
            self.LabelSustancia.setGeometry(QtCore.QRect(30, 30, 161, 41))  # Ajuste de la posición vertical
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

            self.SeleccionNunca = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionNunca.setGeometry(QtCore.QRect(240, 40, 95, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca.setFont(font)
            self.SeleccionNunca.setObjectName("SeleccionNunca")

            self.Seleccion1o2Veces = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.Seleccion1o2Veces.setGeometry(QtCore.QRect(350, 40, 131, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces.setFont(font)
            self.Seleccion1o2Veces.setObjectName("Seleccion1o2Veces")

            self.SeleccionCadaMes = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaMes.setGeometry(QtCore.QRect(510, 40, 121, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes.setFont(font)
            self.SeleccionCadaMes.setObjectName("SeleccionCadaMes")

            self.SeleccionCadaSemana = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.SeleccionCadaSemana.setGeometry(QtCore.QRect(660, 40, 161, 20))  # Ajuste de la posición vertical
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana.setFont(font)
            self.SeleccionCadaSemana.setObjectName("SeleccionCadaSemana")
            self.radioButton = QtWidgets.QRadioButton(self.SustanciaFrame)
            self.radioButton.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName("radioButton")

            self.Sustancia2Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia2Frame.setGeometry(QtCore.QRect(410, 330, 1081, 101))
            self.Sustancia2Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia2Frame.setObjectName("Sustancia2Frame")

            self.LabelSustancia2 = QtWidgets.QLabel(self.Sustancia2Frame)
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

            self.SeleccionNunca2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionNunca2.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca2.setFont(font)
            self.SeleccionNunca2.setObjectName("SeleccionNunca2")

            self.Seleccion1o2Veces2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.Seleccion1o2Veces2.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces2.setFont(font)
            self.Seleccion1o2Veces2.setObjectName("Seleccion1o2Veces2")

            self.SeleccionCadaMes2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaMes2.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes2.setFont(font)
            self.SeleccionCadaMes2.setObjectName("SeleccionCadaMes2")

            self.SeleccionCadaSemana2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.SeleccionCadaSemana2.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana2.setFont(font)
            self.SeleccionCadaSemana2.setObjectName("SeleccionCadaSemana2")

            self.radioButton2 = QtWidgets.QRadioButton(self.Sustancia2Frame)
            self.radioButton2.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton2.setFont(font)
            self.radioButton2.setObjectName("radioButton2")

            self.Sustancia3Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia3Frame.setGeometry(QtCore.QRect(410, 440, 1081, 101))
            self.Sustancia3Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia3Frame.setObjectName("Sustancia3Frame")

            self.LabelSustancia3 = QtWidgets.QLabel(self.Sustancia3Frame)
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

            self.SeleccionNunca3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionNunca3.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca3.setFont(font)
            self.SeleccionNunca3.setObjectName("SeleccionNunca3")

            self.Seleccion1o2Veces3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.Seleccion1o2Veces3.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces3.setFont(font)
            self.Seleccion1o2Veces3.setObjectName("Seleccion1o2Veces3")

            self.SeleccionCadaMes3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaMes3.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes3.setFont(font)
            self.SeleccionCadaMes3.setObjectName("SeleccionCadaMes3")

            self.SeleccionCadaSemana3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.SeleccionCadaSemana3.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana3.setFont(font)
            self.SeleccionCadaSemana3.setObjectName("SeleccionCadaSemana3")

            self.radioButton3 = QtWidgets.QRadioButton(self.Sustancia3Frame)
            self.radioButton3.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton3.setFont(font)
            self.radioButton3.setObjectName("radioButton3")

            self.Sustancia4Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia4Frame.setGeometry(QtCore.QRect(410, 550, 1081, 101))
            self.Sustancia4Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia4Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia4Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia4Frame.setObjectName("Sustancia4Frame")

            self.LabelSustancia4 = QtWidgets.QLabel(self.Sustancia4Frame)
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

            self.SeleccionNunca4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionNunca4.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca4.setFont(font)
            self.SeleccionNunca4.setObjectName("SeleccionNunca4")

            self.Seleccion1o2Veces4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.Seleccion1o2Veces4.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces4.setFont(font)
            self.Seleccion1o2Veces4.setObjectName("Seleccion1o2Veces4")

            self.SeleccionCadaMes4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionCadaMes4.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes4.setFont(font)
            self.SeleccionCadaMes4.setObjectName("SeleccionCadaMes4")

            self.SeleccionCadaSemana4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.SeleccionCadaSemana4.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana4.setFont(font)
            self.SeleccionCadaSemana4.setObjectName("SeleccionCadaSemana4")

            self.radioButton4 = QtWidgets.QRadioButton(self.Sustancia4Frame)
            self.radioButton4.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton4.setFont(font)
            self.radioButton4.setObjectName("radioButton4")

            self.Sustancia5Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia5Frame.setGeometry(QtCore.QRect(410, 660, 1081, 101))
            self.Sustancia5Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia5Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia5Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia5Frame.setObjectName("Sustancia5Frame")

            self.LabelSustancia5 = QtWidgets.QLabel(self.Sustancia5Frame)
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

            self.SeleccionNunca5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.SeleccionNunca5.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca5.setFont(font)
            self.SeleccionNunca5.setObjectName("SeleccionNunca5")

            self.Seleccion1o2Veces5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.Seleccion1o2Veces5.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces5.setFont(font)
            self.Seleccion1o2Veces5.setObjectName("Seleccion1o2Veces5")

            self.SeleccionCadaMes5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.SeleccionCadaMes5.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes5.setFont(font)
            self.SeleccionCadaMes5.setObjectName("SeleccionCadaMes5")

            self.SeleccionCadaSemana5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.SeleccionCadaSemana5.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana5.setFont(font)
            self.SeleccionCadaSemana5.setObjectName("SeleccionCadaSemana5")

            self.radioButton5 = QtWidgets.QRadioButton(self.Sustancia5Frame)
            self.radioButton5.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton5.setFont(font)
            self.radioButton5.setObjectName("radioButton5")

            self.Sustancia6Frame = QtWidgets.QFrame(Pregunta2)
            self.Sustancia6Frame.setGeometry(QtCore.QRect(410, 770, 1081, 101))
            self.Sustancia6Frame.setStyleSheet("QFrame {\n"
                                               "  border: 3px solid black;\n"
                                               "  border-radius: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QFrame > QLabel {\n"
                                               "\n"
                                               "}")

            self.Sustancia6Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Sustancia6Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Sustancia6Frame.setObjectName("Sustancia6Frame")

            self.LabelSustancia6 = QtWidgets.QLabel(self.Sustancia6Frame)
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

            self.SeleccionNunca6 = QtWidgets.QRadioButton(self.Sustancia6Frame)
            self.SeleccionNunca6.setGeometry(QtCore.QRect(240, 40, 95, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionNunca6.setFont(font)
            self.SeleccionNunca6.setObjectName("SeleccionNunca6")

            self.Seleccion1o2Veces6 = QtWidgets.QRadioButton(self.Sustancia6Frame)
            self.Seleccion1o2Veces6.setGeometry(QtCore.QRect(350, 40, 131, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Seleccion1o2Veces6.setFont(font)
            self.Seleccion1o2Veces6.setObjectName("Seleccion1o2Veces6")

            self.SeleccionCadaMes6 = QtWidgets.QRadioButton(self.Sustancia6Frame)
            self.SeleccionCadaMes6.setGeometry(QtCore.QRect(510, 40, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaMes6.setFont(font)
            self.SeleccionCadaMes6.setObjectName("SeleccionCadaMes6")

            self.SeleccionCadaSemana6 = QtWidgets.QRadioButton(self.Sustancia6Frame)
            self.SeleccionCadaSemana6.setGeometry(QtCore.QRect(660, 40, 161, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.SeleccionCadaSemana6.setFont(font)
            self.SeleccionCadaSemana6.setObjectName("SeleccionCadaSemana6")

            self.radioButton6 = QtWidgets.QRadioButton(self.Sustancia6Frame)
            self.radioButton6.setGeometry(QtCore.QRect(840, 40, 221, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.radioButton6.setFont(font)
            self.radioButton6.setObjectName("radioButton6")

            QtCore.QMetaObject.connectSlotsByName(Pregunta2)

            _translate = QtCore.QCoreApplication.translate
            Pregunta2.setWindowTitle(_translate("Pregunta2", "Pregunta2"))
            self.LabelSustancia.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[0]}"))
            self.SeleccionNunca.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton.setText(_translate("Pregunta2", "A diario o casi diario"))
            self.pushButton.setText(_translate("Pregunta2", "SIGUIENTE PREGUNTA"))

            self.LabelSustancia2.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[1]}"))
            self.SeleccionNunca2.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces2.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes2.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana2.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton2.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia3.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[2]}"))
            self.SeleccionNunca3.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces3.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes3.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana3.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton3.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia4.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[3]}"))
            self.SeleccionNunca4.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces4.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes4.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana4.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton4.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia5.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[4]}"))
            self.SeleccionNunca5.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces5.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes5.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana5.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton5.setText(_translate("Pregunta2", "A diario o casi diario"))

            self.LabelSustancia6.setText(_translate("Pregunta2", f"{lista_sustancias_escogidas[5]}"))
            self.SeleccionNunca6.setText(_translate("Pregunta2", "Nunca"))
            self.Seleccion1o2Veces6.setText(_translate("Pregunta2", "1 ó 2 veces \n"""))
            self.SeleccionCadaMes6.setText(_translate("Pregunta2", "Cada mes \n"""))
            self.SeleccionCadaSemana6.setText(_translate("Pregunta2", "Cada semana"))
            self.radioButton6.setText(_translate("Pregunta2", "A diario o casi diario"))







    def abrir_pregunta3(self):
        puntajes_pregunta_actual = []
        if self.canitdad_sustancias == 1:
            if self.SeleccionNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton.isChecked():
                puntajes_pregunta_actual.append(6)
        elif self.canitdad_sustancias == 2:
            if self.SeleccionNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces2.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes2.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana2.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton2.isChecked():
                puntajes_pregunta_actual.append(6)
        elif self.canitdad_sustancias == 3:
            if self.SeleccionNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces2.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes2.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana2.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton2.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces3.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes3.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana3.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton3.isChecked():
                puntajes_pregunta_actual.append(6)
        elif self.canitdad_sustancias == 4:
            if self.SeleccionNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces2.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes2.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana2.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton2.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces3.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes3.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana3.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton3.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca4.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces4.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes4.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana4.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton4.isChecked():
                puntajes_pregunta_actual.append(6)
        elif self.canitdad_sustancias == 5:
            if self.SeleccionNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces2.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes2.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana2.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton2.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces3.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes3.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana3.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton3.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca4.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces4.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes4.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana4.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton4.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca5.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces5.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes5.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana5.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton5.isChecked():
                puntajes_pregunta_actual.append(6)
        elif self.canitdad_sustancias == 6:
            if self.SeleccionNunca.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca2.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces2.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes2.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana2.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton2.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca3.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces3.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes3.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana3.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton3.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca4.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces4.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes4.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana4.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton4.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca5.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces5.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes5.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana5.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton5.isChecked():
                puntajes_pregunta_actual.append(6)

            if self.SeleccionNunca6.isChecked():
                puntajes_pregunta_actual.append(0)
            elif self.Seleccion1o2Veces6.isChecked():
                puntajes_pregunta_actual.append(2)
            elif self.SeleccionCadaMes6.isChecked():
                puntajes_pregunta_actual.append(3)
            elif self.SeleccionCadaSemana6.isChecked():
                puntajes_pregunta_actual.append(4)
            elif self.radioButton6.isChecked():
                puntajes_pregunta_actual.append(6)

        print(puntajes_pregunta_actual)
        self.pregunta3 = QMainWindow()
        self.ui = Ui_Pregunta3()
        self.ui.setupUi(self.pregunta3, self.Lista_sustancias, puntajes_pregunta_actual)
        self.pregunta3.showFullScreen()



