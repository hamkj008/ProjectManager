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
import resource_rc

class Ui_ProjectFeatureTaskIssueWindow(object):
    def setupUi(self, ProjectFeatureTaskIssueWindow):
        if not ProjectFeatureTaskIssueWindow.objectName():
            ProjectFeatureTaskIssueWindow.setObjectName(u"ProjectFeatureTaskIssueWindow")
        ProjectFeatureTaskIssueWindow.resize(1253, 816)
        self.verticalLayout = QVBoxLayout(ProjectFeatureTaskIssueWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(ProjectFeatureTaskIssueWindow)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 10)
        self.TopFrame = QFrame(self.MainFrame)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setFrameShape(QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.TopFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TitleFrame = QFrame(self.TopFrame)
        self.TitleFrame.setObjectName(u"TitleFrame")
        self.TitleFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.TitleFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.TitleLabel = QLabel(self.TitleFrame)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.TitleLabel)


        self.verticalLayout_3.addWidget(self.TitleFrame)

        self.SearchFrame = QFrame(self.TopFrame)
        self.SearchFrame.setObjectName(u"SearchFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchFrame.sizePolicy().hasHeightForWidth())
        self.SearchFrame.setSizePolicy(sizePolicy)
        self.SearchFrame.setFrameShape(QFrame.StyledPanel)
        self.SearchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.BackBtn = QPushButton(self.SearchFrame)
        self.BackBtn.setObjectName(u"BackBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BackBtn.sizePolicy().hasHeightForWidth())
        self.BackBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.BackBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.AddNewFrame = QFrame(self.SearchFrame)
        self.AddNewFrame.setObjectName(u"AddNewFrame")
        self.AddNewFrame.setFrameShape(QFrame.StyledPanel)
        self.AddNewFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.AddNewFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.AddNewBtn = QPushButton(self.AddNewFrame)
        self.AddNewBtn.setObjectName(u"AddNewBtn")
        icon = QIcon()
        icon.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddNewBtn.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.AddNewBtn)


        self.horizontalLayout_8.addWidget(self.AddNewFrame)


        self.verticalLayout_3.addWidget(self.SearchFrame)


        self.verticalLayout_2.addWidget(self.TopFrame)

        self.BottomFrame = QFrame(self.MainFrame)
        self.BottomFrame.setObjectName(u"BottomFrame")
        self.BottomFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.BottomFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ProjectTabFrame = QFrame(self.BottomFrame)
        self.ProjectTabFrame.setObjectName(u"ProjectTabFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ProjectTabFrame.sizePolicy().hasHeightForWidth())
        self.ProjectTabFrame.setSizePolicy(sizePolicy2)
        self.ProjectTabFrame.setFrameShape(QFrame.StyledPanel)
        self.ProjectTabFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ProjectTabFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.ProjectTabFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.FeaturesTab = QWidget()
        self.FeaturesTab.setObjectName(u"FeaturesTab")
        sizePolicy2.setHeightForWidth(self.FeaturesTab.sizePolicy().hasHeightForWidth())
        self.FeaturesTab.setSizePolicy(sizePolicy2)
        self.verticalLayout_44 = QVBoxLayout(self.FeaturesTab)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(20, 20, 20, 20)
        self.tabWidget.addTab(self.FeaturesTab, "")
        self.TasksTab = QWidget()
        self.TasksTab.setObjectName(u"TasksTab")
        sizePolicy2.setHeightForWidth(self.TasksTab.sizePolicy().hasHeightForWidth())
        self.TasksTab.setSizePolicy(sizePolicy2)
        self.TasksTab.setStyleSheet(u"")
        self.verticalLayout_45 = QVBoxLayout(self.TasksTab)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.TaskTabGrid = QFrame(self.TasksTab)
        self.TaskTabGrid.setObjectName(u"TaskTabGrid")
        self.TaskTabGridLayout_4 = QGridLayout(self.TaskTabGrid)
        self.TaskTabGridLayout_4.setObjectName(u"TaskTabGridLayout_4")
        self.TaskTabGridLayout_4.setHorizontalSpacing(10)
        self.TaskTabGridLayout_4.setVerticalSpacing(0)
        self.TaskTabGridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.TaskRightFrame = QFrame(self.TaskTabGrid)
        self.TaskRightFrame.setObjectName(u"TaskRightFrame")
        self.TaskRightFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskRightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.TaskRightFrame)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.TaskCompleteScrollArea = QScrollArea(self.TaskRightFrame)
        self.TaskCompleteScrollArea.setObjectName(u"TaskCompleteScrollArea")
        self.TaskCompleteScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.TaskCompleteScrollArea.setWidgetResizable(True)
        self.TaskCompleteScrollAreaContents = QWidget()
        self.TaskCompleteScrollAreaContents.setObjectName(u"TaskCompleteScrollAreaContents")
        self.TaskCompleteScrollAreaContents.setGeometry(QRect(0, 0, 379, 574))
        self.verticalLayout_47 = QVBoxLayout(self.TaskCompleteScrollAreaContents)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.TaskCompleteScrollArea.setWidget(self.TaskCompleteScrollAreaContents)

        self.verticalLayout_46.addWidget(self.TaskCompleteScrollArea)


        self.TaskTabGridLayout_4.addWidget(self.TaskRightFrame, 4, 2, 1, 1)

        self.TaskCompletedLabelFrame = QFrame(self.TaskTabGrid)
        self.TaskCompletedLabelFrame.setObjectName(u"TaskCompletedLabelFrame")
        self.TaskCompletedLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskCompletedLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.TaskCompletedLabelFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 10, 0, 10)
        self.CompletedLabel = QLabel(self.TaskCompletedLabelFrame)
        self.CompletedLabel.setObjectName(u"CompletedLabel")
        self.CompletedLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.CompletedLabel)


        self.TaskTabGridLayout_4.addWidget(self.TaskCompletedLabelFrame, 1, 2, 1, 1)

        self.TaskCentralFrame = QFrame(self.TaskTabGrid)
        self.TaskCentralFrame.setObjectName(u"TaskCentralFrame")
        self.TaskCentralFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskCentralFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.TaskCentralFrame)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.TaskInProgressScrollArea = QScrollArea(self.TaskCentralFrame)
        self.TaskInProgressScrollArea.setObjectName(u"TaskInProgressScrollArea")
        self.TaskInProgressScrollArea.setFrameShape(QFrame.NoFrame)
        self.TaskInProgressScrollArea.setFrameShadow(QFrame.Plain)
        self.TaskInProgressScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.TaskInProgressScrollArea.setWidgetResizable(True)
        self.TaskInProgressScrollAreaContents = QWidget()
        self.TaskInProgressScrollAreaContents.setObjectName(u"TaskInProgressScrollAreaContents")
        self.TaskInProgressScrollAreaContents.setGeometry(QRect(0, 0, 382, 576))
        self.verticalLayout_49 = QVBoxLayout(self.TaskInProgressScrollAreaContents)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.TaskInProgressScrollArea.setWidget(self.TaskInProgressScrollAreaContents)

        self.verticalLayout_48.addWidget(self.TaskInProgressScrollArea)


        self.TaskTabGridLayout_4.addWidget(self.TaskCentralFrame, 4, 1, 1, 1)

        self.TaskLeftFrame = QFrame(self.TaskTabGrid)
        self.TaskLeftFrame.setObjectName(u"TaskLeftFrame")
        self.TaskLeftFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskLeftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.TaskLeftFrame)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.TaskScrollArea = QScrollArea(self.TaskLeftFrame)
        self.TaskScrollArea.setObjectName(u"TaskScrollArea")
        self.TaskScrollArea.setFrameShape(QFrame.NoFrame)
        self.TaskScrollArea.setFrameShadow(QFrame.Plain)
        self.TaskScrollArea.setLineWidth(0)
        self.TaskScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.TaskScrollArea.setWidgetResizable(True)
        self.TaskScrollAreaContents = QWidget()
        self.TaskScrollAreaContents.setObjectName(u"TaskScrollAreaContents")
        self.TaskScrollAreaContents.setGeometry(QRect(0, 0, 381, 576))
        self.verticalLayout_51 = QVBoxLayout(self.TaskScrollAreaContents)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.TaskScrollArea.setWidget(self.TaskScrollAreaContents)

        self.verticalLayout_50.addWidget(self.TaskScrollArea)


        self.TaskTabGridLayout_4.addWidget(self.TaskLeftFrame, 4, 0, 1, 1)

        self.TasksLabelFrame = QFrame(self.TaskTabGrid)
        self.TasksLabelFrame.setObjectName(u"TasksLabelFrame")
        self.TasksLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.TasksLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.TasksLabelFrame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 10, 0, 10)
        self.TasksLabel = QLabel(self.TasksLabelFrame)
        self.TasksLabel.setObjectName(u"TasksLabel")
        self.TasksLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.TasksLabel)


        self.TaskTabGridLayout_4.addWidget(self.TasksLabelFrame, 1, 0, 1, 1)

        self.TaskInProgressLabelFrame = QFrame(self.TaskTabGrid)
        self.TaskInProgressLabelFrame.setObjectName(u"TaskInProgressLabelFrame")
        self.TaskInProgressLabelFrame.setStyleSheet(u"")
        self.TaskInProgressLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskInProgressLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.TaskInProgressLabelFrame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 10, 0, 10)
        self.InProgressLabel = QLabel(self.TaskInProgressLabelFrame)
        self.InProgressLabel.setObjectName(u"InProgressLabel")
        self.InProgressLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.InProgressLabel)


        self.TaskTabGridLayout_4.addWidget(self.TaskInProgressLabelFrame, 1, 1, 1, 1)


        self.verticalLayout_45.addWidget(self.TaskTabGrid)

        self.tabWidget.addTab(self.TasksTab, "")
        self.IssuesTab = QWidget()
        self.IssuesTab.setObjectName(u"IssuesTab")
        sizePolicy2.setHeightForWidth(self.IssuesTab.sizePolicy().hasHeightForWidth())
        self.IssuesTab.setSizePolicy(sizePolicy2)
        self.verticalLayout_52 = QVBoxLayout(self.IssuesTab)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.IssueTabGrid = QGridLayout()
        self.IssueTabGrid.setObjectName(u"IssueTabGrid")
        self.IssueCompletedLabelFrame = QFrame(self.IssuesTab)
        self.IssueCompletedLabelFrame.setObjectName(u"IssueCompletedLabelFrame")
        self.IssueCompletedLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueCompletedLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.IssueCompletedLabelFrame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, 10, 10, 10)
        self.IssueCompletedLabel = QLabel(self.IssueCompletedLabelFrame)
        self.IssueCompletedLabel.setObjectName(u"IssueCompletedLabel")
        self.IssueCompletedLabel.setLineWidth(1)
        self.IssueCompletedLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.IssueCompletedLabel)


        self.IssueTabGrid.addWidget(self.IssueCompletedLabelFrame, 0, 1, 1, 1)

        self.IssueLabelFrame = QFrame(self.IssuesTab)
        self.IssueLabelFrame.setObjectName(u"IssueLabelFrame")
        self.IssueLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.IssueLabelFrame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(10, 10, 10, 10)
        self.IssueLabel = QLabel(self.IssueLabelFrame)
        self.IssueLabel.setObjectName(u"IssueLabel")
        self.IssueLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.IssueLabel)


        self.IssueTabGrid.addWidget(self.IssueLabelFrame, 0, 0, 1, 1)

        self.IssueLeftFrame = QFrame(self.IssuesTab)
        self.IssueLeftFrame.setObjectName(u"IssueLeftFrame")
        self.IssueLeftFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueLeftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.IssueLeftFrame)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.IssueScrollArea = QScrollArea(self.IssueLeftFrame)
        self.IssueScrollArea.setObjectName(u"IssueScrollArea")
        self.IssueScrollArea.setFrameShape(QFrame.NoFrame)
        self.IssueScrollArea.setFrameShadow(QFrame.Plain)
        self.IssueScrollArea.setLineWidth(1)
        self.IssueScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.IssueScrollArea.setWidgetResizable(True)
        self.IssueScrollAreaContents = QWidget()
        self.IssueScrollAreaContents.setObjectName(u"IssueScrollAreaContents")
        self.IssueScrollAreaContents.setGeometry(QRect(0, 0, 588, 568))
        self.verticalLayout_54 = QVBoxLayout(self.IssueScrollAreaContents)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.IssueGridFrame = QFrame(self.IssueScrollAreaContents)
        self.IssueGridFrame.setObjectName(u"IssueGridFrame")
        self.gridLayout_11 = QGridLayout(self.IssueGridFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")

        self.verticalLayout_54.addWidget(self.IssueGridFrame)

        self.IssueScrollArea.setWidget(self.IssueScrollAreaContents)

        self.verticalLayout_53.addWidget(self.IssueScrollArea)


        self.IssueTabGrid.addWidget(self.IssueLeftFrame, 3, 0, 1, 1)

        self.IssueRightFrame = QFrame(self.IssuesTab)
        self.IssueRightFrame.setObjectName(u"IssueRightFrame")
        self.IssueRightFrame.setFrameShape(QFrame.StyledPanel)
        self.IssueRightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.IssueRightFrame)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.IssueCompleteScrollArea = QScrollArea(self.IssueRightFrame)
        self.IssueCompleteScrollArea.setObjectName(u"IssueCompleteScrollArea")
        self.IssueCompleteScrollArea.setFrameShape(QFrame.NoFrame)
        self.IssueCompleteScrollArea.setFrameShadow(QFrame.Plain)
        self.IssueCompleteScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.IssueCompleteScrollArea.setWidgetResizable(True)
        self.IssueCompleteScrollAreaContents = QWidget()
        self.IssueCompleteScrollAreaContents.setObjectName(u"IssueCompleteScrollAreaContents")
        self.IssueCompleteScrollAreaContents.setGeometry(QRect(0, 0, 587, 568))
        self.verticalLayout_56 = QVBoxLayout(self.IssueCompleteScrollAreaContents)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.IssueCompleteGridFrame = QFrame(self.IssueCompleteScrollAreaContents)
        self.IssueCompleteGridFrame.setObjectName(u"IssueCompleteGridFrame")
        self.gridLayout_12 = QGridLayout(self.IssueCompleteGridFrame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")

        self.verticalLayout_56.addWidget(self.IssueCompleteGridFrame)

        self.IssueCompleteScrollArea.setWidget(self.IssueCompleteScrollAreaContents)

        self.verticalLayout_55.addWidget(self.IssueCompleteScrollArea)


        self.IssueTabGrid.addWidget(self.IssueRightFrame, 3, 1, 1, 1)


        self.verticalLayout_52.addLayout(self.IssueTabGrid)

        self.tabWidget.addTab(self.IssuesTab, "")

        self.verticalLayout_8.addWidget(self.tabWidget)


        self.verticalLayout_7.addWidget(self.ProjectTabFrame)

        self.DescriptionFrame = QFrame(self.BottomFrame)
        self.DescriptionFrame.setObjectName(u"DescriptionFrame")
        self.DescriptionFrame.setFrameShape(QFrame.StyledPanel)
        self.DescriptionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.DescriptionFrame)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.DescriptionLabel = QLabel(self.DescriptionFrame)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")
        sizePolicy.setHeightForWidth(self.DescriptionLabel.sizePolicy().hasHeightForWidth())
        self.DescriptionLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.DescriptionLabel)

        self.DescriptionScrollArea = QScrollArea(self.DescriptionFrame)
        self.DescriptionScrollArea.setObjectName(u"DescriptionScrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.DescriptionScrollArea.sizePolicy().hasHeightForWidth())
        self.DescriptionScrollArea.setSizePolicy(sizePolicy3)
        self.DescriptionScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.DescriptionScrollArea.setWidgetResizable(True)
        self.DescriptionScrollAreaContents = QWidget()
        self.DescriptionScrollAreaContents.setObjectName(u"DescriptionScrollAreaContents")
        self.DescriptionScrollAreaContents.setGeometry(QRect(0, 0, 1208, 69))
        self.verticalLayout_11 = QVBoxLayout(self.DescriptionScrollAreaContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.DescriptionTextFrame = QFrame(self.DescriptionScrollAreaContents)
        self.DescriptionTextFrame.setObjectName(u"DescriptionTextFrame")
        self.DescriptionTextFrame.setFrameShape(QFrame.StyledPanel)
        self.DescriptionTextFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.DescriptionTextFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.DescriptionTextLabel = QLabel(self.DescriptionTextFrame)
        self.DescriptionTextLabel.setObjectName(u"DescriptionTextLabel")
        self.DescriptionTextLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_12.addWidget(self.DescriptionTextLabel)


        self.verticalLayout_11.addWidget(self.DescriptionTextFrame)

        self.DescriptionScrollArea.setWidget(self.DescriptionScrollAreaContents)

        self.verticalLayout_9.addWidget(self.DescriptionScrollArea)


        self.verticalLayout_7.addWidget(self.DescriptionFrame)


        self.verticalLayout_2.addWidget(self.BottomFrame)


        self.verticalLayout.addWidget(self.MainFrame)


        self.retranslateUi(ProjectFeatureTaskIssueWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ProjectFeatureTaskIssueWindow)
    # setupUi

    def retranslateUi(self, ProjectFeatureTaskIssueWindow):
        ProjectFeatureTaskIssueWindow.setWindowTitle(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Project Name", None))
        self.BackBtn.setText(QCoreApplication.translate("ProjectFeatureTaskIssueWindow", u"Back", None))
        self.AddNewBtn.setText("")
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

