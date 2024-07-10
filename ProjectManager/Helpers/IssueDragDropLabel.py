from icecream import ic

from PySide6.QtWidgets import QLabel, QApplication
from PySide6.QtCore import Qt, QMimeData, QDataStream, QByteArray
from PySide6.QtGui import QDrag, QPixmap, QPainter


class IssueDragDropLabel(QLabel):
    def __init__(self, text, parentView, issue):
        super().__init__(text)    
        
        self.parentView = parentView
        self.issue = issue
           
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragStartPosition = event.position()
            self.parentView.rowClicked(self.issue["issueDescription"], event)


    def mouseMoveEvent(self, event):
        # If the left mouse button is not held, exit the event
        if not (event.buttons() & Qt.LeftButton):
            return
        # Checks that the drag is long enough to trigger. Tries to prevent unintentional drags 
        if (event.position() - self.dragStartPosition).manhattanLength() < QApplication.startDragDistance():
            return
        
        
        rowPixmap = self.createRowPixmap()
        drag = QDrag(self)
        mimedata = QMimeData()
        

        # Serialize data into a QByteArray
        byteArray = QByteArray()
        dataStream = QDataStream(byteArray, QDataStream.WriteOnly)
        
        dataStream.writeInt32(self.issue["projectId"])
        dataStream.writeInt32(self.issue["issueId"])
        dataStream.writeString(self.issue["isComplete"])
        dataStream.writeString(self.text())
        
        mimedata.setData('application/x-issueData', byteArray)
        drag.setMimeData(mimedata)
        
        drag.setPixmap(rowPixmap)
        drag.setHotSpot(event.position().toPoint())
        drag.exec(Qt.CopyAction | Qt.MoveAction)
        


    # """Creates a composite pixmap for the entire row."""
    def createRowPixmap(self):
        
        gridLayout = self.parentWidget().layout()
        row_index = gridLayout.getItemPosition(gridLayout.indexOf(self))[0]
        
        rowPixmap = QPixmap(self.parentWidget().width(), self.height())
        
        painter = QPainter(rowPixmap)
        painter.drawPixmap(self.parentWidget().rect(), self.grab())
        
        for col in range(gridLayout.columnCount()):
            item = gridLayout.itemAtPosition(row_index, col)
            if item is not None:
                widget = item.widget()
                if isinstance(widget, QLabel):
                    widget.render(painter, widget.pos())
        
        painter.end()
        
        return rowPixmap
