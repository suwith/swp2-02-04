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
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        #레이블, 입력
        lbl1 = QLabel("Name:", self)
        lbl1.move(10, 5)
        self.NameEdit = QLineEdit(self)
        self.NameEdit.move(60, 5)
        lbl2 = QLabel("Age:", self)
        lbl2.move(170, 5)
        self.AgeEdit = QLineEdit(self)
        self.AgeEdit.move(210, 5)
        lbl3 = QLabel("Score:", self)
        lbl3.move(320, 5)
        self.ScoreEdit = QLineEdit(self)
        self.ScoreEdit.move(370, 5)
        lbl4 = QLabel("Amount:", self)
        lbl4.move(200, 40)
        self.AmountEdit = QLineEdit(self)
        self.AmountEdit.move(260, 40)
        lbl5 = QLabel("Keys:", self)
        lbl5.move(370, 40)

        #버튼 구현
        self.addButton = QPushButton("Add", self)
        self.delButton = QPushButton("Del", self)
        self.findButton = QPushButton("Find", self)
        self.incButton = QPushButton("Inc", self)
        self.showButton = QPushButton("show", self)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.delButton)
        hbox.addWidget(self.findButton)
        hbox.addWidget(self.incButton)
        hbox.addWidget(self.showButton)
        vbox = QVBoxLayout()
        vbox.addStretch(100)
        vbox.addLayout(hbox)
        vbox.addStretch(200)
        self.setLayout(vbox)

        # 이벤트 발신
        self.addButton.clicked.connect(self.addClicked)
        self.delButton.clicked.connect(self.delClicked)
        self.findButton.clicked.connect(self.findClicked)
        self.incButton.clicked.connect(self.incClicked)
        self.showButton.clicked.connect(self.showClicked)

        #결과창
        lbl6 = QLabel("Result:", self)
        lbl6.move(10, 100)
        self.result = QTextEdit(self)
        self.result.setAcceptRichText(False)
        self.result.resize(480, 115)
        self.result.move(10,130)

        #콤보상자
        self.combo = QComboBox(self)
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")
        self.combo.resize(80, 30)
        self.combo.move(410, 40)

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

    def showScoreDB(self):
        self.result.clear()
        keyname = self.combo.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            out = ""
            for attr in sorted(p):
                out += (attr + " = " + str(p[attr]) + "     ")
            self.result.append(out)

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    #이벤트 구현
    def addClicked(self):
        sender = self.sender()
        name = self.NameEdit.text()
        age = self.AgeEdit.text()
        score = self.ScoreEdit.text()
        record = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb += [record]
        self.showScoreDB()

    def delClicked(self):
        sender = self.sender()
        name = self.NameEdit.text()
        a = []
        for p in self.scoredb:
            if p['Name'] == name:
                b = self.scoredb.index(p)
                a.append(b)
        a.sort(reverse=True)
        for i in a:
            self.scoredb.pop(i)
        self.showScoreDB()

    def findClicked(self):
        sender = self.sender()
        self.result.clear()
        name = self.NameEdit.text()
        for p in self.scoredb:
            if p['Name'] == name:
                out = ""
                for attr in sorted(p):
                    out += attr + " = " + str(p[attr]) + "     "
                self.result.append(out)


    def incClicked(self):
        sender = self.sender()
        name = self.NameEdit.text()
        amount = self.AmountEdit.text()
        for p in self.scoredb:
            if p['Name'] == name:
                p['Score'] = str(int(p['Score']) + int(amount))
        self.showScoreDB()

    def showClicked(self):
        sender = self.sender()
        self.showScoreDB()


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
