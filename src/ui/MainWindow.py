import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from PySide6.QtCore import Qt

from Sidebar import Sidebar
from MenuBar import AppMenuBar

from Pages import (
    DocumentsPage,
    ThemesPage,
    ProjectPage,
    SettingsPage,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(900, 600)

        central = QWidget()
        self.setCentralWidget(central)
        
        self.menu_bar = AppMenuBar(self)
        self.setMenuBar(self.menu_bar)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar = Sidebar()
        self.pages = QStackedWidget()

        self.pages.addWidget(DocumentsPage())
        self.pages.addWidget(ThemesPage())
        self.pages.addWidget(ProjectPage())
        self.pages.addWidget(SettingsPage())

        self.sidebar.page_selected.connect(self.pages.setCurrentIndex)
        self.sidebar.page_selected.connect(self.sidebar.set_active)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.pages)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())