import urllib
from PyQt5.QtGui import QPixmap

#이미지 불러오기 위한 이미지 주소 링크
class image:
    def img(self, wea):
        if wea == '맑음':
            img_url = 'https://ac-illust.com/_next/image?url=https%3A%2F%2Fthumb.ac-illust.com%2Fee%2Fee3e46641e55d35026b8c1321f8a124d_w.jpeg&w=1920&q=75'
        elif wea == '구름조금':
            img_url = 'https://pbs.twimg.com/media/CmtsHbwVIAA-QgZ.jpg'
        elif wea == '구름많음':
            img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4X1Gzav1uRVoz6xPg1CfylnekFA5Ar0t9WQ&usqp=CAU'
        elif wea == '흐림':
            img_url = 'https://en.pimg.jp/068/603/368/1/68603368.jpg'
        elif wea == '비':
            img_url = 'https://previews.123rf.com/images/surfupvector/surfupvector1607/surfupvector160700070/59718324-%EB%B9%97%EB%B0%A9%EC%9A%B8%EC%9D%B4-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8%EC%99%80-%ED%95%A8%EA%BB%98-%EA%B5%AC%EB%A6%84-%ED%9D%90%EB%A6%B0-%EB%82%A0%EC%94%A8-%EB%B9%84-%EC%9D%BC%EA%B8%B0-%EC%98%88%EB%B3%B4-%EB%82%A0%EC%94%A8-%EA%B0%9C%EB%85%90%EC%9E%85%EB%8B%88%EB%8B%A4-%EB%82%A0%EC%94%A8-%EA%B8%B0%ED%9B%84-%EA%B8%B0%EC%83%81-%EC%9D%BC%EA%B8%B0-%EC%98%88%EB%B3%B4%EC%99%80-%EA%B0%99%EC%9D%80-%EC%A3%BC%EC%A0%9C%EC%97%90-%EC%82%AC%EC%9A%A9%ED%95%A0-%EC%88%98-%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4-.jpg'
        elif wea == '눈':
            img_url = 'https://www.urbanbrush.net/web/wp-content/uploads/edd/2018/10/urbanbrush-20181027060217785326.png'

        img_data = urllib.request.urlopen(img_url).read()
        img_obj = QPixmap()
        img_obj.loadFromData(img_data)
        img_obj = img_obj.scaledToWidth(100)

        return img_obj
