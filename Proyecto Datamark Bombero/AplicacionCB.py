from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import os
from PyQt5.Qt import QApplication,  QStyleFactory, QTableWidgetItem
import sys
import MethPrincipal

from interfaz.ui_ui_cuerpoBombero2 import Ui_MainWindow



class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventanaPert = MethPrincipal.MethPrincipal(self.ui)
        
      
    
    def resolver_ruta(self, ruta_relativa):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, ruta_relativa)
        return os.path.join(os.path.abspath('.'), ruta_relativa)

    def rutaParaCSS(self,rutaFondo):
        nuevaRutaiM = ""
        for iRu in range(0, len(rutaFondo), 1):
            if ord(rutaFondo[iRu]) == 92:
                nuevaRutaiM += str("/")
            else:
                nuevaRutaiM += rutaFondo[iRu]
        return nuevaRutaiM

 


# Inicia la aplicación
if __name__ == '__main__':
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    mi_App = VentanaPrincipal()
    #Definir icono ventana
    rutaIcono = mi_App.resolver_ruta("interfaz/img/iconoFiretruck.ico")
    mi_App.setWindowIcon(QIcon(rutaIcono))
    #Fondo Frame Pert
    rutaFondoIm = mi_App.resolver_ruta("interfaz/img/fondoApp.png")
    nuevaRutaiMagen = mi_App.rutaParaCSS(rutaFondoIm)
    mi_App.ui.lblFondo.setStyleSheet("background-image: url("+nuevaRutaiMagen+");")

    mi_App.show()
    sys.exit(app.exec_())
