\# AIOps Project: Gemini AI 기반 서버 로그 분석기



이 프로젝트는 대규모 시스템 로그 중에서 장애의 근본 원인을 자동으로 탐지하고, AI(Gemini 2.5/3.0)를 통해 전문 엔지니어 수준의 대응 가이드를 제공하는 \*\*AIOps(Artificial Intelligence for IT Operations) 솔루션\*\*입니다.



\## 🛠 주요 기능

\- \*\*실시간 가상 로그 생성\*\*: `INFO`, `WARNING`, `ERROR` 등 다양한 레벨의 서버 로그를 무작위로 생성하여 테스트 환경 구축

\- \*\*데이터 구조화 및 저장\*\*: 생성된 로그를 분석에 용이한 `CSV` 형식으로 자동 변환 및 저장

\- \*\*AI 기반 장애 원인 분석\*\*: Gemini API를 연동하여 에러 로그 간의 상관관계를 파악하고 근본 원인(Root Cause) 요약

\- \*\*맞춤형 조치 사항 제언\*\*: 장애 상황별 시스템 엔지니어의 즉각적인 조치 및 심층 분석 가이드 자동 생성



\## 기술 스택

\- \*\*Language\*\*: Python 3.x

\- \*\*AI Model\*\*: Google Gemini 2.5 Flash / Pro

\- \*\*Libraries\*\*: 

&#x20; - `google-genai`: 최신 Gemini API 연동

&#x20; - `pandas`: 데이터 전처리 및 구조화

&#x20; - `python-dotenv`: 보안을 위한 API Key 관리

\- \*\*Version Control\*\*: Git / GitHub



\##  프로젝트 구조

\- `log\_gen.py`: 실시간 가상 로그 생성 및 CSV 저장 프로그램

\- `ai\_analyzer.py`: 최신 Gemini SDK 기반 로그 분석 엔진

\- `server\_logs.csv`: 분석 대상 로그 데이터 (자동 생성됨)

\- `.env`: API 키 등 민감 정보 관리 파일 (보안을 위해 `.gitignore` 처리)



\##  실행 방법



1\. \*\*환경 변수 설정\*\*: `.env` 파일에 Gemini API 키를 입력합니다.

&#x20;  ```text

&#x20;  GEMINI\_API\_KEY=your\_actual\_api\_key\_here

