import os, sys, logging
from pyrogram import Client
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOGGER = logging.getLogger(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH")
DB_URI = os.environ.get("DATABASE_URL", None)
CHANNEL_ID = os.environ.get("CHANNEL_ID", None)
if CHANNEL_ID and CHANNEL_ID.isdecimal(): CHANNEL_ID = int(CHANNEL_ID)
if not BOT_TOKEN or not API_ID or not API_HASH:
    LOGGER.error("One or more env variables missing! Exiting now...")
    sys.exit(1)
class CloneBot(Client):
    def __init__(self):
        super().__init__("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="bot/plugins"), time_offset=0)
        async def start(self):
        await super().start()
        LOGGER.info("Bot Started Successfully!")
        async def stop(self):
        await super().stop()
        LOGGER.info("Bot Stopped!")
bot = CloneBot()
