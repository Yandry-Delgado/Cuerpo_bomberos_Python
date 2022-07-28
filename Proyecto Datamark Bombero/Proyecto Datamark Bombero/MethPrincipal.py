

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import  QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import QBrush
from PyQt5.Qt import QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.artist import Artist
import mysql.connector
from mysql.connector import Error



class MethPrincipal(QMainWindow):
    
    def __init__(self,ui):
        super(MethPrincipal, self).__init__()
        self.ui = ui 
        self.asignarComponentes()
        self.eventosDeBotones()
        self.grafica1 = None
    
    def asignarComponentes(self):
        # Combo box lista desplegables
        self.comboAnio = QtWidgets.QComboBox
        self.comboAnio = self.ui.cmbAnio
        self.comboMes = QtWidgets.QComboBox
        self.comboMes = self.ui.cmbMes
        # LLenar cmb 
        objMes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        self.comboMes.addItems(objMes) 
        objAnio = ["2021", "2022"]
        self.comboAnio.addItems(objAnio)   
        # Botones
        self.botonAceptar = QtWidgets.QPushButton
        self.botonAceptar = self.ui.btnAceptar
        # Campos de texto
        self.textFieldDir = QtWidgets.QLineEdit
        self.textFieldDir = self.ui.txtProducto
        # Tablas
        self.tablaPri = QtWidgets.QTableWidget
        self.tablaPri = self.ui.tabla
        # Grafico
        self.graficoCircular = self.ui.grafica_dos_2
       
    def eventosDeBotones(self):
        self.botonAceptar.clicked.connect(self.cargarProceso)
       
    def cargarProceso(self):
        self.tablaPri.clear()
        self.consultar()
        
    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host='localhost', 
                port='3306',
                user='root',
                password='mysql123',     
                database='datamart_bombero'
            )

            if conexion.is_connected():
                print("Conexion exitosa a la Base de datos")
            

        except Error as ex:
            print("Error durante la conexion a la base de datos ", ex)
       
        return conexion
  

    def consultar(self):
        direccionSelec = self.textFieldDir.text()
        anioSelec = str(self.comboAnio.currentText())
        mesSelec = str(self.comboMes.currentText())
        sql=""
        if not self.textFieldDir.text():
            sql = ("select dim_tiempo.año, dim_tiempo.mes, dim_emergencias.descripcion, dim_estacion.direccion, count(hecho_incidencias.hecho) AS hecho\n" +
            "from hecho_incidencias\n" +
            "inner join dim_emergencias on dim_emergencias.id = hecho_incidencias.dim_emergencias_id\n" +
            "inner join dim_estacion on dim_estacion.id = hecho_incidencias.dim_estacion_id\n" +
            "inner join dim_tiempo on dim_tiempo.fecha = hecho_incidencias.dim_tiempo_fecha\n" +
            "where dim_tiempo.mes = '" + mesSelec + "'" +
            "and dim_tiempo.año =  '" + anioSelec+ "'" + 
            "group by dim_emergencias.descripcion")
        else:
           
            sql = ("select dim_tiempo.año, dim_tiempo.mes, dim_emergencias.descripcion, dim_estacion.direccion, count(hecho_incidencias.hecho) AS hecho\n" +
            "from hecho_incidencias\n" +
            "inner join dim_emergencias on dim_emergencias.id = hecho_incidencias.dim_emergencias_id\n" +
            "inner join dim_estacion on dim_estacion.id = hecho_incidencias.dim_estacion_id\n" +
            "inner join dim_tiempo on dim_tiempo.fecha = hecho_incidencias.dim_tiempo_fecha\n" +
            "where dim_tiempo.mes = '" + mesSelec + "'" +
            "and dim_tiempo.año =  '" + anioSelec+ "'" + 
                            "and dim_estacion.direccion like '%" + direccionSelec + "%'" +
            "group by dim_emergencias.descripcion")
        
        #conectar con la BD
        conexion = self.conectar()
        self.cursor = conexion.cursor()
        self.cursor.execute(sql)
        self.resultados =self.cursor.fetchall()
     
        # numero de filas
        self.numeroFilas =self.cursor.rowcount
        self.tablaPri.setRowCount(self.numeroFilas)
    
         # numero de columnas
        self.tablaPri.setColumnCount(5)
        # ponemos los titulos de la columna
        self.listColumnas = [" Año", " Mes", "Descripcion", " Direccion","Hecho"]
        # insertar columnas
        for i in range(5):
            item = QTableWidgetItem(self.listColumnas[i])
            item.setBackground(QtGui.QColor(21, 30, 61))
            item.setForeground(QBrush(QColor(255, 223, 0)))
            self.tablaPri.setHorizontalHeaderItem(i, item)
         # insertat celdas    
        for j in range(self.numeroFilas):
            for k in range(5):
               item = QTableWidgetItem(str(self.resultados[j][k]))
               self.tablaPri.setItem(j, k, item)

        self.tablaPri.resizeColumnsToContents()
        self.graficar(self.resultados)


    def graficar(self,resultados):
      
        #Graficos
        if self.grafica1 is not None: 
            # widget will be None if the item is a layout
            self.grafica1.deleteLater()
        self.grafica1 = Canvas_grafica2(resultados) 
        self.graficoCircular.addWidget(self.grafica1)



class Canvas_grafica2(FigureCanvas): 
    def __init__(self, descripcion):     
        self.descripciones= descripcion
 
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
         
        nombres = [] 
        colores = []
        tamaño = []
        explotar=[]
        sumHechos=0

        for fila in range(len(self.descripciones)):
            sumHechos+=int(self.descripciones[fila][4])

        for fila in range(len(self.descripciones)):
            desc=str(self.descripciones[fila][2])
            nombres.append(desc)
            calculoPorce = int(self.descripciones[fila][4])*100/sumHechos
            tamaño.append(calculoPorce)
            explotar = [0.05]*len(self.descripciones) 
            
            if desc == "ACCIDENTE DE TRANSITO":
                colores.append('blue')
            elif  desc == "MATERIALES PELIGROSOS":
                colores.append('beige')
            elif  desc == "INCENDIO":
                colores.append('aquamarine')
            elif  desc == "Inundaciones":
                colores.append('azure')
            elif  desc == "CONATO DE INCENDIO":
                colores.append('red')
            elif  desc == "ASISTENCIAS PRE-HOSPITALARIA":
                colores.append('bisque')
            elif  desc == "Conflictos":
                colores.append('yellow')
            elif  desc =="Terremotos":
                colores.append('blanchedalmond')
            elif  desc == "Deslaves":
                colores.append('blue')
            elif  desc == "Inundaciones":
                colores.append('blueviolet')
            elif  desc == "Emisiones nucleares":
                colores.append('brown')
            elif desc == "Tormentas":
                colores.append('burlywood')
            elif desc == "Tsunami":
                colores.append('cadetblue')
            elif desc == "Plagas":
                colores.append('linen')
            elif desc == "Simulacro":
                colores.append('salmon')
            elif desc == "búsqueda y rescate":
                colores.append('orange')
            elif desc == "lavar calzadas":
                colores.append('gold')
            elif desc == "abrir vivienda o vehiculos":
                colores.append('cyan')
            elif desc == "labor social":
                colores.append('purple')
            elif desc == "fuga de gas":
                colores.append('magenta')
            else:
                colores.append('green')

        self.ax.pie(tamaño, explode = explotar, labels = nombres, 
            colors = colores,
                autopct = '%1.0f%%', pctdistance = 0.6,
                shadow=True, startangle=90, radius = 0.8, 
                labeldistance=1.1)  
        self.ax.axis('equal')
        print("Datos graficados correctamente")
        
        
        



