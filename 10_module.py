# 라이브러리, 패키지, 모듈
# - 라이브러리 >= 패키지 >= 모듈(그냥 같은 의미)

# 라이브러리: 여러 패키지와 모듈의 묶음, 집합체(예: 표준 라이브러리, 서드파티 라이브러리) numpy, pandas, matplotlib 라이브러리들임
# 모듈: 이미 작성된 프로그램(일반적으로 *.py)
# 패키지: 특정 기능과 관련된 여러 모듈의 묶음 lecture가 패키지이고 sjosd.py가 모듈(맞겠지...?)

# 내부: python이 기본적으로 제공하는 것
# 외부: 외부 개발자가 개발한 라이브러리
# 사용자: 직접 개발해서 사용하는 경우

# 외부 모듈
# 가정: requests 1,000개 모듈로 구성(그 중 1개가 get 모듈)
# 1. 다운로드 및 설치 -> pip install [패키지명]
# 2. 호출 -> import [패키지명], import [패키지명].[모듈명]
#  ㄴ import requests     1,000개 모두 호출
#  ㄴ import requests as req  # 별칭   1,000개 모두 호출
#  ㄴ from requests import get  # requests 모듈에서 get 함수만 호출       get 1개만 호출
# 3. 사용
#  ㄴ requests.get('https://www.naver.com')  #.(점, 도트)는 참조 연산자
#  ㄴ req.get('https://www.naver.com')
#  ㄴ get('https://www.naver.com')