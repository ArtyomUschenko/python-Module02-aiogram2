from xml.dom.xmlbuilder import DOMBuilder

import asyncpg

from config.bot_config import HOST, PASSWORD, USER, DB

async def get_post(post_id):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, database=DB, host=HOST)
    row = await conn.fetchrow("SELECT post_name,post_description, post_image FROM posts WHERE id = $1", post_id)
    await conn.close()

    if row is None:
        return "None"
    else:
        return row
