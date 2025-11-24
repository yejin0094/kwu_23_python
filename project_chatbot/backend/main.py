import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chat import chat_router # 호출시켜 줌

app = FastAPI() # FastAPI를 사용해서 Backend 서버를 구축하겠다

origins = [
    "http://localhost:5000" # 프론트엔드 도메인 주소
]


# 면접 단골 질문
# CORS(Cross Origin Resource Sharing)
# - 브라우저가 다른 도메인(주소-naver.com같은 거) 간 요청을 보안 때문에 제한하는 정책
# - 프론트엔드 -> 백엔드 요청을 보내면 기본적으로 브라우저가 막음(보안 이슈)
# - 특정 도메인(프론트엔드 도메인 주소: 5000번)은 허용해주세요~ -> CORS 설정


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router.router)

# Backend 서버 구동!(실제 서비스를 하는 곳)
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=9000) # http://127.0.0.1:9000/docs - 서버 구동 및 테스트(로컬 컴퓨터를 서버화 시킴)