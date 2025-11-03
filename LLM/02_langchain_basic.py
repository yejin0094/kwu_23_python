# Langchain
# - python 언어 기반의 LLM을 쉽게 사용할 수 있도록 도와주는 라이브러리
# - 챗봇, 에이전트 등을 개발
# * GPT API를 사용해서도 챗봇 또는 에이전트 개발 가능
# * Gemini API를 사용해서도 챗봇 또는 에이전트 개발 가능
# * Cluade API
# * Grok API, ...
# 왜? Langchain을 사용할까? 그냥 GPT API를 사용해서 개발해도 되지 않나?
# - 현재 LLM 중 춘추전국시대...
# - 만약에 GPT API 개발 -> Gemini API로 변경(전체 코드를 수정해야 함)
# - Langchain을 사용한다 -> 모델 변경(코드 1줄)

import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. env 불러오기(API KEY)
_ = load_dotenv(find_dotenv()) # 환경변수 파일(.env) 불러오기

# 2. LLM 모델 (빌려오기)
llm = ChatOpenAI(
    model="gpt-4.1-mini", 
    api_key=os.getenv("OPENAI_API_KEY"), # 발급받은 키 값을 인증해서 쓸 수 있게 해줌??
    temperature=0, # 교수) 1에 가까울수록 AI 창의력 ↑ ,예진) 0부터 1사이의 값을 바꿈 1로 올릴 수록 인공지능의 상상력이 풍부해짐(창착에 관련된거는 1로 올려주면 됨)
)

# 3. 프롬프트
# - LLM으로부터 원하는 답변을 얻기 위한 명령(instruction?)
# - 프롬프트가 3가지가 있음
# 가. System prompt: 역할, 설정, 명령   ...?(교수님 녹음 설명 듣기) , 답변을 어떻게 할지 설정해줌
# 나. Human Prompt: 질문(Query(질문 = 퀘스쳔))
# 다. AI prompt: 답변(AI가 생성한)

system_prompt = """
    너는 사용자의 질문에 도움을 주는 어시스턴트야.
    사용자의 질문에 대한 답변을 생성해줘.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt), 
    ("human", "{query}")
])

# 4. Chain 생성
chain = prompt | llm # | 파이프라는 연산자(or과 같음)

# 5. Chain 실행
query = "나의 이름은 양예진이야!" # 질문을 쓰는 곳
answer = chain.invoke({"query": query})
print(answer)

# Langchain 챗봇(싱글턴 챗봇?)
# 1. api-key 불러오기
# 2. LLM 모델
# 3. Prompt 작성
# 4. Chain 생성
# 5. 실행

# 싱글턴 챗봇: 질문 -> 답변 끝(대화 X) 질문한번 대화한번씩 하고 끝 대화 하지 않음
# ㄴ System + Human
# 멀티턴 챗봇: 대화(질문,답변, 질문,답변 저장) 대화가능하고 저장을 가능?
# ㄴ System(설정값) + History(대화??기록) + Human(??)

