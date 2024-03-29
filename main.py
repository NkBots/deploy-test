import os

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        elif message.content == 'neko':
            await message.channel.send('にゃーん')
        elif message.content == 'hoge':
            await message.channel.send('fuga')
        elif message.content == 'foo':
            await message.channel.send('bar')


client = MyClient()
client.run(os.environ['TOKEN'])