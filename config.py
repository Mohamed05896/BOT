from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/aac35f002094ac4a8391f.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/aac35f002094ac4a8391f.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AF_64")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/INTRNT05896")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656828413").split()))


FAILED = "https://graph.org/file/9681d7086cc9c32b85d5a.jpg"
