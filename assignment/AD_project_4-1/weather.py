import datetime
from bs4 import BeautifulSoup
import urllib.request


class weather:

    #콤보상자의 위치에 따른 날씨 웹 리턴
    def location(self, lct):
        if lct == '현재 위치':
            self.webpage = urllib.request.urlopen(
                'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hjrKssp0JXVssAhimcRssssst4o-368279')
        elif lct == '서울':
            self.webpage = urllib.request.urlopen(
                'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8')
        elif lct == '인천':
            self.webpage = urllib.request.urlopen(
                'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hjJD3dprvN8ss7rD%2FDosssssse0-211436&acq=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8&acr=2&qdt=0')
        elif lct == '광주':
            self.webpage = urllib.request.urlopen(
                'https://search.naver.com/search.naver?sm=tab_sug.asiw&where=nexearch&query=%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8&tqi=hjJEilprvxZsskg2bpossssstRR-023720&acq=%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&acr=1&qdt=0')
        elif lct == '부산':
            self.webpage = urllib.request.urlopen(
                'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&tqi=hjJEFlprvOssshDI1EZsssssshZ-366366')
        elif lct == '제주':
            self.webpage = urllib.request.urlopen(
                'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%A0%9C%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&tqi=hjJEXsprvhGssRH74yZssssstPN-094037&acq=%EC%A0%9C%EC%A3%BC+%EB%82%A0%EC%94%A8&acr=2&qdt=0')
        self.soup = BeautifulSoup(self.webpage, 'html.parser')
        return self.soup

    #현재시간 리턴
    def dt(self):
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분')
        return nowDate
    #현재온도 리턴
    def temp(self, lct):
        soup = weather.location(self, lct)
        temps = soup.find('div', "temperature_text")
        t = temps.get_text()
        return t
    #어제와의비교 리턴
    def temp_c(self, lct):
        soup = weather.location(self, lct)
        temp_c = soup.find('span', "temperature down")
        t = temp_c.get_text()
        return t
    #강수확률 리턴
    def rain(self, lct):
        soup = weather.location(self, lct)
        rain = soup.find('dd', "desc")
        r = rain.get_text()
        return r
    #날씨 리턴
    def wea(self, lct):
        soup = weather.location(self, lct)
        weathe = soup.find('span', "weather before_slash")
        w = weathe.get_text()
        return w
    #미세먼지,자외선이 포함된 문자열 추출후 리스트로 리턴(각각 추출이 안되서)
    def w_list(self, lct):
        soup = weather.location(self, lct)
        dust = soup.find('ul', "today_chart_list")
        d = str(dust.get_text())
        w = d.strip().split()
        return w
    #코로나 확진자수 리턴
    def corona(self):
        self.webpage2 = urllib.request.urlopen(
            'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98&oquery=%EC%98%A4%EB%8A%98+%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90%EC%88%98&tqi=hjwF4lp0JXossn%2BL8UCssssstww-250123')
        self.soup2 = BeautifulSoup(self.webpage2, 'html.parser')
        covid19 = self.soup2.find('em', "info_variation")
        c = covid19.get_text()
        return c

#단위테스트
if __name__ == '__main__':
    test = weather.temp('', '서울') + weather.wea('', '부산') + weather.corona('')
    print(test)
