# fastapi_mysite_card
fastapi, jinja2, sqlalchemy, mariadb, docker, docker-compose, aws, langchain, apscheduler, uvicorn, requests


### 라이브러리 설명
1. fastapi: 웹 프레임워크 + API
2. uvicorn: WAS(웹 어플리케이션 서버)
3. jinja2: 템플릿 엔진(HTML, CSS, JS)



### Web 프로그래밍 기초 설명

#### 1.URL
    - http://127.0.0.1:8000 = http://locatlhost:8000
    - 127.0.0.1과 localhost는 루프백 주소(현재 디바이스의 IP를 의미)
    - 서비스를 위해서 127.0.0.1 을 고정IP로 변경해야 한다.(통신사)
    - IP주소는 외우기 어렵기 때문에 고정IP->DNS서버에 올림(구매) -> ex)chosun.edu
    - http -> 프로토콜
    - 8000 -> Port 번호
    - http 프로토콜 제공하는 함수(get, post, put, delete)
    - http://127.0.0.1:8000/member?id=abc1234&name=cherry -> ? = 쿼리스트링(get방식)
    - 쿼리스트링 : member라는 키워드로 부터 id=abc1234를 전달
    - 단점 : 주소창에 노출됨(패스워드 같은 보안)
    - 숨겨야하는 정보들(post 방식)

### 카카오 나에게 톡 보내기
- 인증코드 URL<Base> : https://kauth.kakao.com/oauth/authorize?client_id={REST API 키}&redirect_uri={Redirect URI}&response_type=code&scope=talk_message
- 인증코드 URL<Me> : https://kauth.kakao.com/oauth/authorize?client_id=d8ea9d83b39a7d3946f273f2d0df02eb&redirect_uri=http://127.0.0.1:8000&response_type=code&scope=talk_message