from icecream import ic
from enum import Enum, auto

# ========================================================================================
      
class Theme(Enum):

    DARK    = auto()
    LIGHT   = auto()
    
# =============================================================================================


""" Class stores all presentation qss based information. 
Facilitates a modular approach to presentation, enabling presentation modes. 
Also allows for absorbing qss files into final build"""

class QSSController:

    def __init__(self):
        ic("qssController")

        self.themes = {
            Theme.DARK: {
                "primaryColor"          : "#343335",
                "secondaryColor"        : "#686b6d",
                "tertiaryColor"         : "black",
                "textColor"             : "white",
                "borderColor"           : "black",
                "buttonColor"           : "black",
                "buttonTextColor"       : "white",
                "buttonHoverColor"      : "blue",
                "rowColor"              : "#686b6d"
            },
            
            Theme.LIGHT: {
                "primaryColor"          : "#8d979b",
                "secondaryColor"        : "white",
                "tertiaryColor"         : "white",
                "textColor"             : "black",
                "borderColor"           : "black",
                "buttonColor"           : "black",
                "buttonTextColor"       : "white",
                "buttonHoverColor"      : "blue",
                "rowColor"              : "#8d979b"
            }
        }


        self.setTheme(Theme.DARK)


    # ========================================================================================
      

    def createTheme(self, themeName, parent, overrides):
        if parent not in self.themes:
            raise ValueError(f"Parent theme {parent} does not exist")

        newTheme = self.themes[parent].copy()
        newTheme.update(overrides)
        self.themes[themeName] = newTheme


    # ========================================================================================
     

    def setTheme(self, chosenTheme):

        if chosenTheme not in self.themes:
            raise ValueError(f"Theme {chosenTheme} does not exist")

        self.currentTheme = chosenTheme
        self.hoverEnter = f"""background-color: blue;"""
        self.hoverLeave = f"""background-color: {self.themes[self.currentTheme]["rowColor"]};"""

   
    # ========================================================================================
     

    def getStandardStyle(self):

        return f""" 
                CustomWindow {{
                    background-color: {self.themes[self.currentTheme]["secondaryColor"]};   
                    border: 2px solid {self.themes[self.currentTheme]["borderColor"]}; 
                }}

                QLabel, QTextEdit, QLineEdit {{
                    color: {self.themes[self.currentTheme]["textColor"]};
                    padding: 7px;
                }}

                QLineEdit {{
                    border-radius: 10px;
                    border: 2px solid {self.themes[self.currentTheme]["borderColor"]};	
	                color: {self.themes[self.currentTheme]["textColor"]};
                    background-color: {self.themes[self.currentTheme]["secondaryColor"]};
                }}

                QPushButton {{
                    color: {self.themes[self.currentTheme]["buttonTextColor"]};
                    background-color: {self.themes[self.currentTheme]["buttonColor"]};
                    border-radius: 10px;
                    padding: 5px 7px 5px 7px;
                }}

                QPushButton:hover {{
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}

               
                /*  ------- Menu Bar ---------- */

                QMenuBar {{
                    color: {self.themes[self.currentTheme]["textColor"]};
                }}

                QMenuBar::item:selected {{
                    color: {self.themes[self.currentTheme]["tertiaryColor"]};
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}

                #containerWidget {{
                    background-color: {self.themes[self.currentTheme]["secondaryColor"]};
                    border-left: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                    border-right: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                }}
                /* ------------------------------- */

                #DescriptionFrame {{
                    border: 1px solid {self.themes[self.currentTheme]["textColor"]};
                    padding: 5px;
                }}

                #titleBar {{
                    background-color: {self.themes[self.currentTheme]["primaryColor"]}; 
                    border: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                }}

                #titleLabel {{
                    color: {self.themes[self.currentTheme]["textColor"]};
                }}

                #titleBarButton {{
                    background-color: {self.themes[self.currentTheme]["buttonColor"]};
                }}

                #titleBarButton:hover {{
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}


                /* ------------------------------------------------------------------------- */


                #row {{
                    background-color: {self.themes[self.currentTheme]["rowColor"]};
                    border-radius: 10px;
                }}

                #header {{
                    padding: 5px;
                }}

                #AddNewBtn {{
                    background-color: {self.themes[self.currentTheme]["buttonColor"]};
                    color: {self.themes[self.currentTheme]["secondaryColor"]};
                    min-width: 30px;
                    min-height: 30px;
                    width: 30px;
                    height: 30px; 
                    border-radius: 15px;
                    padding: 0px;
                }}

                #AddNewBtn:hover {{
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}


                #MainFrame, #ProjectScrollAreaContents, #DescriptionScrollAreaContents {{
                    background-color: {self.themes[self.currentTheme]["primaryColor"]};    
                }}

                #MainFrame {{
                    border-radius: 10px;
                }}


                #TitleLabel, #PreferencesTitleLabel {{
                    font-weight: bold;
                }}
                           
                
                #PreferencesGridFrame, #ProjectGridFrame, #DescriptionTextFrame, #AboutFrame {{
                    background-color: {self.themes[self.currentTheme]["tertiaryColor"]};
                }}   
                    
        """


    # ======================================================================================== 
    

    def getAddStyle(self):
        
        return f"""
                    QTextEdit, QLineEdit, QComboBox, QDateEdit {{
                        font-size: 12pt;
                        min-height: 40px;
                    }}
                            
                    QTextEdit, QLineEdit {{
                        border-radius: 10px;
                    }}
 
                    QTextEdit, QLineEdit {{
                        background-color: {self.themes[self.currentTheme]["tertiaryColor"]};
                        color: {self.themes[self.currentTheme]["textColor"]};
                    }}  

                    #AddFrame {{
                        background-color: {self.themes[self.currentTheme]["primaryColor"]}
                    }}
                            
                    #AddNewBtn {{
                        background-color: {self.themes[self.currentTheme]["buttonColor"]};
                        font: 10pt "Arial";
                        font-weight: bold;
	                    color: {self.themes[self.currentTheme]["textColor"]};
                        border: 2px solid {self.themes[self.currentTheme]["borderColor"]};	
                        border-radius: 10px;
                        padding: 8px;
                        min-width: 100px;
                        min-height: 30px;
                    }}

                    #AddNewBtn:hover {{
                        background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                    }}

                """
    

    # ======================================================================================== 
    

    def getProjectFeatureTaskIssueStyle(self):
        
        return f"""
                QTabWidget::pane {{
                    background-color: lightgray; /* Set the background color of the tab widget */
                }}


                QTabBar::tab:selected {{
                    background-color: lightblue; /* Set the background color of the selected tab */
                }}


                QTabBar::tab:!selected {{
                    background-color: gray; /* Set the background color of unselected tabs */
                }}


                #IssuesTab, #FeaturesTab, #TasksTab,
                #TaskScrollAreaContents, #TaskInProgressScrollAreaContents, #TaskCompleteScrollAreaContents, 
                #IssueScrollAreaContents, #IssueCompleteScrollAreaContents, #AddNewBtnFrame {{
                    background-color: {self.themes[self.currentTheme]["tertiaryColor"]};
                }}
                                            
                #editDescriptionText {{
                    color: white;
                    background-color: {self.themes[self.currentTheme]["tertiaryColor"]};
                }}
                                            

                #FeaturesTab, #TasksLabelFrame, #TaskInProgressLabelFrame, #TaskCompletedLabelFrame,
                #TaskLeftFrame, #TaskCentralFrame, #TaskRightFrame, 
                #IssueLabelFrame, #IssueCompletedLabelFrame, 
                #IssueLeftFrame, #IssueRightFrame {{
                    border: 1px solid {self.themes[self.currentTheme]["textColor"]};
                    border-radius: 0px;
                }}




                #taskLabel {{
                    background-color: {self.themes[self.currentTheme]["rowColor"]};
                    border-radius: 10px;
                    padding: 2px 5px 2px 5px;
                }}

                #placeholder {{
                    font-size: 5pt;
                    padding: 5px;
                }}
            """
    

    # ======================================================================================== 
    

    def getDialogStyle(self):
        return f"""
                QLabel {{
                    font-size: 15pt;
                    background-color #fcfcfc;
                    color: white;
                    padding: 10px;
                }}
                
                #dialog {{
                    background-color: {self.themes[self.currentTheme]["secondaryColor"]};
                }}
            """
