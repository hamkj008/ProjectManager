# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewIssueWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_AddNewIssueWindow(object):
    def setupUi(self, AddNewIssueWindow):
        if not AddNewIssueWindow.objectName():
            AddNewIssueWindow.setObjectName(u"AddNewIssueWindow")
        AddNewIssueWindow.resize(1250, 566)
        self.centralwidget = QWidget(AddNewIssueWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 0)
        self.IssueLayoutVBox = QVBoxLayout()
        self.IssueLayoutVBox.setSpacing(20)
        self.IssueLayoutVBox.setObjectName(u"IssueLayoutVBox")
        self.IssueNameHBox = QHBoxLayout()
        self.IssueNameHBox.setSpacing(20)
        self.IssueNameHBox.setObjectName(u"IssueNameHBox")
        self.IssueNameLabel = QLabel(self.centralwidget)
        self.IssueNameLabel.setObjectName(u"IssueNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IssueNameLabel.sizePolicy().hasHeightForWidth())
        self.IssueNameLabel.setSizePolicy(sizePolicy)
        self.IssueNameLabel.setMinimumSize(QSize(100, 0))

        self.IssueNameHBox.addWidget(self.IssueNameLabel)

        self.IssueNameInputField = QLineEdit(self.centralwidget)
        self.IssueNameInputField.setObjectName(u"IssueNameInputField")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IssueNameInputField.sizePolicy().hasHeightForWidth())
        self.IssueNameInputField.setSizePolicy(sizePolicy1)

        self.IssueNameHBox.addWidget(self.IssueNameInputField)


        self.IssueLayoutVBox.addLayout(self.IssueNameHBox)

        self.IssueDescriptionHBox = QHBoxLayout()
        self.IssueDescriptionHBox.setSpacing(20)
        self.IssueDescriptionHBox.setObjectName(u"IssueDescriptionHBox")
        self.IssueDescriptionLabel = QLabel(self.centralwidget)
        self.IssueDescriptionLabel.setObjectName(u"IssueDescriptionLabel")
        sizePolicy.setHeightForWidth(self.IssueDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.IssueDescriptionLabel.setSizePolicy(sizePolicy)
        self.IssueDescriptionLabel.setMinimumSize(QSize(100, 0))
        self.IssueDescriptionLabel.setBaseSize(QSize(100, 0))

        self.IssueDescriptionHBox.addWidget(self.IssueDescriptionLabel)

        self.IssueDescriptionTextEdit = QTextEdit(self.centralwidget)
        self.IssueDescriptionTextEdit.setObjectName(u"IssueDescriptionTextEdit")

        self.IssueDescriptionHBox.addWidget(self.IssueDescriptionTextEdit)


        self.IssueLayoutVBox.addLayout(self.IssueDescriptionHBox)


        self.verticalLayout_2.addLayout(self.IssueLayoutVBox)

        self.AddIssueBtnFrame = QHBoxLayout()
        self.AddIssueBtnFrame.setObjectName(u"AddIssueBtnFrame")
        self.AddIssueBtnFrame.setContentsMargins(10, 10, 10, 10)
        self.AddIssueBtn = QPushButton(self.centralwidget)
        self.AddIssueBtn.setObjectName(u"AddIssueBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AddIssueBtn.sizePolicy().hasHeightForWidth())
        self.AddIssueBtn.setSizePolicy(sizePolicy2)
        self.AddIssueBtn.setMinimumSize(QSize(100, 40))

        self.AddIssueBtnFrame.addWidget(self.AddIssueBtn)


        self.verticalLayout_2.addLayout(self.AddIssueBtnFrame)

        AddNewIssueWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddNewIssueWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 22))
        AddNewIssueWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddNewIssueWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddNewIssueWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewIssueWindow)

        QMetaObject.connectSlotsByName(AddNewIssueWindow)
    # setupUi

    def retranslateUi(self, AddNewIssueWindow):
        AddNewIssueWindow.setWindowTitle(QCoreApplication.translate("AddNewIssueWindow", u"MainWindow", None))
        self.IssueNameLabel.setText(QCoreApplication.translate("AddNewIssueWindow", u"Name: ", None))
        self.IssueDescriptionLabel.setText(QCoreApplication.translate("AddNewIssueWindow", u"Description:", None))
        self.AddIssueBtn.setText(QCoreApplication.translate("AddNewIssueWindow", u"Add Issue", None))
    # retranslateUi

