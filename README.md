# discord-Gemini

디스코드 제미나이 봇

### 필요한 패키지 설치

```bash
pip install google-genai
pip install discord
pip install python-dotenv
```

### Gemini API 키 발급

1. [Google AI Studio](https://aistudio.google.com/apikey)에 접속
2. API 키를 생성
3. `.env` 파일에 `GEMINI_API_KEY`로 저장

### Discord Bot 설정

1. [Discord Developers](https://discord.com/developers/applications)에 들어가서 애플리케이션을 만듭니다.
2. 봇 토큰을 생성하고 `.env` 파일에 `DISCORD_TOKEN`으로 저장합니다.
3. Bot Intent Privilege의 모든 스위치를 enable 합니다.

### 봇 초대

디스코드 개발자 화면에서 OAuth2 > URL Generator에 들어가 다음 권한을 선택:

- Scopes: `bot`
- Bot Permissions: `Send Messages`, `Read Messages/View Channels`, `Read Message History`

생성된 URL로 봇을 서버에 초대합니다.

### .env 파일 설정

```env
GEMINI_API_KEY=your_gemini_api_key_here
DISCORD_TOKEN_BARD=your_discord_bot_token_here
```

### 제미나이 봇 사용법

`!제미나이` 를 입력하고 이후에 질문을 입력하면 Gemini AI가 답변합니다.
