# Import external modules
import sys
from PySide6.QtWidgets import QApplication

# Importing main components
from src.ui.MainWindow import MainWindow

# Importing project datastructure
from src.model.Project import Project


if __name__ == "__main__":
    project = Project()
    project.documents.add_document("Example Title", "Example Content")
    project.documents.add_document("Example Title 2", "Example Content 2")

    app = QApplication(sys.argv)
    window = MainWindow(project)
    window.show()
    sys.exit(app.exec())