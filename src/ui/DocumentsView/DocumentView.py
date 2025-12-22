from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QSplitter,
    QTabWidget,
    QVBoxLayout,
    QPushButton,
    QTreeView,
    QLabel,
)
from PySide6.QtCore import Qt

from PySide6.QtGui import QStandardItemModel, QStandardItem


class DocumentsViewerPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # tbc
        mainlayout = QVBoxLayout(self)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        
        # tbc
        self.title_label = QLabel("Documents")
        self.title_label.setStyleSheet("font-size: 24px;")
        self.title_label.setFixedHeight(28)

        mainlayout.addWidget(self.title_label)

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

        tree = QTreeView()
        self.model = QStandardItemModel()

        root = self.model.invisibleRootItem()
        parent = QStandardItem("Parent")
        parent.setData(1, Qt.UserRole)
        parent.setFlags(parent.flags() & ~Qt.ItemIsSelectable)
        child = QStandardItem("Child")
        child.setData(2, Qt.UserRole)
        parent.appendRow(child)
        root.appendRow(parent)

        tree.setModel(self.model)
        tree.setHeaderHidden(True)
        tree.expandAll()
        tree.show()
        self.left_layout.addWidget(tree, stretch=1)
        
        # --- Add and Manage Docs Button On Bottom
        self.add_document = QPushButton("Add Document")
        self.left_layout.addWidget(self.add_document)
        self.manage_document = QPushButton("Manage Document")
        self.left_layout.addWidget(self.manage_document)

        splitter.addWidget(self.left_container)

        # --- Right Column (75%) ---
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
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(0)

        theme_tree = QTreeView()
        self.theme_model = QStandardItemModel()

        theme_root = self.theme_model.invisibleRootItem()
        theme_parent = QStandardItem("Parent")
        theme_parent.setData(1, Qt.UserRole)
        theme_child = QStandardItem("Child")
        theme_child.setData(2, Qt.UserRole)
        theme_parent.appendRow(theme_child)
        theme_root.appendRow(theme_parent)

        theme_tree.setModel(self.theme_model)
        theme_tree.setHeaderHidden(True)
        theme_tree.expandAll()
        theme_tree.show()
        self.left_layout.addWidget(theme_tree, stretch=1)
        actions_layout.addWidget(theme_tree)

        self.add_themes = QPushButton("Add Attributes")
        actions_layout.addWidget(self.add_themes)

        self.manage_themes = QPushButton("Manage Attributes")
        actions_layout.addWidget(self.manage_themes)

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

        self.manage_attributes = QPushButton("Manage Attributes")
        attributes_layout.addWidget(self.manage_attributes)

        self.tabs.addTab(attributes_tab, "Attributes")

        # Notes tab
        self.notes_editor = QTextEdit()
        self.notes_editor.setPlaceholderText("Add notes about this document...")

        notes_tab = QWidget()
        notes_layout = QVBoxLayout(notes_tab)
        notes_layout.addWidget(self.notes_editor)

        self.save_notes = QPushButton("Save Notes")
        notes_layout.addWidget(self.save_notes)

        self.tabs.addTab(notes_tab, "Notes")

        # Initial proportions
        splitter.setSizes([250, 500, 250])

        layout.addWidget(splitter)

        mainlayout.addLayout(layout)

        # Connections
        # self.document_list.currentTextChanged.connect(self.load_document)
        tree.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselected):
        indexes = selected.indexes()
        if not indexes:
            return

        index = indexes[0]
        item = self.model.itemFromIndex(index)

        self.load_document(item.text())


    def load_document(self, title: str):
        self.title_label.setText(title)
        
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