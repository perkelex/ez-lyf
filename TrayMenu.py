from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction

tray_menu = QMenu()

tray_icon_theme_menu = tray_menu.addMenu("Tray icon theme")

light_theme_action = QAction("Light")
dark_theme_action = QAction("Dark")

tray_icon_theme_menu.addAction(light_theme_action)
tray_icon_theme_menu.addAction(dark_theme_action)