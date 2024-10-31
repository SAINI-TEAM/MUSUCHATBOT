from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "12380656"
# -------------------------------------------------------------
API_HASH = "d927c13beaaf5110f25c505b7c071273"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7673640235"))
SUPPORT_GRP = "quizbysu"
UPDATE_CHNL = "quizbys"
OWNER_USERNAME = "attitude_boy91"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002373440231"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7673640235").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SAINI-TEAM/MUSUCHATBOT",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
