from xml.dom.xmlbuilder import DOMBuilder

import asyncpg

from config.bot_config import HOST, PASSWORD, USER, DB

async def chek_db_user_role(user_id):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, database=DB, host=HOST)
    row = await conn.fetchrow("SELECT user_role FROM users WHERE user_id = $1", user_id)
    await conn.close()

    if row is None:
        return "None"
    else:
        return row["user_role"]
