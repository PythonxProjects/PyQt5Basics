import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.show()
    w.setWindowTitle("Hello World lesson 1")
    sys.exit(app.exec_())


window()