
# Built in
import os
import sys

# PyQt4
from PyQt4.QtGui import QStringListModel

# Blur
from trax.api.data import ShotGroup


class ShotGroupModel(QStringListModel):
	def __init__(self, project, *args, **kwargs):
		super(ShotGroupModel, self).__init__(*args, **kwargs)
		self.project = project
		self.sequences = sorted(
			list(self.project.sequences()),
			key=lambda x: x.displayName()
		)
		self.setStringList([seq.displayName() for seq in self.sequences])

