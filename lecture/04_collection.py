# 퍼플렉시티AI: 자료 조사
# ChatGPT: 요약, 정리 -> NotebookLM: 마인드맵
# whisk: 그림 생성




# Collection type
# - 여러값을 저장하고 싶은 경우 사용
# - 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 세트(set)
# 리스트와 튜플은 순서가 있고 딕셔너리, 세트는 순서가 없음
# 값을 여러개 담음 그래서 꾸러미가 필요함

# * 순서가 있는 자료형 = 시퀀스 자료형: list, tuple
# * 순서가 없는 자료형: dict , set

# 1. 리스트(list): 예) 기차
# - 시퀀스 자료형(순서가 있는 자료형이라 그래서 index 사용 가능)
# - index(인덱스) 사용 가능(슬라이싱 가능)
# - [] 대괄호 사용

# - 정렬 가능
# - mutable(생성 후 값 변경 가능) 값을 만든 다음에 변경할 수 있음, 하지만 튜플은 값을 못 바꿈 그래서 튜플은 다시 만들어야 함

# - 멤버함수 존재(append, insert, remove, sort, reverse, ...)
# - 문자열을 리스트로 표현하기 때문에 index 사용 가능
str = "abc" # ["a", "b", "c"]
a = [1, 2, 3] # packing <- 괄호로 묶는 행위를 패킹했다
b, c, d = [1, 2, 3] # unpacking

# Quiz: aa와 bb의 값을 서로 교환
aa = 5
bb = 3

# JAVA, C
temp = aa # temp는 템프로리의 약자
aa = bb
bb = temp

# python
aa, bb = bb, aa # python은 이렇게 간단하게 가능

# 리스트 생성
list_a = [1, 2, 3]
list_b = [] # 빈 리스트 생성 가능
list_c = [1, "a", 3.14, True] # 다양한 자료형을 섞어서 사용 가능

# append(넣을 값): 리스트에 값 추가
list_a.append(4) # list_a = [1, 2, 3, 4] (맨 마지막에 추가)

# insert(인덱스, 값(어디 인덱스에다가 넣을 값)): 리스트에 특정 위치에 값 추가
list_a.insert(1, 5) # list_a = [1, 5, 2, 3, 4] (1번 인덱스 자리에 5 추가(원래 있던 1번 인덱스 값은 뒤로 밀림))

# extend(): 리스트에 여러개의 값 추가
a = [1, 2, 3] 
b = [2, 3, 4]
a.extend(b) # a = [1, 2, 3, 2, 3, 4] (a리스트에 b리스트의 값들을 추가)
a.append(b) # a = [1, 2, 3, [2, 3, 4]] (합쳐서 넣는게 아니라 b리스트 자체를 하나의 값으로 추가)
print(a)
# a+b == a.extend(b) 와 동일

# remove(): 리스트에 특정 값 제거(실제 값을 삭제 주의!! 인덱스 값이 아니라 실제 값!)
list_a.remove(2)

# pop(): 리스트에 특정 위치의 값 제거(인덱스로 삭제)
list_a.pop(0)
temp = list_a.pop(0) # 0번 인덱스의 값을 temp에 담고, 삭제하세요.(잘 사용 X)

# index(값): 리스트에 특정 값의 인덱스 반환(해당 값의 인덱스 출력)
# <list_a.index(2)> # 에러나는 이유: list_a = [1, 2, 3]이지만 list_a.remove(2)를 하면 실제 값 2가 삭제된 상태여서 list_a.index(2)를 하면 2 값의 인덱스 번호를 알려달라고 하기 때문에 error가 생김
a.index(2) # 2라는 값의 인덱스 출력

# sort(): 리스트 정렬(원본 값을 바꿈)  : 지양

# sorted(): 리스트 정렬(원본은 변경되지 않음, 원본값의 복제본을 바꿈)  : 지향
a = [95, 1, 3, 27, 5]
a = sorted(a)               # 오름차순
a = sorted(a, reverse=True) # 내림차순

# Tip: 데이터 분석 or 인공지능 데이터 활용
#       -> 원본 데이터는 유지, 복제 사용

# 멤버함수 함수들이 ...? 리스트에 국한돼서 사용하는 함수들을 멤버함수라고 함

# 2. 튜플(tuple) <- 순서를 바꿀 수 없기 때문에 멤버함수가 없음!!
# - 시퀀스 자료형(순서가 있는 자료형이라 그래서 index 사용 가능)
# - index(인덱스) 사용 가능(슬라이싱 가능)
# - {} 소괄호 사용, 하지만 소괄호 생략 가능
# - immutable(생성 후 값 변경 불가)
# - packing과 unpacking 가능
a = [1,2,3] # list
b = (1,2,3) # tuple
c = 1,2,3 # tuple
d = (5) # tuple
e = 5 # int
f = 5, # tuple


# 3. 딕셔너리(dictionary) ex) 복주머니, 가방 생각
# - 순서가 없음(Non-시퀀스)
# - 인덱스 없음(순서가 없기 때문에)
# - {} 중괄호 사용
# - {key:value} 데이터 구조 사용
# - key는 중복 불가능
# - value는 중복 가능
# - value는 key로만 접근 가능
a = {
    "Korea": "Seoul", # 컴마(,) 사용
    "Canada": "Ottwa",
    "USA": 3.14
}

# dict 항목 추가 및 변경 (값을 넣으면서 수정이 가능, 리스트는 수정 없음)
# - 기존에 key가 존재하면 update(수정)
# - 기존에 key가 존재하지 않으면 insert(삽입)
a["Japan"] = "Tokyo" # insert
a["Japan"] = "Kyoto" # update

# dict 항목 삭제(key를 사용)
# - del 키워드
# - pop 함수 이용
# del a["Japan"] # 사용금지 (존재 자체를 지워버림)
a.pop("Japan") 

# dict 병합 리스트에서는 값이 중복도
# - update()
a = {"a": 1, "b": 2}
b = {"a": 2, "c": 5}
a.update(b) # a가 주체 b가 a로 들어감
print(a) # {'a': 2, 'b': 2, 'c': 5}

# clear()
# - 딕셔너리의 모든 값을 초기화
a.clear() # a에 있는 값이 싹다 날아감

# in()
# - dict안에 key가 존재하는지 확인
print("japan" in a) # ?...딕셔너리 안에 a가 있나요??

# value access
print(a["japan"]) # "japan"이라는 key가 없으면 오류남(오류난다는 것은 동작중이 작업이 꺼져버림)
print(a.get("japan")) # "japan"이라는 key가 없으면 None을 반환, 이게 더 좋음(이거 써)

# 모든 key, value 접근
# - keys() : key만 추출
# - values() : value만 추출
# - items() : key + value만 추출(튜플 타입)
print(list(a.keys())) # lsit 타입으로 무조건 싸서 가져오기 아니면 나중에 타입오류뜸(list 타입으로 바꾸세요)
print(list(a.values()))
print(list(a.items()))


# 4. 세트(set)
# 순서가 없음, 인덱스 없음
# {} 사용
# 수학의 집합
# *중복값을 허용하지 않음*
set_a = {1,2,3,2,2,2,2,2,2} # set{1,2,3}
# 실무에서 set은 중복값을 제거할 때만 사용

aa = {} # 딕셔너리

# 중복값 사용 예시
list_c = [1,2,3,2,3,4,5] # 리스트타입
set(list_c) # set타입, list를 set타입을 변환하면 중복값이 사람짐
list(set(list_c)) # [1,2,3,4,5] 원본이 list형태였으면 다시 list형태로 바꿔야 함