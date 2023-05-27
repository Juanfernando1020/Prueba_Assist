import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from RegisterPage import Ui_RegisterPage



class IntroductionPage(QWidget,object):
    def __init__(self):
        super().__init__()
        self.InitUi()


    def InitUi(self):
        self.setObjectName("Form")
        self.resize(1920, 1080)
        self.LabelBanner = QtWidgets.QLabel(self)
        self.LabelBanner.setGeometry(QtCore.QRect(10, 10, 1901, 171))
        pixmap = QtGui.QPixmap("imagenes/Banner.png")
        self.LabelBanner.setPixmap(pixmap)
        self.LabelBanner.setObjectName("LabelBanner")
        self.ParrafoLabel1 = QtWidgets.QLabel(self)
        self.ParrafoLabel1.setGeometry(QtCore.QRect(500, 520, 1021, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ParrafoLabel1.setFont(font)
        self.ParrafoLabel1.setObjectName("ParrafoLabel1")
        self.ParrafoLabel2 = QtWidgets.QLabel(self)
        self.ParrafoLabel2.setGeometry(QtCore.QRect(520, 560, 981, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ParrafoLabel2.setFont(font)
        self.ParrafoLabel2.setObjectName("ParrafoLabel2")
        self.ParrafoLabel3 = QtWidgets.QLabel(self)
        self.ParrafoLabel3.setGeometry(QtCore.QRect(690, 590, 681, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ParrafoLabel3.setFont(font)
        self.ParrafoLabel3.setObjectName("ParrafoLabel3")
        self.LabelAdvertencia = QtWidgets.QLabel(self)
        self.LabelAdvertencia.setGeometry(QtCore.QRect(600, 480, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.LabelAdvertencia.setFont(font)
        self.LabelAdvertencia.setObjectName("LabelAdvertencia")
        self.ParrafoLabel4 = QtWidgets.QLabel(self)
        self.ParrafoLabel4.setGeometry(QtCore.QRect(790, 630, 431, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ParrafoLabel4.setFont(font)
        self.ParrafoLabel4.setObjectName("ParrafoLabel4")
        self.CheckBox = QtWidgets.QCheckBox(self)
        self.CheckBox.setGeometry(QtCore.QRect(60, 990, 511, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CheckBox.setFont(font)
        self.CheckBox.setObjectName("CheckBox")
        self.CoontinueBottom = QtWidgets.QPushButton(self)
        self.CoontinueBottom.setGeometry(QtCore.QRect(1580, 932, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CoontinueBottom.setFont(font)
        self.CoontinueBottom.setStyleSheet("QPushButton {\n"
                                      "  border: 3px solid black;\n"
                                      "  border-radius: 20px;\n"
                                      "  background-color: #FA9300;\n"
                                      "  color: white;\n"
                                      "  font-weight: bold;\n"
                                      "  padding: 10px 20px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {  q\n"
                                      "  background-color: #FFB347;\n"
                                      "}")
        self.CoontinueBottom.setObjectName("CoontinueBottom")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Introducción"))
        self.ParrafoLabel1.setText(_translate("Form",
                                              "La entrevista Assist es una herramienta en psicología para evaluar el nivel de riesgo en el consumo de sustancias."))
        self.ParrafoLabel2.setText(_translate("Form",
                                              "Se recopila información sobre la frecuencia, cantidad, historia personal y familiar de adicción y otros factores."))
        self.ParrafoLabel3.setText(
            _translate("Form", "La información se utiliza para determinar el nivel de intervención requerido,"))
        self.LabelAdvertencia.setText(
            _translate("Form", "Es esencial responder con transparencia a todos los campos de la entrevista."))
        self.ParrafoLabel4.setText(_translate("Form", " desde prevención hasta atención especializada."))
        self.CheckBox.setText(_translate("Form", "Acepto el tratamiento de información de mis resultados."))
        self.CoontinueBottom.setText(_translate("Form", "CONTINUAR"))
        self.CoontinueBottom.clicked.connect(self.abrir_register_page)

    def abrir_register_page(self):
        if self.CheckBox.isChecked():
            self.RegisterPage =QMainWindow()
            self.ui_register_page = Ui_RegisterPage()
            self.ui_register_page.setupUi(self.RegisterPage)
            self.RegisterPage.showFullScreen()
        else:
            QMessageBox.warning(self, "Alerta", "No has aceptado los términos.", QMessageBox.Ok)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntroductionPage()
    window.showFullScreen()
    sys.exit(app.exec_())
