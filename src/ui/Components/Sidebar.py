from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStyle
from PySide6.QtCore import Qt, QSize, Signal


class Sidebar(QWidget):
    page_selected = Signal(str)  # emits page index

    def __init__(self, parent=None):
        
        # Initialize the sidebar widget
        super().__init__(parent)
        self.setFixedWidth(50)
        self.setAutoFillBackground(True)

        # Set up the layout for the sidebar
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Prepare style and button list
        style = self.style()
        self.buttons = []

        # Icons and their corresponding page indices
        self.top_buttons = [
            (QStyle.StandardPixmap.SP_DirIcon, "Docs"),                     # Documents
            (QStyle.StandardPixmap.SP_FileDialogDetailedView, "Themes"),    # Themes
        ]
        self.bottom_buttons = [
            (QStyle.StandardPixmap.SP_FileDialogInfoView, "Project"),       # Project
            (QStyle.StandardPixmap.SP_FileDialogListView, "Settings"),      # Settings
        ]

        # Add top and bottom buttons
        for icon, page in self.top_buttons:
            btn = self._make_button(style, icon, page)
            layout.addWidget(btn)
        layout.addStretch()
        for icon, page in self.bottom_buttons:
            btn = self._make_button(style, icon, page)
            layout.addWidget(btn)

        # Apply styling for the sidebar
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
                           QWidget {
                                background-color: #1e1e1e;
                           }

                            QPushButton {
                                background-color: #1e1e1e;
                                border: none;
                            }

                            QPushButton:hover {
                                background-color: #2d2d30;
                            }

                            QPushButton:checked {
                                background-color: #0078d7;
                            }
                            """)

    def _make_button(self, style, icon, page):
        # Create a sidebar button with the specified icon and page index
        btn = QPushButton()
        btn.setIcon(style.standardIcon(icon))
        btn.setIconSize(QSize(24, 24))
        btn.setMinimumHeight(48)
        btn.setCheckable(True)

        # Connect button click to signal emission
        btn.clicked.connect(lambda: self.page_selected.emit(page))

        # Store button reference
        self.buttons.append(btn)
        return btn
    
    def set_active(self, page: str):
        # Update button states/designs based on the active page
        for i in range(len(self.top_buttons)):
            if self.top_buttons[i][1] == page:
                self.buttons[i].setChecked(True)
            else:
                self.buttons[i].setChecked(False)
        for i in range(len(self.bottom_buttons)):
            if self.bottom_buttons[i][1] == page:
                self.buttons[i+len(self.top_buttons)].setChecked(True)
            else:
                self.buttons[i+len(self.top_buttons)].setChecked(False)