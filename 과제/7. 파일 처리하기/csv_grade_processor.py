import csv

def save_grades_to_csv(filename, students_data):
    """
    학생 성적 데이터를 CSV 파일로 저장합니다.
    Args:
        filename (str): CSV 파일 이름.
        students_data (list of dict): 각 학생의 '이름'과 '점수'를 포함하는 딕셔너리 리스트.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['이름', '점수'])  # 헤더 작성
        for student in students_data:
            writer.writerow([student['이름'], student['점수']])
    print(f"학생 성적이 {filename}에 저장되었습니다.")

def load_grades_from_csv(filename):
    """
    CSV 파일에서 학생 성적 데이터를 읽어옵니다.
    Args:
        filename (str): CSV 파일 이름.
    Returns:
        list of dict: 각 학생의 '이름'과 '점수'를 포함하는 딕셔너리 리스트.
    """
    students_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 헤더 건너뛰기
        for row in reader:
            if row:  # 빈 줄 방지
                name = row[0]
                score = int(row[1])
                students_data.append({'이름': name, '점수': score})
    return students_data

def analyze_grades(students_data):
    """
    학생 성적을 분석하여 개인 점수와 전체 평균을 출력합니다.
    Args:
        students_data (list of dict): 각 학생의 '이름'과 '점수'를 포함하는 딕셔너리 리스트.
    """
    total_score = 0
    print("\n성적 분석 결과:")
    for student in students_data:
        print(f"{student['이름']}: {student['점수']}점")
        total_score += student['점수']
    
    if students_data:
        average_score = total_score / len(students_data)
        print(f"전체 평균: {average_score:.1f}점")
    else:
        print("분석할 학생 데이터가 없습니다.")

# --- 메인 프로그램 ---
if __name__ == "__main__":
    grades_file = "grades.csv"
    
    # 예시 학생 데이터
    student_records = [
        {'이름': '김철수', '점수': 85},
        {'이름': '이영희', '점수': 92},
        {'이름': '박민수', '점수': 78},
        {'이름': '최수진', '점수': 95},
    ]

    # 1. 학생 성적 데이터를 CSV 파일에 저장
    save_grades_to_csv(grades_file, student_records)

    # 2. CSV 파일에서 학생 성적 데이터 읽기
    loaded_students = load_grades_from_csv(grades_file)

    # 3. 읽어온 데이터로 성적 분석 및 출력
    analyze_grades(loaded_students)