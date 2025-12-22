from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSplitter, QTreeView, QPushButton, QTabWidget, QTableWidget, QTextEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


class DocumentTabs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- Right Column (25%) with Tabs ---
        self.tabs = QTabWidget()

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
        #self.left_layout.addWidget(theme_tree, stretch=1)
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