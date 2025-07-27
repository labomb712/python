a = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}


print("학생 성적:")
for name, score in a.items():
    print(f"{name}: {score}점")


l = list(a.values())
ave = sum(l)/len(l)

print("평균 점수", ave)