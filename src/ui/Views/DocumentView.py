from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QListWidget,
    QTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QSplitter,
    QTabWidget,
    QVBoxLayout,
    QPushButton
)
from PySide6.QtCore import Qt


class DocumentViewerPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main layout for the page
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Splitter for resizable columns
        splitter = QSplitter(Qt.Horizontal, self)

        # --- Left Sidebar (25%) ---
        # --- Document List On Top
        self.left_container = QWidget()
        self.left_layout = QVBoxLayout(self.left_container)
        self.left_layout.setContentsMargins(0, 0, 0, 0)

        self.document_list = QListWidget()
        self.document_list.addItems([
            "Document A",
            "Document B",
            "Document C"
        ])
        self.left_layout.addWidget(self.document_list, stretch=1)
        
        # --- Add Button On Bottom
        self.add_document = QPushButton("Add Document")
        self.left_layout.addWidget(self.add_document)

        splitter.addWidget(self.left_container)
        

        # --- Center Column (50%) ---
        self.document_text = QTextEdit()
        self.document_text.setReadOnly(True)
        self.document_text.setPlaceholderText(
            "Select a document from the left to view its contents."
        )
        splitter.addWidget(self.document_text)

        # --- Right Column (25%) with Tabs ---
        self.tabs = QTabWidget()
        splitter.addWidget(self.tabs)

        # Themes tab
        actions_tab = QWidget()
        actions_layout = QVBoxLayout(actions_tab)
        actions_layout.setContentsMargins(8, 8, 8, 8)
        actions_layout.setSpacing(6)
        self.action_open = QPushButton("Open")
        self.action_export = QPushButton("Export")
        self.action_archive = QPushButton("Archive")
        self.action_delete = QPushButton("Delete")

        for btn in (
            self.action_open,
            self.action_export,
            self.action_archive,
            self.action_delete,
        ):
            actions_layout.addWidget(btn)
        actions_layout.addStretch()  # Push buttons to top

        self.tabs.addTab(actions_tab, "Themes")

        # Attributes tab
        self.attributes_table = QTableWidget(0, 2)
        self.attributes_table.setHorizontalHeaderLabels(
            ["Attribute", "Value"]
        )
        self.attributes_table.horizontalHeader().setStretchLastSection(True)

        attributes_tab = QWidget()
        attributes_layout = QVBoxLayout(attributes_tab)
        attributes_layout.addWidget(self.attributes_table)

        self.save_attributes = QPushButton("Save Attributes")
        attributes_layout.addWidget(self.save_attributes)

        self.edit_attributes = QPushButton("Edit Attributes")
        attributes_layout.addWidget(self.edit_attributes)

        self.tabs.addTab(attributes_tab, "Attributes")

        # Notes tab
        self.notes_editor = QTextEdit()
        self.notes_editor.setPlaceholderText("Add notes about this document...")

        notes_tab = QWidget()
        notes_layout = QVBoxLayout(notes_tab)
        notes_layout.addWidget(self.notes_editor)

        self.tabs.addTab(notes_tab, "Notes")

        # Initial proportions
        splitter.setSizes([250, 500, 250])

        layout.addWidget(splitter)

        # Connections
        self.document_list.currentTextChanged.connect(self.load_document)

    def load_document(self, title: str):
        self.document_text.setPlainText(
            f"This is the full text of {title}.\n\nLorem ipsum dolor sit amet..."
        )

        attributes = {
            "Title": title,
            "Author": "Jane Doe",
            "Pages": "12",
            "Status": "Draft"
        }

        self.attributes_table.setRowCount(len(attributes))
        for row, (key, value) in enumerate(attributes.items()):
            self.attributes_table.setItem(row, 0, QTableWidgetItem(key))
            self.attributes_table.setItem(row, 1, QTableWidgetItem(value))