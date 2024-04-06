from PySide6.QtWidgets import QSystemTrayIcon
from tray.TrayIcon import TrayIcon
from tray.TrayMenu import TrayMenu
from datetime import date
from getpass import getuser

tray_ico_path = "C:\\Users\\" + getuser() + "\\AppData\\Local\\Temp\\currentWeek_icon.ico"

tray = QSystemTrayIcon()
tray.setIcon(TrayIcon(tray_ico_path, date.today().isocalendar()[1]))
tray.setContextMenu(TrayMenu())
tray.setVisible(True)