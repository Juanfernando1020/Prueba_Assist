import sys
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import *
from Pregunta1 import Ui_Pregunta1
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2 as psy


conn = psy.connect(dbname='assist', user='postgres', password='rodriyadri20')
cur = conn.cursor()

class Ui_RegisterPage(QWidget):
    def setupUi(self, RegisterPage):
        self.lista_informacion = []
        RegisterPage.setObjectName("RegisterPage")
        RegisterPage.resize(1920, 1080)
        pixmap = QPixmap("imagenes/Banner.png")
        self.BannerLabel = QLabel(RegisterPage)
        self.BannerLabel.setGeometry(QRect(10, 10, 1901, 171))
        self.BannerLabel.setPixmap(pixmap)
        self.BannerLabel.setObjectName("BannerLabel")
        self.comboBox = QComboBox(RegisterPage)
        self.comboBox.setGeometry(QRect(440, 430, 301, 41))
        self.comboBox.setStyleSheet("\n"
"border: 3px solid black;\n"
"border-radius: 5px\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Hombre")
        self.comboBox.addItem("Mujer")
        self.comboBox.addItem("Otro")
        self.label_2 = QLabel(RegisterPage)
        self.label_2.setGeometry(QRect(440, 400, 61, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(RegisterPage)
        self.label_3.setGeometry(QRect(1080, 660, 111, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QComboBox(RegisterPage)
        self.comboBox_2.setGeometry(QRect(1080, 690, 301, 41))
        self.comboBox_2.setStyleSheet("\n"
"border: 3px solid black;\n"
"border-radius: 5px\n"
"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setPlaceholderText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("1")
        self.comboBox_2.addItem("2")
        self.comboBox_2.addItem("3")
        self.comboBox_2.addItem("4")
        self.comboBox_2.addItem("5")
        self.comboBox_2.addItem("6")
        self.label_4 = QLabel(RegisterPage)
        self.label_4.setGeometry(QRect(440, 530, 61, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QComboBox(RegisterPage)
        self.comboBox_3.setGeometry(QRect(440, 560, 301, 41))
        self.comboBox_3.setStyleSheet("\n"
"border: 3px solid black;\n"
"border-radius: 5px\n"
"")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setPlaceholderText("")
        for i in range(100):
            self.edadstr = str(i)
            self.comboBox_3.addItem(self.edadstr)
        self.label_5 = QLabel(RegisterPage)
        self.label_5.setGeometry(QRect(1080, 385, 111, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(RegisterPage)
        self.label_6.setGeometry(QRect(440, 650, 81, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(RegisterPage)
        self.label_7.setGeometry(QRect(1080, 530, 91, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(RegisterPage)
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
                                      "QPushButton:hover {  q\n"
                                      "  background-color: #FFB347;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(RegisterPage)
        self.lineEdit.setGeometry(QRect(440, 690, 301, 41))
        self.lineEdit.setStyleSheet("border: 3px solid black;\n"
"border-radius: 5px\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(RegisterPage)
        self.lineEdit_2.setGeometry(QRect(1080, 430, 301, 41))
        self.lineEdit_2.setStyleSheet("border: 3px solid black;\n"
"border-radius: 5px\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QLineEdit(RegisterPage)
        self.lineEdit_3.setGeometry(QRect(1080, 560, 301, 41))
        self.lineEdit_3.setStyleSheet("border: 3px solid black;\n"
"border-radius: 5px\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")

        QMetaObject.connectSlotsByName(RegisterPage)

        self.pushButton.clicked.connect(self.abrir_pregunta1)

        _translate = QCoreApplication.translate
        RegisterPage.setWindowTitle(_translate("RegisterPage", "RegisterPage"))
        self.label_2.setText(_translate("RegisterPage", "SEXO:"))
        self.label_3.setText(_translate("RegisterPage", "ESTRATO:"))
        self.label_4.setText(_translate("RegisterPage", "EDAD:"))
        self.label_5.setText(_translate("RegisterPage", "OCUPACÓN:"))
        self.label_6.setText(_translate("RegisterPage", "CLÍNICA:"))
        self.label_7.setText(_translate("RegisterPage", "BARRIO:"))
        self.pushButton.setText(_translate("RegisterPage", "EMPEZAR PRUEBA"))

    def campos_llenos(self):
        if self.comboBox.currentText() == "":
            return False
        if self.comboBox_2.currentText() == "":
            return False
        if self.comboBox_3.currentText() == "":
            return False
        if self.lineEdit.text() == "":
            return False
        if self.lineEdit_2.text() == "":
            return False
        if self.lineEdit_3.text() == "":
            return False

        self.lista_informacion.append(self.comboBox.currentText())
        self.lista_informacion.append(self.comboBox_2.currentText())
        self.lista_informacion.append(self.comboBox_3.currentText())
        self.lista_informacion.append(self.lineEdit.text())
        self.lista_informacion.append(self.lineEdit_2.text())
        self.lista_informacion.append(self.lineEdit_3.text())

        return True

    def abrir_pregunta1(self):

        if not self.campos_llenos():
            QMessageBox.warning(self, "Alerta", "Debes llenar toda la información requerida.")
            return
        print(self.lista_informacion)
        sentencia_agregar_usuario = f"INSERT INTO usuarios (sexo,edad,ocupacion,clinica,barrio,estrato) values ('{self.lista_informacion[0]}','{self.lista_informacion[2]}','{self.lista_informacion[4]}','{self.lista_informacion[3]}','{self.lista_informacion[5]}','{self.lista_informacion[1]}')"
        cur.execute(sentencia_agregar_usuario)
        conn.commit()
        self.pregunta1 = QMainWindow()
        self.ui = Ui_Pregunta1()
        self.ui.setupUi(self.pregunta1)
        self.pregunta1.showFullScreen()

