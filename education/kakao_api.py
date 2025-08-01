# 카카오 API를 사용해서 나에게 톡 보내기
#   1.Kakao Developer 설정
#   2.인증 코드를 요청 -> 카카오 서버 -> 인증 코드 전달(인증 코드는 1회성 -> 토큰 1회 발급받음과 동시에 효력X)
#   3.인증 코드를 사용해서 토큰 발급
#   4.토큰을 사용해서 나에게 메세지 보내기
import requests
import json


# 1.카카오 OAUTH URL과 Redirect Key를 사용해서 인증 코드 요청
#   - 웹 브라우저 URL:https://kauth.kakao.com/oauth/authorize?client_id=d8ea9d83b39a7d3946f273f2d0df02eb&redirect_uri=http://127.0.0.1:8000&response_type=code&scope=talk_message
#   - 위의 코드를 웹 브라우저 URL에 입력하고 엔터누르면 새로운 URL로 변경 code=[???]
#   - [???] -> 카카오로부터 전달받은 인증코드

# 2.인증코드를 사용해서 토큰 발급받기
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": "d8ea9d83b39a7d3946f273f2d0df02eb",    # RESTAPI KEY
    "redirect_uri": "http://127.0.0.1:8000",             # Redirect URI
    "code": "gSasYyAal21QMmPMUgjADsEMJB9hWTtA2s2hcJenVYnknEUWirbwq-3KOL0KPXObAAABjuTk4ar6Fwx8Dt1GgQ"    # 받은 인증코드
}

# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)

#   access_token 발급
#   refresh_token 발급

# 3.토큰 이용해서 나에게 톡 보내기
access_token = "ekAYwgAagmtNR46F1_QSTQ4nUH7cdPXslZQKKcjZAAABjuTlgv237mS5Kc-sjw"
refresh_token = "vzXUdunYCZUkbJMidLe_7WJdoEnI97ymldwKKcjZAAABjuTlgvq37mS5Kc-sjw"

msg_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + access_token
}
msg_data = {
    "template_object": json.dumps({
        "object_type": "text",
        "text": "카카오톡 테스트",
        "link": {"mobile_web_url": "https://www.naver.com"}
    })
}
response = requests.post(msg_url, headers=headers, data=msg_data)