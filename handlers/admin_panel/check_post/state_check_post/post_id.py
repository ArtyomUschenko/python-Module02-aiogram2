from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot, CHAT_ID
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.check_post.check_post import FSM_check_post
from db_handler.get_post.get_post import get_post


@dp.message_handler(state=FSM_check_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            row = await get_post(int(message.text))
            data['post_id'] = message.text

            await state.finish()

            await bot.send_photo(message.from_user.id, photo=row['post_image'], caption=
                                f"ID поста: {data['post_id']}\n" 
                                f"Название поста: {row['post_name']}\n"
                                f"Описание поста: {row['post_description']}\n"
                                f"Тег поста: {row['post_tag']}\n",
                                   reply_markup=admin_panel_keyboard_back_to_main_menu, parse_mode="HTML")
        except TypeError:
            await state.finish()
            await bot.send_message(message.from_user.id,  f"ID поста: {message.text}\n"
                                   f"Ошибка. Поста с данным ID нет в базе данных\n",
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)