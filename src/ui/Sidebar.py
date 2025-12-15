from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStyle
from PySide6.QtCore import Qt, QSize, Signal


class Sidebar(QWidget):
    page_selected = Signal(int)  # emits page index

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(50)
        self.setAutoFillBackground(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        style = self.style()
        self.buttons = []

        # Icons and their corresponding page indices
        top_buttons = [
            (QStyle.StandardPixmap.SP_FileIcon, 0),      # Documents
            (QStyle.StandardPixmap.SP_DesktopIcon, 1),   # Themes
        ]
        bottom_buttons = [
            (QStyle.StandardPixmap.SP_FileDialogDetailedView, 2),  # Settings
            (QStyle.StandardPixmap.SP_DirIcon, 3),                 # Projects
        ]

        # Add top and buttom buttons
        for icon, index in top_buttons:
            btn = self._make_button(style, icon, index)
            layout.addWidget(btn)
        layout.addStretch()
        for icon, index in bottom_buttons:
            btn = self._make_button(style, icon, index)
            layout.addWidget(btn)

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

    def _make_button(self, style, icon, index):
        btn = QPushButton()
        btn.setIcon(style.standardIcon(icon))
        btn.setIconSize(QSize(24, 24))
        btn.setMinimumHeight(48)
        btn.setCheckable(True)
        btn.clicked.connect(lambda: self.page_selected.emit(index))
        self.buttons.append(btn)
        return btn

    def set_active(self, index: int):
        for i, btn in enumerate(self.buttons):
            btn.setChecked(i == index)