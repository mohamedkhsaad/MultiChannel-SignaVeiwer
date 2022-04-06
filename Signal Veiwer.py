import os
import io
import statistics
from tkinter import filedialog
from turtle import color
from typing import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from fpdf import FPDF
import numpy  as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pyqtgraph as pg
import qdarkstyle


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1399, 782)
        MainWindow.setMinimumSize(QtCore.QSize(1240, 0))
        MainWindow.setSizeIncrement(QtCore.QSize(10, 10))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Signal_Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Signal_Title.setFont(font)
        self.Signal_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Signal_Title.setObjectName("Signal_Title")
        self.verticalLayout_11.addWidget(self.Signal_Title)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.First_Channel_Label = QtWidgets.QLabel(self.centralwidget)
        self.First_Channel_Label.setObjectName("First_Channel_Label")
        self.verticalLayout.addWidget(self.First_Channel_Label)
        self.Second_Channel_Label = QtWidgets.QLabel(self.centralwidget)
        self.Second_Channel_Label.setObjectName("Second_Channel_Label")
        self.verticalLayout.addWidget(self.Second_Channel_Label)
        self.Third_Channel_Label = QtWidgets.QLabel(self.centralwidget)
        self.Third_Channel_Label.setObjectName("Third_Channel_Label")
        self.verticalLayout.addWidget(self.Third_Channel_Label)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem1)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.signal_display = PlotWidget(self.centralwidget)
        self.signal_display.setEnabled(True)
        self.signal_display.setSizeIncrement(QtCore.QSize(0, 0))
        self.signal_display.setMouseTracking(False)
        self.signal_display.setFrameShape(QtWidgets.QFrame.Box)
        self.signal_display.setObjectName("signal_display")
        self.verticalLayout_5.addWidget(self.signal_display)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_15.addLayout(self.horizontalLayout)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.Play_Button = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_Button.setIcon(icon)
        self.Play_Button.setIconSize(QtCore.QSize(25, 28))
        self.Play_Button.setObjectName("Play_Button")
        self.State="play"
        self.horizontalLayout_8.addWidget(self.Play_Button)
        self.Pause_Button = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pause_Button.setIcon(icon1)
        self.Pause_Button.setIconSize(QtCore.QSize(25, 28))
        self.Pause_Button.setObjectName("Pause_Button")
        self.horizontalLayout_8.addWidget(self.Pause_Button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SpeedDown_Label = QtWidgets.QLabel(self.centralwidget)
        self.SpeedDown_Label.setObjectName("SpeedDown_Label")
        self.verticalLayout_2.addWidget(self.SpeedDown_Label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SpeedUp_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SpeedUp_Button.setIconSize(QtCore.QSize(30, 22))
        self.SpeedUp_Button.setObjectName("SpeedUp_Button")
        self.gridLayout_3.addWidget(self.SpeedUp_Button, 1, 0, 1, 1)
        self.SpeedDown_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SpeedDown_Button.setIconSize(QtCore.QSize(30, 22))
        self.SpeedDown_Button.setObjectName("SpeedDown_Button")
        self.gridLayout_3.addWidget(self.SpeedDown_Button, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Spectrogram_Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Spectrogram_Title.setFont(font)
        self.Spectrogram_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Spectrogram_Title.setObjectName("Spectrogram_Title")
        self.verticalLayout_3.addWidget(self.Spectrogram_Title)
        self.Spectrogram_Display = QtWidgets.QGraphicsView(self.centralwidget)
        self.Spectrogram_Display.setObjectName("Spectrogram_Display")
        self.figure=plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_3.addWidget(self.canvas)
        self.axis=self.figure.add_subplot(111)
        self.canvas.draw()
        self.axis.set_xlabel("time (in seconds)")
        self.axis.set_ylabel("frequency (Hz)") 
        spacerItem8 = QtWidgets.QSpacerItem(6, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Spectrogram_Checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Spectrogram_Checkbox.setText("")
        self.Spectrogram_Checkbox.setObjectName("Spectrogram_Checkbox")
        self.horizontalLayout_3.addWidget(self.Spectrogram_Checkbox)
        self.Spectrogram_ShowHide_Label = QtWidgets.QLabel(self.centralwidget)
        self.Spectrogram_ShowHide_Label.setObjectName("Spectrogram_ShowHide_Label")
        self.horizontalLayout_3.addWidget(self.Spectrogram_ShowHide_Label)
        self.Export_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Export_Button.setIconSize(QtCore.QSize(30, 22))
        self.Export_Button.setObjectName("Export_Button")
        self.horizontalLayout_3.addWidget(self.Export_Button)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.Spectrogram_Channel_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Spectrogram_Channel_ComboBox.setObjectName("Spectrogram_Channel_ComboBox")
        self.Spectrogram_Channel_ComboBox.addItem("")
        self.Spectrogram_Channel_ComboBox.addItem("")
        self.Spectrogram_Channel_ComboBox.addItem("")
        self.Spectrogram_Channel_ComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.Spectrogram_Channel_ComboBox)
        self.Spectrogram_Color_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Spectrogram_Color_ComboBox.setObjectName("Spectrogram_Color_ComboBox")
        self.Spectrogram_Color_ComboBox.addItem("")
        self.Spectrogram_Color_ComboBox.addItem("")
        self.Spectrogram_Color_ComboBox.addItem("")
        self.Spectrogram_Color_ComboBox.addItem("")
        self.Spectrogram_Color_ComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.Spectrogram_Color_ComboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Range_Lable = QtWidgets.QLabel(self.centralwidget)
        self.Range_Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Range_Lable.setObjectName("Range_Lable")
        self.verticalLayout_12.addWidget(self.Range_Lable)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Spectrogram_Slider_Min = QtWidgets.QSlider(self.centralwidget)
        self.Spectrogram_Slider_Min.setOrientation(QtCore.Qt.Vertical)
        self.Spectrogram_Slider_Min.setObjectName("Spectrogram_Slider_Min")
        self.verticalLayout_4.addWidget(self.Spectrogram_Slider_Min)
        self.Spectrogram_Slider_Min_Label = QtWidgets.QLabel(self.centralwidget)
        self.Spectrogram_Slider_Min_Label.setObjectName("Spectrogram_Slider_Min_Label")
        self.verticalLayout_4.addWidget(self.Spectrogram_Slider_Min_Label)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Spectrogram_Slider_Max = QtWidgets.QSlider(self.centralwidget)
        self.Spectrogram_Slider_Max.setOrientation(QtCore.Qt.Vertical)
        self.Spectrogram_Slider_Max.setObjectName("Spectrogram_Slider_Max")
        self.verticalLayout_9.addWidget(self.Spectrogram_Slider_Max)
        self.Spectrogram_Slider_Max_Label = QtWidgets.QLabel(self.centralwidget)
        self.Spectrogram_Slider_Max_Label.setObjectName("Spectrogram_Slider_Max_Label")
        self.verticalLayout_9.addWidget(self.Spectrogram_Slider_Max_Label)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        spacerItem10 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Signal_ShowHide_Label = QtWidgets.QLabel(self.centralwidget)
        self.Signal_ShowHide_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Signal_ShowHide_Label.setObjectName("Signal_ShowHide_Label")
        self.horizontalLayout_10.addWidget(self.Signal_ShowHide_Label)
        self.ChooseFile_label = QtWidgets.QLabel(self.centralwidget)
        self.ChooseFile_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ChooseFile_label.setWordWrap(False)
        self.ChooseFile_label.setObjectName("ChooseFile_label")
        self.horizontalLayout_10.addWidget(self.ChooseFile_label)
        self.LineEdit_Label = QtWidgets.QLabel(self.centralwidget)
        self.LineEdit_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LineEdit_Label.setObjectName("LineEdit_Label")
        self.horizontalLayout_10.addWidget(self.LineEdit_Label)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.Signal_Color_Label = QtWidgets.QLabel(self.centralwidget)
        self.Signal_Color_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Signal_Color_Label.setObjectName("Signal_Color_Label")
        self.horizontalLayout_10.addWidget(self.Signal_Color_Label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.First_Channel_Checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.First_Channel_Checkbox.setText("")
        self.First_Channel_Checkbox.setObjectName("First_Channel_Checkbox")
        self.horizontalLayout_5.addWidget(self.First_Channel_Checkbox)
        self.First_Channel_Checkbox_Label = QtWidgets.QLabel(self.centralwidget)
        self.First_Channel_Checkbox_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.First_Channel_Checkbox_Label.setObjectName("First_Channel_Checkbox_Label")
        self.horizontalLayout_5.addWidget(self.First_Channel_Checkbox_Label)
        self.First_Channel_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.First_Channel_Browse.setObjectName("First_Channel_Browse")
        self.horizontalLayout_5.addWidget(self.First_Channel_Browse)
        self.First_Channel_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.First_Channel_lineEdit.setObjectName("First_Channel_lineEdit")
        self.horizontalLayout_5.addWidget(self.First_Channel_lineEdit)
        self.Color_Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Color_Button1.setIconSize(QtCore.QSize(20, 20))
        self.Color_Button1=pg.ColorButton()
        self.Color_Button1.setObjectName("Color_Button1")
        self.horizontalLayout_5.addWidget(self.Color_Button1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Second_Channel_Checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Second_Channel_Checkbox.setText("")
        self.Second_Channel_Checkbox.setObjectName("Second_Channel_Checkbox")
        self.horizontalLayout_6.addWidget(self.Second_Channel_Checkbox)
        self.Second_Channel_Checkbox_Label = QtWidgets.QLabel(self.centralwidget)
        self.Second_Channel_Checkbox_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Second_Channel_Checkbox_Label.setObjectName("Second_Channel_Checkbox_Label")
        self.horizontalLayout_6.addWidget(self.Second_Channel_Checkbox_Label)
        self.Second_Channel_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Second_Channel_Browse.setObjectName("Second_Channel_Browse")
        self.horizontalLayout_6.addWidget(self.Second_Channel_Browse)
        self.Second_Channel_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Second_Channel_lineEdit.setObjectName("Second_Channel_lineEdit")
        self.horizontalLayout_6.addWidget(self.Second_Channel_lineEdit)
        self.Color_Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Color_Button2.setIconSize(QtCore.QSize(20, 20))
        self.Color_Button2=pg.ColorButton()
        self.Color_Button2.setObjectName("Color_Button2")
        self.horizontalLayout_6.addWidget(self.Color_Button2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Third_Channel_Checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Third_Channel_Checkbox.setText("")
        self.Third_Channel_Checkbox.setObjectName("Third_Channel_Checkbox")
        self.horizontalLayout_9.addWidget(self.Third_Channel_Checkbox)
        self.Third_Channel_Checkbox_Label = QtWidgets.QLabel(self.centralwidget)
        self.Third_Channel_Checkbox_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Third_Channel_Checkbox_Label.setObjectName("Third_Channel_Checkbox_Label")
        self.horizontalLayout_9.addWidget(self.Third_Channel_Checkbox_Label)
        self.Third_Channel_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Third_Channel_Browse.setObjectName("Third_Channel_Browse")
        self.horizontalLayout_9.addWidget(self.Third_Channel_Browse)
        self.Third_Channel_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Third_Channel_lineEdit.setObjectName("Third_Channel_lineEdit")
        self.horizontalLayout_9.addWidget(self.Third_Channel_lineEdit)
        self.Color_Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Color_Button3.setIconSize(QtCore.QSize(20, 20))
        self.Color_Button3=pg.ColorButton()
        self.Color_Button3.setObjectName("Color_Button3")
        self.horizontalLayout_9.addWidget(self.Color_Button3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_13)
        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1399, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.Spectrogram_Checkbox.stateChanged.connect(self.Spectogram_hide)
        self.First_Channel_lineEdit.returnPressed.connect(lambda: self.do_action(0))
        self.First_Channel_Checkbox.stateChanged.connect(self.show_hide_signal)
        self.Second_Channel_Checkbox.stateChanged.connect(self.show_hide_signal2)
        self.Third_Channel_Checkbox.stateChanged.connect(self.show_hide_signal3)
        self.Second_Channel_lineEdit.returnPressed.connect(lambda: self.do_action(1))
        self.Third_Channel_lineEdit.returnPressed.connect(lambda: self.do_action(2))
        self.SpeedUp_Button.clicked.connect(self.SpeedUp_Functin)
        self.SpeedDown_Button.clicked.connect(self.SpeedDown_Functin)
        self.Spectrogram_Slider_Min.valueChanged[int].connect(self.Spectrogram_Contrast)
        self.Spectrogram_Slider_Max.valueChanged[int].connect(self.Spectrogram_Contrast)
        
    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Signal_Title.setText(_translate("MainWindow", "Vital Signals"))
        self.First_Channel_Label.setText(_translate("MainWindow", "Channel 1"))
        self.Second_Channel_Label.setText(_translate("MainWindow", "Channel 2"))
        self.Third_Channel_Label.setText(_translate("MainWindow", "Channel 3"))
        self.Play_Button.setText(_translate("MainWindow", "Play"))
        self.Pause_Button.setText(_translate("MainWindow", "Pause"))
        self.SpeedUp_Button.setText(_translate("MainWindow", "Speed UP"))
        self.SpeedDown_Button.setText(_translate("MainWindow", "Speed Down"))
        self.Spectrogram_Title.setText(_translate("MainWindow", "Spectrogram"))
        self.Spectrogram_ShowHide_Label.setText(_translate("MainWindow", "Hide"))
        self.Export_Button.setText(_translate("MainWindow", "Export Data"))
        self.Spectrogram_Channel_ComboBox.setItemText(0, _translate("MainWindow", "Choose Chanel"))
        self.Spectrogram_Channel_ComboBox.setItemText(1, _translate("MainWindow", "Channel 1"))
        self.Spectrogram_Channel_ComboBox.setItemText(2, _translate("MainWindow", "Channel 2"))
        self.Spectrogram_Channel_ComboBox.setItemText(3, _translate("MainWindow", "Channel 3"))
        self.Spectrogram_Color_ComboBox.setItemText(0, _translate("MainWindow", "Choose palette"))
        self.Spectrogram_Color_ComboBox.setItemText(1, _translate("MainWindow", "viridis"))
        self.Spectrogram_Color_ComboBox.setItemText(2, _translate("MainWindow", "plasma"))
        self.Spectrogram_Color_ComboBox.setItemText(3, _translate("MainWindow", "inferno"))
        self.Spectrogram_Color_ComboBox.setItemText(4, _translate("MainWindow", "magma"))
        self.Range_Lable.setText(_translate("MainWindow", "Range"))
        self.Spectrogram_Slider_Min_Label.setText(_translate("MainWindow", "Min"))
        self.Spectrogram_Slider_Max_Label.setText(_translate("MainWindow", "Max"))
        self.Signal_ShowHide_Label.setText(_translate("MainWindow", "Hide"))
        self.ChooseFile_label.setText(_translate("MainWindow", "Choose"))
        self.LineEdit_Label.setText(_translate("MainWindow", "  Change Signal Name"))
        self.Signal_Color_Label.setText(_translate("MainWindow", "Color"))
        self.First_Channel_Checkbox_Label.setText(_translate("MainWindow", "Channel 1"))
        self.First_Channel_Browse.setText(_translate("MainWindow", "Browse..."))
        self.Color_Button1.setText(_translate("MainWindow", "Color"))
        self.Second_Channel_Checkbox_Label.setText(_translate("MainWindow", "Channel 2"))
        self.Second_Channel_Browse.setText(_translate("MainWindow", "Browse..."))
        self.Color_Button2.setText(_translate("MainWindow", "Color"))
        self.Third_Channel_Checkbox_Label.setText(_translate("MainWindow", "Channel 3"))
        self.Third_Channel_Browse.setText(_translate("MainWindow", "Browse..."))
        self.Color_Button3.setText(_translate("MainWindow", "Color"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.Speed=50
        self.Increment=0
        self.speed=45
        self.Specto_Color='viridis'
        self.xchanel1=[]
        self.xchanel2=[]
        self.xchanel3=[]
        self.ychanel3=[]
        self.ychanel2=[]
        self.ychanel1=[]
        self.First_Channel_Browse.clicked.connect(lambda: self.Browse1(0))
        self.Second_Channel_Browse.clicked.connect(lambda: self.Browse1(1))
        self.Third_Channel_Browse.clicked.connect(lambda: self.Browse1(2))
        self.Color_Button1.sigColorChanged.connect(self.Done_Color1)
        self.Color_Button2.sigColorChanged.connect(self.Done_Color2)
        self.Color_Button3.sigColorChanged.connect(self.Done_Color3)
        self.Play_Button.clicked.connect(lambda: self.Play_Pause_State(0))
        self.Pause_Button.clicked.connect(lambda: self.Play_Pause_State(1))
        self.Export_Button.clicked.connect(lambda: self.Export_To_PDF())
        self.Spectrogram_Channel_ComboBox.currentIndexChanged.connect(lambda: self.Spectogram_show())
        self.Spectrogram_Color_ComboBox.currentTextChanged.connect(lambda: self.Spectogram_Color_show())
        
    def Done_Color1(self):
        self.pencolor1=self.Color_Button1.color('byte')
        print(self.pencolor1)
    def Done_Color2(self):
        self.pencolor2=self.Color_Button2.color('byte')
        print(self.pencolor2)
    def Done_Color3(self):
        self.pencolor3=self.Color_Button3.color('byte')
        print(self.pencolor3)    

    def Browse1(self,input):
        if input ==0:
            fname=QFileDialog.getOpenFileName(self, "Open file", "D:" )
            data = np.loadtxt(fname[0])
            self.xchanel1 = data[:, 0]
            self.ychanel1 = data[:, 1]
            print(self.xchanel1,self.ychanel1)
            self.Add_Plot1()  
        elif input==1:
            fname=QFileDialog.getOpenFileName(self, "Open file", "D:" )
            data = np.loadtxt(fname[0]) 
            self.xchanel2 = data[:, 0]
            self.ychanel2 = data[:, 1]
            print(self.xchanel2,self.ychanel2)
            self.Add_Plot2()
        elif input==2:
            fname=QFileDialog.getOpenFileName(self, "Open file", "D:" )
            data = np.loadtxt(fname[0])
            self.xchanel3 = data[:, 0]
            self.ychanel3 = data[:, 1]
            print(self.xchanel3,self.ychanel3)
            self.Add_Plot3()
        
    def show_hide_signal(self):
        if self.First_Channel_Checkbox.isChecked():
            print("inside")
            self.plotline1.hide()
        else:
            self.plotline1.show()

    def show_hide_signal2(self):
        if self.Second_Channel_Checkbox.isChecked():
            print("inside")
            self.plotline2.hide()
        else:
            self.plotline2.show()

    def show_hide_signal3(self):
        if self.Third_Channel_Checkbox.isChecked():
            print("inside")
            self.plotline3.hide()
        else:
            self.plotline3.show()

    def Spectrogram_Contrast(self):
         print(self.Spectrogram_Slider_Max.value())
         print(self.Spectrogram_Slider_Max.value())
         self.axis.clear()
         self.axis.specgram(self.ychanel1, NFFT=None, Fs=None, Fc=None, detrend=None, window=None, noverlap=None, cmap=self.Specto_Color,vmin=self.Spectrogram_Slider_Min.value()-100,vmax=self.Spectrogram_Slider_Max.value())
         self.canvas.draw()
    

   
    def zoomin(self):
        self.signal_display.setXRange(min=0, max=10, padding=1, update=True)
       
    
    def zoomout(self):
       self.signal_display.setXRange(min=0, max=1000, padding=1, update=True)

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        self.axis.cla()
        x = np.arange(self.current,self.current+10)
        linesData = self.lines[self.current:self.current+10]
        y = [float(line.split(',')[0]) for line in linesData]
        self.axis.plot(x,y, 'r')
        self.current = self.current+10
        self.show()


    def SpeedUp_Functin(self):
        
        self.Speed+=10

        if self.Speed+10>100:
            self.Speed=100

        self.timer1.setInterval(5*(100-self.Speed))
           
    def SpeedDown_Functin(self):
        self.Speed-=10

        if self.Speed-10<0:
            self.Speed=0

        self.timer1.setInterval(5*(100-self.Speed))
        
    def Play_Pause_State(self,input):
        if input==0:
            self.State="play"
            print(self.State)
        else:
            self.State="pause"
            print(self.State)

    def Export_To_PDF(self):
        pdf = FPDF ('P', 'mm', 'Letter')
        pdf.add_page()
        pdf.set_font('helvetica','B',16)
        pdf.cell(40, 10, 'Inistant Report', ln=True,border=False, align='C')
        pdf.ln(20)
        plt.rcParams["figure.figsize"] = [25, 20]
        plt.rcParams["figure.autolayout"] = True
        plt.figure()

        if self.xchanel1.all():
            print("inside")
            for i in range(self.Increment):
                plt.plot(self.xchanel1[:i],self.ychanel1[:i])

  
        if self.xchanel2:
            for i in range(self.Increment):
               plt.plot(self.xchanel2[:i],self.ychanel2[:i])        

      
        if self.xchanel3:
           for i in range(self.Increment):
               plt.plot(self.xchanel3[:i],self.ychanel3[:i])
       

        img_buf = io.BytesIO()
        plt.savefig('output.png', format='png')
        pdf.image('output.png', 50, 40, 100)
        pdf.ln(20)
        


        pdf.output('pdf_trail1.pdf')


    def Spectogram_show(self):
        if self.Spectrogram_Channel_ComboBox.currentIndex()==1:
            self.axis.clear()
            self.axis.specgram(self.ychanel1, NFFT=None, Fs=None, Fc=None, detrend=None, window=None, noverlap=None, cmap=self.Specto_Color)
            self.canvas.draw()
            self.Temp_Spectrogram=self.ychanel1
        elif  self.Spectrogram_Channel_ComboBox.currentIndex()==2:
            self.axis.clear()
            self.axis.specgram(self.ychanel2, NFFT=None, Fs=None, Fc=None, detrend=None, window=None, noverlap=None, cmap=self.Specto_Color)
            self.canvas.draw()
            self.Temp_Spectrogram=self.ychanel2
        elif self.Spectrogram_Channel_ComboBox.currentIndex()==3:
            self.axis.clear()
            self.axis.specgram(self.ychanel3, NFFT=None, Fs=None, Fc=None, detrend=None, window=None, noverlap=None, cmap=self.Specto_Color)
            self.canvas.draw()
            self.Temp_Spectrogram=self.ychanel3


    def Spectogram_Color_show(self):
        self.Specto_Color=self.Spectrogram_Color_ComboBox.currentText()
        print(self.Specto_Color)
        self.Spectogram_show()

   

    def Add_Plot1(self):
        self.plotline1=self.signal_display.plot(self.xchanel1[:self.Increment],self.ychanel1[:self.Increment],pen=self.pencolor1)
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.update1)
        self.timer1.start(50)
        
    def Add_Plot2(self):
            self.plotline2=self.signal_display.plot(self.xchanel2[:self.Increment],self.ychanel2[:self.Increment],pen=self.pencolor2)
            self.timer2 = QtCore.QTimer()
            self.timer2.timeout.connect(self.update2)
            self.timer2.start(50)

    def Add_Plot3(self):
        self.plotline3=self.signal_display.plot(self.xchanel3[:self.Increment],self.ychanel3[:self.Increment],pen=self.pencolor3) 
        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.update3)
        self.timer3.start(50)
    
        

    def Spectogram_show1(self,input):
        self.axis.specgram(self.ychanel1)
        self.canvas.draw()

    def  Spectogram_hide(self):  
        if self.Spectrogram_Checkbox.isChecked():
            print("checked")
            self.ychanel=[0]
            self.axis.clear()
            self.axis.specgram(self.ychanel)
            self.canvas.draw()
        else:
            self.axis.clear()
            self.axis.specgram(self.Temp_Spectrogram)
            self.canvas.draw()
            print("unchecked")   

    def update1(self):
        if self.State=="play":
            self.Increment += 10
            self.signal_display.setLimits(xMin=min(self.xchanel1), xMax=max(self.xchanel1),minXRange=0, maxXRange=100,yMin=min(self.ychanel1), yMax=max(self.ychanel1))
            self.plotline1.setData(self.xchanel1[:self.Increment],self.ychanel1[:self.Increment]) 
            self.signal_display.setAutoPan(x=True)

         
    def update2(self):
        if self.State=="play":
            self.Increment += 10
            self.signal_display.setLimits(xMin=min(self.xchanel2), xMax=max(self.xchanel2),minXRange=0, maxXRange=100,yMin=min(self.ychanel2), yMax=max(self.ychanel2))
            self.plotline2.setData(self.xchanel2[:self.Increment],self.ychanel2[:self.Increment])
            self.signal_display.setAutoPan(x=True) 
   
    def update3(self):
        if self.State=="play":
            self.Increment += 10
            self.signal_display.setLimits(xMin=min(self.xchanel3), xMax=max(self.xchanel3),minXRange=0, maxXRange=100,yMin=min(self.ychanel3), yMax=max(self.ychanel3))
            self.plotline3.setData(self.xchanel3[:self.Increment],self.ychanel3[:self.Increment])
            self.signal_display.setAutoPan(x=True) 
        
    def do_action(self,input):
        if input==0:
            value1 = self.First_Channel_lineEdit.text()
            self.First_Channel_Label.setText(value1)
            self.First_Channel_Label.adjustSize()
            self.Spectrogram_Channel_ComboBox.setItemText(1, value1)
            self.First_Channel_Checkbox_Label.setText(value1)
        elif input==1:
            value2 = self.Second_Channel_lineEdit.text()
            self.Second_Channel_Label.setText(value2)
            self.Second_Channel_Label.adjustSize()
            self.Spectrogram_Channel_ComboBox.setItemText(2, value2)
            self.Second_Channel_Checkbox_Label.setText(value2)
        elif input==2:
            value3 = self.Third_Channel_lineEdit.text()
            self.Third_Channel_Label.setText(value3)
            self.Third_Channel_Label.adjustSize()  
            self.Spectrogram_Channel_ComboBox.setItemText(3, value3)
            self.Third_Channel_Checkbox_Label.setText(value3)                              

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())