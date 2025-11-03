# solution-1
# 리스트 a의 평균을 계산하고 출력하세요


# 예진이 풀이

a = [1,2,3,4,5,99,87,52,2,5,4]
for i in a:
    score = i + 0 # score = score + i
    result = score/len(a)
print(f"평균: {result}")



# 교수님 정답지

a = [1,2,3,4,5,99,87,52,2,5,4]
total = 0 # 총합을 저장할 변수
for num in a:
    total = total + num # 사용 안함 -> total = total + num을 사용!!!
    # 먼저 total과 num을 먼저 계산한 후에(더하기니깐 더하라는 소리) total에 집어넣으세요(=부분)
result = total / len(a)
print(f"평균: {result}")
    


# solution-2
# - 리스트에서 최소값과 최대값 찾기

# 예진이 풀이

c = [2, 5, 7, 1, 8]

num_min = c[0] # num_min = 0을 주면 최소값이 0이 됨
num_max = c[0]

for num in c:
    if num < num_min:
        num_min = num
    if num > num_max:
        num_max = num

print(f"최소값: {num_min}")
print(f"최대값: {num_max}")


# 한번에 찾는 법

c = [2, 5, 7, 1, 8]
list(set(c)).sort() # 중복 제거 후 정렬이 됨 [1, 2, 5, 7, 8]

num_min = c[0]
num_max = c[-1]


