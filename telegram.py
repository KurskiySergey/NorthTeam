import argparse
import configparser
from config import TELEGRAM_CONFIG_PATH
from telethon import TelegramClient
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--enable", "-e", action="store_true")
    parser.add_argument("--disable", "-d", action="store_true")
    args = parser.parse_args()

    if args.enable:
        config = configparser.ConfigParser()
        config.read(TELEGRAM_CONFIG_PATH)
        api_id = os.environ.get("TELEGRAM_API_ID", "17646873")
        api_hash = os.environ.get("TELEGRAM_API_HASH", "493a1866a8f5534092d962c66058c47b")
        username = os.environ.get("TELEGRAM_USERNAME", "User")
        config.set("Telegram", "connect", "1")
        config.set("Telegram", "api_id", api_id)
        config.set("Telegram", "api_hash", api_hash)
        config.set("Telegram", "username", username)
        with open(TELEGRAM_CONFIG_PATH, "w") as configfile:
            config.write(configfile)

        client = TelegramClient(username, api_id=api_id, api_hash=api_hash)
        client.start()

    if args.disable:
        config = configparser.ConfigParser()
        config.read(TELEGRAM_CONFIG_PATH)
        try:
            os.remove(f"{config['Telegram']['username']}.session")
        except FileNotFoundError:
            pass

        config.set("Telegram", "connect", "0")
        with open(TELEGRAM_CONFIG_PATH, "w") as configfile:
            config.write(configfile)
