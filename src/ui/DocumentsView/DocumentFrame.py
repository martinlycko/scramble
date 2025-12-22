from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QSplitter
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


class DocumentFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.document_text = QTextEdit()
        self.document_text.setReadOnly(True)
        self.document_text.setPlaceholderText(
            "Select a document from the left to view its contents."
        )