# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_file_label = QtWidgets.QLabel(self.centralwidget)
        self.input_file_label.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_file_label.setFont(font)
        self.input_file_label.setObjectName("input_file_label")
        self.output_file_label = QtWidgets.QLabel(self.centralwidget)
        self.output_file_label.setGeometry(QtCore.QRect(10, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.output_file_label.setFont(font)
        self.output_file_label.setObjectName("output_file_label")
        self.input_file_input = QtWidgets.QLineEdit(self.centralwidget)
        self.input_file_input.setGeometry(QtCore.QRect(90, 10, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_file_input.setFont(font)
        self.input_file_input.setObjectName("input_file_input")
        self.output_file_input = QtWidgets.QLineEdit(self.centralwidget)
        self.output_file_input.setGeometry(QtCore.QRect(90, 60, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.output_file_input.setFont(font)
        self.output_file_input.setObjectName("output_file_input")
        self.radio_overwrite = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_overwrite.setGeometry(QtCore.QRect(90, 100, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_overwrite.setFont(font)
        self.radio_overwrite.setObjectName("radio_overwrite")
        self.radio_new = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_new.setGeometry(QtCore.QRect(90, 130, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_new.setChecked(True)
        self.radio_new.setFont(font)
        self.radio_new.setObjectName("radio_new")
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(110, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_save.setFont(font)
        self.button_save.setObjectName("button_save")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(110, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setGeometry(QtCore.QRect(30, 230, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.message_label.setFont(font)
        self.message_label.setText("")
        self.message_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.message_label.setObjectName("message_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_file_label.setText(_translate("MainWindow", "Input File"))
        self.output_file_label.setText(_translate("MainWindow", "Output File"))
        self.radio_overwrite.setText(_translate("MainWindow", "Overwrite Existing"))
        self.radio_new.setText(_translate("MainWindow", "Create New"))
        self.button_save.setText(_translate("MainWindow", "SAVE"))
        self.button_clear.setText(_translate("MainWindow", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())