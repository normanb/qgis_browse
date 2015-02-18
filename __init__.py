"""
/***************************************************************************
 GPKG
                                 A QGIS plugin
 GPKG
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
 This script initializes the plugin, making it known to QGIS.
"""
def classFactory(iface):
    # load GPKG class from file GPKG
    from gpkg import GPKG
    return GPKG(iface)
