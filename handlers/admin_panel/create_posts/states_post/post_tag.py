from handlers.admin_panel.create_posts.states_post.post_description import post_description
from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot, CHAT_ID
from aiogram.dispatcher import FSMContext

from handlers.admin_panel.create_posts.create_post import FSM_create_post
from db_handler.create_post.create_post import create_post
from db_handler.create_post.check_user_name import check_db_user_name
import datetime


@dp.message_handler(state=FSM_create_post.post_tag)
async def post_image(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_tag'] = message.html_text
        await state.finish()

        user_id = int(message.from_user.id)
        post_name = str(data['post_name'])
        post_description = str(data['post_description'])
        post_image = str(data['post_image'])
        post_tag = str(data['post_tag'])
        cur_data = str(datetime.datetime.now().date())
        cur_time = str(datetime.datetime.now().time().replace(microsecond=0))
        user_name = await check_db_user_name(user_id=user_id)

        await create_post(post_name=post_name, post_description=post_description, post_image=post_image,post_tag=post_tag,user_name=user_name, create_date=cur_data, create_time=cur_time)

        await bot.send_photo(message.from_user.id, photo=post_image, caption=
                            f"Название поста: {post_name}\n"
                            f"Текста поста: {post_description}\n"
                            f"Тег поста: #{post_tag}\n"
                            f"Дата создания: {cur_data}\n"
                            f"Время создания: {cur_time}\n"
                            f"Автор поста: {user_name}\n"
                            f"Вы успешно создали пост!\n", reply_markup=admin_panel_keyboard_back_to_main_menu, parse_mode="HTML"
                             )

        await bot.send_photo(CHAT_ID, photo=post_image, caption=f"{post_name}\n\n"
                             f"{post_description}", parse_mode="HTML")