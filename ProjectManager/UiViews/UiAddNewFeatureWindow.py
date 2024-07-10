# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewFeatureWindow.ui'
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

class Ui_AddNewFeatureWindow(object):
    def setupUi(self, AddNewFeatureWindow):
        if not AddNewFeatureWindow.objectName():
            AddNewFeatureWindow.setObjectName(u"AddNewFeatureWindow")
        AddNewFeatureWindow.resize(1250, 564)
        self.centralwidget = QWidget(AddNewFeatureWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 0)
        self.FeatureLayoutVBox = QVBoxLayout()
        self.FeatureLayoutVBox.setSpacing(20)
        self.FeatureLayoutVBox.setObjectName(u"FeatureLayoutVBox")
        self.FeatureNameHBox = QHBoxLayout()
        self.FeatureNameHBox.setSpacing(20)
        self.FeatureNameHBox.setObjectName(u"FeatureNameHBox")
        self.FeatureNameLabel = QLabel(self.centralwidget)
        self.FeatureNameLabel.setObjectName(u"FeatureNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FeatureNameLabel.sizePolicy().hasHeightForWidth())
        self.FeatureNameLabel.setSizePolicy(sizePolicy)
        self.FeatureNameLabel.setMinimumSize(QSize(100, 0))

        self.FeatureNameHBox.addWidget(self.FeatureNameLabel)

        self.FeatureNameInput = QLineEdit(self.centralwidget)
        self.FeatureNameInput.setObjectName(u"FeatureNameInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FeatureNameInput.sizePolicy().hasHeightForWidth())
        self.FeatureNameInput.setSizePolicy(sizePolicy1)

        self.FeatureNameHBox.addWidget(self.FeatureNameInput)


        self.FeatureLayoutVBox.addLayout(self.FeatureNameHBox)

        self.FeatureDescriptionHBox = QHBoxLayout()
        self.FeatureDescriptionHBox.setSpacing(20)
        self.FeatureDescriptionHBox.setObjectName(u"FeatureDescriptionHBox")
        self.FeatureDescriptionLabel = QLabel(self.centralwidget)
        self.FeatureDescriptionLabel.setObjectName(u"FeatureDescriptionLabel")
        sizePolicy.setHeightForWidth(self.FeatureDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.FeatureDescriptionLabel.setSizePolicy(sizePolicy)
        self.FeatureDescriptionLabel.setMinimumSize(QSize(100, 0))
        self.FeatureDescriptionLabel.setBaseSize(QSize(100, 0))

        self.FeatureDescriptionHBox.addWidget(self.FeatureDescriptionLabel)

        self.FeatureDescriptionTextEdit = QTextEdit(self.centralwidget)
        self.FeatureDescriptionTextEdit.setObjectName(u"FeatureDescriptionTextEdit")

        self.FeatureDescriptionHBox.addWidget(self.FeatureDescriptionTextEdit)


        self.FeatureLayoutVBox.addLayout(self.FeatureDescriptionHBox)


        self.verticalLayout_2.addLayout(self.FeatureLayoutVBox)

        self.AddFeatureBtnFrame = QHBoxLayout()
        self.AddFeatureBtnFrame.setObjectName(u"AddFeatureBtnFrame")
        self.AddFeatureBtnFrame.setContentsMargins(10, 10, 10, 10)
        self.AddFeatureBtn = QPushButton(self.centralwidget)
        self.AddFeatureBtn.setObjectName(u"AddFeatureBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AddFeatureBtn.sizePolicy().hasHeightForWidth())
        self.AddFeatureBtn.setSizePolicy(sizePolicy2)
        self.AddFeatureBtn.setMinimumSize(QSize(100, 40))

        self.AddFeatureBtnFrame.addWidget(self.AddFeatureBtn)


        self.verticalLayout_2.addLayout(self.AddFeatureBtnFrame)

        AddNewFeatureWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddNewFeatureWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 22))
        AddNewFeatureWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddNewFeatureWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddNewFeatureWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewFeatureWindow)

        QMetaObject.connectSlotsByName(AddNewFeatureWindow)
    # setupUi

    def retranslateUi(self, AddNewFeatureWindow):
        AddNewFeatureWindow.setWindowTitle(QCoreApplication.translate("AddNewFeatureWindow", u"MainWindow", None))
        self.FeatureNameLabel.setText(QCoreApplication.translate("AddNewFeatureWindow", u"Name: ", None))
        self.FeatureDescriptionLabel.setText(QCoreApplication.translate("AddNewFeatureWindow", u"Description:", None))
        self.AddFeatureBtn.setText(QCoreApplication.translate("AddNewFeatureWindow", u"Add Feature", None))
    # retranslateUi

