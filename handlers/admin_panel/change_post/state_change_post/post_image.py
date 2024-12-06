from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post
from db_handler.create_post.check_user_name import check_db_user_name
from db_handler.change_post.change_post import change_post

import datetime


@dp.message_handler(content_types=["photo"], state=FSM_change_post.post_image)
async def post_image(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_image'] = message.photo[0].file_id

        post_name = str(data['post_name'])
        post_description = str(data['post_description'])
        post_image = str(data['post_image'])
        post_tag = str(data['post_tag'])
        cur_date = str(datetime.datetime.now().date())
        cur_time = str(datetime.datetime.now().time().replace(microsecond=0))
        post_id = int(data['post_id'])
        user_id = int(message.from_user.id)

        await state.finish()

        user_name = await check_db_user_name(user_id=user_id)


        await change_post(post_name=post_name, post_description=post_description, post_image=post_image,
                          post_tag=post_tag, change_user_name=user_name, change_date=cur_date, change_time=cur_time, post_id=post_id)

        await bot.send_message(message.chat.id, f"ID поста: {data['post_id']}"
                                f"Новое название поста: {data['post_name']}\n"
                                f"Новое описание поста: {data['post_description']}\n"
                                f"Новый тег поста: {data['post_tag']}\n"
                                f"пост успешно обновлен",
                                reply_markup=admin_panel_keyboard_back_to_main_menu)