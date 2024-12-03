from aiogram import types
from config.bot_config import dp, bot, ADMIN
from keyboard.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from db_handler.user_role.check_user_role import chek_db_user_role

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = int(message.from_user.id)
    check_user_role = await chek_db_user_role(user_id=user_id)

    if check_user_role == "admin":
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, вы вошли как админ!', reply_markup=admin_panel_keyboard_main_menu)
    else:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, вы не админ!')