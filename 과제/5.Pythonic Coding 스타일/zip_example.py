

students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

print("학생과 점수 매칭:")
# zip() 함수는 여러 개의 이터러블(리스트, 튜플 등)을 인자로 받아
# 각 이터러블의 동일한 인덱스에 해당하는 요소들을 묶어서 튜플로 반환하는 이터레이터를 생성합니다.
for student, score in zip(students, scores):
    print(f"{student}: {score}점")

# zip을 사용하여 딕셔너리 생성
# zip으로 묶인 (키, 값) 쌍을 dict() 생성자에 바로 전달하여 딕셔너리를 만들 수 있습니다.
scores_dict = dict(zip(students, scores))
print(f"점수별 학생 딕셔너리: {scores_dict}")