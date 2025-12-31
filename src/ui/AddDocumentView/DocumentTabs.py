from PySide6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QPushButton, QTabWidget, QTableWidget, QTextEdit, QTableWidgetItem, QHeaderView, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from src.ui.Components.AddAttributeDialog import AddAttributeDialog


class DocumentTabs(QWidget):
    def __init__(self, parent=None, project=None):

        self.project = project
        self.uiparent = parent
        
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

        # Populate the table with row based on project attributes
        self.attributes_table.setRowCount(0)
        for attr in self.project.attributes.list:
            row = self.attributes_table.rowCount()
            self.attributes_table.insertRow(row)
            self.attributes_table.setItem(row, 0, QTableWidgetItem(attr))
            self.attributes_table.setItem(row, 1, QTableWidgetItem(None))

        # Disable editing the attribute name column
        for row in range(self.attributes_table.rowCount()):
            item = self.attributes_table.item(row, 0)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Create tab layout
        attributes_tab = QWidget()
        attributes_layout = QVBoxLayout(attributes_tab)
        attributes_layout.addWidget(self.attributes_table)

        # Add the attributes tab to the main tabs
        self.tabs.addTab(attributes_tab, "Attributes")

        # Buttons for adding attributes
        self.add_attributes = QPushButton("Add Attribute")
        self.add_attributes.clicked.connect(self.add_attribute)
        attributes_layout.addWidget(self.add_attributes)

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
        self.uiparent.uiparent.refresh_page()

    def update(self, Attributes):
        #  TODO - make sure already entered attribute values are maintained

        # Update attribute name column
        self.attributes_table.setRowCount(0)
        for attr in Attributes:
            row = self.attributes_table.rowCount()
            self.attributes_table.insertRow(row)
            self.attributes_table.setItem(row, 0, QTableWidgetItem(attr))
            self.attributes_table.setItem(row, 1, QTableWidgetItem(None))

        # Disable editing the attribute name column
        for row in range(self.attributes_table.rowCount()):
            item = self.attributes_table.item(row, 0)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)