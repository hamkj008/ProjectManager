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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AddNewProjectWindow(object):
    def setupUi(self, AddNewProjectWindow):
        if not AddNewProjectWindow.objectName():
            AddNewProjectWindow.setObjectName(u"AddNewProjectWindow")
        AddNewProjectWindow.resize(1257, 573)
        self.AddFrame = QWidget(AddNewProjectWindow)
        self.AddFrame.setObjectName(u"AddFrame")
        self.verticalLayout_2 = QVBoxLayout(self.AddFrame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 0)
        self.GridFrame = QFrame(self.AddFrame)
        self.GridFrame.setObjectName(u"GridFrame")
        self.GridFrame.setFrameShape(QFrame.StyledPanel)
        self.GridFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.GridFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.DescriptionLabel = QLabel(self.GridFrame)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")

        self.gridLayout_2.addWidget(self.DescriptionLabel, 1, 0, 1, 1)

        self.NameLabelFrame = QFrame(self.GridFrame)
        self.NameLabelFrame.setObjectName(u"NameLabelFrame")
        self.NameLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.NameLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.NameLabelFrame)
        self.verticalLayout_28.setSpacing(1)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.NameLabelErrorFrame = QFrame(self.NameLabelFrame)
        self.NameLabelErrorFrame.setObjectName(u"NameLabelErrorFrame")
        self.NameLabelErrorFrame.setFrameShape(QFrame.StyledPanel)
        self.NameLabelErrorFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.NameLabelErrorFrame)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_28.addWidget(self.NameLabelErrorFrame)

        self.NameLabel = QLabel(self.NameLabelFrame)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.NameLabel)


        self.gridLayout_2.addWidget(self.NameLabelFrame, 0, 0, 1, 1)

        self.NameInputFrame = QFrame(self.GridFrame)
        self.NameInputFrame.setObjectName(u"NameInputFrame")
        self.NameInputFrame.setFrameShape(QFrame.StyledPanel)
        self.NameInputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.NameInputFrame)
        self.verticalLayout_29.setSpacing(1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.NameInputErrorFrame = QFrame(self.NameInputFrame)
        self.NameInputErrorFrame.setObjectName(u"NameInputErrorFrame")
        self.NameInputErrorFrame.setFrameShape(QFrame.StyledPanel)
        self.NameInputErrorFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.NameInputErrorFrame)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_29.addWidget(self.NameInputErrorFrame)

        self.NameInput = QLineEdit(self.NameInputFrame)
        self.NameInput.setObjectName(u"NameInput")

        self.verticalLayout_29.addWidget(self.NameInput)


        self.gridLayout_2.addWidget(self.NameInputFrame, 0, 2, 1, 1)

        self.DescriptionTextEdit = QTextEdit(self.GridFrame)
        self.DescriptionTextEdit.setObjectName(u"DescriptionTextEdit")

        self.gridLayout_2.addWidget(self.DescriptionTextEdit, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.GridFrame)

        self.AddNewBtnFrame = QHBoxLayout()
        self.AddNewBtnFrame.setObjectName(u"AddNewBtnFrame")
        self.AddNewBtnFrame.setContentsMargins(10, 10, 10, 10)
        self.AddNewBtn = QPushButton(self.AddFrame)
        self.AddNewBtn.setObjectName(u"AddNewBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddNewBtn.sizePolicy().hasHeightForWidth())
        self.AddNewBtn.setSizePolicy(sizePolicy)
        self.AddNewBtn.setMinimumSize(QSize(100, 40))

        self.AddNewBtnFrame.addWidget(self.AddNewBtn)


        self.verticalLayout_2.addLayout(self.AddNewBtnFrame)

        AddNewProjectWindow.setCentralWidget(self.AddFrame)
        self.menubar = QMenuBar(AddNewProjectWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1257, 22))
        AddNewProjectWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddNewProjectWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddNewProjectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewProjectWindow)

        QMetaObject.connectSlotsByName(AddNewProjectWindow)
    # setupUi

    def retranslateUi(self, AddNewProjectWindow):
        AddNewProjectWindow.setWindowTitle(QCoreApplication.translate("AddNewProjectWindow", u"MainWindow", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("AddNewProjectWindow", u"Description:", None))
#if QT_CONFIG(tooltip)
        self.NameLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.NameLabel.setText(QCoreApplication.translate("AddNewProjectWindow", u"Name: *", None))
        self.AddNewBtn.setText(QCoreApplication.translate("AddNewProjectWindow", u"Add Task", None))
    # retranslateUi

