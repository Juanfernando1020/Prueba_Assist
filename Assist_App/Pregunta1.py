from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Pregunta2 import Ui_Pregunta2


class Ui_Pregunta1(QWidget):
    def setupUi(self, Pregunta1):
        Pregunta1.setObjectName("Pregunta1")
        Pregunta1.resize(1924, 1089)
        self.BannerLabel = QtWidgets.QLabel(Pregunta1)
        self.BannerLabel.setGeometry(QtCore.QRect(10, 10, 1901, 171))
        pixmap = QtGui.QPixmap("imagenes/Banner.png")
        self.BannerLabel.setPixmap(pixmap)
        self.BannerLabel.setObjectName("BannerLabel")
        self.LabelInstruccion = QtWidgets.QLabel(Pregunta1)
        self.LabelInstruccion.setGeometry(QtCore.QRect(440, 250, 1201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LabelInstruccion.setFont(font)
        self.LabelInstruccion.setObjectName("LabelInstruccion")
        self.TabacoCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.TabacoCheckBox.setGeometry(QtCore.QRect(530, 370, 651, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TabacoCheckBox.setFont(font)
        self.TabacoCheckBox.setObjectName("TabacoCheckBox")
        self.BebidasAlcohoolicasCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.BebidasAlcohoolicasCheckBox.setGeometry(QtCore.QRect(530, 420, 651, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BebidasAlcohoolicasCheckBox.setFont(font)
        self.BebidasAlcohoolicasCheckBox.setObjectName("BebidasAlcohoolicasCheckBox")
        self.CannabisCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.CannabisCheckBox.setGeometry(QtCore.QRect(530, 470, 651, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CannabisCheckBox.setFont(font)
        self.CannabisCheckBox.setObjectName("CannabisCheckBox")
        self.CocainaCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.CocainaCheckBox.setGeometry(QtCore.QRect(530, 520, 651, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CocainaCheckBox.setFont(font)
        self.CocainaCheckBox.setObjectName("CocainaCheckBox")
        self.AnfetaminasCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.AnfetaminasCheckBox.setGeometry(QtCore.QRect(530, 570, 651, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AnfetaminasCheckBox.setFont(font)
        self.AnfetaminasCheckBox.setObjectName("AnfetaminasCheckBox")
        self.InhalantesCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.InhalantesCheckBox.setGeometry(QtCore.QRect(530, 610, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InhalantesCheckBox.setFont(font)
        self.InhalantesCheckBox.setObjectName("InhalantesCheckBox")
        self.TranquilizantesCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.TranquilizantesCheckBox.setGeometry(QtCore.QRect(530, 670, 1211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TranquilizantesCheckBox.setFont(font)
        self.TranquilizantesCheckBox.setObjectName("TranquilizantesCheckBox")
        self.AlucinogenosCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.AlucinogenosCheckBox.setGeometry(QtCore.QRect(530, 720, 1031, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AlucinogenosCheckBox.setFont(font)
        self.AlucinogenosCheckBox.setObjectName("AlucinogenosCheckBox")
        self.OpiaceosCheckBox = QtWidgets.QCheckBox(Pregunta1)
        self.OpiaceosCheckBox.setGeometry(QtCore.QRect(530, 770, 1031, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OpiaceosCheckBox.setFont(font)
        self.OpiaceosCheckBox.setObjectName("OpiaceosCheckBox")
        self.progressBar = QtWidgets.QProgressBar(Pregunta1)
        self.progressBar.setGeometry(QtCore.QRect(40, 1000, 1841, 23))
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
                                       "  background-color: #FA9300;\n"
                                       "}\n"
                                       "QProgressBar {\n"
                                       "  border: 2px solid black;\n"
                                       "  border-radius: 20px;\n"
                                       "}")

        self.progressBar.setProperty("value", 12)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.pushButton = QtWidgets.QPushButton(Pregunta1)
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

        self.pushButton.clicked.connect(self.abrir_pregunta2)

        self.retranslateUi(Pregunta1)
        QtCore.QMetaObject.connectSlotsByName(Pregunta1)

    def retranslateUi(self, Pregunta1):
        _translate = QtCore.QCoreApplication.translate
        Pregunta1.setWindowTitle(_translate("Pregunta1", "Pregunta1"))
        self.LabelInstruccion.setText(
            _translate("Pregunta1", "1. DE LAS SIGUIENTES SUSTANCIAS ESCOJA LAS QUE HALLA CONSUMIDO :"))
        self.TabacoCheckBox.setText(
            _translate("Pregunta1", "Tabaco (cigarrillos, cigarros habanos, tabaco de mascar, pipa, etc.) "))
        self.BebidasAlcohoolicasCheckBox.setText(
            _translate("Pregunta1", " Bebidas alcohólicas (cerveza, vino, licores, destilados, etc.) "))
        self.CannabisCheckBox.setText(_translate("Pregunta1", "Cannabis (marihuana, costo, hierba, hashish, etc.) "))
        self.CocainaCheckBox.setText(_translate("Pregunta1", "Cocaína (coca, farlopa, crack, base, etc.) "))
        self.AnfetaminasCheckBox.setText(_translate("Pregunta1",
                                                    "Anfetaminas u otro tipo de estimulantes (speed, éxtasis, píldoras adelgazantes, etc.) "))
        self.InhalantesCheckBox.setText(_translate("Pregunta1", " Inhalantes (colas, gasolina/nafta, pegamento, etc.)"))
        self.TranquilizantesCheckBox.setText(_translate("Pregunta1",
                                                        "Tranquilizantes o pastillas para dormir (valium/diazepam,Trankimazin/Alprazolam/Xanax, Orfidal/Lorazepam, Rohipnol, etc.)"))
        self.AlucinogenosCheckBox.setText(_translate("Pregunta1", "Alucinógenos (LSD, ácidos, ketamina, PCP, etc.)"))
        self.OpiaceosCheckBox.setText(
            _translate("Pregunta1", "Opiáceos (heroína, metadona, codeína, morfina, dolantina/petidina, etc.) "))
        self.pushButton.setText(_translate("Pregunta1", "SIGUIENTE PREGUNTA"))

    def abrir_pregunta2(self):
        lista_sustancias_escogidas =[]
        if self.TabacoCheckBox.isChecked():
            lista_sustancias_escogidas.append("Tabaco")
        if self.BebidasAlcohoolicasCheckBox.isChecked():
            lista_sustancias_escogidas.append("Licor")
        if self.CannabisCheckBox.isChecked():
            lista_sustancias_escogidas.append("Cannabis")
        if self.CocainaCheckBox.isChecked():
            lista_sustancias_escogidas.append("Cocaina")
        if self.AnfetaminasCheckBox.isChecked():
            lista_sustancias_escogidas.append("Anfetamina")
        if self.InhalantesCheckBox.isChecked():
            lista_sustancias_escogidas.append("Inhalantes")
        if self.TranquilizantesCheckBox.isChecked():
            lista_sustancias_escogidas.append("Tranquilizantes")
        if self.AlucinogenosCheckBox.isChecked():
            lista_sustancias_escogidas.append("Alucinogenos")
        if self.OpiaceosCheckBox.isChecked():
            lista_sustancias_escogidas.append("Opiaceos")
        print(lista_sustancias_escogidas)
        canitdad_sustancias = len(lista_sustancias_escogidas)
        print(canitdad_sustancias)
        self.pregunta2 = QMainWindow()
        self.ui = Ui_Pregunta2()
        self.ui.setupUi(self.pregunta2,lista_sustancias_escogidas)
        self.pregunta2.showFullScreen()
