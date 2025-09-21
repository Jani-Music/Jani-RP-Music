from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗠𝗮𝘆𝘂𝗿𝗶 𝗥𝗲𝗽𝗼 ❃</u>
 
✼ 𝗥𝗲𝗽𝗼 𝗧𝗼 𝗡𝗵𝗶 𝗠𝗶𝗹𝗲𝗴𝗮
 
❉ 𐏓𐏓꯭꯭ ⃪꯭꯭꯭꯭꯭🇻꯭꯭꯭꯭꯭꯭꯭꯭꯭꯭ɪ֟፝ᴘ]꯭꯭꯭꯭᭄ ⃪꯭꯭꯭꯭꯭𝗝𝗮꯭꯭꯭꯭꯭𝗻𝗶]꯭꯭꯭꯭᭄𝅃꯭᳚𝆺꯭𝅥𝆺𝅥. 【꯭꯭꯭꯭꯭𝐒ᴀ꯭꯭꯭꯭꯭֟፝ŋa‌꯭꯭꯭꯭꯭ᴛᴀ꯭꯭꯭꯭꯭ɴ꯭꯭꯭꯭꯭ɪ🜲꯭꯭꯭꯭꯭Ꭾᴏ꯭꯭꯭꯭꯭𝚆𝙴꯭꯭꯭꯭꯭𝚁-[🇮🇳] 

✼ || [𝗠𝗮𝘆𝘂𝗿𝗶 𝗨𝗽𝗱𝗮𝘁𝗲](https://t.me/+GI_pjeSUwvtmMWI9) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜєʟᴘ •", url="http://t.me/RamHackerTG"),
          InlineKeyboardButton("• 𝛅ᴜᴘᴘσʀᴛ •", url="https://t.me/+GI_pjeSUwvtmMWI9"),
          ],
[
InlineKeyboardButton("• ϻᴧɪη ʙσᴛ •", url=f"https://t.me/MayuriMusicBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/dt2165.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
