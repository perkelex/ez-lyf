from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from widgets.HorizontalLine import HLine
from functools import partial
from utils.MildEncryption import hide, reveal, isValidToken
from enum import Enum
import json

class ClipboardMessage(str, Enum):
    EMPTY = "Clipboard is empty"
    CONTENT = "Clipboard has content"

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowTitle("EZ Lyf")
        self.setMinimumWidth(200)
        self.setMinimumHeight(150)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        self.buttons_grid = QWidget()
        self.buttons_grid_layout = QGridLayout(self.buttons_grid)
        self.buttons_grid_layout.setContentsMargins(0, 0, 0, 0)

        self.control_section = QWidget()
        self.control_section_layout = QHBoxLayout(self.control_section)
        self.control_section_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(self.buttons_grid)
        self.main_layout.addWidget(HLine())
        self.main_layout.addWidget(self.control_section)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clearClipboard)
        self.control_section_layout.addWidget(clear_button)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(QApplication.instance().exit)
        self.control_section_layout.addWidget(exit_button)

        self.parse_config()
        self.updateStatusBar(ClipboardMessage.EMPTY)

    def updateStatusBar(self, message: str):
        self.statusBar().showMessage(message)
        match message:
            case ClipboardMessage.EMPTY:
                self.statusBar().setStyleSheet("background-color: rgba(0, 255, 0, 0.75)")
            case ClipboardMessage.CONTENT:
                self.statusBar().setStyleSheet("background-color: rgba(255, 255, 0, 0.75)")

    def clearClipboard(self):
        QGuiApplication.clipboard().clear()
        self.updateStatusBar(ClipboardMessage.EMPTY)

    def cbButtonClickedEvent(self, content: str):
        QGuiApplication.clipboard().setText(content)
        self.updateStatusBar(ClipboardMessage.CONTENT)

    def parse_config(self):
        with open("config.json", "r+") as config_file:
            config_needs_dumping = False
            config = json.load(config_file)
            for row_num, config_button in enumerate(config["buttons"]):
                match config_button["type"]:
                    case "email":
                        for col_num, part in enumerate(config_button["content"].split("@")):
                            if col_num == 0:
                                button = QPushButton(part)
                                button.clicked.connect(partial(self.cbButtonClickedEvent, part))
                            else:
                                button = QPushButton("@" + part)
                                button.clicked.connect(partial(self.cbButtonClickedEvent, config_button["content"]))
                            self.buttons_grid_layout.addWidget(button, row_num, col_num)
                    case "obscured": # "●"
                        button = QPushButton("●" * 10)
                        if not isValidToken(config_button["content"]):
                            config_button["content"] = hide(config_button["content"])
                            config_needs_dumping = True
                        button.clicked.connect(partial(self.cbButtonClickedEvent, reveal(config_button["content"])))
                        self.buttons_grid_layout.addWidget(button, row_num, 0)
                        if "hint" in config_button:
                            self.buttons_grid_layout.addWidget(QLabel(config_button["hint"]), row_num, 1)
                    case _:
                        button = QPushButton(config_button["content"])
                        button.clicked.connect(partial(self.cbButtonClickedEvent, config_button["content"]))
                        self.buttons_grid_layout.addWidget(button, row_num, 0)
            if config_needs_dumping:
                config_file.seek(0)
                json.dump(config, config_file, indent=4)
