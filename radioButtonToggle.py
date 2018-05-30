import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication,  QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel("Which do you like best?")
        self.cat = QRadioButton("Cats")
        self.dog = QRadioButton("Dogs")
        # self.btn = QPushButton("Select")

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.cat)
        layout.addWidget(self.dog)
        # layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle("PyQt5 lesson 10")

        # self.btn.clicked.connect(lambda: self.btn_click(self.cat.isChecked(), self.lbl))
        self.cat.toggled.connect(lambda: self.btn_state(self.cat, self.lbl))
        self.dog.toggled.connect(lambda: self.btn_state(self.dog, self.lbl))


        self.show()


    def btn_state(self, checkbox, lbl):
        if checkbox.text() == "Cats":
            lbl.setText("I guess you like cats")
        else:
            lbl.setText("So its cats for you")


    # def btn_click(self, chk, lbl):
    #     if chk:
    #         lbl.setText("I guess you like cats")
    #     else:
    #         lbl.setText("So its cats for you")

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())