import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
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
        Name = QLabel("Name:")
        Age = QLabel("Age:")
        Score = QLabel("Score:")
        Amount = QLabel("Amount:")
        Result = QLabel("Result:")

        self.NameEdit = QLineEdit()
        self.AgeEdit = QLineEdit()
        self.ScoreEdit = QLineEdit()
        self.AmountEdit = QLineEdit()
        self.ResultText = QTextEdit()
        self.ResultText.setAcceptRichText(False)

        AddButten = QPushButton("Add")
        DelButten = QPushButton("Del")
        FindButten = QPushButton("Find")
        IncButten = QPushButton("Inc")
        ShowButten = QPushButton("Show")

        Key = QLabel("Key:")
        self.KeyBox = QComboBox()
        self.KeyBox.addItem('Name')
        self.KeyBox.addItem('Age')
        self.KeyBox.addItem('Score')

        hbox0 = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()

        hbox0.addStretch(1)
        hbox0.addWidget(Name)
        hbox0.addWidget(self.NameEdit)
        hbox0.addWidget(Age)
        hbox0.addWidget(self.AgeEdit)
        hbox0.addWidget(Score)
        hbox0.addWidget(self.ScoreEdit)

        hbox1.addStretch(1)
        hbox1.addWidget(Amount)
        hbox1.addWidget(self.AmountEdit)
        hbox1.addWidget(Key)
        hbox1.addWidget(self.KeyBox)

        hbox2.addStretch(1)
        hbox2.addWidget(AddButten)
        hbox2.addWidget(DelButten)
        hbox2.addWidget(FindButten)
        hbox2.addWidget(IncButten)
        hbox2.addWidget(ShowButten)

        hbox3.addWidget(Result)
        hbox3.addStretch(1)
        hbox4.addWidget(self.ResultText)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

        AddButten.clicked.connect(self.addButten)
        DelButten.clicked.connect(self.delButten)
        FindButten.clicked.connect(self.findButten)
        IncButten.clicked.connect(self.incButten)
        ShowButten.clicked.connect(self.showScoreDB)



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



if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
