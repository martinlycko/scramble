import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from PySide6.QtCore import Qt

# Import top level components
from src.ui.Components.Sidebar import Sidebar
from src.ui.Components.MenuBar import AppMenuBar

# Import individual pages
from src.ui.DocumentsView._page import DocumentsPage
from src.ui.AddDocumentView._page import AddDocumentPage
from src.ui.ThemesView._page import ThemesPage
from src.ui.ProjectView._page import ProjectPage
from src.ui.SettingsView._page import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self, project):
        
        # Initialize the main window
        super().__init__()
        self.resize(900, 600)
        central = QWidget()
        self.setCentralWidget(central)

        # Store reference to project
        self.project = project

        # Set up the main layout
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create widgets and pages 
        self.create_menu_bar()
        self.create_side_bar()
        self.create_pages()
        layout.addWidget(self.sidebar)
        layout.addWidget(self.pages)

    def create_menu_bar(self):
        menu_bar = AppMenuBar(self)
        self.setMenuBar(menu_bar)

    def create_side_bar(self):
        self.sidebar = Sidebar()

    def create_pages(self):
        self.pages = QStackedWidget()

        # Create individual pages
        self.DocumentsPage = DocumentsPage(project=self.project)
        self.AddDocumentsPage = AddDocumentPage(parent=self, project=self.project)
        self.ThemesPage = ThemesPage()
        self.ProjectPage = ProjectPage()
        self.SettingsPage = SettingsPage()

        # Add pages to the stacked widget
        self.pages.addWidget(self.DocumentsPage)
        self.pages.addWidget(self.AddDocumentsPage)
        self.pages.addWidget(self.ThemesPage)
        self.pages.addWidget(self.ProjectPage)
        self.pages.addWidget(self.SettingsPage)

        # Map page names to widgets for easy access
        self.pages_map = {
            "Docs": self.DocumentsPage,
            "Themes": self.ThemesPage,
            "Project": self.ProjectPage,
            "Settings": self.SettingsPage,
            "AddDoc": self.AddDocumentsPage,
        }

        # Connect sidebar buttons to page display functions
        self.sidebar.buttons[0].clicked.connect(lambda: self.show_page("Docs"))
        self.sidebar.buttons[1].clicked.connect(lambda: self.show_page("Themes"))
        self.sidebar.buttons[2].clicked.connect(lambda: self.show_page("Project"))
        self.sidebar.buttons[3].clicked.connect(lambda: self.show_page("Settings"))

    def show_page(self, name: str):
        # Display the selected page and update sidebar state using page name
        self.pages.setCurrentWidget(self.pages_map[name])
        self.sidebar.set_active(name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())