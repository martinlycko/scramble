from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSplitter, QTreeView, QPushButton
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


class DocumentSelector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.left_container = QWidget()
        self.left_layout = QVBoxLayout(self.left_container)
        self.left_layout.setContentsMargins(0, 0, 0, 4)

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