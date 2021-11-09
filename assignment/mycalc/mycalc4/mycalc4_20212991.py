from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        numLayout = QGridLayout()
        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        numtext = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '=']
        numloctn = [[3, 0], [2, 0], [2, 1], [2, 2], [1, 0], [1, 1],
               [1, 2], [0, 0], [0, 1], [0, 2], [3, 1], [3, 2]]
        for i, j in zip(numtext, numloctn):
            button = Button(i, self.buttonClicked)
            numLayout.addWidget(button, j[0], j[1])

        opLayout = QGridLayout()

        opertext = ['*', '/', '+', '-', '(', ')', 'C']
        operloctn = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [3, 0]]
        for i, j in zip(opertext, operloctn):
            button = Button(i, self.buttonClicked)
            opLayout.addWidget(button, j[0], j[1])
        
        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")

    #연산기능구현
    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
