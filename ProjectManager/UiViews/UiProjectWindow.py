# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_ProjectWindow(object):
    def setupUi(self, ProjectWindow):
        if not ProjectWindow.objectName():
            ProjectWindow.setObjectName(u"ProjectWindow")
        ProjectWindow.resize(1272, 719)
        self.verticalLayout = QVBoxLayout(ProjectWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(ProjectWindow)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 10)
        self.TitleFrame = QFrame(self.MainFrame)
        self.TitleFrame.setObjectName(u"TitleFrame")
        self.TitleFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.TitleFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.TitleLabel = QLabel(self.TitleFrame)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.TitleLabel)


        self.verticalLayout_2.addWidget(self.TitleFrame)

        self.SearchFrame = QFrame(self.MainFrame)
        self.SearchFrame.setObjectName(u"SearchFrame")
        self.SearchFrame.setFrameShape(QFrame.StyledPanel)
        self.SearchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.SearchInput = QLineEdit(self.SearchFrame)
        self.SearchInput.setObjectName(u"SearchInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchInput.sizePolicy().hasHeightForWidth())
        self.SearchInput.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.SearchInput)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.HorizontalFrame = QFrame(self.SearchFrame)
        self.HorizontalFrame.setObjectName(u"HorizontalFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.HorizontalFrame.sizePolicy().hasHeightForWidth())
        self.HorizontalFrame.setSizePolicy(sizePolicy1)
        self.HorizontalFrame.setFrameShape(QFrame.StyledPanel)
        self.HorizontalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.HorizontalFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.AddNewBtn = QPushButton(self.HorizontalFrame)
        self.AddNewBtn.setObjectName(u"AddNewBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AddNewBtn.sizePolicy().hasHeightForWidth())
        self.AddNewBtn.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddNewBtn.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.AddNewBtn)


        self.horizontalLayout_10.addWidget(self.HorizontalFrame)


        self.verticalLayout_2.addWidget(self.SearchFrame)

        self.ProjectFrame = QFrame(self.MainFrame)
        self.ProjectFrame.setObjectName(u"ProjectFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ProjectFrame.sizePolicy().hasHeightForWidth())
        self.ProjectFrame.setSizePolicy(sizePolicy3)
        self.ProjectFrame.setFrameShape(QFrame.StyledPanel)
        self.ProjectFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ProjectFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ProjectScrollArea = QScrollArea(self.ProjectFrame)
        self.ProjectScrollArea.setObjectName(u"ProjectScrollArea")
        self.ProjectScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ProjectScrollArea.setWidgetResizable(True)
        self.ProjectScrollAreaContents = QWidget()
        self.ProjectScrollAreaContents.setObjectName(u"ProjectScrollAreaContents")
        self.ProjectScrollAreaContents.setGeometry(QRect(0, 0, 1229, 547))
        self.verticalLayout_4 = QVBoxLayout(self.ProjectScrollAreaContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ProjectGridFrame = QFrame(self.ProjectScrollAreaContents)
        self.ProjectGridFrame.setObjectName(u"ProjectGridFrame")
        self.ProjectGridFrame.setFrameShape(QFrame.StyledPanel)
        self.ProjectGridFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.ProjectGridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_4.addWidget(self.ProjectGridFrame)

        self.ProjectScrollArea.setWidget(self.ProjectScrollAreaContents)

        self.verticalLayout_3.addWidget(self.ProjectScrollArea)


        self.verticalLayout_2.addWidget(self.ProjectFrame)

        self.DescriptionFrame = QFrame(self.MainFrame)
        self.DescriptionFrame.setObjectName(u"DescriptionFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.DescriptionFrame.sizePolicy().hasHeightForWidth())
        self.DescriptionFrame.setSizePolicy(sizePolicy4)
        self.DescriptionFrame.setFrameShape(QFrame.StyledPanel)
        self.DescriptionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.DescriptionFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.DescriptionLabel = QLabel(self.DescriptionFrame)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")

        self.verticalLayout_6.addWidget(self.DescriptionLabel)

        self.DescriptionScrollArea = QScrollArea(self.DescriptionFrame)
        self.DescriptionScrollArea.setObjectName(u"DescriptionScrollArea")
        self.DescriptionScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.DescriptionScrollArea.setWidgetResizable(True)
        self.DescriptionScrollAreaContents = QWidget()
        self.DescriptionScrollAreaContents.setObjectName(u"DescriptionScrollAreaContents")
        self.DescriptionScrollAreaContents.setGeometry(QRect(0, 0, 1229, 69))
        self.verticalLayout_5 = QVBoxLayout(self.DescriptionScrollAreaContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.DescriptionTextFrame = QFrame(self.DescriptionScrollAreaContents)
        self.DescriptionTextFrame.setObjectName(u"DescriptionTextFrame")
        self.DescriptionTextFrame.setFrameShape(QFrame.StyledPanel)
        self.DescriptionTextFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.DescriptionTextFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.DescriptionTextLabel = QLabel(self.DescriptionTextFrame)
        self.DescriptionTextLabel.setObjectName(u"DescriptionTextLabel")
        self.DescriptionTextLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_9.addWidget(self.DescriptionTextLabel)


        self.verticalLayout_5.addWidget(self.DescriptionTextFrame)

        self.DescriptionScrollArea.setWidget(self.DescriptionScrollAreaContents)

        self.verticalLayout_6.addWidget(self.DescriptionScrollArea)


        self.verticalLayout_2.addWidget(self.DescriptionFrame)


        self.verticalLayout.addWidget(self.MainFrame)


        self.retranslateUi(ProjectWindow)

        QMetaObject.connectSlotsByName(ProjectWindow)
    # setupUi

    def retranslateUi(self, ProjectWindow):
        ProjectWindow.setWindowTitle(QCoreApplication.translate("ProjectWindow", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("ProjectWindow", u"Projects", None))
        self.SearchInput.setPlaceholderText(QCoreApplication.translate("ProjectWindow", u"Search...", None))
        self.AddNewBtn.setText("")
        self.DescriptionLabel.setText(QCoreApplication.translate("ProjectWindow", u"Description:", None))
        self.DescriptionTextLabel.setText("")
    # retranslateUi

