from PySide6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QPushButton
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


class DocumentSelector(QWidget):
    def __init__(self, parent=None):

        # Initialise main selector
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # --- Add Tree View for Documents ---
        tree = QTreeView()
        self.model = QStandardItemModel()

        # Create sample data for tree view
        root = self.model.invisibleRootItem()
        parent = QStandardItem("Parent")
        parent.setData(1, Qt.UserRole)
        parent.setFlags(parent.flags() & ~Qt.ItemIsSelectable)
        child = QStandardItem("Child")
        child.setData(2, Qt.UserRole)
        parent.appendRow(child)
        root.appendRow(parent)

        # Set model to tree view
        tree.setModel(self.model)
        tree.setHeaderHidden(True)
        tree.expandAll()
        tree.show()
        self.main_layout.addWidget(tree, stretch=1)
        
        # --- Add and Manage Docs Button On Bottom
        self.add_document = QPushButton("Add Document")
        self.main_layout.addWidget(self.add_document)