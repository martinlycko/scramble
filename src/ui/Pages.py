from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget

from Views.DocumentView import DocumentViewerPage


class BasePage(QWidget):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)


class DocumentsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Documents", parent)
    
        self.main_layout.addWidget(DocumentViewerPage())


class ThemesPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Themes", parent)


class ProjectPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Project", parent)


class SettingsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Settings", parent)