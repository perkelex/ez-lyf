from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon
from TrayImage import TrayImage
from datetime import date

tray_image = TrayImage().draw(date.today().isocalendar()[1])

tray = QSystemTrayIcon()
tray.setIcon(QIcon(tray_image))
tray.setVisible(True)