from PySide6.QtWidgets import QApplication
app = QApplication.instance() if QApplication.instance() else QApplication([])
# app.setQuitOnLastWindowClosed(False)

from PySide6.QtGui import QGuiApplication
from utils.WindowsInhibitor import WindowsInhibitor
from MainWindow import MainWindow
from tray.Tray import tray

def onExit():
    QGuiApplication.clipboard().clear()
    WindowsInhibitor.uninhibit()

app.aboutToQuit.connect(onExit)

WindowsInhibitor.inhibit()
MainWindow().show()

if __name__ == "__main__":
    app.exec()
