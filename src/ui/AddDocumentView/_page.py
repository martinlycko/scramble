from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from PySide6.QtCore import Qt

from src.ui.AddDocumentView.DocumentTitle import DocumentTitle
from src.ui.AddDocumentView.DocumentText import DocumentText
from src.ui.AddDocumentView.DocumentTabs import DocumentTabs

class AddDocumentPage(QWidget):
    def __init__(self, parent=None, project=None):

        self.uiparent = parent
        self.project = project
        
        # Initialise main page
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 4)

        # Add title bar
        self.title = DocumentTitle(parent=self)
        self.title.setFixedHeight(40)
        self.main_layout.addWidget(self.title)

        # Add split layout and components
        self.split_layout = QHBoxLayout()
        self.split_layout.setContentsMargins(0, 0, 0, 0)
        splitter = QSplitter(Qt.Horizontal, self)

        self.docFrame = DocumentText()
        splitter.addWidget(self.docFrame)

        self.docTabs = DocumentTabs(parent=self, project=self.project)
        splitter.addWidget(self.docTabs)

        # Initial proportions
        splitter.setSizes([500, 250])
        self.split_layout.addWidget(splitter)

        self.main_layout.addLayout(self.split_layout)

    def refresh_page(self):
        attributes = self.project.attributes.list
        self.docTabs.update(attributes)

    def discard(self):
        self.title.title_input.setText("")
        self.docFrame.document_text.setText("")
        self.uiparent.show_page("Docs")
    
    def save_doc(self):
        print("save")