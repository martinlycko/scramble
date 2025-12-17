from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget

from Views.DocumentView import DocumentViewerPage


class BasePage(QWidget):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)

        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 24px;")
        title_label.setFixedHeight(28)

        self.main_layout.addWidget(title_label)

        self.content_layout = QVBoxLayout()
        self.main_layout.addLayout(self.content_layout)


class DocumentsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Documents", parent)

        self.content_layout.addWidget(DocumentViewerPage())


class ThemesPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Themes", parent)


class ProjectPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Project", parent)


class SettingsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Settings", parent)