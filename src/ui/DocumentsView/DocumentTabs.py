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
        self.themes_layout = QVBoxLayout(themes_tab)

        # Create a tree view for themes
        self.tree = QTreeView()
        self.model = QStandardItemModel()

        # Set model and configure tree view
        root = self.model.invisibleRootItem()
        for theme in self.project.themes.list:
            item = QStandardItem(theme.title)
            item.setData(theme.id, Qt.UserRole)
            root.appendRow(item)

        # Set model to tree view
        self.tree.setModel(self.model)
        self.tree.setHeaderHidden(True)
        self.tree.expandAll()
        self.tree.show()
        self.themes_layout.addWidget(self.tree, stretch=1)

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

        # Add the notes tab to the main tabs
        self.tabs.addTab(notes_tab, "Notes")

    def update(self, Themes, Notes, Attributes):
        # Temporarily block selection handling
        selection_model = self.tree.selectionModel()
        selection_model.blockSignals(True)
        self.model.clear()
        root = self.model.invisibleRootItem()
        for theme in Themes.list:
            item = QStandardItem(theme.title)
            item.setData(theme.id, Qt.UserRole)
            root.appendRow(item)
        selection_model.blockSignals(False)

        # Update attribute tab
        self.attributes_table.setRowCount(0)
        for attr, value in Attributes.items():
            row = self.attributes_table.rowCount()
            self.attributes_table.insertRow(row)
            self.attributes_table.setItem(row, 0, QTableWidgetItem(attr))
            self.attributes_table.setItem(row, 1, QTableWidgetItem(value))

        # Disable editing the attribute name column
        for row in range(self.attributes_table.rowCount()):
            item = self.attributes_table.item(row, 0)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Update notes tab
        self.notes_editor.setText(Notes)

    def add_attribute(self):
        dialog = AddAttributeDialog(project=self.project)
        if dialog.exec() == QDialog.Accepted:
            value = dialog.edit.text()
            print(value)
        self.uiparent.uiparent.refresh_page()