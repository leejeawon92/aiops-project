import pandas as pd
from google import genai  # 최신 라이브러리 사용
from dotenv import load_dotenv
import os

# 1. 환경 설정 및 API 키 로드
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_logs(file_path):
    # 2. 로그 파일 읽기
    df = pd.read_csv(file_path)
    
    # 3. 에러 로그만 추출
    error_logs = df[df['level'] == 'ERROR']
    
    if error_logs.empty:
        return "분석할 에러 로그가 없습니다. 시스템이 정상입니다."

    # 4. AI에게 보낼 질문 구성
    log_text = error_logs.to_string(index=False)
    prompt = f"""
    당신은 숙련된 시스템 엔지니어입니다. 
    아래의 서버 에러 로그를 분석하여 다음 형식으로 보고해 주세요:
    1. 주요 장애 원인 요약
    2. 엔지니어가 취해야 할 조치 사항
    
    [로그 데이터]
    {log_text}
    """
    
    # 5. Gemini AI에게 분석 요청 (모델명: gemini-1.5-flash)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    print("최신 Gemini SDK를 사용하여 로그 분석을 시작합니다...")
    try:
        result = analyze_logs("server_logs.csv")
        print("\n--- 분석 결과 ---")
        print(result)
    except Exception as e:
        print(f"\n[오류 발생] 분석 중 문제가 생겼습니다: {e}")