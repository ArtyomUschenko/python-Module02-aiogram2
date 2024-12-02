from aiogram import types
from config.bot_config import dp,  bot

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

class FSM_create_user_role_content_manager(StatesGroup):
    user_id = State()


@dp.callback_query_handler(text=['take_user_role_content_manager'], state=None)
async def load_user_role_admin(callback_query: types.Message):
    await FSM_create_user_role_content_manager.user_id.set()
    await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, "Роль была успешно добавлена \n Введите id пользователя")

@dp.message_handler(state=FSM_create_user_role_content_manager.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text

    await state.finish()
    await bot.delete_message(message.from_user.id, message_id=message.message_id)
    await bot.send_message(message.from_user.id, F"Контент менеджер  с ID {data['user_id']} успешно создан", reply_markup=admin_panel_keyboard_back_to_main_menu)
