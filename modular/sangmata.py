################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

import asyncio
import random

from pyrogram import *
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import *

from Mix import *

__modles__ = "SangMata"
__help__ = get_cgr("help_sangmata")


@ky.ubot("sg", sudo=True)
@ky.devs("siapa")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    puki = await c.extract_user(m)
    if len(m.command) < 2 and not m.reply_to_message:
        return await m.reply(cgr("sangmat_1").format(em.gagal))
    if puki in DEVS:
        return await m.reply(
            f"{em.gagal} <b>DILARANG KERAS MENGGUNAKAN FITUR INI KEPADA SEORANG DEV MIX-USERBOT!</b>"
        )
    try:
        (await c.get_users(puki)).id
    except Exception:
        try:
            int(message.command[1])
        except Exception as err:
            return await m.reply(cgr("err").format(em.gagal, err))
    proses = await m.reply(cgr("proses").format(em.proses))
    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)
    try:
        a = await c.send_message(sg, f"{argu}")
        await a.delete()
    except Exception as e:
        return await proses.edit(e)

    await asyncio.sleep(1)

    async for respon in c.search_messages(a.chat.id):
        if respon.text == None:
            continue
        if not respon:
            await m.reply(cgr("sangmat_3").format(em.gagal))
        elif respon:
            await m.reply(cgr("sangmat_4").format(em.sukses, respon.text))
            break

    try:
        user_info = await c.resolve_peer(sg)
        await c.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await proses.delete()
