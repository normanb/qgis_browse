"""
/***************************************************************************
 GPKGDialog
                                 A QGIS plugin
 GPKGDialog
                             -------------------
        begin                : 2014-12-01
        copyright            : (C) 2014 by Norman Barker
        email                : norman@cloudant.com
        website              : https://www.cloudant.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_gpkg import Ui_GPKG
from qgis.core import *

import user

import string
import random
import tempfile
import os
import os.path
import re

plugin_path = os.path.abspath(os.path.dirname(__file__))

class GPKGDialog(QtGui.QDialog):

	def __init__(self, parent):
		QtGui.QDialog.__init__(self)
		# Set up the user interface from Designer.
		self.parent = parent
		self.ui = Ui_GPKG()
		self.ui.setupUi(self)

		# Load default cloudant url
		self.parameter_lineedits = []
		self.parameter_labels = []

		self.settings = QtCore.QSettings()
		self.init_variables()

		QtCore.QObject.connect(self.ui.cmdSelectFile, QtCore.SIGNAL("clicked()"), self.selectFile)
		self.ui.buttonBox.accepted.connect(self.accept)
		self.ui.buttonBox.rejected.connect(self.reject)

	def init_variables(self):
		self.filename = None

	def selectFile(self):
		self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Write GPKG', user.home, 'GPKG(*.gpkg)')
		self.ui.txtFileName.setText(self.filename)
