from typing import Literal
from pydantic import BaseModel, UUID4

class ChatDTO(BaseModel): #  챗디티오는 쉽게 말해 가방이다
    type: Literal["text", "voice"] # 텍스트인지 음성인지 체크
    query: str # 사용자 질문
    voice_path: str # 음성 파일 경로(path)
#    session_id: UUID4 | None = None -> 채팅 세션 번호(방 번호), 챗봇 사용자가 여러명이면 방을 만들어 줌, 방을 보통 session이라고 함