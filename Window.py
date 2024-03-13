from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from functools import partial

window = QWidget()
window.setWindowFlag(Qt.WindowStaysOnTopHint, True)
layout = QGridLayout(window)

def clipboardAdd(content: str):
    QGuiApplication.clipboard().setText(content)

with open("config", "r") as file:
    lines = file.readlines()
    for row_num, line in enumerate(lines):
        line = line.strip("\r\n")
        print(line)
        if "@" in line:
            for col_num, part in enumerate(line.split("@")):
                if col_num == 0:
                    button = QPushButton(part)
                    button.clicked.connect(partial(clipboardAdd, part))
                else:
                    button = QPushButton("@" + part)
                    button.clicked.connect(partial(clipboardAdd, line))
                layout.addWidget(button, row_num, col_num)
        else:
            button = QPushButton(line)
            button.clicked.connect(partial(clipboardAdd, line))
            layout.addWidget(button, row_num, 0, 1, 2)
