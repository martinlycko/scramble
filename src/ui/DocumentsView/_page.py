from PySide6.QtWidgets import QWidget, QVBoxLayout

from .DocumentView import DocumentsViewerPage


class DocumentsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(DocumentsViewerPage())