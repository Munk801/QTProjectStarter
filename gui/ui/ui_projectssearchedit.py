
import os
import sys

from PyQt4 import QtGui


class ProjectsSearchEDIT(QtGui.QLineEdit):
	def __init__(self, *args, **kwargs):
		super(ProjectsSearchEDIT, self).__init__(*args, **kwargs)
		self.currentProject = None
