import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗞 𝗜 𝗠 𝗢ِ", url=f"https://t.me/T_5_C"), 
                 ],[
                    InlineKeyboardButton(
                        "Linr", url=f"https://t.me/F5ll3"),
                ],[
                    InlineKeyboardButton(
                        "S.J.O", url=f"https://t.me/xNoticce"),
                    InlineKeyboardButton(
                        "DoDe", url=f"https://t.me/FlFIF1"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝⚡", url=f"https://t.me/D8_8Q"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["كرار","مطور","كيمو","مبرمج","KiMo","kimo"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("DEV_TOM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["لينر انجم","ناي","لينور","ايلاينر","Lener","Lenr"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["سجو انجم","سجو","سجاد","سجوو","SJO","Sjo"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("dr_criss")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["نوف انجم","نوف","نوفه","DoDe","dode"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("C1_I_I")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗞 𝗜 𝗠 𝗢", url=f"https://t.me/T_5_C"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝⚡", url=f"https://t.me/D8_8Q"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹⊷━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس cr\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗞 𝗜 𝗠 𝗢", url=f"https://t.me/T_5_C"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝙎𝙊𝙐𝙍𝘾𝙀 𝗞𝗜𝗠𝗢 ⌝⚡", url=f"https://t.me/D8_8Q"),
                ],

            ]

        ),

    )



    
