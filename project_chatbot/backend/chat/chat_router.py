from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from chat.chat_schema import ChatDTO
from chat.chat_service import ChatService

# 123.0.0.1:9000 -> 도메인 주소
# 127.0.0.1:9000/api 아래로 가세요...??
router = APIRouter(prefix="/api") # 127.0.0.1=9000(주소)

# 127.0.0.1:9000/api/chat <- 사용자가 요런 요청을 보내면 아래 함수를 타세요
# Gabia라는 사이트에서 도메인 주소를 사면 됨
@router.post("/chat")
async def chat(chat_dto: ChatDTO):
    query = chat_dto.query.strip()
    print(f"Human: {query}")
    
    chat_service = ChatService() # 라우터가하는게 아니라 실제 얘가 함..?, 챗서비스 객체 생성
    answer = await chat_service.gen_answer(query) # 가면 호출문이고 갔다오면 변수...?
    
    print(f"AI: {answer}")
    
    return {"success_code": 200, "answer": answer}