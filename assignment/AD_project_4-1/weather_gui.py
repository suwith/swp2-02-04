
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton
from PyQt5.QtWidgets import QTextEdit, QLineEdit
from PyQt5.QtGui import *
from weather import *
from image import *
from caster import *

class cast(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 410, 430)
        self.setWindowTitle('현재 날씨 정보')

        #레이블, 입력
        lbl1 = QLabel("현재 시각", self)
        lbl1.move(10, 15)
        lbl1.setFont(QFont('Arial', 11))
        #현재시간입력
        self.time = QLineEdit(self)
        self.time.move(75, 15)
        self.time.resize(165, 30)
        self.time.setFont(QFont('Arial'))
        self.time.setReadOnly(True)
        #현재온도입력
        self.temp = QLineEdit(self)
        self.temp.move(190, 70)
        self.temp.resize(170, 50)
        self.temp.setFont(QFont('Arial', 20))
        self.temp.setReadOnly(True)
        #어제와현재온도비교입력
        self.temp_c = QLineEdit(self)
        self.temp_c.move(190, 125)
        self.temp_c.resize(170, 50)
        self.temp_c.setFont(QFont('Arial', 13))
        self.temp_c.setReadOnly(True)
        #날씨입력
        self.wea = QLineEdit(self)
        self.wea.move(50, 150)
        self.wea.resize(100, 40)
        self.wea.setFont(QFont('Arial', 15))
        self.wea.setReadOnly(True)
        #강수확률입력
        self.rain = QLineEdit(self)
        self.rain.move(10, 340)
        self.rain.resize(90, 50)
        self.rain.setFont(QFont('Arial', 11))
        self.rain.setReadOnly(True)
        #미세먼지입력
        self.dust = QLineEdit(self)
        self.dust.move(110, 340)
        self.dust.resize(90, 50)
        self.dust.setFont(QFont('Arial', 11))
        self.dust.setReadOnly(True)
        #자외선입력
        self.uv = QLineEdit(self)
        self.uv.move(210, 340)
        self.uv.resize(90, 50)
        self.uv.setFont(QFont('Arial', 11))
        self.uv.setReadOnly(True)
        #코로나확진자수입력
        self.corona = QLineEdit(self)
        self.corona.move(310, 340)
        self.corona.resize(90, 50)
        self.corona.setFont(QFont('Arial', 11))
        self.corona.setReadOnly(True)

        #푸시버튼
        #날씨조회
        self.LButton = QPushButton("조회", self)
        self.LButton.move(335, 15)
        self.LButton.resize(70, 30)
        #강수확률조회
        self.RButton = QPushButton("강수확률", self)
        self.RButton.move(10, 390)
        self.RButton.resize(90, 30)
        #미세먼지조회
        self.DButton = QPushButton("미세먼지", self)
        self.DButton.move(110, 390)
        self.DButton.resize(90, 30)
        #자외선조회
        self.UVButton = QPushButton("자외선", self)
        self.UVButton.move(210, 390)
        self.UVButton.resize(90, 30)
        #확진자수조회
        self.CButton = QPushButton("신규 확진자 수", self)
        self.CButton.move(310, 390)
        self.CButton.resize(90, 30)

        #이벤트 발신
        self.LButton.clicked.connect(self.LClicked)
        self.RButton.clicked.connect(self.RClicked)
        self.DButton.clicked.connect(self.DClicked)
        self.UVButton.clicked.connect(self.UVClicked)
        self.CButton.clicked.connect(self.CClicked)

        # 콤보상자
        self.combo = QComboBox(self)
        self.combo.addItem("현재 위치")
        self.combo.addItem("서울")
        self.combo.addItem("인천")
        self.combo.addItem("광주")
        self.combo.addItem("부산")
        self.combo.addItem("제주")
        self.combo.resize(85, 30)
        self.combo.move(245, 15)
        self.combo.setFont(QFont('Arial', 11))

        #결과창
        self.result = QTextEdit(self)
        self.result.setAcceptRichText(False)
        self.result.resize(390, 130)
        self.result.move(10, 200)
        self.result.setFont(QFont('Arial', 12))
        self.result.setReadOnly(True)

        #이미지
        # self.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.label.move(50, 60)
        self.label.resize(100, 80)

    def LClicked(self):
        sender = self.sender()
        #입력창 초기화
        self.rain.clear()
        self.dust.clear()
        self.uv.clear()
        self.corona.clear()
        self.result.clear()

        #키값받기
        key = self.combo.currentText()

        #LineEdit들에 입력
        self.time.setText(weather.dt(self))
        self.temp.setText(weather.temp(self, key))
        self.temp_c.setText('  어제보다  ' + weather.temp_c(self, key))
        self.wea.setText('     ' + weather.wea(self, key))

        #결과 textEdit에 입력
        wea = weather.wea(self, key)
        rain = weather.rain(self, key)
        w = weather.w_list(self, key)
        dust = w[1]
        uv = w[5]
        crn = weather.corona(self)
        sen = caster.casting(self, wea, rain, dust, uv, crn)
        self.result.append(sen)

        #이미지 받아서 레이블에 삽입
        img = image.img(self, wea)
        self.label.setPixmap(img)

    def RClicked(self):
        sender = self.sender()
        key = self.combo.currentText()
        self.rain.setText('      ' + weather.rain(self, key))

    def DClicked(self):
        sender = self.sender()
        key = self.combo.currentText()
        w = weather.w_list(self, key)
        self.dust.setText("       " + w[1])

    def UVClicked(self):
        sender = self.sender()
        key = self.combo.currentText()
        w = weather.w_list(self, key)
        self.uv.setText("       " + w[5])

    def CClicked(self):
        sender = self.sender()
        self.corona.setText('      ' + weather.corona(self))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    cast = cast()
    cast.show()
    sys.exit(app.exec_())
