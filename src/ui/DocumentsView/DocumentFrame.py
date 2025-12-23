from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt


class DocumentFrame(QWidget):
    def __init__(self, parent=None):
        
        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add text area to display document contents
        self.document_text = QTextEdit()
        self.document_text.setReadOnly(True)
        self.document_text.setPlaceholderText(
            "Select a document from the left to view its contents."
        )
        self.main_layout.addWidget(self.document_text)