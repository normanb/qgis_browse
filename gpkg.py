"""
/***************************************************************************
 GPKG
                                 A QGIS plugin
 Geopackage
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import qgis.utils

import os
import os.path

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from gpkgdialog import GPKGDialog

class GPKG:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/gpkg/icon.png"), \
            "GPKG", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        self.aboutAction=QAction(QIcon(":/plugins/gpkg/icon.png"), \
            "GPKG About", self.iface.mainWindow())
        QObject.connect(self.aboutAction, SIGNAL("activated()"), self.about)

        # Add toolbar button and menu item
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.addPluginToWebMenu("&GPKG", self.action)
            self.iface.addPluginToWebMenu("&GPKG", self.aboutAction)
            self.iface.addWebToolBarIcon(self.action)
        else:
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("&GPKG", self.action)
            self.iface.addPluginToMenu("&GPKG", self.aboutAction)

    def unload(self):
        # Remove the plugin menu item and icon
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.removePluginWebMenu("&GPKG", self.action)
            self.iface.removePluginWebMenu("&GPKG", self.aboutAction)
            self.iface.removeWebToolBarIcon(self.action)
        else:
            self.iface.removeToolBarIcon(self.action)
            self.iface.removePluginMenu("&GPKG", self.action)
            self.iface.removePluginMenu("&GPKG", self.aboutAction)

    def about(self):
        infoString = "<table><tr><td colspan=\"2\"><b>GPKG 0.0.1</b></td></tr><tr><td colspan=\"2\"></td></tr><tr><td>Author:</td><td>Norman Barker</td></tr><tr><td>Mail:</td><td><a href=\"mailto:norman@cloudant.com\">norman@cloudant.com</a></td></tr><tr><td>Website:</td><td><a href=\"https://www.cloudant.com\">https://www.cloudant.com</a></td></tr></table>"
        QMessageBox.information(self.iface.mainWindow(), "About GPKG", infoString)

    # run method that performs all the real work
    def run(self):
        # create and show the dialog
        dlg = GPKGDialog(self)
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            filename = dlg.filename
            if filename:
                ogr_driver_name = 'GPKG'
                # QGIS only supports exporting one layer as sqlite
                layer = qgis.utils.iface.activeLayer()
                if layer:
                    extent = qgis.utils.iface.mapCanvas().extent()
                    layerType = layer.type()
                    if layerType == QgsMapLayer.VectorLayer:
                        print 'Writing:' + layer.name()
                        crs = qgis.utils.iface.mapCanvas().mapRenderer().destinationCrs()
                        print "CRS selected: " + crs.description()
                        result2 = qgis.core.QgsVectorFileWriter.writeAsVectorFormat(layer, filename, 
                            layer.dataProvider().encoding(), crs, ogr_driver_name,
                            filterExtent=extent)
                        print "Status: " + str(result2)
                        if result2 != 0:
                            QMessageBox.critical(self.iface.mainWindow(), "Error", "Failed to export: " + layer.name() + \
                                " Status: " + str(result2))
                else:
                    QMessageBox.critical(self.iface.mainWindow(), "Error", "No active layer for export")  
            else:
                QMessageBox.critical(self.iface.mainWindow(), "Error", "No filename specified for export")              
