# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewProjectWindow.ui'
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

class Ui_AddNewProjectWindow(object):
    def setupUi(self, AddNewProjectWindow):
        if not AddNewProjectWindow.objectName():
            AddNewProjectWindow.setObjectName(u"AddNewProjectWindow")
        AddNewProjectWindow.resize(1250, 566)
        self.centralwidget = QWidget(AddNewProjectWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 0)
        self.ProjectLayoutVBox = QVBoxLayout()
        self.ProjectLayoutVBox.setSpacing(20)
        self.ProjectLayoutVBox.setObjectName(u"ProjectLayoutVBox")
        self.ProjectNameHBox = QHBoxLayout()
        self.ProjectNameHBox.setSpacing(20)
        self.ProjectNameHBox.setObjectName(u"ProjectNameHBox")
        self.ProjectNameLabel = QLabel(self.centralwidget)
        self.ProjectNameLabel.setObjectName(u"ProjectNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProjectNameLabel.sizePolicy().hasHeightForWidth())
        self.ProjectNameLabel.setSizePolicy(sizePolicy)
        self.ProjectNameLabel.setMinimumSize(QSize(100, 0))

        self.ProjectNameHBox.addWidget(self.ProjectNameLabel)

        self.ProjectNameInputField = QLineEdit(self.centralwidget)
        self.ProjectNameInputField.setObjectName(u"ProjectNameInputField")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ProjectNameInputField.sizePolicy().hasHeightForWidth())
        self.ProjectNameInputField.setSizePolicy(sizePolicy1)

        self.ProjectNameHBox.addWidget(self.ProjectNameInputField)


        self.ProjectLayoutVBox.addLayout(self.ProjectNameHBox)

        self.ProjectDescriptionHBox = QHBoxLayout()
        self.ProjectDescriptionHBox.setSpacing(20)
        self.ProjectDescriptionHBox.setObjectName(u"ProjectDescriptionHBox")
        self.ProjectDescriptionLabel = QLabel(self.centralwidget)
        self.ProjectDescriptionLabel.setObjectName(u"ProjectDescriptionLabel")
        sizePolicy.setHeightForWidth(self.ProjectDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.ProjectDescriptionLabel.setSizePolicy(sizePolicy)
        self.ProjectDescriptionLabel.setMinimumSize(QSize(100, 0))
        self.ProjectDescriptionLabel.setBaseSize(QSize(100, 0))

        self.ProjectDescriptionHBox.addWidget(self.ProjectDescriptionLabel)

        self.ProjectDescriptionTextEdit = QTextEdit(self.centralwidget)
        self.ProjectDescriptionTextEdit.setObjectName(u"ProjectDescriptionTextEdit")

        self.ProjectDescriptionHBox.addWidget(self.ProjectDescriptionTextEdit)


        self.ProjectLayoutVBox.addLayout(self.ProjectDescriptionHBox)


        self.verticalLayout_2.addLayout(self.ProjectLayoutVBox)

        self.AddNewProjectBtnLayout = QHBoxLayout()
        self.AddNewProjectBtnLayout.setObjectName(u"AddNewProjectBtnLayout")
        self.AddNewProjectBtnLayout.setContentsMargins(10, 10, 10, 10)
        self.AddNewProjectBtn = QPushButton(self.centralwidget)
        self.AddNewProjectBtn.setObjectName(u"AddNewProjectBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AddNewProjectBtn.sizePolicy().hasHeightForWidth())
        self.AddNewProjectBtn.setSizePolicy(sizePolicy2)
        self.AddNewProjectBtn.setMinimumSize(QSize(100, 40))

        self.AddNewProjectBtnLayout.addWidget(self.AddNewProjectBtn)


        self.verticalLayout_2.addLayout(self.AddNewProjectBtnLayout)

        AddNewProjectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddNewProjectWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 22))
        AddNewProjectWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddNewProjectWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddNewProjectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewProjectWindow)

        QMetaObject.connectSlotsByName(AddNewProjectWindow)
    # setupUi

    def retranslateUi(self, AddNewProjectWindow):
        AddNewProjectWindow.setWindowTitle(QCoreApplication.translate("AddNewProjectWindow", u"MainWindow", None))
        self.ProjectNameLabel.setText(QCoreApplication.translate("AddNewProjectWindow", u"Name: ", None))
        self.ProjectDescriptionLabel.setText(QCoreApplication.translate("AddNewProjectWindow", u"Description:", None))
        self.AddNewProjectBtn.setText(QCoreApplication.translate("AddNewProjectWindow", u"Add Project", None))
    # retranslateUi

