from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class BasePage(QWidget):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel(title)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px;")
        layout.addWidget(label)


class DocumentsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Documents", parent)


class ThemesPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Themes", parent)


class SettingsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Project", parent)


class ProjectsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__("Settings", parent)