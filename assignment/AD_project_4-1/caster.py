
class caster:
    #텍스트에딧에 들어갈 문장 리턴
    def casting(self, wea, rain, dust, uv, crn):
        sen = ""
        if wea == '비' or wea == '눈':
            sen += wea + "가 오니 우산을 챙기세요.\n"
        elif wea == '맑음':
            sen += "날씨가 맑고 좋아요.\n"
        else:
            if rain == '60%' or rain == '70%' or rain == '80%' or rain == '90%':
                sen += "비가 올 수 있으니 우산을 챙기는게 좋아요.\n"

        if dust == '나쁨':
            sen += "미세먼지가 심하니 황사마스크를 쓰시는게 좋아요.\n"
        elif dust == '좋음' or dust == '보통':
            sen += "오늘은 공기가 나쁘지 않아요!\n"
        if uv == '나쁨':
            sen += "자외선이 세니 자외선 차단제를 바르시는게 좋아요.\n"

        sen += "신규 확진자 수는 " + crn + "명이에요. 언제나 조심하세요."
        return sen

#단위테스트
if __name__ == '__main__':
    test = caster.casting('', '비', '30%', '나쁨', '나쁨', '7000')
    print(test)
    test2 = caster.casting('', '구름많음', '80%', '보통', '좋음', '5000')
    print(test2)
