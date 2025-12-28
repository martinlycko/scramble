from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class DocumentText(QWidget):
    def __init__(self, parent=None):
        
        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add text area to display document contents
        self.document_text = QTextEdit()
        self.document_text.setPlaceholderText(
            "Document Content"
        )
        self.main_layout.addWidget(self.document_text)