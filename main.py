import discord
from dotenv import load_dotenv
import os
import bardapi

load_dotenv()
BARD_SESSION_ID = os.getenv("BARD_SESSION_ID")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN_BARD")


def get_bard_message(message):
    response = bardapi.core.Bard(BARD_SESSION_ID).get_answer(message)
    return response["content"]


class BotClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

        if message.author != self.user and "!바드" in message.content:
            await message.channel.send(
                get_bard_message(message.content.replace("!바드", ""))
            )


intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)
client.run(DISCORD_TOKEN)
