import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout,
    QLineEdit, QPushButton, QMessageBox
)


class AddAttributeDialog(QDialog):
    def __init__(self, parent=None, project=None):
        
        self.project = project

        super().__init__(parent)

        self.setWindowTitle("Edit Value")
        self.resize(300, 100)

        # Widgets
        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Enter text...")

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.save_button)

    def save(self):
        text = self.edit.text()
        if self.project.add_attribute(text):
            QMessageBox.information(self, "Saved", f"You entered:\n{text}")
            self.accept()   # closes the dialog with Accepted state
        else:
            QMessageBox.information(self, "Failed", f"{text} already exists")
