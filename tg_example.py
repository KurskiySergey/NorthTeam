import configparser
from config import TELEGRAM_CONFIG_PATH, PROFILE_IMG_DIR
import os
import asyncio

from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact


async def get_phone_contacts(client: TelegramClient, phone="89116254127"):
    contact = InputPhoneContact(client_id=0, phone=phone, first_name="a", last_name="")
    result = await client(ImportContactsRequest([contact]))
    users = result.__dict__['users']
    return users


def get_user_info(user):
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    user_id = user.id

    return user_id, first_name, last_name, username


async def get_profile_photo(client, user_id, path):
    result = await client.download_profile_photo(user_id, file=path)
    return result


async def get_tg_user_main_info(client, phone):
    print("get contact info")
    tg_users = await get_phone_contacts(client=client, phone=phone)

    if len(tg_users) > 0:
        tg_user = tg_users[0]
        user_id, first_name, last_name, username = get_user_info(tg_user)
        print(user_id, first_name, last_name, username, sep=" ")
        photo_path = os.path.join(PROFILE_IMG_DIR, str(user_id))
        result = await get_profile_photo(client=client, user_id=user_id, path=photo_path)
        if result is not None:
            print("downloaded photo")
            print(result)


def read_tg_config():
    config = configparser.ConfigParser()
    config.read(TELEGRAM_CONFIG_PATH)

    # Присваиваем значения внутренним переменным
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    username = config['Telegram']['username']
    connect = bool(int(config["Telegram"]['connect']))

    return api_id, api_hash, username, connect


def download_profile_info(phone):
    api_id, api_hash, username, connect = read_tg_config()

    if connect:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("creating client")
        client = TelegramClient(username, api_id, api_hash)
        print("start connect")
        client.start()
        print("start main loop")
        with client:
            client.loop.run_until_complete(get_tg_user_main_info(client, phone))
    else:
        print("not connected")
