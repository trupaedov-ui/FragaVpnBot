import aiosqlite

DB_NAME = "db/vpn.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            sub_until INTEGER
        )
        """)
        await db.commit()