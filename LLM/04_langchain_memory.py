# 디프리케이티드 - 새로운 버전으로 업데이트(예전꺼는 이제 안써요!-이전에 불편한 것을 보완해서 새로운 버전으로 업데이트시킴, 절대 사용하면 안됨)



# input을 넣으면 LLM(GPT 4.1-mini) answer를 줌

# > input 정의
# 1. System Prompt(답변 생성 관련 명령)
# 2. Human Prompt(질의: Query)
# 3. chat history(사람과 AI의 대화 기록) **1,2,3번은 멀티턴이지만 3번을 빼면 1,2번만 싱글턴이다!

# > answer
# 1. ai prompt(답변 생성)

# 멀티턴 챗봇의 핵심: Chat History
#   ㄴ 1. Memory: 휘발성(날아가버림), 속도 빠름 ↑ ex) LG 서비스 챗봇
#   ㄴ 2. Database: 영속성(전원공급만 되면 영원히 반영구적으로 쓸 수 있음), 속도 느림 ↓ ex) 개인용 GPT

import os # os는 .env에서 씀..?
import uuid
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# from langchain.memory import ConversationBufferMemory (사용 안함)
# from langchain.schema.runnable import RunnablePassthrough (사용 안함)


# from langchain_core.memory
# Langchain보다 더 복잡하게 할 수 있는 LangGraph가 최근에 만들어졌음 그래서 랭체인에서 쓰던 코드를 랭그래프와 병합해서 from langchain_core.memory를 지원하지 않게 되었음...
# 왜 적었냐고 그냥 재밌으라고 ㅋㅋㅋ

# 1. .env파일 불러오기(불어오기만 한거지 사용하지 않음)
_ = load_dotenv(find_dotenv()) # 전부다 가지고 오세요

# 2. LLM 모델
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.2,
)


# +. 세션별 히스토리 저장소(휘발성)
# - 현재 대화기록(히스토리)은 메모리에 저장되기 때문에 서버 종료되면 소멸 됨
#      ㄴ 영구적으로 보관하고 싶으면 DB에 저장해야 함
# - 세션 -> 사용자의 대화 Room(방) 개념...? 녹음 듣고 더 보충하기
#    ㄴ 예진 -> 세션 A, 세션 B, 세션 C
#    ㄴ 고은 -> 세션 D, 세션 E, 세션 F
#    ㄴ 하은 -> 세션 S, 세션 Z, 세션 A  사용자가 여러개의 방을 만들 수 있음/ 근데!! 똑같은 방 이름을 만들 수 없음(세션A가 중복되면 안됨)
#                                                                                                             ㄴ (세션 이름은 중복 X)
# - 중복되면 안되는 경우 -> UUID(난수값) 값을 사용! uuid는 랜덤한 값을 만들어줌
session_id = str(uuid.uuid4()) # 세션을 랜덤한 값으로 만듦 uuid4함수를 사용해서...
# print(session_id) # 세션 아이디 출력/ 난수가 너무 길어서 앞에 양예진에 id를 붙어사용
# exit() # 여기까지 실행하고 나가짐


# - 세션별 히스토리 저장소(휘발성)
_store = {} # 빈 딕셔너리 생성, 메모리라고 생각

def get_history(session_id: str) -> ChatMessageHistory:
    # session_id: str -> 세션 아이디를 문자열로 받음
    # -> ChatMessageHistory:  ChatMessageHistory 객체를 반환함
    # session_id가 메모리에 없는 경우 생성 후 가져오기,
    #                             있는 경우 가져오기
    """세션 아이디에 해당하는 히스토리 객체를 반환하는 함수"""
    if session_id not in _store:
        _store[session_id] = ChatMessageHistory() # 세션 아이디가 없으면 새로 생성
    return _store[session_id] # 있으면 있는거 반환
# 해석
# 녹음 파일 듣고 적기...?


# 3. Prompt 작성
system_prompt = """
    너는 사용자의 질문에 도움을 주는 어시스턴트야.
    사용자의 질문에 대한 답변을 생성해줘.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt), # System prompt랑 Human prompt를 같이 전달한다 (멀티턴이엿다면 챗히스토리 프롬프트가 추가된다), system prompt
    MessagesPlaceholder(variable_name="history"), # 대화기록, chat history
    ("human", "{query}"), # 질문, Human prompt
    
])

# 4. Chain 생성
# 기존 버전) chain = prompt | llm
base_chain = prompt | llm # 챗_히스토리에서 대화기록을 꺼내오세요 ****프롬프트 만들때 llm에 전달****

chain = RunnableWithMessageHistory(
    base_chain, # 히스토리, 사용자의 질문(휴먼거 필요)
    get_session_history=get_history, # 대화기록을 가져옴
    input_messages_key="query", # 사용자의 질문
    history_messages_key="history", # 대화기록
)


# 로드_메모리...?

# 5. chain 실행

while True:
    #  5.1 사용자로부터 질문 받기
    query = input("Human: ") # 질문 던짐
    if query.lower() == "exit":
        break
    
    # 5.2 AI에게  프롬프트 전달 및 답변 생성하기
    result = chain.invoke(
        {"query": query},
        config={"configurable": {"session_id": session_id}},
        ) # 답변..?
    
    
    # 5.3 답변 출력하기
    print(f"AI: {result.content}")
    
    # 5.4 히스토리 출력
    history = get_history(session_id)
    print(f"히스토리 상태: {len(history.messages)}")
    
    # 챗봇 프로세스 익히기(코드를 외우는게 아니라 원리를 파악하기) 녹음본 무조건 듣기
    