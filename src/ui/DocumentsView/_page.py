from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from PySide6.QtCore import Qt

from DocumentsView.DocumentTitle import DocumentTitle
from DocumentsView.DocumentSelector import DocumentSelector
from DocumentsView.DocumentFrame import DocumentFrame
from DocumentsView.DocumentTabs import DocumentTabs


class DocumentsPage(QWidget):
    def __init__(self, parent=None):
        
        # Initialise main page
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 4)

        # Add title bar
        self.title = DocumentTitle()
        self.title.setFixedHeight(40)
        self.main_layout.addWidget(self.title)

        # Add split layout and components
        self.split_layout = QHBoxLayout(self)
        self.split_layout.setContentsMargins(0, 0, 0, 0)
        splitter = QSplitter(Qt.Horizontal, self)

        self.documents = DocumentSelector()
        splitter.addWidget(self.documents)

        self.docFrame = DocumentFrame()
        splitter.addWidget(self.docFrame)

        self.docTabs = DocumentTabs()
        splitter.addWidget(self.docTabs)

        # Initial proportions
        splitter.setSizes([250, 500, 250])
        self.split_layout.addWidget(splitter)

        self.main_layout.addLayout(self.split_layout)