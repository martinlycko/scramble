import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    )
from PySide6.QtCore import Qt, QSize




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scramble")
        self.resize(900, 600)

        # --- Central widget ---
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # --- Left menu ---
        menu_widget = QWidget()
        menu_widget.setFixedWidth(50)
        menu_widget.setStyleSheet("background-color: #2c3e50;")
        menu_layout = QVBoxLayout(menu_widget)
        menu_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        from PySide6.QtWidgets import QStyle

        btn_documents = QPushButton()
        btn_themes = QPushButton()
        btn_settings = QPushButton()
        btn_projects = QPushButton()

        style = self.style()
        btn_documents.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileIcon))
        btn_themes.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
        btn_settings.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogDetailedView))
        btn_projects.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DirIcon))

        btn_documents.setToolTip("Documents")
        btn_themes.setToolTip("Themes")
        btn_settings.setToolTip("Settings")
        btn_projects.setToolTip("Projects")

        # Top section buttons
        for btn in (btn_documents, btn_themes):
            btn.setMinimumHeight(48)
            btn.setIconSize(QSize(40, 40))
            btn.setSizePolicy(btn.sizePolicy().horizontalPolicy(), btn.sizePolicy().verticalPolicy())
            btn.setStyleSheet("text-align: center;")
            btn.setFlat(True)
            menu_layout.addWidget(btn)

        # Push bottom buttons down
        menu_layout.addStretch()

        # Bottom section buttons
        for btn in (btn_settings, btn_projects):
            btn.setMinimumHeight(48)
            btn.setIconSize(QSize(24, 24))
            btn.setSizePolicy(btn.sizePolicy().horizontalPolicy(), btn.sizePolicy().verticalPolicy())
            btn.setStyleSheet("text-align: center;")
            btn.setFlat(True)
            menu_layout.addWidget(btn)

        # --- Main content area ---
        self.pages = QStackedWidget()
        self.pages.addWidget(self._make_page("Documents Page"))
        self.pages.addWidget(self._make_page("Themes Page"))
        self.pages.addWidget(self._make_page("Settings Page"))
        self.pages.addWidget(self._make_page("Projects Page"))
        self.pages.addWidget(self._make_page("Settings Page"))

        # --- Connections ---
        btn_documents.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        btn_themes.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        btn_settings.clicked.connect(lambda: self.pages.setCurrentIndex(2))
        btn_projects.clicked.connect(lambda: self.pages.setCurrentIndex(3))

        # --- Assemble layout ---
        main_layout.addWidget(menu_widget)
        main_layout.addWidget(self.pages)

        menu_widget.setStyleSheet("""
            background-color: #2c3e50;
                                  
            QPushButton {      
                background-transparent: true;
                background-color: #2c3e50;
                color: white;
                border: none;       
            }

            QPushButton:hover {
                background-color: yellow;
            }

            QPushButton:pressed {
                background-color: #3e3e42;
            }

            QPushButton:checked {
                background-color: #0078d7;
            }
            """)

        btn_documents.setCheckable(True)
        btn_themes.setCheckable(True)
        btn_settings.setCheckable(True)
        btn_projects.setCheckable(True)

    def _make_page(self, text: str) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px;")
        layout.addWidget(label)
        return page

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())