from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client("session", api_id='25000350', api_hash='bbbcea7a53df4b34e5f5a2062c395cd1')


chat_id = "@anonkarubot"

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Собеседник найден!" in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(2.1)
        await app.send_message(chat_id, "Приветик я  Д19,я тут только ради интима!")
        sleep(2.2)
        await app.send_message(chat_id, "Я кончила 13раз за один подход посмотришь?)💦")

        if "Собеседник найден!" in message.text:
                sleep(2.3)
                await app.send_sticker(chat_id, "CAACAgIAAxkBAAEIEzdkCxZqeIgOw1RO0TDMwjcJ6s87bQAC5yQAAgTbuErwHbfUyBhwFi8E")
                sleep(2.4)

                if "Собеседник найден!" in message.text:  # Меняем это значение если хотим спамить в другом чате
                       await app.send_message(chat_id, "/stop")
                       sleep(2.5)
                       await app.send_message(chat_id, "/next")


app.run()

