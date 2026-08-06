import json
import os
import random
from datetime import datetime

class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1-based index
        self.hint = hint

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", "힌트가 제공되지 않는 문제입니다.")
        )


class QuizGame:
    def __init__(self, folder_path="E1-2", filename="state.json"):
        # E1-2 폴더 경로 설정 및 없으면 자동 생성
        self.folder_path = folder_path
        self.filepath = os.path.join(self.folder_path, filename)
        
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path, exist_ok=True)

        self.quizzes = []
        self.best_score = 0.0
        self.history = []
        self.load_data()

    def get_default_quizzes(self):
        """state.json이 없거나 비어있을 때 불러올 기본 5개 퀴즈 데이터"""
        return [
            Quiz(
                question="컴퓨터의 '뇌' 역할을 하며 연산과 명령을 처리하는 핵심 하드웨어 장치는?",
                choices=["RAM (메모리)", "CPU (중앙처리장치)", "SSD (보조기억장치)", "GPU (그래픽카드)"],
                answer=2,
                hint="중앙처리장치의 약자입니다."
            ),
            Quiz(
                question="전원이 꺼지면 저장된 데이터가 사라지는 '휘발성' 기억장치는?",
                choices=["RAM", "HDD", "SSD", "ROM"],
                answer=1,
                hint="주기억장치 중 하나로 주소를 직접 참조합니다."
            ),
            Quiz(
                question="컴퓨터가 사용하는 2진법에서 0과 1의 최소 데이터 단위를 무엇이라고 할까요?",
                choices=["Byte", "Bit", "KB", "Word"],
                answer=2,
                hint="Binary Digit의 줄임말입니다."
            ),
            Quiz(
                question="CPU, 메모리, 그래픽카드 등 컴퓨터의 모든 부품을 연결하는 메인 회로 기판은?",
                choices=["파워 서플라이", "메인보드 (마더보드)", "랜카드", "사운드 카드"],
                answer=2,
                hint="마더보드라고도 부릅니다."
            ),
            Quiz(
                question="다음 중 비휘발성 저장장치로 물리적 회전 디스크 대신 반도체를 사용하는 보조기억장치는?",
                choices=["RAM", "HDD", "SSD", "CD-ROM"],
                answer=3,
                hint="Solid State Drive의 약자입니다."
            )
        ]

    def load_data(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                loaded_quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                
                if loaded_quizzes:
                    self.quizzes = loaded_quizzes
                else:
                    self.quizzes = self.get_default_quizzes()
                    
                self.best_score = float(data.get("best_score", 0.0))
                self.history = data.get("history", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0.0
            self.history = []
            self.save_data()

    def save_data(self):
        # 저장 시 디렉토리가 존재하는지 한 번 더 확인
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path, exist_ok=True)

        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "history": self.history
        }
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play_quiz(self):
        if not self.quizzes:
            print("\n[!] 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print(f"\n--- 퀴즈 풀기 (총 {len(self.quizzes)}문제 보유) ---")
        
        while True:
            try:
                count_input = input(f"풀고 싶은 문제 수를 입력하세요 (1~{len(self.quizzes)}): ").strip()
                quiz_count = int(count_input)
                if 1 <= quiz_count <= len(self.quizzes):
                    break
                print(f"[!] 1에서 {len(self.quizzes)} 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("[!] 올바른 숫자를 입력해주세요.")

        selected_quizzes = random.sample(self.quizzes, quiz_count)
        current_score = 0.0

        for idx, quiz in enumerate(selected_quizzes, start=1):
            print(f"\n[문제 {idx}/{quiz_count}] {quiz.question}")
            for i, choice in enumerate(quiz.choices, start=1):
                print(f"  {i}. {choice}")
            print("  H. 힌트 보기 (사용 시 정답 점수 0.5점 차감)")

            hint_used = False
            while True:
                user_input = input("정답 번호(1~4) 또는 H를 입력하세요: ").strip().upper()
                
                if user_input == 'H':
                    if not hint_used:
                        print(f"  💡 [힌트] {quiz.hint}")
                        hint_used = True
                    else:
                        print("  [!] 이미 힌트를 확인했습니다.")
                    continue

                if user_input.isdigit() and 1 <= int(user_input) <= len(quiz.choices):
                    user_ans = int(user_input)
                    if user_ans == quiz.answer:
                        gained_score = 0.5 if hint_used else 1.0
                        current_score += gained_score
                        print(f"⭕ 정답입니다! (+{gained_score}점)")
                    else:
                        print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")
                    break
                else:
                    print("[!] 올바른 선택지를 입력해주세요.")

        print(f"\n[결과] 총 {quiz_count}문제 중 {current_score}점을 획득하셨습니다!")

        if current_score > self.best_score:
            print(f"🎉 축하합니다! 새로운 최고 점수 달성! ({self.best_score}점 -> {current_score}점)")
            self.best_score = current_score

        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": quiz_count,
            "score": current_score
        }
        self.history.append(record)
        self.save_data()

    def add_quiz(self):
        print("\n--- 새 퀴즈 추가 ---")
        question = input("문제 내용을 입력하세요: ").strip()
        while not question:
            question = input("[!] 문제 내용을 입력하셔야 합니다: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"보기 {i}: ").strip()
            while not choice:
                choice = input(f"[!] 보기 {i}을(를) 입력해 주세요: ").strip()
            choices.append(choice)

        while True:
            try:
                answer = int(input("정답 번호 (1~4): ").strip())
                if 1 <= answer <= 4:
                    break
                print("[!] 1에서 4 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("[!] 올바른 숫자를 입력해주세요.")

        hint = input("힌트를 입력하세요 (없으면 엔터): ").strip()
        if not hint:
            hint = "힌트가 제공되지 않는 문제입니다."

        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")

    def list_quizzes(self):
        print(f"\n--- 전체 퀴즈 목록 (총 {len(self.quizzes)}개) ---")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{idx}] {quiz.question}")
            for i, choice in enumerate(quiz.choices, start=1):
                print(f"    {i}. {choice}")
            print(f"    정답: {quiz.answer}번 | 힌트: {quiz.hint}")

    def delete_quiz(self):
        self.list_quizzes()
        if not self.quizzes:
            return

        print("\n--- 퀴즈 삭제 ---")
        while True:
            try:
                del_input = input("삭제할 퀴즈 번호를 입력하세요 (취소: 0): ").strip()
                del_idx = int(del_input)
                if del_idx == 0:
                    print("삭제를 취소했습니다.")
                    return
                if 1 <= del_idx <= len(self.quizzes):
                    deleted = self.quizzes.pop(del_idx - 1)
                    self.save_data()
                    print(f"✅ [{deleted.question}] 퀴즈가 삭제되었습니다.")
                    return
                print("[!] 올바른 퀴즈 번호를 입력해주세요.")
            except ValueError:
                print("[!] 숫자를 입력해주세요.")

    def show_score_and_history(self):
        print("\n--- 점수 및 게임 기록 ---")
        print(f"🏆 최고 점수: {self.best_score}점")
        print("\n[최근 게임 기록]")
        if not self.history:
            print("아직 진행한 게임 기록이 없습니다.")
            return

        for idx, h in enumerate(reversed(self.history[-5:]), start=1):
            print(f" {idx}. 일시: {h['date']} | 푼 문제: {h['total_questions']}개 | 획득 점수: {h['score']}점")

    def main_menu(self):
        while True:
            print("\n" + "="*30)
            print("   컴퓨터 하드웨어 퀴즈 게임")
            print("="*30)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 퀴즈 삭제")
            print("5. 점수 및 기록 확인")
            print("6. 종료")
            print("="*30)

            choice = input("메뉴 번호를 선택하세요 (1~6): ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.list_quizzes()
            elif choice == "4":
                self.delete_quiz()
            elif choice == "5":
                self.show_score_and_history()
            elif choice == "6":
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                break
            else:
                print("[!] 올바른 메뉴 번호를 선택해 주세요 (1~6).")


if __name__ == "__main__":
    game = QuizGame()
    game.main_menu()