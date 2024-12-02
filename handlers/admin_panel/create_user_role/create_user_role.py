from aiogram import types
from config.bot_config import dp, bot

from keyboard.admin_panel_keyboard_take_user_role import admin_panel_keyboard_take_user_role

@dp.callback_query_handler(text="make_user_role")
async def admin_panel_create_user_role(callback_quare: types.CallbackQuery):
    await bot.delete_message(callback_quare.from_user.id, message_id=callback_quare.message.message_id)

    await bot.send_message(callback_quare.from_user.id, "Кого вы хотите добавить?", reply_markup=admin_panel_keyboard_take_user_role)