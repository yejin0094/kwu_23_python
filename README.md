## 0. Markdown(MD)
   - MD언어: 설명, 정리 언어!(설명서, 메모장 같은거)
   - MD문법 존재(30분 공부)
   
## 1. 개발환경 구축
### 1-1. Anaconda
   - anaconda prompt 실행
   - conda env list : 가상환경 목록 보기
   - conda create -n llm python=3.11 :  llm 가상환경 생성
   - conda activate llm : llm 가상환경 접속
   - pip list : 가상환경에 설치 된 라이브러리 목록 보기
   - pip install [라이브러리] : 라이브러리 설치
   - cls : 화면 청소
   - Anaconda는 편리하지만 매우 무거움....

### 1-2. 로컬 가상환경
- 불편하지만, 매우 가벼움
- Python을 직접 설치 + 가상환경 직접 생성(venv -> 버추얼 인바이러먼트)
- python -m venv venv

### 1-3. Github
   - 버전관리도구
   - 코드를 관리해주는 웹 저장소

#### Git: 형상관리도구 or 버전관리도구
   - GitHub( O ) - 웹 클라우드
   - GitLab - 폐쇄망 직접 관리

   
#### Repository(=프로젝트라는 뜻 = 그냥 방(room)이라고 생각) 연결
- Github는 프로젝트 단위로 Repository 생성
- 팀장이 Repository를 생성하고 팀원들을 초대해서 협업
-  Github는 Git이라는 하는 버전관리도구를 손쉽게 사용할 수 있는 플랫폼(Git 설치) / git -v 확인 가능
- 로컬(컴퓨터, 노트북) - 글로벌(website)
- Repository가 로컬, 글로벌에 둘다 존재해야 함!
- git status : git Repository 현재 상태
- git init.(git init) : git Repository 생성(로컬에 생성)
- git remote -v : 원격 Repository 연결 상태 확인(글로벌과 연결)
깃허브에서 코드 복사해서 붙여 넣기...
- git remote add origin [URL] : 로컬과 글로벌 Repository 연결
- git branch -M main : Master branch -> Main branch 변경
- git pull origin main
- git pull(코드를 글로벌에서 로컬로 내려받아라) origin main : 글로벌의 Main 코드를 내려받기
- git add [file] : 앞으로 해당 파일을 버전관리 목록 추가(관리할 파일인지 확인)
- git add . : 현재 경로의 모든 파일을 버전관리 목록에 추가
- git commit -m "내용" : 버전 생성 내용 -> Add lecture("내용"에 치기)
- git config --global user.email "you@example.com"
- git config --global user.name "Your Name"
- git add와 commit 로컬에서 행위(글로벌 변화 x)
- git push origin main : Local의 commit으로 생성한 버전을 글로벌에 업로드