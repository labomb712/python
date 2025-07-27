import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")

print(f"Python 버전: {sys.version.splitlines()[0]}") 

print(f"운영체제: {sys.platform}")

path_env = os.environ.get('PATH')
if path_env:
    print(f"환경 변수 PATH 일부: {':'.join(path_env.split(os.pathsep)[:3])}")
else:
    print("환경 변수 PATH를 찾을 수 없습니다.")

example_file_path = "/Users/username/documents/report.txt" 

print("\n파일 경로 정보:")
print(f"- 디렉토리: {os.path.dirname(example_file_path)}")
print(f"- 파일명: {os.path.basename(example_file_path)}")
print(f"- 확장자: {os.path.splitext(example_file_path)[1]}")

print(f"파일 존재 여부: {os.path.exists(example_file_path)}")