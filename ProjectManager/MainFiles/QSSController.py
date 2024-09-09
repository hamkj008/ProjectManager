from icecream import ic

# ========================================================================================
      

""" Class stores all presentation qss based information. 
Facilitates a modular approach to presentation, enabling presentation modes. 
Also allows for absorbing qss files into final build"""

class QSSController:
    def __init__(self):
        ic("qssController")

         # -- Frames --
        self.modeProgramTitleFrameColor         =   "#024087"       # slate blue
        self.modePrimaryColor                   =   "black"
        self.modeSecondaryColor                 =   "#4b4a4c"
        self.modeFrameBorderColor               =   self.modePrimaryColor
        
        # -- Label --
        self.modeLabelTextColor                 =   "white"
        self.modeLabelBackgroundColor           =   self.modePrimaryColor
        
        # -- Button --
        self.modeButtonTextColor                =   self.modeLabelTextColor
        self.modeButtonBackgroundColor          =   self.modeSecondaryColor
        
        # -- Search --
        self.modeSearchColor                    =   self.modeLabelTextColor
        self.modeSearchBackgroundColor          =   self.modeSecondaryColor
        
        # -- Line Edit --
        self.modeLineEditColor                  =   self.modeLabelTextColor
        self.modeLineEditBackgroundColor        =   self.modePrimaryColor
        
        # -- Hover --
        self.hoverEnterStyle                    =   "background-color: #024087;"
        self.hoverLeaveStyle                    =   "background-color: #4b4a4c;"
        
        self.modeLineColor                      =   self.modeProgramTitleFrameColor


    # ========================================================================================
      
    def getStandardStyle(self):
        
        standardStyle = f""" /** ---------- GENERIC -----------------  **/ 
                            QLabel {{
                                font-size: 15pt;
                                color: {self.modeLabelTextColor};
                                padding: 10px;
                            }}

                            QFrame {{
                                border-radius: 10px;
                                border-style: outset; 
                            }}

                            QLineEdit {{
                                border-radius: 10px;
                                border-style: outset;
                                border: 2px solid {self.modeFrameBorderColor};	
                                font: 15pt "Arial";
	                            color: {self.modeSearchColor};
                                min-height: 40px;
                                background-color: {self.modeSearchBackgroundColor};
                            }}


                            QPushButton {{
                                background-color: {self.modeButtonBackgroundColor};
                                font: 10pt "Arial";
                                font-weight: bold;
	                            color: {self.modeButtonTextColor};
                                border: 2px solid {self.modeFrameBorderColor};	
                                border-radius: 10px;
                                border-style: outset;
                                padding: 8px;
                                min-width: 60px;
                                min-height: 20px;
                            }}


                            QPushButton:hover {{
                                {self.hoverEnterStyle}
                            }}

                                 
                            /** ----------- NAMED ---------------------  **/ 
                            #MainFrame, #ProjectScrollAreaContents, #DescriptionScrollAreaContents {{
                                background-color: {self.modeSecondaryColor};    
                            }}

                            #TitleFrame, #PreferencesTitle {{
                                background-color: {self.modeProgramTitleFrameColor};
                                border: 3px solid {self.modeFrameBorderColor};
                            }}

                            #TitleLabel, #PreferencesTitleLabel {{
                                font: 20pt "Papyrus";
                                font-weight: bold;
                                color: white;
                            }}
                            
                            #PreferencesGridFrame, #ProjectGridFrame, #DescriptionFrame {{
                                background-color: {self.modePrimaryColor};
                            }}   

                            #row {{
                                background-color: {self.modeSecondaryColor};
                                border-radius: 0px;
                            }}
                            
                            /** Changing font size, padding, width/height, border **/
                            #AddNewBtn {{
                                background-color: {self.modeButtonBackgroundColor};
                                font: 15pt "Arial";
                                color: {self.modeButtonTextColor};
                                padding: 5px;
                                min-width: 30px;
                                min-height: 30px;
                                width: 30px;
                                height: 30px;
                                border: 3px solid {self.modeFrameBorderColor};
                                border-radius: 15px;
                                border-style: inset; 
                            }}
                            
                            #AddNewBtn:hover {{
                                {self.hoverEnterStyle}
                            }}
                            """        

        return standardStyle
    

    # ======================================================================================== 
    
    def getAddStyle(self):
        
        addStyle = f"""QTextEdit, QLineEdit, QComboBox, QDateEdit {{
                                font-size: 12pt;
                                min-height: 40px;
                            }}
                            
                            QTextEdit, QLineEdit {{
                                border-radius: 10px;
                            }}
                    
                            QTextEdit, QLineEdit {{
                                background-color: {self.modeLineEditBackgroundColor};
                                color: {self.modeLineEditColor};
                            }}  
                            
                            #AddNewBtn {{
                                background-color: #4b4a4c;
                                font: 10pt "Arial";
                                font-weight: bold;
	                            color: black;
                                border: 2px solid black;	
                                border-radius: 10px;
                                border-style: outset;
                                padding: 8px;
                                min-width: 80px;
                                min-height: 20px;
                            }}

                            #AddNewBtn:hover {{
                                background-color: #024087;
                            }}

                            /* --------------------------------------------------- */ """
        
        return addStyle
    

    # ======================================================================================== 
    

    def getProjectFeatureTaskIssueStyle(self):
        
        projectFeatureTaskIssueStyle = """QTabWidget::pane {
                                                background-color: lightgray; /* Set the background color of the tab widget */
                                            }


                                            QTabBar::tab:selected {
                                                background-color: lightblue; /* Set the background color of the selected tab */
                                            }


                                            QTabBar::tab:!selected {
                                                background-color: gray; /* Set the background color of unselected tabs */
                                            }


                                            #IssuesTab, #FeaturesTab, #TasksTab,
                                            #TaskScrollAreaContents, #TaskInProgressScrollAreaContents, #TaskCompleteScrollAreaContents, 
                                            #IssueScrollAreaContents, #IssueCompleteScrollAreaContents,
                                            #DescriptionTextFrame, #AddNewBtnFrame {
                                                background-color: black;
                                            }
                                            
                                            #editDescriptionText {
                                                color: white;
                                                background-color: black;
                                            }
                                            

                                            #TasksLabelFrame, #TaskInProgressLabelFrame, #TaskCompletedLabelFrame,
                                            #TaskLeftFrame, #TaskCentralFrame, #TaskRightFrame, 
                                            #IssueLabelFrame, #IssueCompletedLabelFrame, 
                                            #IssueLeftFrame, #IssueRightFrame {
                                                border: 2px solid white;
                                                border-radius: 0px;
                                            }


                                            #FeaturesTab, #TasksTab, #IssuesTab {
                                                border-radius: 10px;
                                                border-style: outset;
                                                border: 2px solid white;
                                            }


                                            #tabWidget, #ProjectNameFrame {
                                                background-color: #4b4a4c;
                                            }


                                            #taskLabel {
                                                font-size: 12pt;
                                                background-color: #4b4a4c;
                                                color: white;
                                                padding: 5px;
                                            }

                                            #placeholder {
                                                font-size: 5pt;
                                                padding: 5px;
                                            } """
        return projectFeatureTaskIssueStyle
    

    # ======================================================================================== 
    

    def getDialogStyle(self):
        dialogStyle = f"""QLabel {{
                                font-size: 15pt;
                                background-color #fcfcfc;
                                color: white;
                                padding: 10px;
                            }}
                
                            #dialog {{
                                background-color: {self.modePrimaryColor};
                            }}
                            """
        return dialogStyle
