from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ Wҽʅƈσɱҽ Tσ Tҽαɱ Mαყυɾι Rҽρσʂ ❃</u>
 
✼ Rҽρσ Tσ Nԋι Mιʅҽɠα
 
❉ Mҽԋυ 420 ραρα Bσʅσ Rҽρσ Oɯɳҽɾ Kσ 

✼ || [Mayuri Update](https://t.me/+dV10ZuqXLBYyYzZl) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜєʟᴘ •", url="http://t.me/Mehu_420"),
          InlineKeyboardButton("• 𝛅ᴜᴘᴘσʀᴛ •", url="https://t.me/+dV10ZuqXLBYyYzZl"),
          ],
[
InlineKeyboardButton("• ϻᴧɪη ʙσᴛ •", url=f"https://t.me/MayuriMusicBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/0rl8s0.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
