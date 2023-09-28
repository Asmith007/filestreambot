# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('29945782'))
    API_HASH = str(getenv('72c65716866cc125fd079f0d27c5c847'))
    BOT_TOKEN = str(getenv(6133212214:AAH3ls935a_AKtHTem-uubQMoOYYi-FzzhY'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'F2LxBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('-1001959187345'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '2068472689'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('5917661208'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
