import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '17461958'))
API_HASH = environ.get('API_HASH', '0f083cb4779252f82b99f5c644274624')
BOT_TOKEN = environ.get('BOT_TOKEN', "8153596130:AAHYoC3QF3uXnbsscBpPU3VC7dWyTJCMqg8")

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
URL = environ.get("URL", "https://creepy-cat-khaan-4bd65bc1.koyeb.app/")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002308375163'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2081516065').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "khaanbarwaani")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
