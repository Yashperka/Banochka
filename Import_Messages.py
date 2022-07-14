from fileinput import filename
from pyrogram import Client, filters
import pyrogram.raw as pyr_raw
import os
from datetime import datetime, timedelta
import pandas as pd
import json 
import service
import Channels

chat = Channels.Channel(Channels.ZERKALO["id"])

app = Client("my_account")

app = Client("my_account",18053160,"195ab02f6f015ed643f42d85b1fe0911")

f = open('result.txt', 'w',encoding='utf-8')

msg =[]

print(os.getcwd())
f
async def main():
    async with app:
        #Создаем обьект "сырого" канала
        ch = await app.resolve_peer(chat.id)
        raw_chat = await app.invoke(pyr_raw.functions.channels.get_full_channel.GetFullChannel(channel = ch))
        #Загружаем доступные реакции в объект канала
        chat.reactions = raw_chat.__str__()
        print(chat.reactions)       
        async for message in app.get_chat_history(chat.id, 10, offset_date= datetime.now() - timedelta(days = 1)):
            post = service.create_end_dict(json.loads(message.__str__()))
            if not(post is None):
                msg.append(post)
            print(message, file = f)

app.run(main())

df = pd.json_normalize(msg)
print(df)
df.to_csv("E:/Работа/Zesta/Zesta/result.csv", sep = "*")


