from PySide6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QPushButton, QTabWidget, QTableWidget, QTextEdit, QTableWidgetItem, QHeaderView, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from src.ui.Components.AddAttributeDialog import AddAttributeDialog


class DocumentTabs(QWidget):
    def __init__(self, parent=None, project=None):
        
        self.uiparent = parent
        self.project = project

        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Create tabs for document details
        self.tabs = QTabWidget()
        self.create_themes_tab()
        self.create_attributes_tab()
        self.create_notes_tab()
        self.main_layout.addWidget(self.tabs)

    def create_themes_tab(self):
        # Create a tab and layout for themes
        themes_tab = QWidget()
        themes_layout = QVBoxLayout(themes_tab)

        # Create a tree view for themes
        theme_tree = QTreeView()
        self.theme_model = QStandardItemModel()

        # Sample data for themes
        theme_root = self.theme_model.invisibleRootItem()
        theme_parent = QStandardItem("Parent")
        theme_parent.setData(1, Qt.UserRole)
        theme_child = QStandardItem("Child")
        theme_child.setData(2, Qt.UserRole)
        theme_parent.appendRow(theme_child)
        theme_root.appendRow(theme_parent)

        # Set model and configure tree view
        theme_tree.setModel(self.theme_model)
        theme_tree.setHeaderHidden(True)
        theme_tree.expandAll()
        theme_tree.show()
        themes_layout.addWidget(theme_tree, stretch=1)
        themes_layout.addWidget(theme_tree)

        # Buttons for adding and managing themes
        self.add_themes = QPushButton("Add Attributes")
        themes_layout.addWidget(self.add_themes)
        self.manage_themes = QPushButton("Manage Attributes")
        themes_layout.addWidget(self.manage_themes)

        # Add the themes tab to the main tabs
        self.tabs.addTab(themes_tab, "Themes")

    def create_attributes_tab(self):
        # Create a tab displaying attributes in a table
        self.attributes_table = QTableWidget(0, 2)
        self.attributes_table.setHorizontalHeaderLabels(
            ["Attribute", "Value"]
        )
        self.attributes_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        # Create tab layout
        attributes_tab = QWidget()
        attributes_layout = QVBoxLayout(attributes_tab)
        attributes_layout.addWidget(self.attributes_table)

        # Buttons for adding attributes
        self.add_attributes = QPushButton("Add Attribute")
        self.add_attributes.clicked.connect(self.add_attribute)
        attributes_layout.addWidget(self.add_attributes)

        # Buttons for saving and managing attributes
        self.save_attributes = QPushButton("Save Attributes")
        attributes_layout.addWidget(self.save_attributes)
        self.manage_attributes = QPushButton("Manage Attributes")
        attributes_layout.addWidget(self.manage_attributes)

        # Add the attributes tab to the main tabs
        self.tabs.addTab(attributes_tab, "Attributes")

    def create_notes_tab(self):
        # Tab for notes regarding the document
        self.notes_editor = QTextEdit()
        self.notes_editor.setPlaceholderText("Add notes about this document...")

        # Create notes tab layout
        notes_tab = QWidget()
        notes_layout = QVBoxLayout(notes_tab)
        notes_layout.addWidget(self.notes_editor)

        # Buttons for saving notes
        self.save_notes = QPushButton("Save Notes")
        notes_layout.addWidget(self.save_notes)

        # Add the notes tab to the main tabs
        self.tabs.addTab(notes_tab, "Notes")

    def update(self, Themes, Notes, Attributes):
        # Update themes tab - tbc

        # Update attribute tab
        self.attributes_table.setRowCount(0)
        for attr, value in Attributes.items():
            row = self.attributes_table.rowCount()
            self.attributes_table.insertRow(row)
            self.attributes_table.setItem(row, 0, QTableWidgetItem(attr))
            self.attributes_table.setItem(row, 1, QTableWidgetItem(value))

        # Update notes tab
        self.notes_editor.setText(Notes)

    def add_attribute(self):
        dialog = AddAttributeDialog(project=self.project)
        if dialog.exec() == QDialog.Accepted:
            value = dialog.edit.text()
            print(value)
        self.uiparent.refresh_page()