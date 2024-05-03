from fastapi import APIRouter
from backend.schemas.message import MessageDTO
from backend.services.service_kakao import KakaoService

router = APIRouter(
    tags=["kakao"],
)

@router.post("/")   # http://127.0.0.1:8000/kakao/
async def send_messagemsg(msg: MessageDTO) -> dict:
    KakaoService().send_message(msg)
    return {"status": {"code": 200, "message": "success"}}