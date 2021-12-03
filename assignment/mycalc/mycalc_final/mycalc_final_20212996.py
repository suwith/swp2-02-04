import math

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
        if n >= 4000:
            return 'Error!'

        romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
        ]

        result = ''
        for value, letters in romans:
            while n >= value:
                result += letters
                n -= value
    except:
        return 'Error!'
    return result

def romanToDec(numStr):
    try:
        n = str(numStr)
        result = 0
        romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        if n.isdigit(): #10진수로 입력했을 떄
            return 'input Roman num'

        for key,value in romans:
                if len(value) == 2:
                    while value in n[:2]:
                        result += key
                        n = n[len(value):]
                else:
                    while value in n[:1]:
                        result += key
                        n = n[len(value):]

    except:
        return 'Error!'
    return result

def sin(numstr):
    try:
        n = int(numstr)
        result = math.sin(n)
    except:
        result = 'Error!'
    return result

def cos(numstr):
    try:
        n = int(numstr)
        result = math.cos(n)
    except:
        result = 'Error!'
    return result

def tan(numstr):
    try:
        n = int(numstr)
        result = math.tan(n)
    except:
        result = 'Error!'
    return result

numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = [
    'pi',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)',
]


functionMap =[
    ('factorial (!)',factorial),
    ('-> binary',decToBin),
    ('binary -> dec',binToDec),
     ('-> roman',decToRoman),
      ('roman -> dec',romanToDec),
    ('sin', sin),
    ('cos', cos),
    ('tan', tan),
]
functionList = [x[0] for x in functionMap]
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

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()

        elif key == constantList[0]:
            self.display.clear()
            self.display.setText(self.display.text() + '3.141592')
        elif key == constantList[1]:
            self.display.clear()
            self.display.setText(self.display.text() + '3E+8')
        elif key == constantList[2]:
            self.display.clear()
            self.display.setText(self.display.text() + '340')
        elif key == constantList[3]:
            self.display.clear()
            self.display.setText(self.display.text() + '1.5E+8')
        elif key in functionList:
            n = self.display.text()
            value = functionMap[functionList.index(key)][1](n)
            self.display.setText(str(value))
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
