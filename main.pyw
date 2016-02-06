##
#	\namespace	Blast
#
#	\remarks
#
#	\author		slu@blur.com
#	\author		Blur Studio
#	\date		6/2015
#
import sys

from PyQt4 import QtGui

if ( __name__ in ( '__main__', '__builtin__' ) ):
	import blurdev
	blurdev.registerScriptPath(__file__)

	import os
	import blur3d.gui.splashscreen
	splash = blur3d.gui.splashscreen.randomSplashScreen("PreviewCheck")
	if splash:
		splash.show()
	from PreviewCheck.gui import PreviewCheckWindow, PreviewCheckWidget
	# app = QtGui.QApplication(sys.argv)
	# app.setStyle('Plastique')
	# window = PreviewCheckWidget()
	# window.show()
	# sys.exit(app.exec_())
	blurdev.launch(PreviewCheckWindow, splash=splash, instance=False)

