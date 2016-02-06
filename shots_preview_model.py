
import os
import sys


from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import (
	QBrush,
	QColor
)

from trax.api.data import FileType, AssetType

def debug():
	from pdb import set_trace
	from PyQt4.QtCore import pyqtRemoveInputHook
	pyqtRemoveInputHook()
	set_trace()

class ShotsPreviewModel(QtCore.QAbstractListModel):
	def __init__(self, shots, *args, **kwargs):
		super(ShotsPreviewModel, self).__init__(*args, **kwargs)
		self.shots = shots
		self.assetType = AssetType.recordByName("Shot")
		self.fileType = FileType.recordByAssetTypeAndId(
			self.assetType,
			"Playblast"
		)

	def getStatusColor(self, shot):
		# Get the paths
		playblastDoesNotExist = False
		pcpreviewDoesNotExist = False
		playblastPath = self.fileType.fullPath(
			shot,
			{"Department" : "Animation"}
		)
		pcpreviewPath = self.fileType.fullPath(
			shot,
			{"Department" : "PCPreview"}
		)
		if not os.path.exists(playblastPath):
			playblastDoesNotExist = True
		if not os.path.exists(pcpreviewPath):
			pcpreviewDoesNotExist = True
		if playblastDoesNotExist or pcpreviewDoesNotExist:
			return QBrush(QColor(55.0, 55.0, 55.0))
		playblastMTime = os.path.getmtime(playblastPath)
		pcpreviewMTime = os.path.getmtime(pcpreviewPath)
		if playblastMTime > pcpreviewMTime:
			# Flag this as playblast is newer
			return QBrush(QColor(153.0, 23.0, 60.0))
		else:
			return QBrush(QColor(220.0, 233.0, 190.0))

	def data(self, index, role):
		if index.isValid() and role == QtCore.Qt.DisplayRole:
			return QtCore.QVariant(self.shots[index.row()].displayName())
		elif role == QtCore.Qt.BackgroundRole:
			currentShot = self.shots[index.row()]
			return self.getStatusColor(currentShot)
		else:
			return QtCore.QVariant()

	def rowCount(self, index=QtCore.QModelIndex()):
		return len(self.shots)
