import discord
import os
import google.generativeai as genai
Gemini_key = os.getenv("Gemini_Key")
genai.configure(api_key=Gemini_key)

model = genai.GenerativeModel("gemini-2.5-flash")

token = os.getenv("Discord_Key")
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        if self.user.mentioned_in(message):                        
            response = model.generate_content(message.content)
            channel = message.channel
            await channel.send(response.text)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)

