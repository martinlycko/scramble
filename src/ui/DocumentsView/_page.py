from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from PySide6.QtCore import Qt

from src.ui.DocumentsView.DocumentTitle import DocumentTitle
from src.ui.DocumentsView.DocumentSelector import DocumentSelector
from src.ui.DocumentsView.DocumentFrame import DocumentFrame
from src.ui.DocumentsView.DocumentTabs import DocumentTabs


class DocumentsPage(QWidget):
    def __init__(self, parent=None, project=None):

        self.uiparent = parent
        self.project = project
        self.openDoc = -1
        
        # Initialise main page
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 4)

        # Add title bar
        self.title = DocumentTitle(self, self.project)
        self.title.setFixedHeight(40)
        self.main_layout.addWidget(self.title)

        # Add split layout and components
        self.split_layout = QHBoxLayout()
        self.split_layout.setContentsMargins(0, 0, 0, 0)
        splitter = QSplitter(Qt.Horizontal, self)

        self.documents = DocumentSelector(self, self.project.documents.list)
        splitter.addWidget(self.documents)

        self.docFrame = DocumentFrame()
        splitter.addWidget(self.docFrame)

        self.docTabs = DocumentTabs(parent=self, project=self.project)
        splitter.addWidget(self.docTabs)

        # Initial proportions
        splitter.setSizes([250, 500, 250])
        self.split_layout.addWidget(splitter)

        self.main_layout.addLayout(self.split_layout)

    def refresh_page(self):
        opendocument = self.project.documents.get_document(self.openDoc)
        self.documents.refresh_page(self.project.documents.list, self.openDoc)
        if opendocument:
            self.title.update(opendocument.title)
            self.docFrame.update(opendocument.content)
            self.docTabs.update(self.project.themes, opendocument.notes, opendocument.attributes)

    def save_document_changes(self):
        if self.openDoc != -1:
            document = self.project.documents.get_document(self.openDoc)

            notes = self.docTabs.notes_editor.toPlainText()
            
            attributes = {}
            for row in range(self.docTabs.attributes_table.rowCount()):
                key_item = self.docTabs.attributes_table.item(row, 0)
                value_item = self.docTabs.attributes_table.item(row, 1)
                if key_item and value_item:
                    key = key_item.text()
                    value = value_item.text() if value_item else ""
                    attributes[key] = value

            if document:
                document.update_content(notes, attributes)