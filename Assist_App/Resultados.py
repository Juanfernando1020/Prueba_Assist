from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import psycopg2 as psy

conn = psy.connect(dbname='assist', user='postgres', password='rodriyadri20')
cur = conn.cursor()

class Ui_Resultados(object):
    def setupUi(self, Resultados,lista_sustancias_escogidas,lista_puntajes_pregunta_anterior):
        self.Lista_sustancias_Escogidas = lista_sustancias_escogidas
        self.puntajes_recibidos = lista_puntajes_pregunta_anterior
        self.hora_actual = datetime.now().strftime("%I:%M %p")
        self. fecha_actual = datetime.now().strftime("%a. %d de %B de %Y")

        Resultados.setObjectName("Resultados")
        Resultados.resize(1924, 1089)
        self.BannerLabel = QtWidgets.QLabel(Resultados)
        self.BannerLabel.setGeometry(QtCore.QRect(10, 10, 1901, 131))
        pixmap = QtGui.QPixmap("imagenes/Banner.png")
        self.BannerLabel.setPixmap(pixmap)
        self.BannerLabel.setObjectName("BannerLabel")
        self.LabelResumendelaEntrevista = QtWidgets.QLabel(Resultados)
        self.LabelResumendelaEntrevista.setGeometry(QtCore.QRect(760, 210, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LabelResumendelaEntrevista.setFont(font)
        self.LabelResumendelaEntrevista.setObjectName("LabelResumendelaEntrevista")
        self.LabelTituloFecha = QtWidgets.QLabel(Resultados)
        self.LabelTituloFecha.setGeometry(QtCore.QRect(280, 320, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTituloFecha.setFont(font)
        self.LabelTituloFecha.setObjectName("LabelTituloFecha")
        self.LabelDatodelaFecha = QtWidgets.QLabel(Resultados)
        self.LabelDatodelaFecha.setGeometry(QtCore.QRect(610, 340, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LabelDatodelaFecha.setFont(font)
        self.LabelDatodelaFecha.setObjectName("LabelDatodelaFecha")
        self.LabelTituloHora = QtWidgets.QLabel(Resultados)
        self.LabelTituloHora.setGeometry(QtCore.QRect(1050, 320, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTituloHora.setFont(font)
        self.LabelTituloHora.setObjectName("LabelTituloHora")
        self.LabelDatodelaHora = QtWidgets.QLabel(Resultados)
        self.LabelDatodelaHora.setGeometry(QtCore.QRect(1360, 340, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LabelDatodelaHora.setFont(font)
        self.LabelDatodelaHora.setObjectName("LabelDatodelaHora")
        self.FrameDatosFechayHora = QtWidgets.QFrame(Resultados)
        self.FrameDatosFechayHora.setGeometry(QtCore.QRect(260, 320, 1441, 71))
        self.FrameDatosFechayHora.setStyleSheet(" border: 3px solid black;\n"
"    border-radius: 5px;\n"
"background-color:  rgb(255, 170, 0);\n"
"")
        self.FrameDatosFechayHora.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameDatosFechayHora.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameDatosFechayHora.setObjectName("FrameDatosFechayHora")
        self.FrameSustanciasLargo = QtWidgets.QFrame(Resultados)
        self.FrameSustanciasLargo.setGeometry(QtCore.QRect(260, 380, 1441, 91))
        self.FrameSustanciasLargo.setStyleSheet(" border: 3px solid black;\n"
"    border-radius: 5px;\n"
"\n"
"Qlabel{\n"
"None\n"
"}")
        self.FrameSustanciasLargo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameSustanciasLargo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameSustanciasLargo.setObjectName("FrameSustanciasLargo")
        self.FrameListaSustanciasCorto = QtWidgets.QFrame(self.FrameSustanciasLargo)
        self.FrameListaSustanciasCorto.setGeometry(QtCore.QRect(0, -11, 481, 111))
        self.FrameListaSustanciasCorto.setStyleSheet("QFrame {\n"
"    border: 3px solid black;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"Qlabel{\n"
"None\n"
"}")
        self.FrameListaSustanciasCorto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameListaSustanciasCorto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameListaSustanciasCorto.setObjectName("FrameListaSustanciasCorto")
        self.label = QtWidgets.QLabel(Resultados)
        self.label.setGeometry(QtCore.QRect(300, 420, 421, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Resultados)
        self.frame.setGeometry(QtCore.QRect(259, 459, 1441, 91))
        self.frame.setStyleSheet("QFrame {\n"
"    border: 3px solid black;\n"
"   \n"
"border-top: none;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 481, 80))
        self.frame_2.setStyleSheet("QFrame {\n"
"border: 3px solid black;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.labelPuntajeXSustanciaTitulo = QtWidgets.QLabel(Resultados)
        self.labelPuntajeXSustanciaTitulo.setGeometry(QtCore.QRect(270, 490, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPuntajeXSustanciaTitulo.setFont(font)
        self.labelPuntajeXSustanciaTitulo.setObjectName("labelPuntajeXSustanciaTitulo")
        self.frame_3 = QtWidgets.QFrame(Resultados)
        self.frame_3.setGeometry(QtCore.QRect(260, 550, 1441, 80))
        self.frame_3.setStyleSheet("QFrame {\n"
"    border: 3px solid black;\n"
"   \n"
"border-top: none;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(-1, 0, 481, 80))
        self.frame_5.setStyleSheet("QFrame {\n"
"border: 3px solid black;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.LabelRiesgoTitulo = QtWidgets.QLabel(Resultados)
        self.LabelRiesgoTitulo.setGeometry(QtCore.QRect(320, 560, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelRiesgoTitulo.setFont(font)
        self.LabelRiesgoTitulo.setObjectName("LabelRiesgoTitulo")
        self.frame_6 = QtWidgets.QFrame(Resultados)
        self.frame_6.setGeometry(QtCore.QRect(260, 630, 1441, 80))
        self.frame_6.setStyleSheet("QFrame {\n"
"    border: 3px solid black;\n"
"   \n"
"border-top: none;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 481, 80))
        self.frame_7.setStyleSheet("QFrame {\n"
"border: 3px solid black;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.LabelIntervencionTitulo = QtWidgets.QLabel(Resultados)
        self.LabelIntervencionTitulo.setGeometry(QtCore.QRect(290, 650, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelIntervencionTitulo.setFont(font)
        self.LabelIntervencionTitulo.setObjectName("LabelIntervencionTitulo")
        self.frame_8 = QtWidgets.QFrame(Resultados)
        self.frame_8.setGeometry(QtCore.QRect(260, 710, 1441, 80))
        self.frame_8.setStyleSheet("QFrame {\n"
"    border: 3px solid black;\n"
"   \n"
"border-top: none;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 481, 80))
        self.frame_9.setStyleSheet("QFrame {\n"
"border: 3px solid black;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.labelResultadoTotalTitulo = QtWidgets.QLabel(Resultados)
        self.labelResultadoTotalTitulo.setGeometry(QtCore.QRect(350, 730, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResultadoTotalTitulo.setFont(font)
        self.labelResultadoTotalTitulo.setObjectName("labelResultadoTotalTitulo")
        self.label_2 = QtWidgets.QLabel(Resultados)
        self.label_2.setGeometry(QtCore.QRect(760, 400, 921, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.LabelListaPuntajes = QtWidgets.QLabel(Resultados)
        self.LabelListaPuntajes.setGeometry(QtCore.QRect(760, 480, 921, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelListaPuntajes.setFont(font)
        self.LabelListaPuntajes.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelListaPuntajes.setObjectName("LabelListaPuntajes")
        self.LabelNiveldeRiego = QtWidgets.QLabel(Resultados)
        self.LabelNiveldeRiego.setGeometry(QtCore.QRect(750, 560, 921, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelNiveldeRiego.setFont(font)
        self.LabelNiveldeRiego.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelNiveldeRiego.setObjectName("LabelNiveldeRiego")
        self.LabelNiveldeIntervencion = QtWidgets.QLabel(Resultados)
        self.LabelNiveldeIntervencion.setGeometry(QtCore.QRect(760, 640, 921, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelNiveldeIntervencion.setFont(font)
        self.LabelNiveldeIntervencion.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelNiveldeIntervencion.setObjectName("LabelNiveldeIntervencion")
        self.LabelResultadoTotal = QtWidgets.QLabel(Resultados)
        self.LabelResultadoTotal.setGeometry(QtCore.QRect(760, 720, 921, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelResultadoTotal.setFont(font)
        self.LabelResultadoTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelResultadoTotal.setObjectName("LabelResultadoTotal")
        self.pushButton = QtWidgets.QPushButton(Resultados)
        self.pushButton.setGeometry(QtCore.QRect(1580, 950, 251, 41))
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
        self.pushButton.clicked.connect(self.guardar_resultado)

        self.FrameSustanciasLargo.raise_()
        self.FrameDatosFechayHora.raise_()
        self.BannerLabel.raise_()
        self.LabelResumendelaEntrevista.raise_()
        self.LabelTituloFecha.raise_()
        self.LabelDatodelaFecha.raise_()
        self.LabelTituloHora.raise_()
        self.LabelDatodelaHora.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.labelPuntajeXSustanciaTitulo.raise_()
        self.frame_3.raise_()
        self.LabelRiesgoTitulo.raise_()
        self.frame_6.raise_()
        self.LabelIntervencionTitulo.raise_()
        self.frame_8.raise_()
        self.labelResultadoTotalTitulo.raise_()
        self.label_2.raise_()
        self.LabelListaPuntajes.raise_()
        self.LabelNiveldeRiego.raise_()
        self.LabelNiveldeIntervencion.raise_()
        self.LabelResultadoTotal.raise_()
        self.pushButton.raise_()

        QtCore.QMetaObject.connectSlotsByName(Resultados)

        _translate = QtCore.QCoreApplication.translate
        Resultados.setWindowTitle(_translate("Resultados", "Pregunta2"))
        self.LabelResumendelaEntrevista.setText(_translate("Resultados", "RESUMEN DE LA ENTREVISTA"))
        self.LabelTituloFecha.setText(_translate("Resultados", "Fecha de la entrevista: "))
        self.LabelDatodelaFecha.setText(_translate("Resultados", f"{self.fecha_actual}"))
        self.LabelTituloHora.setText(_translate("Resultados", "Hora de la entrevista: "))
        self.LabelDatodelaHora.setText(_translate("Resultados", f"{self.hora_actual}"))
        self.label.setText(_translate("Resultados", "Sustancias consumidas por el paciente"))
        self.labelPuntajeXSustanciaTitulo.setText(_translate("Resultados", "Puntaje segun la prueba para cada sustancia"))
        self.LabelRiesgoTitulo.setText(_translate("Resultados", "Nivel de riesgo para cada sustancia"))
        self.LabelIntervencionTitulo.setText(_translate("Resultados", "Nivel de intervension para cada sustancia"))
        self.labelResultadoTotalTitulo.setText(_translate("Resultados", "Resultado total de la prueba"))
        self.label_2.setText(_translate("Resultados", f"{self.Lista_sustancias_Escogidas}"))
        self.LabelListaPuntajes.setText(_translate("Resultados", f"{self.puntajes_recibidos}"))
        self.LabelNiveldeRiego.setText(_translate("Resultados", "Bajo,Medio,Alto,Medio"))
        self.LabelNiveldeIntervencion.setText(_translate("Resultados", "Sin intervencion, Intervemcion Breve, Tratamiento intensivo, Sin intervension"))
        self.LabelResultadoTotal.setText(_translate("Resultados", f"{sum(self.puntajes_recibidos)}"))
        self.pushButton.setText(_translate("Resultados", "FINALIZAR PRUEBA"))

    def guardar_resultado(self):
        sentencia_agregar_resultado = f"INSERT INTO resultados (sustancias,puntuacion_por_sustancia,puntuacion_total) values (ROW '{self.Lista_sustancias_Escogidas}', ROW {self.puntajes_recibidos},{sum(self.puntajes_recibidos)}')"
        cur.execute(sentencia_agregar_resultado)
        conn.commit()



