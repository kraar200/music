import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("cr")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس cr \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𝗞𝗜𝗠𝗢ِ", url=f"https://t.me/T_5_C"),
                    InlineKeyboardButton(
                        "KiMo", url=f"https://t.me/DevKiMo"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝⚡", url=f"https://t.me/D8_8Q"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━★⊷⌯⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝⌯⊶★━⩺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━★⊷⌯⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="tommm")],
            [InlineKeyboardButton("𝗞𝗜𝗠𝗢ِ", url=f"https://t.me/D8_8Q"),
             InlineKeyboardButton("ρ᥆kᥱꪔ᥆ꪀ", url=f"https://t.me/devpokemon")],
            [InlineKeyboardButton("★⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝⚡", url=f"https://t.me/D8_8Q")],
        ]
    ))

