from aiogram import types
from config.bot_config import dp, bot, ADMIN
from keyboard.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)

    if user_id == ADMIN:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, вы вошли как админ!', reply_markup=admin_panel_keyboard_main_menu)
    else:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, вы не админ!')