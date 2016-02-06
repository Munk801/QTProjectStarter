
import fnmatch
import getpass
import glob
import os
import re
import subprocess
import sys
import urllib

from blur3d.pipe.cinematic.gui.resource.icons import Icons
from blur3d.gui import WaitCursor
import blurdev
import blurdev.gui
import blursg

from trax.api.data import Project, ShotGroup

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (
	QApplication,
	QCompleter,
	QTreeWidgetItem,
	QMessageBox,
	QPixmap
)
from PyQt4.QtCore import Qt

# Model Imports
from PreviewCheck.projects_model import ProjectsModel
from PreviewCheck.shotgroup_model import ShotGroupModel
from PreviewCheck.shots_preview_model import ShotsPreviewModel

# UI
from .ui.ui_previewcheckwidget import Ui_widget

sg = blursg.sg()

def debug():
	from PyQt4.QtCore import pyqtRemoveInputHook
	from blurdev.debug import set_trace
	pyqtRemoveInputHook()
	set_trace()

class PreviewCheckWidget(QtGui.QWidget):
	# GlOBALS
	BANNERPATH = "C:\\temp\\blast_banner"

	def __init__(self, parent=None):
		super(PreviewCheckWidget, self).__init__(parent)
		self.parent = parent
		self.currentProjectName = ""
		# blurdev.gui.loadUi(__file__, self, 'shooterwidget')
		self.ui = Ui_widget()
		self.ui.setupUi(self)
		self.connectProjectsEdit()
		self.ui.header.hide()
		self.ui.ProjectsEDIT.editingFinished.connect(self.getProjectsBanner)
		self.ui.ProjectsEDIT.clearFocus()
		self.ui.ShotGroupEDIT.editingFinished.connect(self.updateShotsListView)
		self.ui.ProjectSelectedContinueBTN.clicked.connect(self.moveToShotsPage)
		self.ui.BackToProjectsBTN.clicked.connect(self.moveToProjects)
		self.loadStyle()


	def getProjectsBanner(self):
		projectName = str(self.ui.ProjectsEDIT.text())
		# Don't requery for the project banner if its there
		if self.currentProjectName == projectName:
			return
		self.currentProjectName = projectName
		self.ui.ProjectsEDIT.currentProject = Project.recordByName(projectName)
		sgProj = sg.find_one(
			"Project",
			[["name", "is", projectName]], ["billboard"]
		)
		if sgProj:
			if sgProj["billboard"]:
				billboardPath = sgProj["billboard"]["url"]
				if billboardPath:
					urllib.urlretrieve(billboardPath, self.BANNERPATH)
					if os.path.exists(self.BANNERPATH):
						bannerPixmap = QPixmap(
							self.ui.ProjectBannerView.maximumWidth(),
							self.ui.ProjectBannerView.maximumHeight()
						)
						didLoad = bannerPixmap.load(self.BANNERPATH)
						# We actually don't care about the height
						# since this will be clamped from the width
						self.ui.ProjectBannerView.setPixmap(
							bannerPixmap.scaled(244, 200, Qt.KeepAspectRatio)
						)
						self.ui.ProjectBannerView.setAlignment(Qt.AlignCenter)
						self.ui.ProjectBannerView.setScaledContents(True)
						# For some reason, calling the window repaint
						# fixes the issue with the flickering
						self.ui.header.show()
						self.repaint()
						self.parent.repaint()


	def connectProjectsEdit(self):
		completer = QCompleter()
		self.ui.ProjectsEDIT.setCompleter(completer)
		model = ProjectsModel()
		completer.setModel(model)

	def loadStyle(self):
		# merge in app specific look and feel
		dirpath = os.path.dirname(__file__)
		css_file = os.path.join(dirpath, "resources", "desktop_dark.css")
		f = open(css_file)
		# css = app.styleSheet() + "\n\n" + f.read()
		css = f.read()
		f.close()
		self.setStyleSheet(css)

	def moveToShotsPage(self):
		self.getProjectsBanner()
		self.slideView(self.ui.ShotInfoPage, "right")
		# Set the model for the presets
		# If no current project is set, send error
		if not self.ui.ProjectsEDIT.currentProject:
			pass
		else:
			shotGroupModel = ShotGroupModel(self.ui.ProjectsEDIT.currentProject)
			completer = QCompleter()
			self.ui.ShotGroupEDIT.setCompleter(completer)
			completer.setModel(shotGroupModel)
			# If no presets exists, open and close UI elements
			# if not presetsModel.presets:
			# 	self.ui.NoPresetsSpecifiedFrame.setProperty("collapsed", True)
			# # Expand
			# if self.ui.NoPresetsSpecifiedFrame.property("collapsed"):
			# 	self.ui.PresetsFrame.show()
			# 	self.ui.NoPresetsSpecifiedFrame.hide()
			# 	self.ui.PresetsFrame.setProperty("collapsed", False)
			# 	self.ui.NoPresetsSpecifiedFrame.setProperty("collapsed", True)
			# else:
			# 	self.ui.NoPresetsSpecifiedFrame.show()
			# 	self.ui.NoPresetsSpecifiedFrame.setProperty("collapsed", False)
			# 	self.ui.PresetsFrame.hide()
			# 	self.ui.PresetsFrame.setProperty("collapsed", True)

	def moveToProjects(self):
		self.slideView(self.ui.ProjectsPage, "left")

	def slideView(self, newPage, fromDirection="right"):
		""" Slides the new page in from a direction. """
		offsetX = self.ui.stack.frameRect().width()
		offsetY = self.ui.stack.frameRect().height()
		currentPage = self.ui.stack.currentWidget()

		newPage.setGeometry(0, 0, offsetX, offsetY)

		if fromDirection == "left":
			offsetX = -offsetX

		currentPosition = newPage.pos()
		newPage.move(currentPosition.x() + offsetX, currentPosition.y())
		newPage.show()
		newPage.raise_()

		animateOld = QtCore.QPropertyAnimation(currentPage, "pos", self)
		animateOld.setDuration(500)
		animateOld.setStartValue(QtCore.QPoint(currentPosition.x(), currentPosition.y()))
		animateOld.setEndValue(QtCore.QPoint(currentPosition.x() - offsetX, currentPosition.y()))
		animateOld.setEasingCurve(QtCore.QEasingCurve.OutBack)

		animateNew = QtCore.QPropertyAnimation(newPage, "pos", self)
		animateNew.setDuration(500)
		animateNew.setStartValue(QtCore.QPoint(currentPosition.x() + offsetX, currentPosition.y()))
		animateNew.setEndValue(QtCore.QPoint(currentPosition.x(), currentPosition.y()))
		animateNew.setEasingCurve(QtCore.QEasingCurve.OutBack)

		animGroup = QtCore.QParallelAnimationGroup(self)
		animGroup.addAnimation(animateOld)
		animGroup.addAnimation(animateNew)

		def slideFinished():
			self.ui.stack.setCurrentWidget(newPage)

		animGroup.finished.connect(slideFinished)
		animGroup.start()

	def updateShotsListView(self):
		shotGroupName = str(self.ui.ShotGroupEDIT.text())
		shotGroupQuery = ShotGroup.c.Project == self.ui.ProjectsEDIT.currentProject
		shotGroupQuery &= ShotGroup.c.Name == shotGroupName
		shotGroupList = shotGroupQuery.select()
		if shotGroupList:
			currentShotGroup = shotGroupList[0]
			# currentShotGroup = ShotGroup.recordByName(shotGroupName)
			shots = [s for s in currentShotGroup.shots()]
			shotsModel = ShotsPreviewModel(shots)
			self.ui.ShotsListView.setModel(shotsModel)
		else:
			self.ui.ShotsListView.clear()

class PreviewCheckWindow(blurdev.gui.Window):
	def __init__(self, parent):
		blurdev.gui.Window.__init__(self, parent)
		blurdev.gui.loadUi(__file__, self, 'previewcheckwindow')
		self._widget = PreviewCheckWidget(parent=self)
		self.setCentralWidget(self._widget)
		# self._widget.cancelled.connect(self.close)
		self.menuBar().hide()
		self.setWindowTitle('PreviewCheck')
		self.setWindowIcon(Icons.getIcon('movies'))
		# This here is to override the css that is being brought
		# from treegrunt
		app = QApplication.instance()
		app.setStyleSheet("")
		self.loadStyle()

	def loadStyle(self):
		# merge in app specific look and feel
		dirpath = os.path.dirname(__file__)
		css_file = os.path.join(dirpath, "resources", "desktop_dark.css")
		f = open(css_file)
		# css = app.styleSheet() + "\n\n" + f.read()
		css = f.read()
		f.close()
		self.setStyleSheet(css)

def main():
	blurdev.registerScriptPath(__file__)
	blurdev.launch(PreviewCheckWindow)

if __name__ == '__main__':
	main()
