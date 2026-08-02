import json
import os
import sys

# ---------------------------------------------------------
# 1. Quiz 클래스 (개별 퀴즈 정보 및 정답 검증)
# ---------------------------------------------------------
class Quiz:
    def __init__(self, question: str, choices: list, answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1-4 사이 번호

    def is_correct(self, user_answer: int) -> bool:
        return self.answer == user_answer

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["question"], data["choices"], data["answer"])


# ---------------------------------------------------------
# 2. QuizGame 클래스 (전체 게임 관리 및 JSON 영속성)
# ---------------------------------------------------------
class QuizGame:
    # main.py 파일이 위치한 디렉토리를 절대경로로 구하여 state.json 경로 고정
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(BASE_DIR, "state.json")

    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_state()

    def get_default_quizzes(self):
        """기본 제공 퀴즈 데이터 (주제: 파이썬 & 프로그래밍 기초)"""
        return [
            Quiz("Python의 창시자는 누구일까요?", ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"], 1),
            Quiz("다음 중 순서가 보장되고 변경 불가능(immutable)한 파이썬 자료형은?", ["list", "dict", "tuple", "set"], 3),
            Quiz("JSON 파일 기본 인코딩으로 표준 권장되는 형식은?", ["EUC-KR", "UTF-8", "CP949", "ASCII"], 2),
            Quiz("Git에서 브랜치를 생성함과 동시에 이동하는 명령어로 올바른 것은?", ["git branch -m", "git checkout -b", "git commit -a", "git merge -b"], 2),
            Quiz("파이썬에서 예외 처리를 위해 사용하는 블록 키워드는?", ["try/except", "do/catch", "try/catch", "begin/end"], 1),
        ]

    def load_state(self):
        """state.json 파일 읽기 및 예외 복구"""
        if not os.path.exists(self.FILE_PATH):
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0
            self.save_state()
            return

        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)
                if not self.quizzes:
                    self.quizzes = self.get_default_quizzes()
        except Exception as e:
            print(f"\n⚠️ 파일 읽기 오류 발생 ({e}). 기본 데이터로 복구합니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0
            self.save_state()

    def save_state(self):
        """state.json 파일 저장"""
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"\n⚠️ 저장 중 오류가 발생했습니다: {e}")

    # --- 공통 입력 처리 유틸리티 ---
    def safe_input_int(self, prompt: str, min_val: int, max_val: int) -> int:
        """예외 처리 기능이 강화된 정수 입력 받기"""
        while True:
            try:
                user_in = input(prompt).strip()
                if not user_in:
                    print("⚠️ 입력값이 비어 있습니다. 다시 입력해 주세요.")
                    continue
                val = int(user_in)
                if min_val <= val <= max_val:
                    return val
                print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("⚠️ 숫자로만 입력해 주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n\n👋 프로그램을 안전하게 종료합니다.")
                self.save_state()
                sys.exit(0)

    # --- 메뉴 기능 ---
    def play_quiz(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for idx, q in enumerate(self.quizzes, 1):
            print(f"\n----------------------------------------")
            print(f"[{idx}] {q.question}")
            for c_idx, choice in enumerate(q.choices, 1):
                print(f"  {c_idx}. {choice}")

            ans = self.safe_input_int("정답 입력 (1-4): ", 1, 4)
            if q.is_correct(ans):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. (정답: {q.answer}번)")

        print("\n========================================")
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        if score > self.best_score:
            print(f"🎉 새로운 최고 점수 달성! ({self.best_score} -> {score})")
            self.best_score = score
            self.save_state()
        print("========================================")

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        try:
            q_text = input("문제를 입력하세요: ").strip()
            while not q_text:
                print("⚠️ 문제는 비어 둘 수 없습니다.")
                q_text = input("문제를 입력하세요: ").strip()

            choices = []
            for i in range(1, 5):
                c_text = input(f"선택지 {i}: ").strip()
                while not c_text:
                    print("⚠️ 선택지는 비어 둘 수 없습니다.")
                    c_text = input(f"선택지 {i}: ").strip()
                choices.append(c_text)

            ans = self.safe_input_int("정답 번호 (1-4): ", 1, 4)
            
            self.quizzes.append(Quiz(q_text, choices, ans))
            self.save_state()
            print("✅ 퀴즈가 성공적으로 추가되었습니다!")
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 작업이 취소되었습니다. 메인 메뉴로 돌아갑니다.")

    def list_quizzes(self):
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for idx, q in enumerate(self.quizzes, 1):
            print(f"[{idx}] {q.question}")
        print("----------------------------------------")

    def show_score(self):
        print("\n========================================")
        print(f"🏆 현재 최고 점수: {self.best_score}점")
        print("========================================")

    def run(self):
        while True:
            print("\n========================================")
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("========================================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("========================================")
            
            choice = self.safe_input_int("선택: ", 1, 5)
            
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                break


if __name__ == "__main__":
    game = QuizGame()
    game.run()