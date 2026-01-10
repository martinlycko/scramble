from PySide6.QtWidgets import (
    QDialog, QVBoxLayout,
    QLineEdit, QPushButton, QMessageBox
)


class AddThemeDialog(QDialog):
    def __init__(self, parent=None, project=None):
        
        self.project = project

        super().__init__(parent)

        self.setWindowTitle("Add Theme")
        self.resize(300, 100)

        # Widgets
        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Enter theme name...")

        self.save_button = QPushButton("Add Theme", self)
        self.save_button.clicked.connect(self.save)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.save_button)

    def save(self):
        text = self.edit.text()
        if self.project.themes.add_theme(text):
            QMessageBox.information(self, "Added Theme:", f"You entered:\n{text}")
            self.accept()   # closes the dialog with Accepted state
        else:
            QMessageBox.information(self, "Adding theme ", f"{text} failed")
