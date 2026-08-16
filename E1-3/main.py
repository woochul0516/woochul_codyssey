import json
import math
import os
import re
import time


def normalize_label(label: str) -> str:
    """
    비정형 라벨('+', 'cross', 'Cross', 'x', 'X' 등)을 표준 라벨('Cross', 'X')로 정규화합니다.
    """
    if not label:
        return "UNKNOWN"
    
    cleaned = re.sub(r'[^a-zA-Z+]', '', str(label)).strip().lower()
    
    if cleaned in ['+', 'cross']:
        return "Cross"
    elif cleaned in ['x']:
        return "X"
    return str(label).strip()


def generate_pattern(size: int, pattern_type: str) -> list[list[int]]:
    """
    [보너스 과제] 크기 N(N x N)에 따른 십자가(Cross) 및 X 패턴 2차원 배열을 동적으로 생성합니다.
    """
    mat = [[0] * size for _ in range(size)]
    norm_type = normalize_label(pattern_type)
    
    if norm_type == "Cross":
        mid = size // 2
        for i in range(size):
            mat[mid][i] = 1
            mat[i][mid] = 1
    elif norm_type == "X":
        for i in range(size):
            mat[i][i] = 1
            mat[i][size - 1 - i] = 1
            
    return mat


def flatten_2d(mat: list[list[float]]) -> list[float]:
    """2차원 리스트를 1차원 평탄화 배열(N^2)로 변환합니다."""
    return [elem for row in mat for elem in row]


def mac_2d(mat_a: list[list[float]], mat_b: list[list[float]]) -> float:
    """
    2차원 배열 기반 MAC 연산 및 유사도 점수 계산
    Score = Dot_Product(A, B) / (Norm(A) * Norm(B))
    """
    rows = len(mat_a)
    cols = len(mat_a[0]) if rows > 0 else 0
    
    dot_product = 0.0
    norm_a = 0.0
    norm_b = 0.0
    
    for i in range(rows):
        for j in range(cols):
            val_a = mat_a[i][j]
            val_b = mat_b[i][j]
            dot_product += val_a * val_b
            norm_a += val_a * val_a
            norm_b += val_b * val_b
            
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (math.sqrt(norm_a) * math.sqrt(norm_b))


def mac_1d(flat_a: list[float], flat_b: list[float]) -> float:
    """
    [보너스 과제] 1차원 평탄화 배열 기반 MAC 최적화 연산 (포인터 접근 단순화)
    """
    dot_product = 0.0
    norm_a = 0.0
    norm_b = 0.0
    length = len(flat_a)
    
    for i in range(length):
        val_a = flat_a[i]
        val_b = flat_b[i]
        dot_product += val_a * val_b
        norm_a += val_a * val_a
        norm_b += val_b * val_b
        
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (math.sqrt(norm_a) * math.sqrt(norm_b))


def classify_pattern(score_cross: float, score_x: float, eps: float = 1e-9) -> str:
    """
    부동소수점 허용오차(Epsilon)를 적용한 패턴 분류 함수.
    두 점수 차이가 Epsilon 미만이면 UNDECIDED(판정 불가) 처리합니다.
    """
    diff = abs(score_cross - score_x)
    if diff < eps:
        return "UNDECIDED"
    return "Cross" if score_cross > score_x else "X"


def ensure_sample_json(filepath: str = "data.json"):
    """data.json 파일이 없을 경우 기본 테스트 데이터셋을 자동 생성합니다."""
    if os.path.exists(filepath):
        return
    
    data = {
        "filters": {
            "size_5": {
                "cross": generate_pattern(5, "Cross"),
                "x": generate_pattern(5, "X")
            },
            "size_13": {
                "cross": generate_pattern(13, "Cross"),
                "x": generate_pattern(13, "X")
            },
            "size_25": {
                "cross": generate_pattern(25, "Cross"),
                "x": generate_pattern(25, "X")
            }
        },
        "patterns": {
            "size_5_cross_test": {
                "input": generate_pattern(5, "Cross"),
                "expected": "+"
            },
            "size_5_x_test": {
                "input": generate_pattern(5, "X"),
                "expected": "x"
            },
            "size_13_1": {
                "input": generate_pattern(13, "X"),
                "expected": "X"
            },
            "size_25_invalid_shape": {
                "input": [[1, 0], [0, 1]],  # 차원 불일치 예외 테스트용
                "expected": "X"
            }
        }
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def run_user_input_mode():
    """모드 1: 3x3 (또는 N x N) 콘솔 사용자 입력 기반 분석"""
    print("\n==========================================")
    print("  [모드 1] 사용자 콘솔 입력 패턴 분석")
    print("==========================================")
    
    try:
        size_str = input("격자 크기 N을 입력하세요 (기본값: 3): ").strip()
        n = int(size_str) if size_str.isdigit() else 3
        
        print(f"\n* 필터 A (Cross) {n}x{n} 입력 (행 단위 공백 구분):")
        filter_a = []
        for i in range(n):
            row = list(map(float, input(f"  {i+1}행: ").strip().split()))
            if len(row) != n:
                raise ValueError(f"열 개수가 {n}개가 아닙니다.")
            filter_a.append(row)
            
        print(f"\n* 필터 B (X) {n}x{n} 입력 (행 단위 공백 구분):")
        filter_b = []
        for i in range(n):
            row = list(map(float, input(f"  {i+1}행: ").strip().split()))
            if len(row) != n:
                raise ValueError(f"열 개수가 {n}개가 아닙니다.")
            filter_b.append(row)
            
        print(f"\n* 테스트 패턴 {n}x{n} 입력 (행 단위 공백 구분):")
        input_pat = []
        for i in range(n):
            row = list(map(float, input(f"  {i+1}행: ").strip().split()))
            if len(row) != n:
                raise ValueError(f"열 개수가 {n}개가 아닙니다.")
            input_pat.append(row)
            
        # 연산 성능 측정
        start_time = time.perf_counter()
        score_a = mac_2d(filter_a, input_pat)
        score_b = mac_2d(filter_b, input_pat)
        result = classify_pattern(score_a, score_b)
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        
        print("\n--- [분석 결과] ---")
        print(f"Filter A (Cross) 점수 : {score_a:.6f}")
        print(f"Filter B (X) 점수     : {score_b:.6f}")
        print(f"최종 분류 결과        : {result}")
        print(f"연산 소요 시간        : {elapsed_ms:.4f} ms")
        
    except Exception as e:
        print(f"\n[!] 입력 오류 발생: {e}")
        print("    3x3 형태의 숫자를 정합성 있게 입력해주십시오.")


def run_json_mode():
    """모드 2: data.json 로드 및 검증 / O(N^2) 성능 분석 리포트"""
    print("\n==========================================")
    print("  [모드 2] data.json 일괄 분석 및 검증")
    print("==========================================")
    
    ensure_sample_json("data.json")
    
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            db = json.load(f)
    except Exception as e:
        print(f"[!] data.json 로드 실패: {e}")
        return
    
    filters = db.get("filters", {})
    patterns = db.get("patterns", {})
    
    pass_count = 0
    fail_count = 0
    
    print("\n[1] 테스트 케이스 수행 결과")
    print("-" * 65)
    print(f"{'패턴 ID':<22} | {'예측 라벨':<10} | {'기대 라벨':<10} | {'결과'}")
    print("-" * 65)
    
    for pat_id, pat_info in patterns.items():
        input_mat = pat_info.get("input", [])
        raw_expected = pat_info.get("expected", "")
        expected_label = normalize_label(raw_expected)
        
        # 차원 검증
        n = len(input_mat)
        if n == 0 or any(len(row) != n for row in input_mat):
            print(f"{pat_id:<22} | {'ERROR':<10} | {expected_label:<10} | FAIL (차원 불일치)")
            fail_count += 1
            continue
        
        filter_key = f"size_{n}"
        if filter_key not in filters:
            # 적절한 필터가 없으면 자동 생성기(보너스 과제) 활용
            filter_cross = generate_pattern(n, "Cross")
            filter_x = generate_pattern(n, "X")
        else:
            filter_cross = filters[filter_key].get("cross", generate_pattern(n, "Cross"))
            filter_x = filters[filter_key].get("x", generate_pattern(n, "X"))
            
        score_cross = mac_2d(filter_cross, input_mat)
        score_x = mac_2d(filter_x, input_mat)
        pred_label = classify_pattern(score_cross, score_x)
        
        is_pass = (pred_label == expected_label)
        status_str = "PASS" if is_pass else "FAIL"
        if is_pass:
            pass_count += 1
        else:
            fail_count += 1
            
        print(f"{pat_id:<22} | {pred_label:<10} | {expected_label:<10} | {status_str}")
        
    print("-" * 65)
    print(f"최종 집계: PASS {pass_count}개 / FAIL {fail_count}개 (총 {pass_count + fail_count}개)")
    
    # O(N^2) 및 1D/2D 메모리 최적화 성능 평가 (보너스 과제)
    print("\n[2] N x N 크기별 연산 성능 및 1D 최적화 비교 표")
    print("-" * 70)
    print(f"{'크기(N x N)':<12} | {'2D MAC 평균(ms)':<16} | {'1D 최적화 평균(ms)':<18} | {'연산 횟수(N^2)'}")
    print("-" * 70)
    
    test_sizes = [3, 5, 13, 25]
    iterations = 500  # 측정 정밀도를 위한 반복 횟수
    
    for sz in test_sizes:
        pat_a = generate_pattern(sz, "Cross")
        pat_b = generate_pattern(sz, "X")
        
        # 2D 측정
        t0 = time.perf_counter()
        for _ in range(iterations):
            _ = mac_2d(pat_a, pat_b)
        t_2d = ((time.perf_counter() - t0) / iterations) * 1000
        
        # 1D 평탄화 측정
        flat_a = flatten_2d(pat_a)
        flat_b = flatten_2d(pat_b)
        t0 = time.perf_counter()
        for _ in range(iterations):
            _ = mac_1d(flat_a, flat_b)
        t_1d = ((time.perf_counter() - t0) / iterations) * 1000
        
        print(f"{f'{sz}x{sz}':<12} | {t_2d:<16.5f} | {t_1d:<18.5f} | {sz*sz}")
    print("-" * 70)


def run_benchmark():
    """모드 3: [보너스 과제] 동적 패턴 생성 기반 1D vs 2D 벤치마크 전용 모드"""
    print("\n==========================================")
    print("  [보너스 과제] 1D 메모리 최적화 벤치마크")
    print("==========================================")
    
    size = int(input("테스트할 격자 크기 N 입력 (예: 50): ").strip() or "50")
    iterations = int(input("반복 연산 횟수 입력 (예: 1000): ").strip() or "1000")
    
    pat_cross = generate_pattern(size, "Cross")
    pat_x = generate_pattern(size, "X")
    
    print(f"\n* N={size} ({size*size} 요소) 패턴 동적 생성 완료.")
    print(f"* 총 {iterations}회 연산 수행 중...\n")
    
    # 2D 측정
    start_2d = time.perf_counter()
    for _ in range(iterations):
        _ = mac_2d(pat_cross, pat_x)
    time_2d = (time.perf_counter() - start_2d) * 1000
    
    # 1D 측정
    flat_cross = flatten_2d(pat_cross)
    flat_x = flatten_2d(pat_x)
    
    start_1d = time.perf_counter()
    for _ in range(iterations):
        _ = mac_1d(flat_cross, flat_x)
    time_1d = (time.perf_counter() - start_1d) * 1000
    
    diff_pct = ((time_2d - time_1d) / time_2d) * 100 if time_2d > 0 else 0
    
    print(f"1) 2D 배열 MAC  총 소요시간: {time_2d:.2f} ms (회당 {time_2d/iterations:.5f} ms)")
    print(f"2) 1D 평탄화 MAC 총 소요시간: {time_1d:.2f} ms (회당 {time_1d/iterations:.5f} ms)")
    print(f"-> 1D 최적화를 통한 성능 향상폭: 약 {diff_pct:.2f}% 속도 개선")


def main():
    while True:
        print("\n==========================================")
        print("      Mini NPU Simulator & Classifier     ")
        print("==========================================")
        print(" 1. 사용자 패턴 직접 입력 (N x N)")
        print(" 2. data.json 로드 및 성능 분석")
        print(" 3. 메모리 접근 최적화 벤치마크")
        print(" 4. 종료")
        print("==========================================")
        
        choice = input("선택 (1~4): ").strip()
        
        if choice == "1":
            run_user_input_mode()
        elif choice == "2":
            run_json_mode()
        elif choice == "3":
            run_benchmark()
        elif choice == "4":
            print("\n시뮬레이터를 종료합니다.")
            break
        else:
            print("\n[!] 올바른 메뉴 번호를 선택해주세요.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n사용자에 의해 프로그램이 정지되었습니다.")