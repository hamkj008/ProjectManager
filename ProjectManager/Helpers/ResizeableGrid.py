from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Qt, QEvent
from icecream import ic
from functools import partial


# ========================================================================================
      

class ResizeableGrid(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create a grid layout
        self.grid = QGridLayout(self)
        self.grid.setContentsMargins(0,0,0,0)
        self.grid.setVerticalSpacing(0)
        self.setLayout(self.grid)
        self.frameIndexMap = {}


    # ---------------------------------------------------        


    def setFrames(self, frames):
        self.frames = frames

        # Add frames to the grid layout
        for i, frame in enumerate(self.frames):
            
            self.frameIndexMap[frame] = i   # Map the frames to their index 
            frame.installEventFilter(self)  # The event filter will handle the mouse press event
            
            # frame.mousePressEvent = partial(self.mousePressEvent, i) # Avoid partial with mouse press events. Only expects the event otherwise error 
            frame.mouseMoveEvent = self.mouseMoveEvent
            frame.mouseReleaseEvent = self.mouseReleaseEvent           

        # Track resizing state
        self.resizing = False
        self.resizingFrame = None
        self.startX = 0
        self.start_width = 0
    
        
    # ---------------------------------------------------
    
    
    """ Enables mouse tracking for all the children of the frame, so that mouse tracking is continuous across the whole area. 
    Without this mouse tracking stops as soon as the mouse crosses from the parent area into the child area. 
    The mouse tracking detects when the cursor is near the divider and switches back to normal cursor when moving away from the divider,
    even when crossing child territory. """   
    
    def enableMouseTrackingRecursive(self):
        def enableMouseTracking(widget):
            if isinstance(widget, QWidget):
                widget.setMouseTracking(True)
                for child in widget.findChildren(QWidget):
                    enableMouseTracking(child)

        enableMouseTracking(self)


    # ========================================================================================   


    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            
            for frame in self.frames:
                self.MousePressHandler(self.frameIndexMap[frame], event)
                return True 
        return super().eventFilter(obj, event)
    
                
    def MousePressHandler(self, frame_index, event):
        for frame in self.frames:
            divider  = frame.geometry().right() - frame.geometry().left()
            if (event.pos().x() <= divider  and event.pos().x() >= divider - 20):     
                self.resizing = True
                self.startX = event.globalX()
                self.resizingFrame = self.frames[frame_index]
                self.start_width = self.resizingFrame.width()
                

    # def mousePressEvent(self, frame_index, event):
        
    #     super().mousePressEvent(event)
        
    #     for frame in self.frames:
    #         divider  = frame.geometry().right() - frame.geometry().left()
    #         if (event.pos().x() <= divider  and event.pos().x() >= divider - 20):     
    #             self.resizing = True
    #             self.startX = event.globalX()
    #             self.resizingFrame = self.frames[frame_index]
    #             self.start_width = self.resizingFrame.width()
            
    # ========================================================================================   
    
    
    def mouseMoveEvent(self, event):
        
        for frame in self.frames:
            divider  = frame.geometry().right() - frame.geometry().left()
            if (event.pos().x() <= divider and event.pos().x() >= divider - 20):
                self.setCursor(Qt.SplitHCursor)
                break
            else:
                self.setCursor(Qt.ArrowCursor)  
        self.update() 
                

        if self.resizing:
            delta = event.globalX() - self.startX
            newWidth = self.start_width + delta            
            minWidth = 150
            columnNumber = 0
            
            # Find the column number of the frame that is being moved to move all frames in the column at once
            for colNum in range(self.grid.columnCount()):
                for row in range(self.grid.rowCount()):
                    item = self.grid.itemAtPosition(row, colNum)
                    if item:
                        widget = item.widget()
                        if widget:
                            if widget == self.resizingFrame:
                                columnNumber = colNum
                 
            # Retrieve the widgets in the column
            colWidgets = self.getColumnWidgets(columnNumber)
                
            for widget in colWidgets:
                widget.setFixedWidth(max(minWidth, newWidth))  # ensure minimum width


    # ========================================================================================   
    
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = False
            self.resizingFrame = None


    # ========================================================================================   
    

    def getColumnWidgets(self, colNum):
        
        widgets = []
        for row in range(self.grid.rowCount()):
            item = self.grid.itemAtPosition(row, colNum)
            if item:
                widget = item.widget()
                if widget:
                    widgets.append(widget)
        return widgets
    

    # ========================================================================================   
           