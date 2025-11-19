import os

import discord
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Gemini API 설정
genai_client = genai.Client(api_key=GEMINI_API_KEY)


def get_gemini_message(message):
    """Gemini API를 사용하여 응답 생성"""
    try:
        response = genai_client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=message
        )
        return response.text
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"


class BotClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

        if message.author != self.user and "!제미나이" in message.content:
            user_message = message.content.replace("!제미나이", "").strip()
            if user_message:
                await message.channel.send(get_gemini_message(user_message))
            else:
                await message.channel.send("메시지를 입력해주세요!")


intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)
client.run(DISCORD_TOKEN)
