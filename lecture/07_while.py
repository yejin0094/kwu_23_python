# while문
# - 반복횟수를 모르는 경우
# - 조건이 만족하는 동안 반복하세요
# - 조건(True) -> 무한루프 -> 조건 + break문 반드시 같이 사용하기

while True:
    if 3 > 0: # for문은 특정 값을 출력 while문은 몇번이상 반복할 때
        break

# 구구단 2단 while문
for i in range(1, 9): # 반복횟수를 아는 경우 for문
    print(f"2x{i}-{2*i}")

i = 1 # 반복횟수를 모르는 경우에 while를 사용
while i < 10:
    print(f"2x{i}-{2*i}")
    i+=1