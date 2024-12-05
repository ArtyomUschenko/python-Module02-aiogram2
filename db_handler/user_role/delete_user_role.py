import asyncpg

from config.bot_config import HOST, PASSWORD, USER, DB


async def delete_user_role(user_id):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, database=DB, host=HOST)
    await conn.execute('''DELETE FROM users WHERE user_id = $1''', user_id)
    await conn.close()


