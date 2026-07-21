"""
Inline va oddiy tugmalar (keyboard) shu yerda yig'ilgan.
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import REQUIRED_CHANNEL


def subscription_keyboard() -> InlineKeyboardMarkup:
    """Majburiy obuna uchun: kanal linki + 'Tekshirish' tugmasi."""
    builder = InlineKeyboardBuilder()
    channel_username = REQUIRED_CHANNEL.lstrip("@")
    builder.row(
        InlineKeyboardButton(
            text="📢 Kanalga o'tish",
            url=f"https://t.me/{channel_username}",
        )
    )
    builder.row(
        InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subscription")
    )
    return builder.as_markup()


def admin_panel_keyboard() -> InlineKeyboardMarkup:
    """Admin panelining asosiy menyusi."""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="➕ Kino qo'shish", callback_data="admin_add"),
        InlineKeyboardButton(text="🗑 Kino o'chirish", callback_data="admin_delete"),
    )
    builder.row(
        InlineKeyboardButton(text="📊 Statistika", callback_data="admin_stats"),
        InlineKeyboardButton(text="📣 Xabar yuborish", callback_data="admin_broadcast"),
    )
    return builder.as_markup()


def cancel_keyboard() -> InlineKeyboardMarkup:
    """Har qanday admin jarayonini bekor qilish tugmasi."""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel"))
    return builder.as_markup()
