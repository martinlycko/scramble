from PySide6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QPushButton, QTabWidget, QTableWidget, QTextEdit, QTableWidgetItem, QHeaderView, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from src.ui.Components.AddAttributeDialog import AddAttributeDialog


class DocumentTabs(QWidget):
    def __init__(self, parent=None, project=None):

        self.project = project
        
        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Create tabs for document details
        self.tabs = QTabWidget()
        self.create_attributes_tab()
        self.create_notes_tab()
        self.main_layout.addWidget(self.tabs)

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

        # Add the attributes tab to the main tabs
        self.tabs.addTab(attributes_tab, "Attributes")

        # Buttons for saving and managing attributes
        self.save_attributes = QPushButton("Add Attribute")
        self.save_attributes.clicked.connect(self.add_attribute)
        attributes_layout.addWidget(self.save_attributes)

    def create_notes_tab(self):
        # Tab for notes regarding the document
        self.notes_editor = QTextEdit()
        self.notes_editor.setPlaceholderText("Add notes about this document...")

        # Create notes tab layout
        notes_tab = QWidget()
        notes_layout = QVBoxLayout(notes_tab)
        notes_layout.addWidget(self.notes_editor)

        # Add the notes tab to the main tabs
        self.tabs.addTab(notes_tab, "Notes")

    def add_attribute(self):
        dialog = AddAttributeDialog(project=self.project)
        if dialog.exec() == QDialog.Accepted:
            value = dialog.edit.text()
            print(value)