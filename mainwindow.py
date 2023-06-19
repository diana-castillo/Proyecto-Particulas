from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from adminpartc import AdminPartc
from particula import Particula
from pprint import pprint, pformat
from algoritmos import busquedaProfundidad, busquedaAmplitud, algoritmoPrim, algoritmoKruskal, algoritmoDijkstra


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.adminpartc = AdminPartc()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregarInicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)


        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)


        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)


        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)


        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_velocidad)


        self.ui.actionGrafo.triggered.connect(self.action_ver_grafo)
        self.ui.actionRecorrido_Profundidad_Amplitud.triggered.connect(self.action_recorridos)
        self.ui.actionPrim.triggered.connect(self.action_prim)
        self.ui.actionKruskal.triggered.connect(self.action_kruskal)
        self.ui.actionDijkstra.triggered.connect(self.action_dijkstra)
    
    @Slot()
    def action_dijkstra(self):
        origenX = self.ui.origen_x_spinBox.value()
        origenY = self.ui.origen_y_spinBox.value()
        destinoX = self.ui.destino_x_spinBox.value()
        destinoY = self.ui.destino_y_spinBox.value()
        grafo = self.adminpartc.hacerGrafo(1)


        if (origenX, origenY) and (destinoX, destinoY) in grafo:
            self.limpiar()
            arregloDistancias, arregloCamino, grafoResultante = algoritmoDijkstra(grafo, (origenX, origenY), (destinoX, destinoY))


            res = '\nDistancias:\n' + pformat(arregloDistancias, width=50, indent=1) + '\n'
            res += 'Camino:\n' + pformat(arregloCamino, width=50, indent=1)
            print(res)


            for vertice in grafoResultante:
                adyacentes = grafoResultante.get(vertice)


                for i in range (len(adyacentes)):
                    origenX = vertice[0]
                    origenY = vertice[1]
                    destinoX = adyacentes[i][0]
                    destinoY = adyacentes[i][1]


                    pen = QPen()
                    pen.setWidth(2)
                    r = 255
                    g = 87
                    b = 87
                    color = QColor(r, g, b)
                    pen.setColor(color)


                    self.scene.addEllipse(origenX, origenY, 3, 3, pen)
                    self.scene.addEllipse(destinoX, destinoY, 3, 3, pen)
                    self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)
        else:
            QMessageBox.warning(self, "Atencion", "Valores no encontrados")


    @Slot()
    def action_kruskal(self):
        grafo = self.adminpartc.hacerGrafo(2)
        grafoResultante = algoritmoKruskal(grafo)


        for vertice in grafoResultante:
            adyacentes = grafoResultante.get(vertice)


            for i in range (len(adyacentes)):
                origenX = vertice[0]
                origenY = vertice[1]
                destinoX = adyacentes[i][0][0]
                destinoY = adyacentes[i][0][1]


                pen = QPen()
                pen.setWidth(2)
                r = 255
                g = 87
                b = 87
                color = QColor(r, g, b)
                pen.setColor(color)


                self.scene.addEllipse(origenX, origenY, 3, 3, pen)
                self.scene.addEllipse(destinoX, destinoY, 3, 3, pen)
                self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)
    
    @Slot()
    def action_prim(self):
        origenX = self.ui.origen_x_spinBox.value()
        origenY = self.ui.origen_y_spinBox.value()
        grafo = self.adminpartc.hacerGrafo(1)


        if (origenX, origenY) in grafo:
            grafoResultante = algoritmoPrim(grafo, (origenX, origenY))
            resultado = "\nPrim\nOrigen:" + str((origenX, origenY)) + "\n"
            resultado += pformat(grafoResultante, width=95, indent=1)
            print(resultado)


            for vertice in grafoResultante:
                adyacentes = grafoResultante.get(vertice)


                for i in range (len(adyacentes)):
                    origenX = vertice[0]
                    origenY = vertice[1]
                    destinoX = adyacentes[i][0][0]
                    destinoY = adyacentes[i][0][1]


                    pen = QPen()
                    pen.setWidth(2)
                    r = 255
                    g = 87
                    b = 87
                    color = QColor(r, g, b)
                    pen.setColor(color)


                    self.scene.addEllipse(origenX, origenY, 3, 3, pen)
                    self.scene.addEllipse(destinoX, destinoY, 3, 3, pen)
                    self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)
        else:
            QMessageBox.warning(self, "Atencion", "Valores no encontrados")
    
    @Slot()
    def action_recorridos(self):
        origenX = self.ui.origen_x_spinBox.value()
        origenY = self.ui.origen_y_spinBox.value()
        grafo = self.adminpartc.hacerGrafo(1)


        if (origenX, origenY) in grafo:
            recorrido = busquedaProfundidad(grafo, (origenX, origenY))
            resultado = "\nOrigen:" + str((origenX, origenY)) + '\n' + "Profundidad\n"
            for vertice in recorrido:
                resultado += str(vertice) + '\n'
            
            recorrido2 = busquedaAmplitud(grafo, (origenX, origenY))
            resultado += "\nAmplitud\n"
            for vertice in recorrido2:
                resultado += str(vertice) + '\n'
            
            print(resultado)
            self.ui.salida.insertPlainText('\n' + resultado)
        
        else:
            QMessageBox.warning(self, "Atencion", "Valores no encontrados")


    @Slot()
    def action_ver_grafo(self):
        self.ui.salida.clear()
        grafo = self.adminpartc.hacerGrafo(1)
        str = pformat(grafo, width=95, indent=1)
        print(str)
        self.ui.salida.insertPlainText(str)


    @Slot()
    def ordenar_id(self):
        self.adminpartc.sort(1)
    
    @Slot()
    def ordenar_distancia(self):
        self.adminpartc.sort(2)
    
    @Slot()
    def ordenar_velocidad(self):
        self.adminpartc.sort(3)
    
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)


        for particula in self.adminpartc:
            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor(r, g, b)
            pen.setColor(color)


            origenX = particula.origenX
            origenY = particula.origenY
            destinoX = particula.destinoX
            destinoY = particula.destinoY


            self.scene.addEllipse(origenX, origenY, 3, 3, pen)
            self.scene.addEllipse(destinoX, destinoY, 3, 3, pen)
            self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)


    @Slot()
    def limpiar(self):
        self.scene.clear()
    
    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()


        encontrado = False
        for particula in self.adminpartc:
            if id == str(particula.id):
                self.ui.tabla.clear()


                self.ui.tabla.setColumnCount(10)
                headers = ["Id", "Origen en x", "Origen en y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                
                self.ui.tabla.setRowCount(1)


                id_widget = QTableWidgetItem(str(particula.id))
                origenX_widget = QTableWidgetItem(str(particula.origenX))
                origenY_widget = QTableWidgetItem(str(particula.origenY))
                destinoX_widget = QTableWidgetItem(str(particula.destinoX))
                destinoY_widget = QTableWidgetItem(str(particula.destinoY))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))


                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenX_widget)
                self.ui.tabla.setItem(0, 2, origenY_widget)
                self.ui.tabla.setItem(0, 3, destinoX_widget)
                self.ui.tabla.setItem(0, 4, destinoY_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)


                encontrado = True
                return
        
        if not encontrado:
            QMessageBox.warning(self, "Atencion", f'La particula con el id "{id}" no fue encontrada')


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen en x", "Origen en y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)


        self.ui.tabla.setRowCount(len(self.adminpartc))


        row = 0
        for particula in self.adminpartc:
            id_widget = QTableWidgetItem(str(particula.id))
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))


            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origenX_widget)
            self.ui.tabla.setItem(row, 2, origenY_widget)
            self.ui.tabla.setItem(row, 3, destinoX_widget)
            self.ui.tabla.setItem(row, 4, destinoY_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)


            row += 1


    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir Archivo', '.', 'JSON (*.json)')[0]
        if self.adminpartc.abrir(ubicacion):
            QMessageBox.information(self, "Exito", "Se abrió el archivo " + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "Error al abrir el archivo " + ubicacion)
    
    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.', 'JSON (*.json)')[0]
        print(ubicacion)
        if self.adminpartc.guardar(ubicacion):
            QMessageBox.information(self, "Exito", "Se pudo crear el archivo " + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el archivo" + ubicacion)


    @Slot()
    def click_mostrar(self):
        #self.adminpartc.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.adminpartc))


    @Slot()
    def click_agregar(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.origen_x_spinBox.value()
        origenY = self.ui.origen_y_spinBox.value()
        destinoX = self.ui.destino_x_spinBox.value()
        destinoY = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()


        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.adminpartc.agregarFinal(particula)


    @Slot()
    def click_agregarInicio(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.origen_x_spinBox.value()
        origenY = self.ui.origen_y_spinBox.value()
        destinoX = self.ui.destino_x_spinBox.value()
        destinoY = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()


        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.adminpartc.agregarInicio(particula)