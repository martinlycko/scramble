import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from Sidebar import Sidebar
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(900, 600)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar = Sidebar()
        self.pages = QStackedWidget()

        self.pages.addWidget(self._page("Documents"))
        self.pages.addWidget(self._page("Themes"))
        self.pages.addWidget(self._page("Settings"))
        self.pages.addWidget(self._page("Projects"))

        self.sidebar.page_selected.connect(self.pages.setCurrentIndex)
        self.sidebar.page_selected.connect(self.sidebar.set_active)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.pages)

    def _page(self, text):
        from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
        w = QWidget()
        layout = QVBoxLayout(w)
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        return w


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())