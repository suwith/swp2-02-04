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
        result = QLabel('Result:')
        key = QLabel('Key:')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.resultEdit = QTextEdit()

        self.keyEdit.addItem('Name')
        self.keyEdit.addItem('Age')
        self.keyEdit.addItem('Score')

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
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(score)
        hbox.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keyEdit)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(result)
        vbox.addWidget(self.resultEdit)

        addButton.clicked.connect(self.addButtonClicked)
        delButton.clicked.connect(self.delButtonClicked)
        findButton.clicked.connect(self.findButtonClicked)
        incButton.clicked.connect(self.incButtonClicked)
        showButton.clicked.connect(self.showButtonClicked)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    

    def showScoreDB(self):
        keyname = self.KeyBox.currentText()
        kn = []
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                kn.append(str(attr) + " = " + str(p[attr]))
                kn.append("                    ")
            kn.append("\n")
        self.ResultText.setText(''.join(kn))

    def addButten(self):
        name = self.NameEdit.text()
        age = self.AgeEdit.text()
        score = self.ScoreEdit.text()
        self.scoredb.append({'Name': name, 'Age': int(age), 'Score': int(score)})
        self.showScoreDB()

    def delButten(self):
        name = self.NameEdit.text()
        a = 0
        for i in self.scoredb:
            if name == i['Name']:
                a += 1
        for k in range(a):
            for i in self.scoredb:
                if name == i['Name']:
                    self.scoredb.remove(i)
                    continue
        self.showScoreDB()

    def incButten(self):
        name = self.NameEdit.text()
        amount = self.AmountEdit.text()
        for p in self.scoredb:
            if p['Name'] == name:
                p['Score'] = int(p['Score']) + int(amount)
                p['Score'] = str(p['Score'])
        self.showScoreDB()

    def findButten(self):
        name = self.NameEdit.text()
        keyname = self.KeyBox.currentText()
        kn = []
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            if name == p['Name']:
                for attr in sorted(p):
                    kn.append(str(attr) + " = " + str(p[attr]))
                    kn.append("                    ")
                kn.append("\n")
        self.ResultText.setText(''.join(kn))
        
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()  



if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
            
