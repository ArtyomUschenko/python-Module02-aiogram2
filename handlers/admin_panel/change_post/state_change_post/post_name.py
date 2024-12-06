from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post



@dp.message_handler(state=FSM_change_post.post_name)
async def post_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_name'] = message.html_text
        await FSM_change_post.next()
        await bot.send_message(message.chat.id, f"ID поста: {data['post_id']}"
                               f"Новое название поста: {data['post_name']}\n"
                               f"Пришлите новое описание поста",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)