from backend.schemas.message import MessageDTO
import os
from dotenv import load_dotenv

class KakaoService:
    # 카카오 토큰 발급받기(+ 인증코드)
    def get_first_token(self):
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": "d8ea9d83b39a7d3946f273f2d0df02eb",    # RESTAPI KEY
            "redirect_uri": "http://127.0.0.1:8000",             # Redirect URI
            "code": "gSasYyAal21QMmPMUgjADsEMJB9hWTtA2s2hcJenVYnknEUWirbwq-3KOL0KPXObAAABjuTk4ar6Fwx8Dt1GgQ"    # 받은 인증코드
        }
    
    # Access Token 재발급(+ Refresh Token)
    def refresh_access_token(self):
        pass
    
    
    # 나에게 카카오톡 보내기!
    def send_message(self, msg: MessageDTO):
        
        # 1. 토큰 유무 체크
        if os.path.isfile("./kakao_code.json"):
            # - 토큰 있는 경우 -> Refresh Token을 활용해서 재발급
            tokens = self.refresh_access_token()
        else:
            # - 토큰 없는 경우 -> 토큰 발급
            tokens = self.get_first_token()
        
        # 2. Access Token을 사용해서 카카오톡 보내기
        
        # 3. DB에 저장
        
        # +. 스케줄러 등록(Refresh Token 재발급)
        #   - Refresh Token은 유효기간 2달
        #   - 그리고 발급받은 날짜로부터 1달 후 재발급 가능
        #   - 스케줄러 -> 1달에 한번씩 Refresh Token을 재발급 받으세요!