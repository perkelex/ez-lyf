from PySide6.QtWidgets import *

class HLine(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        line_widget_layout = QHBoxLayout(self)
        line_widget_layout.setContentsMargins(0, 0, 0, 0)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)

        line_widget_layout.addWidget(line)