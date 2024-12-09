from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram  import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_publish_post(StatesGroup):
    post_id = State()

@dp.callback_query_handler(text='publish_post')
async def admin_panel_publish_post_callback(callback_query: types.CallbackQuery):
    await FSM_publish_post.post_id.set()
    await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Введите ID поста для опубликования', reply_markup=admin_panel_keyboard_back_to_main_menu)


