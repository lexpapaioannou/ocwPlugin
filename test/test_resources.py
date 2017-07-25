# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'john.papaioannou.1@gmail.com'
__date__ = '2017-07-24'
__copyright__ = 'Copyright 2017, Alex Sakelariou'

import unittest

from PyQt4.QtGui import QIcon



class View2PNGDialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/View2PNG/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(View2PNGResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



