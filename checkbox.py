import sys
from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)



class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        self.lbl = QLabel()
        self.cbx = QCheckBox("Do you like cats?")
        self.btn = QPushButton("Push me")


        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.cbx)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.btn.clicked.connect(lambda: self.btn_click(self.cbx.isChecked(), self.lbl))


        self.setWindowTitle("PyQt5 lesson 9")

        self.show()


    def btn_click(self, chk, lbl):
        if chk:
            lbl.setText("I guess you like cats")
        else:
            lbl.setText("Cat hater than")


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())