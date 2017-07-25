# -*- coding: utf-8 -*-
"""
/***************************************************************************
 View2PNG
                                 A QGIS plugin
 Runs an OCW script on Raster input files
                             -------------------
        begin                : 2017-07-25
        copyright            : (C) 2017 by Lex Papaioannou
        email                : papaioannou.alexander1@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ocwPlugin class from file ocwPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ocwPlugin import ocwPlugin
    return ocwPlugin(iface)
