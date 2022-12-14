import configparser
from config import TELEGRAM_CONFIG_PATH, PROFILE_IMG_DIR, USE_TELEGRAM
import os
import io
from PIL import Image
import asyncio

from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest


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


async def get_tg_user_main_info(client, user):
    tg_users = await get_phone_contacts(client=client, phone=user.phone.as_e164)

    if len(tg_users) > 0:
        tg_user = tg_users[0]
        user_id, first_name, last_name, username = get_user_info(tg_user)
        photo_path = os.path.join(PROFILE_IMG_DIR, str(user_id))
        result = await get_profile_photo(client=client, user_id=user_id, path=photo_path)
        if result is not None:
            img = Image.open(result)
            img_format = img.format
            img_size = img.size
            im_resize = img.resize(img_size)
            buf = io.BytesIO()
            im_resize.save(buf, format=img_format)
            byte_im = buf.getvalue()
            user.photo = byte_im
            try:
                os.remove(result)
            except FileNotFoundError:
                pass


def read_tg_config():
    config = configparser.ConfigParser()
    config.read(TELEGRAM_CONFIG_PATH)

    # Присваиваем значения внутренним переменным
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    username = config['Telegram']['username']
    connect = bool(int(config["Telegram"]['connect']))

    return api_id, api_hash, username, connect


def download_profile_info(user):
    api_id, api_hash, username, connect = read_tg_config()

    if connect and USE_TELEGRAM:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient(username, api_id, api_hash)
        client.start()
        with client:
            client.loop.run_until_complete(get_tg_user_main_info(client, user))
    else:
        print("not connected")
    user.save()
