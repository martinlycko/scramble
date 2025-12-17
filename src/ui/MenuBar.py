from PySide6.QtWidgets import QMenuBar, QFileDialog, QMessageBox, QStyle
from PySide6.QtGui import QAction


class AppMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        style = self.style()

        # File menu
        file_menu = self.addMenu("File")

        project_action = QAction("Project", self)
        project_action.triggered.connect(lambda: self.parent().show_page("Project"))
        file_menu.addAction(project_action)

        file_menu.addSeparator()

        # Open action
        open_action = QAction(style.standardIcon(QStyle.SP_DialogOpenButton), "Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Save action
        save_action = QAction(style.standardIcon(QStyle.SP_DialogSaveButton), "Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Save-As action
        save_as_action = QAction(style.standardIcon(QStyle.SP_DialogSaveButton), "Save As", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()

        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(lambda: self.parent().show_page("Settings"))
        file_menu.addAction(settings_action)

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

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*)"
        )
        if file_name:
            QMessageBox.information(self, "Open", f"Opened:\n{file_name}")

    def save_as_file(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "All Files (*)"
        )
        if file_name:
            QMessageBox.information(self, "Save", f"Saved:\n{file_name}")

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "All Files (*)"
        )
        if file_name:
            QMessageBox.information(self, "Save", f"Saved:\n{file_name}")