import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from mainScene import MainScene

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScene()
    sys.exit(app.exec_())
