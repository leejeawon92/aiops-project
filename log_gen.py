import random
import time
import pandas as pd
from datetime import datetime
import os

# 로그 설정
LEVELS = ["INFO", "INFO", "INFO", "WARNING", "ERROR"]
MESSAGES = {
    "INFO": ["User logged in", "Database query successful", "Cache cleared"],
    "WARNING": ["High memory usage", "Slow response time", "Disk space 80% full"],
    "ERROR": ["Connection timeout", "Permission denied", "Critical system failure"]
}
LOG_FILE = "server_logs.csv" # 저장될 파일 이름

def generate_log():
    level = random.choice(LEVELS)
    message = random.choice(MESSAGES[level])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"timestamp": timestamp, "level": level, "message": message}

if __name__ == "__main__":
    print(f"{LOG_FILE}에 로그 저장을 시작합니다... (Ctrl+C 종료)")
    
    log_list = []
    try:
        while True:
            log_data = generate_log()
            log_list.append(log_data) # 데이터를 리스트에 추가
            print(f"[{log_data['timestamp']}] {log_data['level']}: {log_data['message']}")
            
            # 10개가 쌓일 때마다 파일에 저장 (성능과 안정성을 고려한 방식)
            if len(log_list) >= 10:
                df = pd.DataFrame(log_list)
                # 파일이 없으면 제목(Header)을 포함해 새로 만들고, 있으면 내용만 추가(append)
                df.to_csv(LOG_FILE, mode='a', index=False, header=not os.path.exists(LOG_FILE))
                log_list = [] # 리스트 비우기
                print(f">>> {LOG_FILE}에 10개의 로그 저장 완료.")
                
            time.sleep(0.5)
    except KeyboardInterrupt:
        # 종료 전 남아있는 로그가 있다면 마저 저장
        if log_list:
            pd.DataFrame(log_list).to_csv(LOG_FILE, mode='a', index=False, header=not os.path.exists(LOG_FILE))
        print("\n로그 생성을 중단하고 모든 데이터를 저장했습니다.")