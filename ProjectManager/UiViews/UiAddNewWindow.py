# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_AddNewWindow(object):
    def setupUi(self, AddNewWindow):
        if not AddNewWindow.objectName():
            AddNewWindow.setObjectName(u"AddNewWindow")
        AddNewWindow.resize(1257, 573)
        self.MainFrame = QWidget(AddNewWindow)
        self.MainFrame.setObjectName(u"MainFrame")
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 0)
        self.GridFrame = QFrame(self.MainFrame)
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

        self.MiddleFrame = QFrame(self.MainFrame)
        self.MiddleFrame.setObjectName(u"MiddleFrame")
        self.MiddleFrame.setFrameShape(QFrame.StyledPanel)
        self.MiddleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MiddleFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.PlaceholderFrame = QFrame(self.MiddleFrame)
        self.PlaceholderFrame.setObjectName(u"PlaceholderFrame")
        self.PlaceholderFrame.setFrameShape(QFrame.StyledPanel)
        self.PlaceholderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.PlaceholderFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout.addWidget(self.PlaceholderFrame)

        self.PriorityFrame = QFrame(self.MiddleFrame)
        self.PriorityFrame.setObjectName(u"PriorityFrame")
        self.PriorityFrame.setFrameShape(QFrame.StyledPanel)
        self.PriorityFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.PriorityFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.PriorityLabel = QLabel(self.PriorityFrame)
        self.PriorityLabel.setObjectName(u"PriorityLabel")
        self.PriorityLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.PriorityLabel)

        self.PriorityComboBox = QComboBox(self.PriorityFrame)
        self.PriorityComboBox.setObjectName(u"PriorityComboBox")

        self.verticalLayout_4.addWidget(self.PriorityComboBox)


        self.horizontalLayout.addWidget(self.PriorityFrame)


        self.verticalLayout_2.addWidget(self.MiddleFrame)

        self.AddNewBtnFrame = QHBoxLayout()
        self.AddNewBtnFrame.setObjectName(u"AddNewBtnFrame")
        self.AddNewBtnFrame.setContentsMargins(10, 10, 10, 10)
        self.AddNewBtn = QPushButton(self.MainFrame)
        self.AddNewBtn.setObjectName(u"AddNewBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddNewBtn.sizePolicy().hasHeightForWidth())
        self.AddNewBtn.setSizePolicy(sizePolicy)
        self.AddNewBtn.setMinimumSize(QSize(100, 40))

        self.AddNewBtnFrame.addWidget(self.AddNewBtn)


        self.verticalLayout_2.addLayout(self.AddNewBtnFrame)

        AddNewWindow.setCentralWidget(self.MainFrame)
        self.menubar = QMenuBar(AddNewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1257, 22))
        AddNewWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddNewWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddNewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewWindow)

        QMetaObject.connectSlotsByName(AddNewWindow)
    # setupUi

    def retranslateUi(self, AddNewWindow):
        AddNewWindow.setWindowTitle(QCoreApplication.translate("AddNewWindow", u"MainWindow", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("AddNewWindow", u"Description:", None))
#if QT_CONFIG(tooltip)
        self.NameLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.NameLabel.setText(QCoreApplication.translate("AddNewWindow", u"Name: *", None))
        self.PriorityLabel.setText(QCoreApplication.translate("AddNewWindow", u"Priority", None))
        self.AddNewBtn.setText(QCoreApplication.translate("AddNewWindow", u"Add Task", None))
    # retranslateUi

