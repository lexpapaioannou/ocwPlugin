# -*- coding: utf-8 -*-
"""
/***************************************************************************
 View2PNG
                                 A QGIS plugin
 Exports current QGIS View to PNG Image File
                             -------------------
        begin                : 2017-07-24
        copyright            : (C) 2017 by Alex Sakelariou
        email                : john.papaioannou.1@gmail.com
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
    """Load View2PNG class from file View2PNG.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .view2png import View2PNG
    return View2PNG(iface)
