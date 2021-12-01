import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QErrorMessage)
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
        label = ["Name:", "Age:", "Score:", "Amount:", "Keys:"]
        l1 = [[10, 5], [170, 5], [320, 5], [200, 40], [370, 40]]
        for i in range(5):
            lbl = QLabel(label[i], self)
            lbl.move(l1[i][0], l1[i][1])
        self.NameEdit = QLineEdit(self)
        self.NameEdit.move(60, 5)
        self.AgeEdit = QLineEdit(self)
        self.AgeEdit.move(210, 5)
        self.ScoreEdit = QLineEdit(self)
        self.ScoreEdit.move(370, 5)
        self.AmountEdit = QLineEdit(self)
        self.AmountEdit.move(260, 40)

        #버튼 구현력, # 이벤트 발신
        hbox = QHBoxLayout()
        hbox.addStretch(1)

        bt = ["Add", "Del", "Find", "Inc", "show"]
        for i in range(5):
            self.button = QPushButton(bt[i], self)
            hbox.addWidget(self.button)
            self.button.clicked.connect(self.buttonClicked)
        vbox = QVBoxLayout()
        vbox.addStretch(100)
        vbox.addLayout(hbox)
        vbox.addStretch(200)
        self.setLayout(vbox)

        #결과창
        lbl6 = QLabel("Result:", self)
        lbl6.move(10, 100)
        self.result = QTextEdit(self)
        self.result.setAcceptRichText(False)
        self.result.resize(480, 115)
        self.result.move(10, 130)

        #콤보상자
        self.combo = QComboBox(self)
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")
        self.combo.resize(80, 30)
        self.combo.move(410, 40)
        self.show()
         #에러 메시지
        self.error = QErrorMessage()

    def closeEvent(self, event):
        self.writeScoreDB()

    def buttonClicked(self):
        sender = self.sender()
        try:
            if sender.text() == "Add":
                name = self.NameEdit.text()
                age = self.AgeEdit.text()
                score = self.ScoreEdit.text()
                if len(name) == 0:
                    m = "input name"
                    self.error.showMessage(m)
                    raise Exception(m)
                if name.isdigit():
                    m = "input name in String from"
                    self.error.showMessage(m)
                    raise Exception(m)
                if len(age) == 0:
                    m = "input age"
                    self.error.showMessage(m)
                    raise Exception(m)
                if len(score) == 0:
                    m = "input score"
                    self.error.showMessage(m)
                    raise Exception(m)
                if not age.isdigit():
                    m = 'input age in integer form'
                    self.error.showMessage(m)
                    raise Exception(m)
                if not score.isdigit():
                    m = 'input score in integer form'
                    self.error.showMessage(m)
                    raise Exception(m)
                record = {'Name': name, 'Age': age, 'Score': score}
                self.scoredb += [record]
                self.showScoreDB()

            elif sender.text() == "Del":
                name = self.NameEdit.text()
                if len(name) == 0:
                    m = "input name"
                    self.error.showMessage(m)
                    raise Exception(m)
                a = []
                for p in self.scoredb:
                    if p['Name'] == name:
                        b = self.scoredb.index(p)
                        a.append(b)
                a.sort(reverse=True)
                for i in a:
                    self.scoredb.pop(i)
                self.showScoreDB()
            elif sender.text() == "Find":
                self.result.clear()
                name = self.NameEdit.text()
                if len(name) == 0:
                    m = "input name"
                    self.error.showMessage(m)
                    raise Exception(m)
                for p in self.scoredb:
                    if p['Name'] == name:
                        out = ""
                        for attr in sorted(p):
                            out += attr + " = " + str(p[attr]) + "     "
                        self.result.append(out)
            elif sender.text() == "Inc":
                name = self.NameEdit.text()
                amount = self.AmountEdit.text()
                if len(name) == 0:
                    m = "input name"
                    self.error.showMessage(m)
                    raise Exception(m)
                if len(amount) == 0:
                    m = "input amount"
                    self.error.showMessage(m)
                    raise Exception(m)
                if not amount.isdigit():
                    m = 'input amount in integer form'
                    self.error.showMessage(m)
                    raise Exception(m)
                for p in self.scoredb:
                    if p['Name'] == name:
                        p['Score'] = str(int(p['Score']) + int(amount))
                self.showScoreDB()
            elif sender.text() == "show":
                self.showScoreDB()
        except Exception as e:
            print("[error]", e)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
