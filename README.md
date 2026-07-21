# 🎬 Kino Kod Bot

Foydalanuvchi kino kodini yuborsa, botning bazasidan mos videoni topib
yuboradigan Telegram bot. **aiogram 3** (async) + **SQLite** asosida yozilgan.

## Imkoniyatlar

- 🔎 Kod bo'yicha kino qidirish (foydalanuvchi uchun)
- ➕ Admin panel orqali video yuklab, unga kod biriktirish
- 🗑 Kod bo'yicha kinoni o'chirish
- 📊 Foydalanuvchilar va kinolar statistikasi
- 📣 Barcha foydalanuvchilarga xabar yuborish (broadcast)
- 🔒 Majburiy kanalga obuna (ixtiyoriy, `.env` orqali yoqiladi/o'chiriladi)

## Talablar

- Python 3.10 yoki undan yuqori
- Telegram bot tokeni ([@BotFather](https://t.me/BotFather) orqali olinadi)

## O'rnatish

```bash
# 1. Loyihaga kiring
cd kino_bot

# 2. Virtual muhit yarating (tavsiya etiladi)
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Kerakli kutubxonalarni o'rnating
pip install -r requirements.txt
```

## Sozlash

1. `.env.example` faylidan nusxa oling:
   ```bash
   cp .env.example .env
   ```
2. `.env` faylini oching va quyidagilarni to'ldiring:
   - **BOT_TOKEN** — [@BotFather](https://t.me/BotFather) dan `/newbot`
     buyrug'i orqali olingan token.
   - **ADMIN_IDS** — sizning Telegram ID raqamingiz. Uni bilish uchun
     [@userinfobot](https://t.me/userinfobot) ga `/start` yozing.
   - **REQUIRED_CHANNEL** *(ixtiyoriy)* — foydalanuvchilar majburiy obuna
     bo'lishi kerak bo'lgan kanal (`@kanal_nomi` ko'rinishida). Botni shu
     kanalga **admin** qilib qo'shishni unutmang, aks holda tekshiruv
     ishlamaydi. Kerak bo'lmasa, shunchaki bo'sh qoldiring.

## Ishga tushirish

```bash
python bot.py
```

Konsolda "Bot ishga tushdi..." yozuvi chiqsa — bot ishlayapti. Telegramda
botingizga `/start` yozib tekshiring.

## Foydalanish

### Oddiy foydalanuvchi uchun

- `/start` — botni ishga tushiradi
- Istalgan vaqtda kino kodini yuborish (masalan `101`) — mos video qaytadi

### Admin uchun

- `/admin` — boshqaruv panelini ochadi (tugmalar orqali boshqariladi):
  - **➕ Kino qo'shish** — avval video yuboriladi, so'ng
    `kod - nom` formatida matn yuboriladi (masalan `101 - Avengers: Endgame`)
  - **🗑 Kino o'chirish** — o'chiriladigan kino kodi so'raladi
  - **📊 Statistika** — foydalanuvchilar va kinolar sonini ko'rsatadi
  - **📣 Xabar yuborish** — yuborilgan xabar (matn/rasm/video) barcha
    foydalanuvchilarga jo'natiladi

> Kino fayllarini yuklashda ulardan foydalanish huquqiga ega ekanligingizni
> o'zingiz nazorat qiling — bu loyiha faqat texnik infratuzilmani taqdim etadi.

## Loyiha tuzilishi

```
kino_bot/
├── bot.py              # Kirish nuqtasi (polling shu yerdan boshlanadi)
├── config.py            # .env dan sozlamalarni o'qiydi
├── database.py           # SQLite bilan ishlash (aiosqlite)
├── keyboards.py           # Inline tugmalar
├── handlers/
│   ├── user.py           # Oddiy foydalanuvchi handlerlari
│   └── admin.py           # Admin panel handlerlari (FSM asosida)
├── requirements.txt
├── .env.example
└── .env                 # O'zingiz yaratasiz (git'ga qo'shilmaydi)
```

## Serverga joylashtirish (production)

Kompyuteringiz o'chganda bot ham to'xtaydi, shuning uchun doimiy ishlashi
uchun uni VPS serverga joylashtirish tavsiya etiladi:

```bash
# tmux yoki screen orqali fon rejimida ishga tushirish
tmux new -s kinobot
python bot.py
# Ctrl+B keyin D — sessiyadan chiqish (bot ishlashda davom etadi)
```

Yanada barqaror yechim uchun `systemd` service yaratish yoki
[Railway](https://railway.app) / [VPS + Docker](https://www.docker.com/)
kabi platformalardan foydalanish mumkin — kerak bo'lsa shu bo'yicha ham
yordam bera olaman.

## Kengaytirish g'oyalari

- Bir nechta majburiy kanal qo'llab-quvvatlash
- Kategoriya/janr bo'yicha qidirish
- Inline rejimda qidirish (`@bot_username 101`)
- PostgreSQL'ga o'tish (foydalanuvchilar soni ko'payganda)
