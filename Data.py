from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hello {}

Iam A Simple Gofiles Uploader Bot. Send Me Any File Or Media To Get gofile.io Stream Link

𝗠𝗮𝗱𝗲 𝗪𝗶𝘁𝗵 ❤ BY @M2Botz
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("Help⚙️", callback_data="help"),
            InlineKeyboardButton("About😎", callback_data="about")
        ],
        [InlineKeyboardButton("💬 Update Channel", url="https://t.me/m2botz"),
        InlineKeyboardButton("🗣 Support Group", url="https://t.me/m2botzsupport")],
        [
        InlineKeyboardButton("🧑‍💻Developer", url="https://t.me/ask_admin01")],
    ]

    # Help Message
    HELP = """
Just Send Me The Media And You Will Get The Link!

✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Bot To Upload Files To gofile.io By @M2Botz

💬 Update Channel  : [Click Here](https://t.me/m2botz)

🗣 Support Group : [Click Here](https://t.me/m2botzsupport)

🔗Source Code : [Comming Soon](https://t.me/m2botz)

🧑‍💻Developer : [M2](https://t.me/ask_admin01)
    """
