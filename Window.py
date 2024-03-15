from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from functools import partial
from MildEncryption import hide, reveal, isValidToken
import json

window = QWidget()
window.setWindowFlag(Qt.WindowStaysOnTopHint, True)
window.setWindowTitle("EZ Lyf")
window.setMinimumWidth(200)
window.setMinimumHeight(150)
layout = QGridLayout(window)

def clipboardAdd(content: str):
    QGuiApplication.clipboard().setText(content)

with open("config.json", "r+") as config_file:
    config_needs_dumping = False
    config = json.load(config_file)
    for row_num, config_button in enumerate(config["buttons"]):
        if config_button["type"] == "email":
            for col_num, part in enumerate(config_button["content"].split("@")):
                if col_num == 0:
                    button = QPushButton(part)
                    button.clicked.connect(partial(clipboardAdd, part))
                else:
                    button = QPushButton("@" + part)
                    button.clicked.connect(partial(clipboardAdd, config_button["content"]))
                layout.addWidget(button, row_num, col_num)
        elif config_button["type"] == "obscured": # "●"
            button = QPushButton("●" * 10)
            if not isValidToken(config_button["content"]):
                config_button["content"] = hide(config_button["content"])
                config_needs_dumping = True
            button.clicked.connect(partial(clipboardAdd, reveal(config_button["content"])))
            layout.addWidget(button, row_num, 0)
            if "hint" in config_button:
                layout.addWidget(QLabel(config_button["hint"]), row_num, 1)
        else:
            button = QPushButton(config_button["content"])
            button.clicked.connect(partial(clipboardAdd, config_button["content"]))
            layout.addWidget(button, row_num, 0)
    if config_needs_dumping:
        config_file.seek(0)
        json.dump(config, config_file, indent=4)