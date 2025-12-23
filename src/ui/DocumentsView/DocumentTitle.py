from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout


class DocumentTitle(QWidget):
    def __init__(self, parent=None):
        
        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add text area to display document contents
        self.title_label = QLabel("Documents")
        self.title_label.setStyleSheet("font-size: 24px;")

        self.main_layout.addWidget(self.title_label)