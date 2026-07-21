"""
Konfiguratsiya fayli.
Barcha maxfiy va sozlanuvchi qiymatlar .env faylidan o'qiladi.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# @BotFather dan olingan bot tokeni
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

# Admin(lar)ning Telegram user ID raqamlari, vergul bilan ajratilgan
# Masalan: ADMIN_IDS=123456789,987654321
ADMIN_IDS: list[int] = [
    int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip().isdigit()
]

# Majburiy obuna kanali (ixtiyoriy).
# Agar bo'sh qoldirilsa, majburiy obuna tekshiruvi ishlamaydi.
# Format: @kanal_username
REQUIRED_CHANNEL: str = os.getenv("REQUIRED_CHANNEL", "").strip()

# SQLite ma'lumotlar bazasi fayli
DB_PATH: str = os.getenv("DB_PATH", "kino_bot.db")


def is_admin(user_id: int) -> bool:
    """Foydalanuvchi admin ekanligini tekshiradi."""
    return user_id in ADMIN_IDS
