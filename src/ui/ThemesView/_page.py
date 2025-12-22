from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ThemesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)

        text = QLabel("Themes View Page - Under Construction")
        self.main_layout.addWidget(text)