from PySide6.QtWidgets import *
from PySide6.QtGui import *

app = QApplication.instance()

class TrayMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.tray_icon_theme = self.addMenu("ToDo: Tray icon theme")

        self.light_theme_action = QAction("Light")
        self.dark_theme_action = QAction("Dark")

        self.tray_icon_theme.addAction(self.light_theme_action)
        self.tray_icon_theme.addAction(self.dark_theme_action)

        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(app.quit)

        self.addAction(self.quit_action)
