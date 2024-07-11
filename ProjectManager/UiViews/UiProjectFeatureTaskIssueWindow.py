# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectFeatureTaskIssueWindow.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_ProjectFeatureTaskIssueWindow(object):
    def setupUi(self, ProjectFeatureTaskIssueWindow):
        if not ProjectFeatureTaskIssueWindow.objectName():
            ProjectFeatureTaskIssueWindow.setObjectName(u"ProjectFeatureTaskIssueWindow")
        ProjectFeatureTaskIssueWindow.resize(1253, 816)
        self.horizontalLayout_2 = QHBoxLayout(ProjectFeatureTaskIssueWindow)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(ProjectFeatureTaskIssueWindow)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.TopFrame = QFrame(self.MainFrame)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setFrameShape(QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.TopFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.ProjectNameFrame = QFrame(self.TopFrame)
        self.ProjectNameFrame.setObjectName(u"ProjectNameFrame")
        self.ProjectNameFrame.setFrameShape(QFrame.StyledPanel)
        self.ProjectNameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.ProjectNameFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.BackBtn = QPushButton(self.ProjectNameFrame)
        self.BackBtn.setObjectName(u"BackBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackBtn.sizePolicy().hasHeightForWidth())
        self.BackBtn.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.BackBtn)

        self.TitleLabel = QLabel(self.ProjectNameFrame)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.TitleLabel)


        self.verticalLayout_2.addWidget(self.ProjectNameFrame)

        self.HorizontalFrame = QFrame(self.TopFrame)
        self.HorizontalFrame.setObjectName(u"HorizontalFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.HorizontalFrame.sizePolicy().hasHeightForWidth())
        self.HorizontalFrame.setSizePolicy(sizePolicy1)
        self.HorizontalFrame.setFrameShape(QFrame.StyledPanel)
        self.HorizontalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.HorizontalFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.HorizontalFrame_2 = QFrame(self.HorizontalFrame)
        self.HorizontalFrame_2.setObjectName(u"HorizontalFrame_2")
        self.HorizontalFrame_2.setFrameShape(QFrame.StyledPanel)
        self.HorizontalFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.HorizontalFrame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.AddNewBtn = QPushButton(self.HorizontalFrame_2)
        self.AddNewBtn.setObjectName(u"AddNewBtn")

        self.horizontalLayout_9.addWidget(self.AddNewBtn)


        self.horizontalLayout_8.addWidget(self.HorizontalFrame_2)


        self.verticalLayout_2.addWidget(self.HorizontalFrame)

        self.tabWidget = QTabWidget(self.TopFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.FeaturesTab = QWidget()
        self.FeaturesTab.setObjectName(u"FeaturesTab")
        self.verticalLayout_31 = QVBoxLayout(self.FeaturesTab)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.FeatureTabGridFrame = QFrame(self.FeaturesTab)
        self.FeatureTabGridFrame.setObjectName(u"FeatureTabGridFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FeatureTabGridFrame.sizePolicy().hasHeightForWidth())
        self.FeatureTabGridFrame.setSizePolicy(sizePolicy2)
        self.FeatureTabGridFrame.setFrameShape(QFrame.StyledPanel)
        self.FeatureTabGridFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.FeatureTabGridFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout_31.addWidget(self.FeatureTabGridFrame)

        self.tabWidget.addTab(self.FeaturesTab, "")
        self.TasksTab = QWidget()
        self.TasksTab.setObjectName(u"TasksTab")
        self.TasksTab.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.TasksTab)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.TaskTabGrid = QFrame(self.TasksTab)
        self.TaskTabGrid.setObjectName(u"TaskTabGrid")
        self.TaskTabGridLayout_3 = QGridLayout(self.TaskTabGrid)
        self.TaskTabGridLayout_3.setObjectName(u"TaskTabGridLayout_3")
        self.TaskTabGridLayout_3.setHorizontalSpacing(10)
        self.TaskTabGridLayout_3.setVerticalSpacing(0)
        self.TaskTabGridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TaskRightFrame = QFrame(self.TaskTabGrid)
        self.TaskRightFrame.setObjectName(u"TaskRightFrame")
        self.TaskRightFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskRightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.TaskRightFrame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.TaskCompleteScrollArea = QScrollArea(self.TaskRightFrame)
        self.TaskCompleteScrollArea.setObjectName(u"TaskCompleteScrollArea")
        self.TaskCompleteScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.TaskCompleteScrollArea.setWidgetResizable(True)
        self.TaskCompleteScrollAreaContents = QWidget()
        self.TaskCompleteScrollAreaContents.setObjectName(u"TaskCompleteScrollAreaContents")
        self.TaskCompleteScrollAreaContents.setGeometry(QRect(0, 0, 380, 500))
        self.verticalLayout_34 = QVBoxLayout(self.TaskCompleteScrollAreaContents)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.TaskCompleteScrollArea.setWidget(self.TaskCompleteScrollAreaContents)

        self.verticalLayout_33.addWidget(self.TaskCompleteScrollArea)


        self.TaskTabGridLayout_3.addWidget(self.TaskRightFrame, 4, 2, 1, 1)

        self.TaskCompletedLabelFrame = QFrame(self.TaskTabGrid)
        self.TaskCompletedLabelFrame.setObjectName(u"TaskCompletedLabelFrame")
        self.TaskCompletedLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskCompletedLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.TaskCompletedLabelFrame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 10, 0, 10)
        self.CompletedLabel = QLabel(self.TaskCompletedLabelFrame)
        self.CompletedLabel.setObjectName(u"CompletedLabel")
        self.CompletedLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.CompletedLabel)


        self.TaskTabGridLayout_3.addWidget(self.TaskCompletedLabelFrame, 1, 2, 1, 1)

        self.TaskCentralFrame = QFrame(self.TaskTabGrid)
        self.TaskCentralFrame.setObjectName(u"TaskCentralFrame")
        self.TaskCentralFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskCentralFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.TaskCentralFrame)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.TaskInProgressScrollArea = QScrollArea(self.TaskCentralFrame)
        self.TaskInProgressScrollArea.setObjectName(u"TaskInProgressScrollArea")
        self.TaskInProgressScrollArea.setFrameShape(QFrame.NoFrame)
        self.TaskInProgressScrollArea.setFrameShadow(QFrame.Plain)
        self.TaskInProgressScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.TaskInProgressScrollArea.setWidgetResizable(True)
        self.TaskInProgressScrollAreaContents = QWidget()
        self.TaskInProgressScrollAreaContents.setObjectName(u"TaskInProgressScrollAreaContents")
        self.TaskInProgressScrollAreaContents.setGeometry(QRect(0, 0, 382, 502))
        self.verticalLayout_36 = QVBoxLayout(self.TaskInProgressScrollAreaContents)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.TaskInProgressScrollArea.setWidget(self.TaskInProgressScrollAreaContents)

        self.verticalLayout_35.addWidget(self.TaskInProgressScrollArea)


        self.TaskTabGridLayout_3.addWidget(self.TaskCentralFrame, 4, 1, 1, 1)

        self.TaskLeftFrame = QFrame(self.TaskTabGrid)
        self.TaskLeftFrame.setObjectName(u"TaskLeftFrame")
        self.TaskLeftFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskLeftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.TaskLeftFrame)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.TaskScrollArea = QScrollArea(self.TaskLeftFrame)
        self.TaskScrollArea.setObjectName(u"TaskScrollArea")
        self.TaskScrollArea.setFrameShape(QFrame.NoFrame)
        self.TaskScrollArea.setFrameShadow(QFrame.Plain)
        self.TaskScrollArea.setLineWidth(0)
        self.TaskScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.TaskScrollArea.setWidgetResizable(True)
        self.TaskScrollAreaContents = QWidget()
        self.TaskScrollAreaContents.setObjectName(u"TaskScrollAreaContents")
        self.TaskScrollAreaContents.setGeometry(QRect(0, 0, 382, 502))
        self.verticalLayout_38 = QVBoxLayout(self.TaskScrollAreaContents)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.TaskScrollArea.setWidget(self.TaskScrollAreaContents)

        self.verticalLayout_37.addWidget(self.TaskScrollArea)


        self.TaskTabGridLayout_3.addWidget(self.TaskLeftFrame, 4, 0, 1, 1)

        self.TasksLabelFrame = QFrame(self.TaskTabGrid)
        self.TasksLabelFrame.setObjectName(u"TasksLabelFrame")
        self.TasksLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.TasksLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.TasksLabelFrame)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 10, 0, 10)
        self.TasksLabel = QLabel(self.TasksLabelFrame)
        self.TasksLabel.setObjectName(u"TasksLabel")
        self.TasksLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.TasksLabel)


        self.TaskTabGridLayout_3.addWidget(self.TasksLabelFrame, 1, 0, 1, 1)

        self.TaskInProgressLabelFrame = QFrame(self.TaskTabGrid)
        self.TaskInProgressLabelFrame.setObjectName(u"TaskInProgressLabelFrame")
        self.TaskInProgressLabelFrame.setStyleSheet(u"")
        self.TaskInProgressLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskInProgressLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.TaskInProgressLabelFrame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 10, 0, 10)
        self.InProgressLabel = QLabel(self.TaskInProgressLabelFrame)
        self.InProgressLabel.setObjectName(u"InProgressLabel")
        self.InProgressLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.InProgressLabel)


        self.TaskTabGridLayout_3.addWidget(self.TaskInProgressLabelFrame, 1, 1, 1, 1)


        self.verticalLayout_32.addWidget(self.TaskTabGrid)

        self.tabWidget.addTab(self.TasksTab, "")
        self.IssuesTab = QWidget()
        self.IssuesTab.setObjectName(u"IssuesTab")
        self.verticalLayout_39 = QVBoxLayout(self.IssuesTab)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.IssueTabGrid = QGridLayout()
        self.IssueTabGrid.setObjectName(u"IssueTabGrid")
        self.IssueCompletedLabelFrame = QFrame(self.IssuesTab)
        self.IssueCompletedLabelFrame.setObjectName(u"IssueCompletedLabelFrame")
        self.IssueCompletedLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueCompletedLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.IssueCompletedLabelFrame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.IssueCompletedLabel = QLabel(self.IssueCompletedLabelFrame)
        self.IssueCompletedLabel.setObjectName(u"IssueCompletedLabel")
        self.IssueCompletedLabel.setLineWidth(1)
        self.IssueCompletedLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.IssueCompletedLabel)


        self.IssueTabGrid.addWidget(self.IssueCompletedLabelFrame, 0, 1, 1, 1)

        self.IssueLabelFrame = QFrame(self.IssuesTab)
        self.IssueLabelFrame.setObjectName(u"IssueLabelFrame")
        self.IssueLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.IssueLabelFrame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.IssueLabel = QLabel(self.IssueLabelFrame)
        self.IssueLabel.setObjectName(u"IssueLabel")
        self.IssueLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.IssueLabel)


        self.IssueTabGrid.addWidget(self.IssueLabelFrame, 0, 0, 1, 1)

        self.IssueLeftFrame = QFrame(self.IssuesTab)
        self.IssueLeftFrame.setObjectName(u"IssueLeftFrame")
        self.IssueLeftFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueLeftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.IssueLeftFrame)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.IssueScrollArea = QScrollArea(self.IssueLeftFrame)
        self.IssueScrollArea.setObjectName(u"IssueScrollArea")
        self.IssueScrollArea.setFrameShape(QFrame.NoFrame)
        self.IssueScrollArea.setFrameShadow(QFrame.Plain)
        self.IssueScrollArea.setLineWidth(1)
        self.IssueScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.IssueScrollArea.setWidgetResizable(True)
        self.IssueScrollAreaContents = QWidget()
        self.IssueScrollAreaContents.setObjectName(u"IssueScrollAreaContents")
        self.IssueScrollAreaContents.setGeometry(QRect(0, 0, 589, 494))
        self.verticalLayout_41 = QVBoxLayout(self.IssueScrollAreaContents)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.IssueGridFrame = QFrame(self.IssueScrollAreaContents)
        self.IssueGridFrame.setObjectName(u"IssueGridFrame")
        self.gridLayout_9 = QGridLayout(self.IssueGridFrame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.verticalLayout_41.addWidget(self.IssueGridFrame)

        self.IssueScrollArea.setWidget(self.IssueScrollAreaContents)

        self.verticalLayout_40.addWidget(self.IssueScrollArea)


        self.IssueTabGrid.addWidget(self.IssueLeftFrame, 3, 0, 1, 1)

        self.IssueRightFrame = QFrame(self.IssuesTab)
        self.IssueRightFrame.setObjectName(u"IssueRightFrame")
        self.IssueRightFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueRightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.IssueRightFrame)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.IssueCompleteScrollArea = QScrollArea(self.IssueRightFrame)
        self.IssueCompleteScrollArea.setObjectName(u"IssueCompleteScrollArea")
        self.IssueCompleteScrollArea.setFrameShape(QFrame.NoFrame)
        self.IssueCompleteScrollArea.setFrameShadow(QFrame.Plain)
        self.IssueCompleteScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.IssueCompleteScrollArea.setWidgetResizable(True)
        self.IssueCompleteScrollAreaContents = QWidget()
        self.IssueCompleteScrollAreaContents.setObjectName(u"IssueCompleteScrollAreaContents")
        self.IssueCompleteScrollAreaContents.setGeometry(QRect(0, 0, 588, 494))
        self.verticalLayout_43 = QVBoxLayout(self.IssueCompleteScrollAreaContents)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.IssueCompleteGridFrame = QFrame(self.IssueCompleteScrollAreaContents)
        self.IssueCompleteGridFrame.setObjectName(u"IssueCompleteGridFrame")
        self.gridLayout_10 = QGridLayout(self.IssueCompleteGridFrame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.verticalLayout_43.addWidget(self.IssueCompleteGridFrame)

        self.IssueCompleteScrollArea.setWidget(self.IssueCompleteScrollAreaContents)

        self.verticalLayout_42.addWidget(self.IssueCompleteScrollArea)


        self.IssueTabGrid.addWidget(self.IssueRightFrame, 3, 1, 1, 1)


        self.verticalLayout_39.addLayout(self.IssueTabGrid)

        self.tabWidget.addTab(self.IssuesTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_6.addWidget(self.TopFrame)

        self.FinishEditFrame = QFrame(self.MainFrame)
        self.FinishEditFrame.setObjectName(u"FinishEditFrame")
        self.FinishEditFrame.setEnabled(True)
        self.FinishEditFrame.setFrameShape(QFrame.StyledPanel)
        self.FinishEditFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.FinishEditFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.FinishEditFrame)

        self.BottomFrame = QFrame(self.MainFrame)
        self.BottomFrame.setObjectName(u"BottomFrame")
        sizePolicy1.setHeightForWidth(self.BottomFrame.sizePolicy().hasHeightForWidth())
        self.BottomFrame.setSizePolicy(sizePolicy1)
        self.BottomFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.BottomFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DescriptionLabel = QLabel(self.BottomFrame)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")

        self.verticalLayout.addWidget(self.DescriptionLabel)

        self.DescriptionTextScrollArea = QScrollArea(self.BottomFrame)
        self.DescriptionTextScrollArea.setObjectName(u"DescriptionTextScrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.DescriptionTextScrollArea.sizePolicy().hasHeightForWidth())
        self.DescriptionTextScrollArea.setSizePolicy(sizePolicy3)
        self.DescriptionTextScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.DescriptionTextScrollArea.setWidgetResizable(True)
        self.DescriptionTextScrollAreaContents = QWidget()
        self.DescriptionTextScrollAreaContents.setObjectName(u"DescriptionTextScrollAreaContents")
        self.DescriptionTextScrollAreaContents.setGeometry(QRect(0, 0, 1190, 69))
        self.verticalLayout_10 = QVBoxLayout(self.DescriptionTextScrollAreaContents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.DescriptionTextLabel = QLabel(self.DescriptionTextScrollAreaContents)
        self.DescriptionTextLabel.setObjectName(u"DescriptionTextLabel")
        sizePolicy2.setHeightForWidth(self.DescriptionTextLabel.sizePolicy().hasHeightForWidth())
        self.DescriptionTextLabel.setSizePolicy(sizePolicy2)
        self.DescriptionTextLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.DescriptionTextLabel)

        self.DescriptionTextScrollArea.setWidget(self.DescriptionTextScrollAreaContents)

        self.verticalLayout.addWidget(self.DescriptionTextScrollArea)


        self.verticalLayout_6.addWidget(self.BottomFrame)


        self.horizontalLayout_2.addWidget(self.MainFrame)


        self.retranslateUi(ProjectFeatureTaskIssueWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ProjectFeatureTaskIssueWindow)
    # setupUi

    def retranslateUi(self, ProjectFeatureTaskIssueWindow):
        ProjectFeatureTaskIssueWindow.setWindowTitle(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Form", None))
        self.BackBtn.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Back", None))
        self.TitleLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Project Name", None))
        self.AddNewBtn.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FeaturesTab), QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Features", None))
        self.CompletedLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Completed", None))
        self.TasksLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Tasks", None))
        self.InProgressLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"In Progress", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TasksTab), QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Tasks", None))
        self.IssueCompletedLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Completed", None))
        self.IssueLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Issues", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IssuesTab), QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Issues", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Description:", None))
        self.DescriptionTextLabel.setText("")
    # retranslateUi

