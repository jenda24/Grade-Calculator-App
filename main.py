import sys
from PyQt6 import QtWidgets
from gui import Ui_MainWindow


def main() -> None:
    """
    This is where the application starts

    :return: None
    """

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # set up the UI and show window
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # start application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()