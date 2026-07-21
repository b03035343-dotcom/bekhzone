"""
Ma'lumotlar bazasi bilan ishlash uchun modul (aiosqlite, asinxron).
"""
import aiosqlite
from datetime import datetime

from config import DB_PATH


async def init_db() -> None:
    """Bazani va jadvallarni (agar mavjud bo'lmasa) yaratadi."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                file_id TEXT NOT NULL,
                added_at TEXT NOT NULL
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                joined_at TEXT NOT NULL
            )
            """
        )
        await db.commit()


# ---------- Kinolar (movies) ----------

async def add_movie(code: str, title: str, file_id: str) -> bool:
    """Yangi kino qo'shadi. Kod band bo'lsa False qaytaradi."""
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO movies (code, title, file_id, added_at) VALUES (?, ?, ?, ?)",
                (code, title, file_id, datetime.utcnow().isoformat()),
            )
            await db.commit()
        return True
    except aiosqlite.IntegrityError:
        return False


async def get_movie_by_code(code: str) -> aiosqlite.Row | None:
    """Kod bo'yicha kinoni qidiradi."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM movies WHERE code = ?", (code,))
        return await cursor.fetchone()


async def delete_movie(code: str) -> bool:
    """Kod bo'yicha kinoni o'chiradi. Topilmasa False qaytaradi."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("DELETE FROM movies WHERE code = ?", (code,))
        await db.commit()
        return cursor.rowcount > 0


async def count_movies() -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM movies")
        row = await cursor.fetchone()
        return row[0] if row else 0


# ---------- Foydalanuvchilar (users) ----------

async def add_user(user_id: int, username: str | None) -> None:
    """Foydalanuvchini bazaga qo'shadi (mavjud bo'lsa, e'tiborsiz qoldiradi)."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username, joined_at) VALUES (?, ?, ?)",
            (user_id, username, datetime.utcnow().isoformat()),
        )
        await db.commit()


async def count_users() -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM users")
        row = await cursor.fetchone()
        return row[0] if row else 0


async def get_all_user_ids() -> list[int]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT user_id FROM users")
        rows = await cursor.fetchall()
        return [row[0] for row in rows]
