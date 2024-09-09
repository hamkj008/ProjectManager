# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutWindow.ui'
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
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(1250, 566)
        self.MainFrame = QWidget(AboutWindow)
        self.MainFrame.setObjectName(u"MainFrame")
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 0)
        self.AboutTitle = QFrame(self.MainFrame)
        self.AboutTitle.setObjectName(u"AboutTitle")
        self.AboutTitle.setFrameShape(QFrame.StyledPanel)
        self.AboutTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.AboutTitle)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(15, 15, 15, 15)
        self.AboutTitleLabel = QLabel(self.AboutTitle)
        self.AboutTitleLabel.setObjectName(u"AboutTitleLabel")
        self.AboutTitleLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.AboutTitleLabel)


        self.verticalLayout_2.addWidget(self.AboutTitle)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.Frame = QFrame(self.MainFrame)
        self.Frame.setObjectName(u"Frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame.sizePolicy().hasHeightForWidth())
        self.Frame.setSizePolicy(sizePolicy)
        self.Frame.setFrameShape(QFrame.StyledPanel)
        self.Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.AboutFrame = QFrame(self.Frame)
        self.AboutFrame.setObjectName(u"AboutFrame")
        self.AboutFrame.setFrameShape(QFrame.StyledPanel)
        self.AboutFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.AboutFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AboutGridFrame = QFrame(self.AboutFrame)
        self.AboutGridFrame.setObjectName(u"AboutGridFrame")
        self.AboutGridFrame.setFrameShape(QFrame.StyledPanel)
        self.AboutGridFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.AboutGridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.VersionHeaderLabel = QLabel(self.AboutGridFrame)
        self.VersionHeaderLabel.setObjectName(u"VersionHeaderLabel")
        self.VersionHeaderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.VersionHeaderLabel, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.VersionDataLabel = QLabel(self.AboutGridFrame)
        self.VersionDataLabel.setObjectName(u"VersionDataLabel")

        self.gridLayout.addWidget(self.VersionDataLabel, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.AboutGridFrame)

        self.HorizontalFrame = QFrame(self.AboutFrame)
        self.HorizontalFrame.setObjectName(u"HorizontalFrame")
        self.HorizontalFrame.setFrameShape(QFrame.StyledPanel)
        self.HorizontalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.HorizontalFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.HorizontalFrame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout.addWidget(self.HorizontalFrame)

        self.HorizontalFrame_2 = QFrame(self.AboutFrame)
        self.HorizontalFrame_2.setObjectName(u"HorizontalFrame_2")
        self.HorizontalFrame_2.setFrameShape(QFrame.StyledPanel)
        self.HorizontalFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.HorizontalFrame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.HorizontalFrame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.HorizontalFrame_2)


        self.horizontalLayout_2.addWidget(self.AboutFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.Frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.CloseBtnFrame = QFrame(self.MainFrame)
        self.CloseBtnFrame.setObjectName(u"CloseBtnFrame")
        self.CloseBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.CloseBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.CloseBtnFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CloseBtn = QPushButton(self.CloseBtnFrame)
        self.CloseBtn.setObjectName(u"CloseBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CloseBtn.sizePolicy().hasHeightForWidth())
        self.CloseBtn.setSizePolicy(sizePolicy1)
        self.CloseBtn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.CloseBtn)


        self.verticalLayout_2.addWidget(self.CloseBtnFrame)

        AboutWindow.setCentralWidget(self.MainFrame)
        self.menubar = QMenuBar(AboutWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 22))
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AboutWindow)
        self.statusbar.setObjectName(u"statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"MainWindow", None))
        self.AboutTitleLabel.setText(QCoreApplication.translate("AboutWindow", u"About", None))
        self.VersionHeaderLabel.setText(QCoreApplication.translate("AboutWindow", u"Version:", None))
        self.VersionDataLabel.setText(QCoreApplication.translate("AboutWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("AboutWindow", u"By Kieran Hambledon", None))
        self.label_2.setText(QCoreApplication.translate("AboutWindow", u"Copyright 2024", None))
        self.CloseBtn.setText(QCoreApplication.translate("AboutWindow", u"Close", None))
    # retranslateUi

