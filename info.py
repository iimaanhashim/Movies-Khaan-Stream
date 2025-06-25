import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '20137089'))
API_HASH = environ.get('API_HASH', '9495c0e40f6b6039fb743ab96e2b5359')
BOT_TOKEN = environ.get('BOT_TOKEN', "7621939312:AAGHh-MXCEi55ZZ6XnnA6aChVtBLv9WTerM")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://atomic-pippy-khaan-c76af0c1.koyeb.app/")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002866997759'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '8057342722').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "khaanbarwaani")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
