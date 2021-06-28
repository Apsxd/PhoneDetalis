import json
import re
import requests

from bot import Bot, Config

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from alternate import send_message


bot = Bot()

START_TEXT = """
H! {}
Here You can Get Details of any phone no.👀
just Paste Your Number in International format👀
Use /cancel TO STOP ALL PROGRESS 
use /phone <Your phone no>

REPORT ANY BUGS&ISSUE** AT 
~ SUPPORT ~
"""

CANCEL = """
OKAY👀,
All progress stopped🙂
by the way
Thanks to give your time☺️
"""

HELP = """
HI...
I am phone no. details tracker bot.
by @Psycho_Bots
i Can give details for any phone no.🤗which you want 
you just have to use /phone <your no>
and i will provide you valid details under the rules of PRIVACY&POLICY.
Because I don't wanna to go ban by telegram
still i provide you information of a no. expect of name i give whole Details 🤗

**Thanks to**
CREATOR❤️:- @Psycho_Bots
CREDITS❤️:- @tubots
"""

@bot.on_message(filters.private & filters.command("start"))
async def start(bot: Bot, msg: Message):
    chat = msg.chat
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="•SUPPORT•❤️", url="https://t.me/PsychoBots_chat")]],
        [[InlineKeyboardButton(text="•Credits•❤️", url="https://t.me/uunitedbotsupport")]]
    )
    await bot.send_message(chat.id, START_TEXT, reply_markup=reply_markup)
    
@bot.on_message(filters.private & filters.command("phone"))
def phone(update, context):
    args = update.effective_message.text.split(None, 1)
    information = args[1]
    number = information
    key = "fe65b94e78fc2e3234c1c6ed1b771abd"
    api = (
        "http://apilayer.net/api/validate?access_key="
        + key
        + "&number="
        + number
        + "&country_code=&format=1"
    )
    output = requests.get(api)
    content = output.text
    obj = json.loads(content)
    country_code = obj["country_code"]
    country_name = obj["country_name"]
    location = obj["location"]
    carrier = obj["carrier"]
    line_type = obj["line_type"]
    validornot = obj["valid"]
    aa = "Valid: " + str(validornot)
    a = "Phone number: " + str(number)
    b = "Country: " + str(country_code)
    c = "Country Name: " + str(country_name)
    d = "Location: " + str(location)
    e = "Carrier: " + str(carrier)
    f = "Device: " + str(line_type)
    g = f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
    send_message(update.effective_message, g)
    
    
@bot.on_message(filters.private & filters.command("cancel"))
async def cancel(bot: Bot, msg: Message):
    chat = msg.chat 
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="•SUPPORT•❤️", url="https://t.me/Psycho_Bots")]],
       [[InlineKeyboardButton(text="•Credits•❤️", url="https://t.me/uunitedbotsupport")]]
    )
    await bot.send_message(chat.id, CANCEL, reply_markup=reply_markup)
    
    
@bot.on_message(filters.private & filters.command("about"))
async def about(bot: Bot, msg: Message):
    chat = msg.id
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="Repository ✨", url="https://github.com/PsychoBots/PhoneDetalis")]]
      )
    await bot.send_message(chat.id, HELP, reply_markup=reply_markup)
      
      #####################
 # By @Alone_loverboy
 # For @Psycho_bots (OWN COMMUNITY)
 # Thanks 
 # KANGER FUCK OFF🙂
