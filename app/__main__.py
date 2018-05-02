import sys

from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtCore import Qt, QFile, QTextStream, QTranslator, QLocale
from PyQt5.QtWidgets import QApplication

from .ui.views.main_view import MainView
from . import resources_rc  # noqa

def main():
    app = QApplication(sys.argv)

    # Support high-res monitors
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        app.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app.setWindowIcon(QIcon(':/icons/app.svg'))

    fontDB = QFontDatabase()
    fontDB.addApplicationFont(':/fonts/Roboto-Regular.ttf')
    app.setFont(QFont('Roboto'))

    f = QFile(':/style.qss')
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    translator = QTranslator()
    translator.load(':/translations/' + QLocale.system().name() + '.qm')
    app.installTranslator(translator)

    mw = MainView()
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
