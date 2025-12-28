from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton


class DocumentTitle(QWidget):
    def __init__(self, parent=None):
        
        self.uiparent = parent

        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add text area to display document contents
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Document Title")
        self.title_input.setStyleSheet("font-size: 24px;")

        self.main_layout.addWidget(self.title_input)

        # Save document button
        self.save_document = QPushButton("Save")
        self.save_document.clicked.connect(self.uiparent.save_doc)
        self.save_document.setStyleSheet("""
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
        self.main_layout.addWidget(self.save_document)

        # Discard/Abort button
        self.discard_document = QPushButton("Discard")
        self.discard_document.clicked.connect(self.uiparent.discard)
        self.discard_document.setStyleSheet("""
                                        QPushButton {
                                            background-color: #e74c3c;
                                            color: white;
                                            border-radius: 6px;
                                            padding: 8px 14px;
                                            font-weight: 600;
                                        }
                                        QPushButton:hover {
                                            background-color: #c0392b;
                                        }
                                        QPushButton:pressed {
                                            background-color: #a93226;
                                        }
                                        QPushButton:disabled {
                                            background-color: #95a5a6;
                                            color: #ecf0f1;
                                        }
                                        """)
        self.main_layout.addWidget(self.discard_document)