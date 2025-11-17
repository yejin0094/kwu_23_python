# RAG(검색 증강 생성) - "래그"라고 읽는다! * 꼭 알아야하는 필수 테크니컬 지식? 
# - Retrieval-Augmented Generation
# - 외부 지식을 활용하여 더 정확한 답변 생성
# - LLM 기본적으로 학습하는데 천문학적인 금액 소모
#      ㄴ LLM을 현재 학습했을 시점까지의 정보만 알고 있음
#      ㄴ 예를 들어, 2025년 05월 31일에 학습을 한 모델의 경우
#         6월 1일 이후의 정보는 알 수 없음
#      문제점 1: 최신 데이터, 정보 반영 X
#      문제점 2: 할루시네이션(환각현상) -> LLM이 거짓말쟁이가 됨
#      문제점 1과 2를 해결하기위해서는 RAG가 필요!

# ** RAG **
# - Human(Query) -> LLM(GPT) -> Answer
# - Human(Query) + 검색결과 -> LLM(GPT) -> Answer

# 예를 들어: 삼성전자 모바일 사업부에서 입사해서 갤럭시 QnA 챗봇을 개발하는 임무를 맡음
#           ㄴ 기존에 LLM은 갤럭시 스마트폰에 대한 자세한 정보 X
#           ㄴ 사용자가 갤럭시에 대한 질문을 하면 그냥 보편적인 답변만 생성
#           ㄴ 갤럭시 스마트폰에 대한 정보가 담긴 PDF파일 생성
#           ㄴ PDF파일로부터 사용자의 질문과 유사한 정보를 Retrieval(검색)을 함
#           ㄴ 검색 된 정보를 사용자 질문과 함께 LLM에게 전달

# 매우 중요(래그에서 매우 핵심)*******************************************************************************
# RAG 아키텍처
# 1. 지식 베이스(래그를 할 때 어디선가 정보를 찾아와야 함)
#  ㄴ 자료(PDF, PPT, ...)들을 불러오기(loader() -> 로더라는 함수로 불러오기) -> Chunk 단위로 분할
#      -> Text Embedding(텍스트 임베딩) -> Vector DB(벡터 데이터베이스)에 저장

# 래그를 쓰면 질문과 검색된 정보를 같이 전달함

# * Txt Embedding(텍스트 임베딩)
# - 단어 또는 문장을 1차원 숫자값의 나열로 변환 -> 벡터
# - 텍스트 데이터를 벡터(숫자)로 변환하는 기법
# - 벡터: 한 차원(방향)으로만 쭉 나열된 숫자값 예) 파이썬에서 리스트가 벡터임 [1, 5, 3, 7]
# - 텍스트 임베딩시 고려할 사항은 청크를 몇개의 숫자로 표현할 것인가?
#    ㄴ 1521개의 숫자로 표현 -> 1521차원 벡터 *숫자가 커지면 커질수록 더 정밀하게 표현 가능, 성능은 좋은데 속도는 느려짐, 보통은 1521개
# 녹음 파일 다시 듣자

# PDF -> Chunk 1 -> 벡터(5, 2, 12, ...) n = 1521  (실수값으로 나옴 정수 nono)
# PDF -> Chunk 1 -> 벡터(1, 52, 3, ...) n = 1521
# PDF -> Chunk 1 -> 벡터(99, 3, 4, ...) n = 1521

# 정보가 금이면 금이나오고 똥이면 똥이나옴
# 래그를 잘하고 싶다면 노가다를 해야함
# 매우 중요(래그에서 매우 핵심)*******************************************************************************

import os
import pprint

from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.document_transformers import EmbeddingsRedundantFilter

_ = load_dotenv(find_dotenv()) #
api_key = os.getenv("OPENAI_API_KEY") # 가지고 온 값을 ...?

llm = ChatOpenAI( # llm 모델 빌려옴
    model="gpt-4.1-mini",
    api_key=api_key,
    temperature=0.2
)

# RAG 프로세스
# 1. 지식 베이스 생성
#  ㄴ PDF 불러오기
# PDF파일의 경로를 알아야함
# 한글에 긁어온 글을 텍스트 형식으로 저장하고 PDF파일로 변환
pdf_path = "./LLM/data/agent.pdf"
docs = PyPDFLoader(pdf_path).load() # PDF파일을 불러옴

#  ㄴ Chunk 단위로 분할
# 청크단위 = 쪼갠다
splitter = RecursiveCharacterTextSplitter( # 청크단위를 어느정도로 설정할지 하는 함수
    chunk_size=100, # 쉽게 말하면 단어 하나씩(1글자씩 아니라)을 100개 단위로 쪼갠다
    chunk_overlap=20 # 오버랩을 20개는 겹치게 쪼갠다(겹쳐서 쪼개야 문맥이 끊기지 않음), # 100 - 20 = 80 (80개 부터 다시 1이 시작으로 20개를 겹치게 쪼갬) - > 검색결과가 더 좋아짐
)
chunks = splitter.split_documents(docs) # 문서를 청크 단위로 쪼개서 chunks에 저장

#  ㄴ Text Embedding 하기(벡터 변환: 1차원 숫자값 나열: 1521개 숫자)
embeddings = OpenAIEmbeddings(api_key=api_key) # 텍스트 임베딩 객체 생성

#  ㄴ Vector DB에 저장하기                      
vector_db = Chroma.from_documents(                   # 학생용 Chroma, 회사용 qdrant
    chunks,
    embeddings,                # 벡터DB를 만든걸 ....? 검색에 사용할 수 있다...?
    collection_name="pdf-agent"
    ) # ...? 저장이 됨
retriever = vector_db.as_retriever() # 검색을 할 수 있는 검색기

# 벡터DB에서 검색된 결과 중 중복된 결과 제거 역할!
deduper = EmbeddingsRedundantFilter(embeddings=embeddings) 

# 레그의 핵심(1, 2번)은 지식베이스어떻게 잘 만들면서 어떻게 검색을 잘 할 수 있는지...?
# 레그의 3번은 기존거랑 똑같음...?


# 2. 지식 베이스 활용
# ㄴ 사용자의 질문(Query)을 텍스트 임베딩 하기     과 유사한 정보 검색
# ㄴ 벡터DB에서 사용자의 질문과 유사한 값 찾기 -> 검색 결과

def retrieve_documents(query: str, k: int=3) -> str: # 쿼리가 사용자 질문 
    # chunk 중 사용자 query와 가장 유사한 3개의 chunk만 활용!
    retriever.search_kwargs["k"] = k # 몇개의 chunk를 사용할건지 설정, 벡터DB에 쪼개진 청크들이 들어 있다 100개의 청크중에서 사용자가 한 질문과 얼마나 유사도 순으로 나열한 다음에 k개 만큼만 쓰겠다
    
    docs = retriever.invoke(query) # 검색 후 3개의 chunk만 선별!(가장 관련성(순위를 매겨서) 높은 3개만 선정), 진짜 검색하는 곳
    docs = deduper.transform_documents(docs) # 유사한 내용이 겹칠 수 있어써 deduper가 중복 된 내용을 제거!
    return format_docs(docs) # format_docs

# 검색 된 결과를 LLM에게 전달하기 전 읽기 쉽게 포맷을 변경
def format_docs(docs):
    out = []
    for i, d in enumerate(docs, 1):
        src = d.metadata.get("source", "unknown")
        out.append(f"[Doc {i}] (source: {src})\n{d.page_content}\n")
        # i가 1로 시작해서 3까지 [Doc 1], [Doc 2], [Doc 3] => 1이 가장 유사함 그리고 [Doc 1] (source: pdf-agent) 한줄 개행, ..?, 한줄 개행, [독스 2](소스: 피디에프-에이전트)
       
    return "\n".join(out)

# 2025.11.17
# 질문과 연관된 문서를 찾는...?

# 3. 답변 생성
# ㄴ 시스템 프롬프트
system_prompt =  """
    아래에서 제공 된 Context만 사용해서 답변을 간결하고 정확하게 생성하세요.
    확실하지 않으면 "답변이 어렵습니다."라고 출력하세요.
    답변 끝에 참고만 [Doc #] 번호를 명시하세요 \n\n
    <context>\n{context}\n</context>\n\n
"""
# ㄴ 휴먼 프롬프트(= 사용자 질문)
prompt = ChatPromptTemplate.from_messages([  # LLM 예를 전달함
    ("system", system_prompt),
    ("human", "{query}")
])

# ㄴ 검색 결과(검색된 정보)
chain = {
    "context": RunnableLambda(lambda x: retrieve_documents(x["query"])), # 사용자가 입력한 요함수를 컨택스에 전달하세요
    "query": RunnablePassthrough() # "Agent를 설명해줘", 전달한 값을 그대로 쓰세요
} | prompt | llm

# ㄴ 를 LLM에게 전달하고 답변 생성
while True:
    query = input("Human: ").strip() # 에이전트 설명해줘
    if not query: # not query는 ""(쿼리가 없음)
        continue
    elif query.lower() in {"exit", "quit"}:
        break
    # 답변 생성
    result = chain.invoke({"query": query})
    print("AI: ", result.content)
    
    # 답변 생성시 참고한 문서 확인
    context = retrieve_documents(query)
    print("=== RETRIEVED CONTEXT ===")
    print(context)
    print("=== END ===")

# 챗봇 만들 주제 정하기 = PBL임


# 최신내용도 답변해줌, 챗지피티가 모르는 내용도, 두번째 거짓말 치는 것도