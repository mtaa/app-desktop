from PyQt5.QtWidgets import QMainWindow
from .main_window_ui import Ui_MainWindow

class MainView(QMainWindow, Ui_MainWindow):
    """Main View."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
