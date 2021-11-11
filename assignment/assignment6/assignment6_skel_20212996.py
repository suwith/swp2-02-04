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

        self.nameEdit = QLineEdit(self)
        self.ageEdit = QLineEdit(self)
        self.scoreEdit = QLineEdit(self)
        self.amountEdit = QLineEdit(self)

        self.keyEdit = QComboBox(self)
        self.keyEdit.addItem("Name")
        self.keyEdit.addItem("Age")
        self.keyEdit.addItem("Score")

        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Del")
        self.findButton = QPushButton("Find")
        self.incButton = QPushButton("Inc")
        self.showButton = QPushButton("Show")

        self.addButton.clicked.connect(self.clickAdd)
        #self.delButton.clicked.connect(self.clickDel)
        self.findButton.clicked.connect(self.clickFind)
        self.incButton.clicked.connect(self.clickInc)
        self.showButton.clicked.connect(self.clickShow)

        self.resultView = QTextEdit(self)
        self.resultView.setAcceptRichText(False)

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
        hbox3.addWidget(self.addButton)
        hbox3.addWidget(self.delButton)
        hbox3.addWidget(self.findButton)
        hbox3.addWidget(self.incButton)
        hbox3.addWidget(self.showButton)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultView)

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
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    #event
    def clickAdd(self):
        name = self.nameEdit.text()
        age = self.ageEdit.text()
        score = self.scoreEdit.text()
        record = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb += [record]
        self.showScoreDB()

    #def clickDel(self):
        #self.resultView.clear()
        #name = self.NameEdit.text()
        #for p in self.scoredb:
            #if p['Name'] == name:
                #self.scoredb.remove(p)
        #self.showScoreDB()

    def clickFind(self):
        sender = self.sender()
        self.resultView.clear()
        name = self.NameEdit.text()
        for p in self.scoredb:
            if p['Name'] == name:
                result = ""
                for attr in sorted(p):
                    result += attr + " = " + str(p[attr]) + '   '
                self.resultView.append(result)


    def clickInc(self):
        sender = self.sender()
        name = self.NameEdit.text()
        amount = self.amountEdit.text()
        for p in self.scoredb:
            if p['Name'] == name:
                p['Score'] = str(int(p['Score']) + int(amount))
        self.showScoreDB()

    def clickShow(self):
        sender = self.sender()
        self.showScoreDB()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.resultView.clear()
        keyname = self.keyEdit.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            resultList=""
            for attr in sorted(p):
                resultList += (attr + " = " + str(p[attr])+"   ")
            self.resultView.append(resultList)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

