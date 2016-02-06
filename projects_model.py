
# Built in
import os
import sys

# PyQt4
from PyQt4.QtGui import QStringListModel

# Blur
from trax.api.data import Project, ProjectStatus


class ProjectsModel(QStringListModel):
	def __init__(self, *args, **kwargs):
		super(ProjectsModel, self).__init__(*args, **kwargs)
		self.activeProjects = self.getProjects()
		self.setStringList([p.name() for p in self.activeProjects])

	def getProjects(self):
		activeProjects = Project.recordsByProjectStatus(
			ProjectStatus(4)
		)
		return activeProjects
