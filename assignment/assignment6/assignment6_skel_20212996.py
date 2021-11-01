import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit )
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result:')

        nameEdit = QLineEdit()
        ageEdit = QLineEdit()
        scoreEdit = QLineEdit()
        amountEdit = QLineEdit()
        keyEdit = QComboBox()
        keyEdit.addItem("Name")
        keyEdit.addItem("Age")
        keyEdit.addItem("Score")

        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")

        resultView = QTextEdit()

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(name)
        hbox.addWidget(nameEdit)
        hbox.addWidget(age)
        hbox.addWidget(ageEdit)
        hbox.addWidget(score)
        hbox.addWidget(scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(keyEdit)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(resultView)

        vbox.addLayout(hbox)  # 세로레이아웃에 가로 레이아웃더하기
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 600, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

