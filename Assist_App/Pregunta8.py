from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Resultados import Ui_Resultados

class Ui_Pregunta8(QWidget,object):
    def setupUi(self, Pregunta8,lista_sustancias_escogidas,lista_puntajes_pregunta_anterior):
        self.Lista_sustancias_Escogidas = lista_sustancias_escogidas
        self.puntajes_recibidos = lista_puntajes_pregunta_anterior
        Pregunta8.setObjectName("Pregunta8")
        Pregunta8.resize(1924, 1089)
        self.BannerLabel = QtWidgets.QLabel(Pregunta8)
        self.BannerLabel.setGeometry(QtCore.QRect(10, 10, 1901, 131))
        pixmap = QtGui.QPixmap("imagenes/Banner.png")
        self.BannerLabel.setPixmap(pixmap)
        self.BannerLabel.setObjectName("BannerLabel")
        self.LabelInstruccion = QtWidgets.QLabel(Pregunta8)
        self.LabelInstruccion.setGeometry(QtCore.QRect(460, 220, 1161, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.LabelInstruccion.setFont(font)
        self.LabelInstruccion.setObjectName("LabelInstruccion")
        self.progressBar = QtWidgets.QProgressBar(Pregunta8)
        self.progressBar.setGeometry(QtCore.QRect(40, 1000, 1841, 23))
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
                                       "  background-color: #FA9300;\n"
                                       "}\n"
                                       "QProgressBar {\n"
                                       "  border: 2px solid black;\n"
                                       "  border-radius: 20px;\n"
                                       "}")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Pregunta8)
        self.pushButton.setGeometry(QtCore.QRect(1580, 870, 251, 41))
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
        self.pushButton.clicked.connect(self.abrir_resultados)

        self.SeleccionNoNunca = QtWidgets.QRadioButton(Pregunta8)
        self.SeleccionNoNunca.setGeometry(QtCore.QRect(880, 410, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SeleccionNoNunca.setFont(font)
        self.SeleccionNoNunca.setObjectName("SeleccionNoNunca")
        self.SeleccionSiEnLosUltimos3Meses = QtWidgets.QRadioButton(Pregunta8)
        self.SeleccionSiEnLosUltimos3Meses.setGeometry(QtCore.QRect(770, 520, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SeleccionSiEnLosUltimos3Meses.setFont(font)
        self.SeleccionSiEnLosUltimos3Meses.setObjectName("SeleccionSiEnLosUltimos3Meses")
        self.SeleccionSiPeroNoEnLosUltimos3Meses = QtWidgets.QRadioButton(Pregunta8)
        self.SeleccionSiPeroNoEnLosUltimos3Meses.setGeometry(QtCore.QRect(720, 640, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SeleccionSiPeroNoEnLosUltimos3Meses.setFont(font)
        self.SeleccionSiPeroNoEnLosUltimos3Meses.setObjectName("SeleccionSiPeroNoEnLosUltimos3Meses")
        self.FrameOpciones = QtWidgets.QFrame(Pregunta8)
        self.FrameOpciones.setGeometry(QtCore.QRect(660, 360, 651, 431))
        self.FrameOpciones.setStyleSheet("QFrame {\n"
                                         "  border: 3px solid black;\n"
                                         "  border-radius: 20px;\n"
                                         "}")
        self.FrameOpciones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameOpciones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameOpciones.setObjectName("FrameOpciones")
        self.FrameOpciones.raise_()
        self.BannerLabel.raise_()
        self.LabelInstruccion.raise_()
        self.progressBar.raise_()
        self.pushButton.raise_()
        self.SeleccionNoNunca.raise_()
        self.SeleccionSiEnLosUltimos3Meses.raise_()
        self.SeleccionSiPeroNoEnLosUltimos3Meses.raise_()

        QtCore.QMetaObject.connectSlotsByName(Pregunta8)

        _translate = QtCore.QCoreApplication.translate
        Pregunta8.setWindowTitle(_translate("Pregunta8", "Pregunta8"))
        self.LabelInstruccion.setText(
            _translate("Pregunta8", "8. ¿Ha consumido alguna vez alguna droga por vía inyectada? "))
        self.pushButton.setText(_translate("Pregunta8", "VER RESUMEN"))
        self.SeleccionNoNunca.setText(_translate("Pregunta8", "No, Nunca "))
        self.SeleccionSiEnLosUltimos3Meses.setText(_translate("Pregunta8", "Si, en los últimos 3 meses "))
        self.SeleccionSiPeroNoEnLosUltimos3Meses.setText(
            _translate("Pregunta8", "Si,  pero no en los últimos 3 meses "))

    def abrir_resultados(self):
        self.resultados = QMainWindow()
        self.ui = Ui_Resultados()
        self.ui.setupUi(self.resultados,self.Lista_sustancias_Escogidas,self.puntajes_recibidos)
        self.resultados.showFullScreen()



