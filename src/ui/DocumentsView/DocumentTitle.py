from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton


class DocumentTitle(QWidget):
    def __init__(self, parent=None, project=None):

        self.uiparent = parent
        self.project = project

        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add text area to display document contents
        self.title_label = QLabel("Documents")
        self.title_label.setStyleSheet("font-size: 24px;")
        self.main_layout.addWidget(self.title_label)

        # Add button to save document
        self.save_changes = QPushButton("Save Changes")
        self.save_changes.clicked.connect(self.uiparent.save_document_changes)
        self.save_changes.setFixedWidth(120)
        self.save_changes.setStyleSheet("""
                                        QPushButton {
                                            background-color: #2ecc71;
                                            color: white;
                                            border-radius: 6px;
                                            padding: 8px 14px;
                                            font-weight: 600;
                                        }
                                        QPushButton:hover {
                                            background-color: #27ae60;
                                        }
                                        QPushButton:pressed {
                                            background-color: #1e8449;
                                        }
                                        QPushButton:disabled {
                                            background-color: #95a5a6;
                                            color: #ecf0f1;
                                        }
                                        """)
        self.main_layout.addWidget(self.save_changes)

    def update(self, DocTitle):
        if DocTitle != "" and DocTitle is not None:
            self.title_label.setText(DocTitle)
        else:
            self.title_label.setText("Documents")