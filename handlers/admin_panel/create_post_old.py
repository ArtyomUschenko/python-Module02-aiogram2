from aiogram import types
from config.bot_config import bot, dp

from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu


@dp.callback_query_handler(text="delete_menu")
async def admin_panel_delete_post_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)

    await bot.send_message(callback_query.from_user.id, "Потом тут можно будет удалить пост", reply_markup=admin_panel_keyboard_back_to_main_menu)