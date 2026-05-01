# check_models.py 라는 파일을 만들어 실행해 보세요
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("사용 가능한 모델 목록:")
for m in client.models.list():
    print(f"- {m.name}")