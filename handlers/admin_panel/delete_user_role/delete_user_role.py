from aiogram import types
from config.bot_config import dp,  bot

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboard.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

from db_handler.user_role.delete_user_role import delete_user_role
from db_handler.user_role.check_user_role import check_db_user_role

class FSM_delete_role_from_user(StatesGroup):
    user_id = State()


@dp.callback_query_handler(text="delete_user_role")
async def admin_panel_delete_user_role(callback_query: types.CallbackQuery):
    await FSM_delete_role_from_user.user_id.set()
    await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, f"Пришлите ID пользователя для удаления роли")




@dp.message_handler(state=FSM_delete_role_from_user.user_id)
async def delete_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            check = await check_db_user_role(user_id=int(message.text))
            data['check'] = message.text
            int_user_id = int(message.text)

            if check == "None":
                await state.finish()
                await bot.send_message(message.from_user.id, f"Пользователь с ID {int_user_id} не найден в базе", reply_markup=admin_panel_keyboard_back_to_main_menu)

            else:
                await state.finish()
                await bot.send_message(message.from_user.id, f"Пользователь с ID {int_user_id} найден в базе")
                await delete_user_role(user_id=int_user_id)
                await bot.send_message(message.from_user.id, f"Роль пользователя с ID {int_user_id} удалена", reply_markup=admin_panel_keyboard_back_to_main_menu)
        except ValueError:
            await state.finish()
            await bot.send_message(message.from_user.id, f"ID пользователя должен быть числом", reply_markup=admin_panel_keyboard_back_to_main_menu)