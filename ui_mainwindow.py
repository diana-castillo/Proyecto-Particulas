# -*- coding: utf-8 -*-


################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(527, 558)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.actionRecorrido_Profundidad_Amplitud = QAction(MainWindow)
        self.actionRecorrido_Profundidad_Amplitud.setObjectName(u"actionRecorrido_Profundidad_Amplitud")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.actionKruskal = QAction(MainWindow)
        self.actionKruskal.setObjectName(u"actionKruskal")
        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName(u"actionDijkstra")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")


        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)


        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")


        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)


        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")


        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)


        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)


        self.gridLayout.addWidget(self.origen_y_spinBox, 2, 2, 1, 1)


        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)


        self.gridLayout.addWidget(self.destino_x_spinBox, 3, 2, 1, 1)


        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")


        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)


        self.ordenar_distancia_pushButton = QPushButton(self.groupBox)
        self.ordenar_distancia_pushButton.setObjectName(u"ordenar_distancia_pushButton")


        self.gridLayout.addWidget(self.ordenar_distancia_pushButton, 13, 0, 1, 3)


        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)


        self.gridLayout.addWidget(self.origen_x_spinBox, 1, 2, 1, 1)


        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)


        self.gridLayout.addWidget(self.green_spinBox, 8, 2, 1, 1)


        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")


        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)


        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")


        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 2)


        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)


        self.gridLayout.addWidget(self.destino_y_spinBox, 4, 2, 1, 1)


        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")


        self.gridLayout.addWidget(self.agregar_final_pushButton, 10, 0, 1, 3)


        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")


        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)


        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")


        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 2)


        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")


        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)


        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")


        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 11, 0, 1, 3)


        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")


        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)


        self.gridLayout.addWidget(self.blue_spinBox, 9, 2, 1, 1)


        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMinimum(0)
        self.red_spinBox.setMaximum(255)


        self.gridLayout.addWidget(self.red_spinBox, 7, 2, 1, 1)


        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")


        self.gridLayout.addWidget(self.mostrar_pushButton, 15, 0, 1, 3)


        self.ordenar_id_pushButton = QPushButton(self.groupBox)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")


        self.gridLayout.addWidget(self.ordenar_id_pushButton, 12, 0, 1, 3)


        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")


        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)


        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")


        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 2, 1, 1)


        self.ordenar_velocidad_pushButton = QPushButton(self.groupBox)
        self.ordenar_velocidad_pushButton.setObjectName(u"ordenar_velocidad_pushButton")


        self.gridLayout.addWidget(self.ordenar_velocidad_pushButton, 14, 0, 1, 3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")


        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)


        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")


        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)


        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")


        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)


        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")


        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)


        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")


        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)


        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_5)
        self.graphicsView.setObjectName(u"graphicsView")


        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)


        self.dibujar = QPushButton(self.tab_5)
        self.dibujar.setObjectName(u"dibujar")


        self.gridLayout_5.addWidget(self.dibujar, 1, 0, 1, 1)


        self.limpiar = QPushButton(self.tab_5)
        self.limpiar.setObjectName(u"limpiar")


        self.gridLayout_5.addWidget(self.limpiar, 1, 1, 1, 1)


        self.tabWidget.addTab(self.tab_5, "")


        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 527, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuVer.addAction(self.actionGrafo)
        self.menuAlgoritmos.addAction(self.actionRecorrido_Profundidad_Amplitud)
        self.menuAlgoritmos.addAction(self.actionPrim)
        self.menuAlgoritmos.addAction(self.actionKruskal)
        self.menuAlgoritmos.addAction(self.actionDijkstra)


        self.retranslateUi(MainWindow)


        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecorrido_Profundidad_Amplitud.setText(QCoreApplication.translate("MainWindow", u"Recorrido Profundidad/Amplitud", None))
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.actionKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.actionDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por id", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (rgb):", None))
        self.ordenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de la part\u00edcula", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Gr\u00e1ficos", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi
