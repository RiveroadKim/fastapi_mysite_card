from fastapi import APIRouter

router = APIRouter(
    tags=["kakao"],
)

@router.post("/")   # http://127.0.0.1:8000/kakao/
async def send_messagemsg(msg: MessageDTO) -> dict:
    return {"status": {"code": 200, "message": "success"}}