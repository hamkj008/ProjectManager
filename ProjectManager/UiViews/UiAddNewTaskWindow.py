# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewTaskWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AddNewTaskWindow(object):
    def setupUi(self, AddNewTaskWindow):
        if not AddNewTaskWindow.objectName():
            AddNewTaskWindow.setObjectName(u"AddNewTaskWindow")
        AddNewTaskWindow.resize(1250, 566)
        self.centralwidget = QWidget(AddNewTaskWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 0)
        self.TaskLayoutVBox = QVBoxLayout()
        self.TaskLayoutVBox.setSpacing(20)
        self.TaskLayoutVBox.setObjectName(u"TaskLayoutVBox")
        self.TaskNameHBox = QHBoxLayout()
        self.TaskNameHBox.setSpacing(20)
        self.TaskNameHBox.setObjectName(u"TaskNameHBox")
        self.TaskNameLabel = QLabel(self.centralwidget)
        self.TaskNameLabel.setObjectName(u"TaskNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TaskNameLabel.sizePolicy().hasHeightForWidth())
        self.TaskNameLabel.setSizePolicy(sizePolicy)
        self.TaskNameLabel.setMinimumSize(QSize(100, 0))

        self.TaskNameHBox.addWidget(self.TaskNameLabel)

        self.TaskNameInputField = QLineEdit(self.centralwidget)
        self.TaskNameInputField.setObjectName(u"TaskNameInputField")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TaskNameInputField.sizePolicy().hasHeightForWidth())
        self.TaskNameInputField.setSizePolicy(sizePolicy1)

        self.TaskNameHBox.addWidget(self.TaskNameInputField)


        self.TaskLayoutVBox.addLayout(self.TaskNameHBox)

        self.TaskDescriptionHBox = QHBoxLayout()
        self.TaskDescriptionHBox.setSpacing(20)
        self.TaskDescriptionHBox.setObjectName(u"TaskDescriptionHBox")
        self.TaskDescriptionLabel = QLabel(self.centralwidget)
        self.TaskDescriptionLabel.setObjectName(u"TaskDescriptionLabel")
        sizePolicy.setHeightForWidth(self.TaskDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.TaskDescriptionLabel.setSizePolicy(sizePolicy)
        self.TaskDescriptionLabel.setMinimumSize(QSize(100, 0))
        self.TaskDescriptionLabel.setBaseSize(QSize(100, 0))

        self.TaskDescriptionHBox.addWidget(self.TaskDescriptionLabel)

        self.TaskDescriptionTextEdit = QTextEdit(self.centralwidget)
        self.TaskDescriptionTextEdit.setObjectName(u"TaskDescriptionTextEdit")

        self.TaskDescriptionHBox.addWidget(self.TaskDescriptionTextEdit)


        self.TaskLayoutVBox.addLayout(self.TaskDescriptionHBox)


        self.verticalLayout_2.addLayout(self.TaskLayoutVBox)

        self.MiddleFrame = QFrame(self.centralwidget)
        self.MiddleFrame.setObjectName(u"MiddleFrame")
        self.MiddleFrame.setFrameShape(QFrame.StyledPanel)
        self.MiddleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MiddleFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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

        self.AddTaskBtnFrame = QHBoxLayout()
        self.AddTaskBtnFrame.setObjectName(u"AddTaskBtnFrame")
        self.AddTaskBtnFrame.setContentsMargins(10, 10, 10, 10)
        self.AddTaskBtn = QPushButton(self.centralwidget)
        self.AddTaskBtn.setObjectName(u"AddTaskBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AddTaskBtn.sizePolicy().hasHeightForWidth())
        self.AddTaskBtn.setSizePolicy(sizePolicy2)
        self.AddTaskBtn.setMinimumSize(QSize(100, 40))

        self.AddTaskBtnFrame.addWidget(self.AddTaskBtn)


        self.verticalLayout_2.addLayout(self.AddTaskBtnFrame)

        AddNewTaskWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddNewTaskWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 22))
        AddNewTaskWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddNewTaskWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddNewTaskWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewTaskWindow)

        QMetaObject.connectSlotsByName(AddNewTaskWindow)
    # setupUi

    def retranslateUi(self, AddNewTaskWindow):
        AddNewTaskWindow.setWindowTitle(QCoreApplication.translate("AddNewTaskWindow", u"MainWindow", None))
        self.TaskNameLabel.setText(QCoreApplication.translate("AddNewTaskWindow", u"Name: ", None))
        self.TaskDescriptionLabel.setText(QCoreApplication.translate("AddNewTaskWindow", u"Description:", None))
        self.PriorityLabel.setText(QCoreApplication.translate("AddNewTaskWindow", u"Priority", None))
        self.AddTaskBtn.setText(QCoreApplication.translate("AddNewTaskWindow", u"Add Task", None))
    # retranslateUi

