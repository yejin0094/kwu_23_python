# 1. 주석(Comment)
# - 인터프리터 번역 X(코드 X)
# - 단순 메모


# 2. 명명 규칙(Naming Rule)
# - 영어 대소문자, 숫자, 특수문자(_) 사용
# - 영어 대소문자 구별 : ABC, ABc, abc, aBC 다 다르게 인식...
# - 숫자로 시작할 수 없음 : abc12(O), 1abc(X)
# - 예약어 사용 불가 : print, if, else, while, for, ... 사용금지

# 3. 명명 함수(Naming Mathod)
# - PascalCase : UniversityStudentName
# - camelCase  : universityStudentName
# - snake_case : university_student_name
# - kebab-case : university-student-name

# 명명 -> 변수, 함수, 클래스

# JAVA와 C는
# - 클래스는(Pascal)
# - 변수와 함수(Camel)

# Python
# - 클래스(Pascal)
# - 변수와 함수(Snake)

# 4. 동적타이핑 언어
# - 자료형을 개발자가 지정 x
# - 인터프리터가 번역하는 과정에서 자동으로 자료형을 지정

# 예: JAVA → int num = 4; (정적 타이핑)
# 예: Python → num = 4 (동적 타이핑)

# 5. print()
# - 이름 옆에 ()붙어 있으면 함수
# - ()안에 있는 값을 출력
print("Hello")
print(123)

# 6. type()
# - ()안에 있는 값의 자료형(type) 알려줌
print(type(123))  # -> print("int") -> "int" (정수형)
print(type("ABC"))  # str(문자열형)