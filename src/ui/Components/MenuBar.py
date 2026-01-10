import json

from PySide6.QtWidgets import QMenuBar, QFileDialog, QMessageBox, QStyle, QDialog
from PySide6.QtGui import QAction

from src.ui.Components.AddAttributeDialog import AddAttributeDialog

class AppMenuBar(QMenuBar):
    def __init__(self, parent=None, project=None):
        
        self.uiparent = parent
        self.project = project

        # Initialize the menu bar
        super().__init__(parent)
        self.style = self.style()

        # Create menu items
        self.create_file_menu()
        self.create_data_menu()

        # Apply styling for the menu bar
        self.setStyleSheet("""
                                QMenuBar {
                                    background-color: #2b2b2b;
                                    color: white;
                                }

                                QMenuBar::item {
                                    background-color: transparent;
                                    padding: 6px 12px;
                                }

                                QMenuBar::item:selected {
                                    background-color: #3c3f41;
                                }

                                QMenu {
                                    background-color: #2b2b2b;
                                    color: white;
                                    border: 1px solid #555;
                                }

                                QMenu::item {
                                    padding: 6px 20px;
                                }

                                QMenu::item:selected {
                                    background-color: #3c3f41;
                                }
                                """)

    def create_file_menu(self):
        # Create file menu
        file_menu = self.addMenu("File")

        # Item navigating to project page
        project_action = QAction("Project", self)
        project_action.triggered.connect(lambda: self.parent().show_page("Project"))
        file_menu.addAction(project_action)

        # Menu seperator
        file_menu.addSeparator()

        # File open action
        open_action = QAction(self.style.standardIcon(QStyle.SP_DialogOpenButton), "Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # File save action
        save_action = QAction(self.style.standardIcon(QStyle.SP_DialogSaveButton), "Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # File save-as action
        save_as_action = QAction(self.style.standardIcon(QStyle.SP_DialogSaveButton), "Save As", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)

        # Menu separator
        file_menu.addSeparator()

        # Item navigator to settings page
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(lambda: self.parent().show_page("Settings"))
        file_menu.addAction(settings_action)

    def create_data_menu(self):
        # Create data menu
        data_menu = self.addMenu("Data")

        # Item navigating to documents page
        docs_action = QAction("Documents", self)
        docs_action.triggered.connect(lambda: self.parent().show_page("Docs"))
        data_menu.addAction(docs_action)

        # Item navigating to add document page
        docs_action = QAction("Add Document", self)
        docs_action.triggered.connect(lambda: self.parent().show_page("AddDoc"))
        data_menu.addAction(docs_action)

        # Item opening add attribute dialogue
        add_attribute = QAction("Add Attribute", self)
        add_attribute.triggered.connect(self.add_attribute_dialogue)
        data_menu.addAction(add_attribute)

        # Menu separator
        data_menu.addSeparator()

        # Item navigating to themes page
        themes_action = QAction("Themes", self)
        themes_action.triggered.connect(lambda: self.parent().show_page("Themes"))
        data_menu.addAction(themes_action)#

        # Item triggering add theme dialogue
        add_theme = QAction("Add Theme", self)
        add_theme.triggered.connect(self.add_theme_dialogue)
        data_menu.addAction(add_theme)

    
    def open_file(self):
        # Action to open a new project file
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*)"
        )
        if file_name:
            QMessageBox.information(self, "Open", f"Opened:\n{file_name}")

    def save_as_file(self):
        # Action to save the current project as a new file
        file_name, selected_filter = QFileDialog.getSaveFileName(
            self, "Save File", "", "Scramble Project (*.scramble);;All Files (*)"
        )
        if not file_name:
            return

        if not file_name.lower().endswith(".scramble"):
            file_name += ".scramble"

        self.project.file_path = file_name

        self.save_file()

    def save_file(self):
        # Action to save the current project
        if not self.project.file_path:
            self.save_as_file()
            return

        with open(self.project.file_path, "w") as f:
            json.dump(self.project.to_dict(), f, indent=2)

    def add_theme_dialogue(self):
        pass

    def add_attribute_dialogue(self):
        dialog = AddAttributeDialog(project=self.project)
        if dialog.exec() == QDialog.Accepted:
            value = dialog.edit.text()
            print(value)
        self.uiparent.refresh_page()