# 퍼플렉시티AI: 자료 조사
# ChatGPT: 요약, 정리 -> NotebookLM: 마인드맵
# whisk: 그림 생성

# Collection type
# - 여러값을 저장하고 싶은 경우 사용
# - 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 세트(set)

# * 순서가 있는 자료형 = 시퀀스 자료형: list, tuple
# * 순서가 없는 자료형: dict , set

# 1. 리스트(list): 예) 기차
# - 시퀀스 자료형(순서가 있는 자료형이라 그래서 index 사용 가능)
# - index(인덱스) 사용 가능(슬라이싱 가능)
# - [] 대괄호 사용
# - 정렬 가능
# - mutable(생성 후 값 변경 가능)
# - packing, unpacking 가능
# - 멤버함수 존재(append, insert, remove, sort, reverse, ...)
# - 문자열을 리스트로 표현하기 때문에 index 사용 가능
str = "abc" # ["a", "b", "c"]
a = [1, 2, 3] # packing
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

# remove(): 리스트에 특정 값 제거(실제 값을 삭제)
list_a.remove(2)

# pop(): 리스트에 특정 위치의 값 제거(인덱스로 삭제)
list_a.pop(0)
temp = list_a.pop(0) # 0번 인덱스의 값을 temp에 담고, 삭제하세요.(잘 사용 X)

# index(값): 리스트에 특정 값의 인덱스 반환(해당 값의 인덱스 출력)
list_a.index(2) # 2라는 값의 인덱스 출력

# sort(): 리스트 정렬(원본 값을 바꿈)  : 지양

# sorted(): 리스트 정렬(원본은 변경되지 않음, 원본값의 복제본을 바꿈)  : 지향
a = [95, 1, 3, 27, 5]
a = sorted(a)               # 오름차순
a = sorted(a, reverse=True) # 내림차순

# Tip: 데이터 분석 or 인공지능 데이터 활용
#       -> 원본 데이터는 유지, 복제 사용
