import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from PySide6.QtCore import Qt

from Components.Sidebar import Sidebar
from Components.MenuBar import AppMenuBar

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

        self.DocumentsPage = DocumentsPage()
        self.ThemesPage = ThemesPage()
        self.ProjectPage = ProjectPage()
        self.SettingsPage = SettingsPage()

        self.pages.addWidget(self.DocumentsPage)
        self.pages.addWidget(self.ThemesPage)
        self.pages.addWidget(self.ProjectPage)
        self.pages.addWidget(self.SettingsPage)

        self.pages_map = {
            "Docs": self.DocumentsPage,
            "Themes": self.ThemesPage,
            "Project": self.ProjectPage,
            "Settings": self.SettingsPage,
        }

        self._connect_sidebar()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.pages)

    def show_page(self, name: str):
        self.pages.setCurrentWidget(self.pages_map[name])
        self.sidebar.set_active(name)

    def _connect_sidebar(self):
        self.sidebar.buttons[0].clicked.connect(lambda: self.show_page("Docs"))
        self.sidebar.buttons[1].clicked.connect(lambda: self.show_page("Themes"))
        self.sidebar.buttons[2].clicked.connect(lambda: self.show_page("Project"))
        self.sidebar.buttons[3].clicked.connect(lambda: self.show_page("Settings"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())