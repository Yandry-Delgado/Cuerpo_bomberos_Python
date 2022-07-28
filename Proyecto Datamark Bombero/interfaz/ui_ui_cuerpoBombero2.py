# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cuerpoBomberosHWiOJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1325, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(132)
        sizePolicy.setVerticalStretch(64)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"background: #FEFEFE; font-size: 14px; font-weight: bold; font-family: Roboto;\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionPrueba = QAction(MainWindow)
        self.actionPrueba.setObjectName(u"actionPrueba")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"padding:0px;")
        self.framePert = QFrame(self.centralwidget)
        self.framePert.setObjectName(u"framePert")
        self.framePert.setGeometry(QRect(0, 0, 1341, 821))
        self.framePert.setFrameShape(QFrame.StyledPanel)
        self.framePert.setFrameShadow(QFrame.Raised)
        self.lblFondo = QLabel(self.framePert)
        self.lblFondo.setObjectName(u"lblFondo")
        self.lblFondo.setGeometry(QRect(-100, 10, 1501, 1100))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.lblFondo.setFont(font)
        self.lblFondo.setStyleSheet(u"background-image: url(\"img/FONDO.png\");")
        self.tabla = QTableWidget(self.framePert)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(10, 250, 651, 341))
        self.tabla.setStyleSheet(u"font-size: 16px; font-weight: bold; font-family: Kameron;\n"
"color: rgb(0,0,0);\n"
"background: rgba(255, 255,255,0.6);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")")
        self.tabla.horizontalHeader().setVisible(True)
        self.tabla.horizontalHeader().setDefaultSectionSize(56)
        self.tabla.verticalHeader().setVisible(False)
        self.btnAceptar = QPushButton(self.framePert)
        self.btnAceptar.setObjectName(u"btnAceptar")
        self.btnAceptar.setGeometry(QRect(540, 180, 131, 41))
        self.btnAceptar.setStyleSheet(u"font-size: 18px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgb(250,250,250);\n"
"border-radius: 10px;\n"
"")
        self.cmbAnio = QComboBox(self.framePert)
        self.cmbAnio.setObjectName(u"cmbAnio")
        self.cmbAnio.setEnabled(True)
        self.cmbAnio.setGeometry(QRect(290, 120, 101, 41))
        self.cmbAnio.setStyleSheet(u"font-size: 18px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgb(250,250,250);\n"
"")
        self.cmbMes = QComboBox(self.framePert)
        self.cmbMes.setObjectName(u"cmbMes")
        self.cmbMes.setGeometry(QRect(90, 120, 61, 41))
        self.cmbMes.setStyleSheet(u"font-size: 18px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgb(250,250,250);\n"
"")
        self.jLabel1 = QLabel(self.framePert)
        self.jLabel1.setObjectName(u"jLabel1")
        self.jLabel1.setGeometry(QRect(510, 20, 411, 51))
        self.jLabel1.setFont(font)
        self.jLabel1.setToolTipDuration(0)
        self.jLabel1.setStyleSheet(u"\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"font-size: 18px; ")
        self.lblAo = QLabel(self.framePert)
        self.lblAo.setObjectName(u"lblAo")
        self.lblAo.setGeometry(QRect(230, 120, 51, 40))
        self.lblAo.setStyleSheet(u"\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"font-size: 18px; ")
        self.lblMes = QLabel(self.framePert)
        self.lblMes.setObjectName(u"lblMes")
        self.lblMes.setGeometry(QRect(20, 120, 51, 31))
        self.lblMes.setStyleSheet(u"\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"font-size: 18px; ")
        self.txtProducto = QLineEdit(self.framePert)
        self.txtProducto.setObjectName(u"txtProducto")
        self.txtProducto.setGeometry(QRect(110, 180, 421, 41))
        font1 = QFont()
        font1.setFamily(u"Kameron")
        font1.setBold(True)
        font1.setWeight(75)
        self.txtProducto.setFont(font1)
        self.txtProducto.setStyleSheet(u"\n"
"font-size: 18px; font-weight: bold; font-family: Kameron;")
        self.lblFiltros = QLabel(self.framePert)
        self.lblFiltros.setObjectName(u"lblFiltros")
        self.lblFiltros.setGeometry(QRect(20, 70, 81, 31))
        self.lblFiltros.setStyleSheet(u"\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"font-size: 18px; ")
        self.lblDireccion = QLabel(self.framePert)
        self.lblDireccion.setObjectName(u"lblDireccion")
        self.lblDireccion.setGeometry(QRect(10, 180, 101, 31))
        self.lblDireccion.setStyleSheet(u"\n"
"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"font-size: 18px; ")
        self.frame_3 = QFrame(self.framePert)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(690, 160, 621, 451))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"border: none;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.grafica_dos_2 = QVBoxLayout()
        self.grafica_dos_2.setObjectName(u"grafica_dos_2")

        self.verticalLayout_4.addLayout(self.grafica_dos_2)

        self.verticalLayout_4.setStretch(1, 5)
        self.lblFondo.raise_()
        self.btnAceptar.raise_()
        self.cmbAnio.raise_()
        self.cmbMes.raise_()
        self.jLabel1.raise_()
        self.lblAo.raise_()
        self.lblFiltros.raise_()
        self.lblDireccion.raise_()
        self.txtProducto.raise_()
        self.lblMes.raise_()
        self.tabla.raise_()
        self.frame_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NIVEL DE INCIDENCIAS POR ESTACI\u00d3N", None))
        self.actionPrueba.setText(QCoreApplication.translate("MainWindow", u"Prueba", None))
        self.lblFondo.setText("")
        self.btnAceptar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.jLabel1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nivel de incidencias por estaci\u00f3n</span></p></body></html>", None))
        self.lblAo.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o:", None))
        self.lblMes.setText(QCoreApplication.translate("MainWindow", u"Mes:", None))
#if QT_CONFIG(tooltip)
        self.txtProducto.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Kameron'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txtProducto.setText("")
        self.lblFiltros.setText(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.lblDireccion.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nivel de incidencias", None))
    # retranslateUi

