# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 6433468  # Get this value from my.telegram.org/apps
    API_HASH = "7895dfd061f656367ccab30032"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://tkvisyvm:K_zczpHtDSrCLEjUtaH6y0z_boU_D0EV@snuffleupagus.db.elephantsql.com/tkvisyvm"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1001603822916
    MESSAGE_DUMP = -1001603822916

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "AlonesHeaven"
    SUPPORT_ID = -1001829172962

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "2323839365:AAFgfdadqawlfdsM7slOa33eM_ghop"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6079943111
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = ""

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
