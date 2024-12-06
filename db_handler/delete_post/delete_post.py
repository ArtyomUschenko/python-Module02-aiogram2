import asyncpg

from config.bot_config import HOST, PASSWORD, USER, DB


async def delete_post(post_id):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, database=DB, host=HOST)
    await conn.execute('''DELETE FROM posts WHERE id = $1''', post_id)
    await conn.close()


