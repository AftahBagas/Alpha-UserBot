from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy2(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama aku suka kamu`")
    sleep(2)
    await typew.edit("`Kedua ternyata kamu udah ada yg punya:(`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah aku sakit hati`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.hai1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Hallo**")


@register(outgoing=True, pattern='^.gabung(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Boleh Gabung Gak?**")


# Create by myself @localheart

CMD_HELP.update({
    "alpha1":
    "🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙`.alpha`\
    \nUsage: alive bot.\
    \n\n🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙`.sadboy2`\
    \nUsage: hiks\
    \n\n🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙`.hai1` ; `.gabung`\
    \nUsage: coba aja.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya."
})
