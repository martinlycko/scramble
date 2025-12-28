# Import external modules
import sys
from PySide6.QtWidgets import QApplication

# Importing main components
from src.ui.MainWindow import MainWindow

# Importing project datastructure
from src.model.Project import Project


if __name__ == "__main__":
    project = Project()
    project.documents.add_document("Example Title",
                                   "Example Content",
                                   "note 1",
                                   {"at1": "v1", "at2": "V2"})
    project.documents.add_document("Example Title 2",
                                   "Example Content 2",
                                   "note 2",
                                   {"at1": "2", "at2": "3"})

    app = QApplication(sys.argv)
    window = MainWindow(project)
    window.show()
    sys.exit(app.exec())