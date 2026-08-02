# 콘솔 기반 나만의 퀴즈 게임 (E1-2 Mission)

Python 기본 문법, 객체지향 프로그래밍(OOP), JSON 파일 입출력을 통한 데이터 영속성 처리, 그리고 체계적인 Git 워크플로우를 학습하고 적용한 터미널 퀴즈 게임 프로젝트입니다.

---

## 1. 프로젝트 개요 및 주제 선정 이유

- **프로젝트 명**: 나만의 파이썬/프로그래밍 기초 퀴즈 게임
- **퀴즈 주제**: Python 핵심 문법 및 Git/프로그래밍 기초 지식
- **선정 이유**:
  - 개발 환경을 구축하고 파이썬 기본기를 정립하는 단계에서 필수적인 개념들을 문제 형태로 검증하고자 하였습니다.
  - 객체지향 설계(Quiz, QuizGame) 및 데이터 파일 연동(`state.json`)의 실제 동작 방식을 명확히 확인하기 위해 구현되었습니다.

---

## 2. 실행 방법

1. **프로젝트 디렉토리 이동**:
   ```bash
   cd WOOCHUL_CODYSSEY/E1-2

2. **프로그램 실행**:
   ```bash
   python3 main.py

---

## 3. 주요 기능 목록

1. **퀴즈 풀기 (1번)**
등록된 문제들이 순차적으로 출제되며, 1~4번 중 정답을 선택합니다.
풀이가 끝나면 정답 개수 및 최고 점수 갱신 여부를 안내합니다.

2. **퀴즈 추가 (2번)**
문제 질문, 4개의 객관식 선택지, 정답 번호를 직접 등록할 수 있습니다.
입력값 검증을 거쳐 state.json 파일에 즉시 반영됩니다.

3. **퀴즈 목록 (3번)**
현재 저장되어 있는 모든 퀴즈의 질문 목록을 확인할 수 있습니다.

4. **점수 확인 (4번)**
역대 기록 중 맞힌 문제의 최고 점수를 조회합니다.

5. **예외 및 에러 처리 (공통)**
숫자 외 입력(abc), 범위 벗어난 선택, 빈 입력(Enter) 시 안내 메시지 출력 후 재입력 흐름 제공
Ctrl+C (KeyboardInterrupt) 및 파일 손상 발생 시 안전 종료 및 기본 데이터 복구 기능 동작

---

## 4. 프로젝트 파일 구조

E1-2/
├── images/             # 실행 결과 스크린샷 폴더
│   ├── menu.png
│   ├── play.png
│   ├── add_quiz.png
│   ├── list.png
│   └── score.png
├── .gitignore          # Git 추적 제외 설정
├── README.md           # 프로젝트 문서화 파일
├── state.json          # 퀴즈 및 점수 데이터 저장소 (자동 생성)
└── main.py             # 게임 실행 메인 코드

---

## 5. 데이터 파일 설명 (state.json)

경로: E1-2/state.json

역할: 프로그램을 종료해도 퀴즈 데이터 및 최고 점수가 유지되도록 UTF-8 인코딩으로 저장되는 데이터 파일입니다.

필드 구조 (Schema):
quizzes (Array): 퀴즈 정보 객체들의 리스트
question (String): 질문 내용
choices (Array of Strings): 4개의 객관식 선택지
answer (Integer): 정답 번호 (1~4)
best_score (Integer): 현재까지 기록된 최고 정답 문제 수

스키마 예시:
{
    "quizzes": [
        {
            "question": "Python의 창시자는 누구일까요?",
            "choices": [
                "Guido van Rossum",
                "Linus Torvalds",
                "James Gosling",
                "Bjarne Stroustrup"
            ],
            "answer": 1
        }
    ],
    "best_score": 5
}