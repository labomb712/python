import logging
import os
import datetime

def setup_logging(log_file):
    """
    로깅 시스템을 설정하고 로그 파일을 지정합니다.
    """
    if os.path.exists(log_file):
        os.remove(log_file)

    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S', 
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8')
        ]
    )
    logging.getLogger().setLevel(logging.INFO)
    print(f"로그 파일이 생성되었습니다: {log_file}")

def generate_sample_logs():
    now = datetime.datetime.now()

    logging.debug(f"{now.strftime('%H:%M:%S')} - 디버그 메시지 (개발용)")
    logging.info(f"{now.strftime('%H:%M:%S')} - 사용자 로그인 성공")
    logging.warning(f"메모리 사용량이 높습니다")
    logging.error(f"데이터베이스 연결 실패") 
    logging.info(f"{now.strftime('%H:%M:%S')} - 파일 업로드 완료")
    logging.warning(f"디스크 공간 부족") 
    logging.error(f"파일을 찾을 수 없음") 
    logging.critical(f"{now.strftime('%H:%M:%S')} - 시스템 긴급 종료!")


def filter_logs_by_level(log_file, level_to_filter):
    filtered_logs = []
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                if f" - {level_to_filter} -" in line:
                    filtered_logs.append(line.strip()) 
    except FileNotFoundError:
        print(f"오류: '{log_file}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"로그 파일을 읽는 중 오류가 발생했습니다: {e}")
    return filtered_logs

if __name__ == "__main__":
    log_file_name = "application.log"
    
    setup_logging(log_file_name)
    generate_sample_logs()

    error_logs = filter_logs_by_level(log_file_name, "ERROR")
    print("\nERROR 레벨 로그들:")
    if error_logs:
        for log in error_logs:
            print(log)
    else:
        print("ERROR 레벨 로그가 없습니다.")

    warning_logs = filter_logs_by_level(log_file_name, "WARNING")
    print("\nWARNING 레벨 로그들:")
    if warning_logs:
        for log in warning_logs:
            print(log)
    else:
        print("WARNING 레벨 로그가 없습니다.")