# This is a QT example Python script.
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


# pip install sip
# pip install PyQt5
# pip install PyQt5-tools


# Press Shift+F10 to execute or replace it with your code.
# Press double-click Shift to search everywhere for classes, files, tool windows, actions and settings.

# Use breakpoints on the following lines of code to debug the script.
class MainWindow(QWidget):
    # Press Ctrl+F8 to toggle breakpoints.
    def __init__(self):
        super().__init__()
        # Dynamically read local QT UI files
        uic.loadUi('pyQT.ui', self)


# Press the green button in the gap to run the script.
if __name__ == '__main__':
    app = QApplication([])
    root = MainWindow()
    root.show()
    sys.exit(app.exec_())


# Visit https://www.jetbrains.com/help/pycharm/ for PyCharm help
