# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gpkg.ui'
#
# Created: Thu Feb 12 15:14:00 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GPKG(object):
    def setupUi(self, GPKG):
        GPKG.setObjectName(_fromUtf8("GPKG"))
        GPKG.resize(394, 149)
        self.buttonBox = QtGui.QDialogButtonBox(GPKG)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.txtFileName = QtGui.QLineEdit(GPKG)
        self.txtFileName.setGeometry(QtCore.QRect(20, 50, 301, 21))
        self.txtFileName.setReadOnly(True)
        self.txtFileName.setObjectName(_fromUtf8("txtFileName"))
        self.cmdSelectFile = QtGui.QToolButton(GPKG)
        self.cmdSelectFile.setGeometry(QtCore.QRect(330, 50, 26, 21))
        self.cmdSelectFile.setObjectName(_fromUtf8("cmdSelectFile"))

        self.retranslateUi(GPKG)
        QtCore.QMetaObject.connectSlotsByName(GPKG)

    def retranslateUi(self, GPKG):
        GPKG.setWindowTitle(_translate("GPKG", "GPKG - Version 0.0.1", None))
        self.cmdSelectFile.setText(_translate("GPKG", "...", None))

