
# Built-in
import json
import os
import sys

# Blur
from trax.api.data import (
	AssetType,
	FileType,
	Project
)

# PyQt4
from PyQt4.QtGui import QStringListModel

class PresetsModel(QStringListModel):
	def __init__(self, project, *args, **kwargs):
		super(PresetsModel, self).__init__(*args, **kwargs)
		self.project = project
		self.presets = self.getPresets()
		self.setStringList([p for p in self.presets.keys()])

	def getPresets(self):
		aType = AssetType.recordByName("Project")
		fType = FileType.recordByAssetTypeAndId(aType, "Blast::Prefs")
		prefsPath = fType.fullPath(self.project)
		if not os.path.exists(prefsPath):
			# Use the prefs stored in _virtual_project as a default to fall back on
			# if the current project doesn't have a prefs file.
			prefsPath = fType.fullPath(Project.recordByName('_virtual_project'))
		presetsPath = os.path.normpath(
			os.path.join(prefsPath, "presets.json")
		)
		with open(presetsPath, "r") as fileinfo:
			filesdata = fileinfo.read()
		presets = json.loads(filesdata)
		return presets
