from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.alfa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`halo kawan`")
    sleep(2)
    await typew.edit("`namaku alfareza`")
    sleep(1)
    await typew.edit("`16 tahun tinggal di Pati,salken ya:)`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.slm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Assalamu'alaikum**")

# Create by myself @localheart


@register(outgoing=True, pattern='^.ikut(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**ikut boleh gak?**")


# Create by myself @localheart


@register(outgoing=True, pattern='^.idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("\n╭╮╱╱╭╮"
                     "\n┃╰╮╭╯┃"
                     "\n╰╮╰╯╭┻━┳╮╭╮"
                     "\n╱╰╮╭┫╭╮┃┃┃┃"
                     "\n╱╱┃┃┃╰╯┃╰╯┃"
                     "\n╱╱╰╯╰━━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮"
                     "\n┃╭━╮┃"
                     "\n┃┃╱┃┣━┳━━╮"
                     "\n┃╰━╯┃╭┫┃━┫"
                     "\n┃╭━╮┃┃┃┃━┫"
                     "\n╰╯╱╰┻╯╰━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╭╮╱╱╱╭╮"
                     "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                     "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                     "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                     "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻┻━━┻━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━╮╱╭╮"
                     "\n┃┃╰╮┃┃"
                     "\n┃╭╮╰╯┣━━╮"
                     "\n┃┃╰╮┃┃╭╮┃"
                     "\n┃┃╱┃┃┃╰╯┃"
                     "\n╰╯╱╰━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                     "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                     "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                     "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                     "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻━━┻━━┻━╯")


CMD_HELP.update({
    "animasi3":
    "🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.alfa`\
    \n↳ : owner repo\
    \n\n🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.slm` dan `.ikut`\
    \n↳ : Coba aja hehehe.\
    \n\n🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.idiot`\
    \n↳ : u're ediot xixixi.\
    \n\n🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `kosong`\
    \n↳ : Tunggu update selanjutnya kawan."
})
