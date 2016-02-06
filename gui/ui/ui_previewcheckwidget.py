# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'previewcheckwidget.ui'
#
# Created: Fri Feb 05 17:33:34 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.resize(245, 503)
        self.verticalLayout = QtGui.QVBoxLayout(widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.header = QtGui.QFrame(widget)
        self.header.setFrameShape(QtGui.QFrame.StyledPanel)
        self.header.setFrameShadow(QtGui.QFrame.Raised)
        self.header.setObjectName(_fromUtf8("header"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.header)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.ProjectBannerView = QtGui.QLabel(self.header)
        self.ProjectBannerView.setMaximumSize(QtCore.QSize(2555555, 16777215))
        self.ProjectBannerView.setText(_fromUtf8(""))
        self.ProjectBannerView.setScaledContents(True)
        self.ProjectBannerView.setAlignment(QtCore.Qt.AlignCenter)
        self.ProjectBannerView.setObjectName(_fromUtf8("ProjectBannerView"))
        self.verticalLayout_9.addWidget(self.ProjectBannerView)
        self.verticalLayout.addWidget(self.header)
        self.stack = QtGui.QStackedWidget(widget)
        self.stack.setMouseTracking(True)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.ProjectsPage = QtGui.QWidget()
        self.ProjectsPage.setObjectName(_fromUtf8("ProjectsPage"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.ProjectsPage)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.body = QtGui.QFrame(self.ProjectsPage)
        self.body.setFrameShape(QtGui.QFrame.StyledPanel)
        self.body.setFrameShadow(QtGui.QFrame.Raised)
        self.body.setObjectName(_fromUtf8("body"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.body)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ProjectsEDIT = ProjectsSearchEDIT(self.groupBox)
        self.ProjectsEDIT.setMinimumSize(QtCore.QSize(0, 40))
        self.ProjectsEDIT.setAutoFillBackground(False)
        self.ProjectsEDIT.setAlignment(QtCore.Qt.AlignCenter)
        self.ProjectsEDIT.setPlaceholderText(_fromUtf8(""))
        self.ProjectsEDIT.setObjectName(_fromUtf8("ProjectsEDIT"))
        self.horizontalLayout_3.addWidget(self.ProjectsEDIT)
        self.ProjectSelectedContinueBTN = QtGui.QToolButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProjectSelectedContinueBTN.sizePolicy().hasHeightForWidth())
        self.ProjectSelectedContinueBTN.setSizePolicy(sizePolicy)
        self.ProjectSelectedContinueBTN.setMinimumSize(QtCore.QSize(0, 40))
        self.ProjectSelectedContinueBTN.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProjectSelectedContinueBTN.setIcon(icon)
        self.ProjectSelectedContinueBTN.setIconSize(QtCore.QSize(20, 20))
        self.ProjectSelectedContinueBTN.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.ProjectSelectedContinueBTN.setObjectName(_fromUtf8("ProjectSelectedContinueBTN"))
        self.horizontalLayout_3.addWidget(self.ProjectSelectedContinueBTN)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_5.addWidget(self.body)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.stack.addWidget(self.ProjectsPage)
        self.ShotInfoPage = QtGui.QWidget()
        self.ShotInfoPage.setObjectName(_fromUtf8("ShotInfoPage"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.ShotInfoPage)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.BackToProjectsBTN = QtGui.QToolButton(self.ShotInfoPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackToProjectsBTN.sizePolicy().hasHeightForWidth())
        self.BackToProjectsBTN.setSizePolicy(sizePolicy)
        self.BackToProjectsBTN.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackToProjectsBTN.setIcon(icon1)
        self.BackToProjectsBTN.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.BackToProjectsBTN.setObjectName(_fromUtf8("BackToProjectsBTN"))
        self.horizontalLayout.addWidget(self.BackToProjectsBTN)
        self.ShotGroupFrame = QtGui.QFrame(self.ShotInfoPage)
        self.ShotGroupFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ShotGroupFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.ShotGroupFrame.setProperty("collapsed", False)
        self.ShotGroupFrame.setObjectName(_fromUtf8("ShotGroupFrame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.ShotGroupFrame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.ShotGroupEDIT = QtGui.QLineEdit(self.ShotGroupFrame)
        self.ShotGroupEDIT.setObjectName(_fromUtf8("ShotGroupEDIT"))
        self.verticalLayout_4.addWidget(self.ShotGroupEDIT)
        self.horizontalLayout.addWidget(self.ShotGroupFrame)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.ShotsFrame = QtGui.QFrame(self.ShotInfoPage)
        self.ShotsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ShotsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.ShotsFrame.setProperty("collapsed", False)
        self.ShotsFrame.setObjectName(_fromUtf8("ShotsFrame"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.ShotsFrame)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.ShotsListView = QtGui.QListView(self.ShotsFrame)
        self.ShotsListView.setEditTriggers(QtGui.QAbstractItemView.EditKeyPressed)
        self.ShotsListView.setObjectName(_fromUtf8("ShotsListView"))
        self.verticalLayout_6.addWidget(self.ShotsListView)
        self.verticalLayout_3.addWidget(self.ShotsFrame)
        self.stack.addWidget(self.ShotInfoPage)
        self.verticalLayout.addWidget(self.stack)

        self.retranslateUi(widget)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "Form", None))
        self.groupBox.setTitle(_translate("widget", "Enter Project", None))
        self.ProjectSelectedContinueBTN.setText(_translate("widget", "Continue", None))
        self.ShotGroupEDIT.setPlaceholderText(_translate("widget", "Shotgroup", None))

from .ui_projectssearchedit import ProjectsSearchEDIT
import resources_rc
