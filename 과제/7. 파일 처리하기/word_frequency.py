import os

def create_sample_file(filename="sample.txt"):
    """
    예시 텍스트 파일을 생성합니다. 파일이 이미 존재하면 덮어씁니다.
    """
    content = """
    파이썬은 배우기 쉬운 강력한 프로그래밍 언어입니다.
    파이썬은 다양한 분야에서 사용되는 언어입니다.
    파이썬 프로그래밍을 즐겨보세요!
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"'{filename}' 파일이 생성되었습니다.")

def count_word_frequency(filepath):
    """
    텍스트 파일의 단어 빈도를 계산합니다.
    소문자 변환 및 구두점 제거를 포함합니다.
    """
    word_counts = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                processed_line = line.strip().lower()
                words = processed_line.split()

                for word in words:
                    word = word.strip('.,!?"\''); 
                    
                    if word: 
                        word_counts[word] = word_counts.get(word, 0) + 1
    except FileNotFoundError:
        print(f"오류: '{filepath}' 파일을 찾을 수 없습니다.")
        return {}
    except Exception as e:
        print(f"파일을 처리하는 중 오류가 발생했습니다: {e}")
        return {}
        
    return word_counts

if __name__ == "__main__":
    file_name = "sample.txt"

    if not os.path.exists(file_name):
        create_sample_file(file_name)
    else:
        print(f"'{file_name}' 파일이 이미 존재합니다. 기존 파일을 사용합니다.")

    word_frequencies = count_word_frequency(file_name)

    print("\n단어 빈도 분석 결과:")
    if word_frequencies:
        sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
        
        for word, count in sorted_word_frequencies:
            print(f"{word}: {count}번")
    else:
        print("분석할 단어가 없거나 파일을 읽을 수 없습니다.")