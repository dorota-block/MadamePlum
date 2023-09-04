import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MadamePlum(QMainWindow):
    def __init__(self):
        super(MadamePlum, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Madame Plum")
        self.init_ui()

    def init_ui(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Woof")


def madame_plum():
    app = QApplication(sys.argv)
    win = MadamePlum()
    win.show()
    sys.exit(app.exec())


madame_plum()

# Command: qt5-tools designer
