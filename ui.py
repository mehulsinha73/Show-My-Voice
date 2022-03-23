from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 664)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Background area for config ui
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("QGroupBox {\n"
                                        "    background-color: rgb(114, 199, 224);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel {\n"
                                        "    color: black;\n"
                                        "}")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        # audio device text
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        # audio device selector drop down
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 20)

        # window length text
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        # input box for window length - default 1000
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        # update interval text
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 4, 1, 1)

        # input box for update interval - default 30
        self.spinBox_updateInterval = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_updateInterval.setMinimum(1)
        self.spinBox_updateInterval.setMaximum(100)
        self.spinBox_updateInterval.setProperty("value", 30)
        self.spinBox_updateInterval.setObjectName("spinBox_updateInterval")
        self.gridLayout_2.addWidget(self.spinBox_updateInterval, 1, 6, 1, 1)

        # yrange max text
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 10, 1, 1)

        # input box for yrange max - default +0.5
        self.doubleSpinBox_yrangemax = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_yrangemax.setDecimals(1)
        self.doubleSpinBox_yrangemax.setMaximum(1.0)
        self.doubleSpinBox_yrangemax.setSingleStep(0.1)
        self.doubleSpinBox_yrangemax.setProperty("value", 0.5)
        self.doubleSpinBox_yrangemax.setObjectName("doubleSpinBox_yrangemax")
        self.gridLayout_2.addWidget(self.doubleSpinBox_yrangemax, 1, 13, 1, 2)

        # Start button
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setStyleSheet("#pushButton {\n"
                                        "    background-color: rgb(63, 166, 61);\n"
                                        "    color: white;\n"
                                        "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 17, 1, 4)

        # sampling rate text
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        #input box for sampling rate - default 44100
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        # Down sample text
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 4, 1, 1)

        # input box for down sample - default 1
        self.spinBox_downsample = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_downsample.setMinimum(1)
        self.spinBox_downsample.setProperty("value", 1)
        self.spinBox_downsample.setObjectName("spinBox_downsample")
        self.gridLayout_2.addWidget(self.spinBox_downsample, 2, 6, 1, 1)

        # yrange min text
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 10, 1, 1)

        # input box for yrange min - default -0.5
        self.doubleSpinBox_yrangemin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_yrangemin.setDecimals(1)
        self.doubleSpinBox_yrangemin.setMinimum(-1.0)
        self.doubleSpinBox_yrangemin.setMaximum(0.0)
        self.doubleSpinBox_yrangemin.setSingleStep(0.1)
        self.doubleSpinBox_yrangemin.setProperty("value", -0.5)
        self.doubleSpinBox_yrangemin.setObjectName("doubleSpinBox_yrangemin")
        self.gridLayout_2.addWidget(self.doubleSpinBox_yrangemin, 2, 13, 1, 2)

        # stop push button
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
                                        "    background-color: rgb(235, 31, 16);\n"
                                        "    color: white;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 17, 1, 4)

        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        #Area for plotting
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(213, 249, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout_4.addWidget(self.widget, 2, 1, 1, 1)

        self.gridLayout_4.addWidget(self.groupBox, 1, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(778, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 3, 1, 1, 1)
        
        spacerItem2 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show My Voice"))
        MainWindow.setWindowIcon(QtGui.QIcon('sound-wave.png'))
        self.groupBox.setTitle(_translate("MainWindow", "Set Parameters"))
        self.label_12.setText(_translate("MainWindow", "YRange(Max)"))
        self.label_13.setText(_translate("MainWindow", "YRange(Min)"))
        self.label_5.setText(_translate("MainWindow", "Down Sample (>0)"))
        self.label_6.setText(_translate("MainWindow", "Update Interval (1 to 100 ms)"))
        self.label_4.setText(_translate("MainWindow", "Sampling Rate (>1000 Hz)"))
        self.label_2.setText(_translate("MainWindow", "Audio Device"))
        self.label_3.setText(_translate("MainWindow", "Window Length (>28)"))
        self.lineEdit.setText(_translate("MainWindow", "1000"))
        self.lineEdit_2.setText(_translate("MainWindow", "44100"))
        self.pushButton.setText(_translate("MainWindow", "Start Plot"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
