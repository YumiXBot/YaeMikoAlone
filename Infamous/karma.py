# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/9417608b498572767c188.jpg",
    "https://telegra.ph/file/c9da8690eb49d5bb323c4.jpg",
    "https://telegra.ph/file/f8a8f824e3d8507ed7d70.jpg",
    "https://telegra.ph/file/8f8897391b02635f6c19a.jpg",
    "https://telegra.ph/file/7293c9538db7cc350be7d.jpg",
    "https://telegra.ph/file/fb963b2b40c076b71120a.jpg",
    "https://telegra.ph/file/1fd3655b3e98b40b76389.jpg",
]

HEY_IMG = "https://telegra.ph/file/dd63646a33309b1eaba35.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://telegra.ph//file/79a6c527e6e6d530bcdc8.mp4",
]


MUTE_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ᴀʟᴏɴᴇ, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⛩𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣⛩",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="⚡️𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦⚡", callback_data="help_back"),
        InlineKeyboardButton(text="𝗨𝗣𝗗𝗔𝗧𝗘𝗦🏥", url="https://t.me/AloneXBots"),
    ],
    [
        InlineKeyboardButton(text="🤖𝗔𝗜", callback_data="ai_handler"),
        InlineKeyboardButton(text="𝗗𝗘𝗩", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="𝗦𝗢𝗨𝗥𝗖𝗘🫧", callback_data="git_source"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⛩𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣⛩",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="𝗖𝗥𝗘𝗔𝗧𝗢𝗥", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/AloneXBots"),
        ib(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/AlonesHeaven"),
    ],
    [
        ib(
            text="⛩𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣⛩",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *ᴀʟᴏɴᴇ ʀᴏʙᴏᴛ* 🫧

☉ *Hᴇʀᴇ, Yᴏᴜ Will Fɪɴᴅ A Lɪsᴛ Oғ Aʟʟ Tʜᴇ Aᴠᴀɪʟʙʟᴇ Cᴏᴍᴍᴀɴᴅs.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
