from PySide6.QtWidgets import QApplication
app = QApplication([])
# app.setQuitOnLastWindowClosed(False)

from PySide6.QtGui import QAction, QGuiApplication
from Window import window
from Tray import tray
from TrayMenu import tray_menu
from WindowsInhibitor import WindowsInhibitor

def onExit():
    QGuiApplication.clipboard().clear()
    WindowsInhibitor.uninhibit()

WindowsInhibitor.inhibit()

quit_action = QAction("Quit")
quit_action.triggered.connect(app.quit)
tray_menu.addAction(quit_action)

tray.setContextMenu(tray_menu)
window.show()

app.aboutToQuit.connect(onExit)

if __name__ == "__main__":


    app.exec()