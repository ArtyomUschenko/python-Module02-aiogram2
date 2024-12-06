from aiogram import executor
from config.bot_config import dp

from handlers.admin_panel.create_posts.create_post import *
from handlers.admin_panel.delete_post import *

from handlers.start.start import *
from handlers.admin_panel.create_user_role.create_user_role import *
from handlers.admin_panel.create_user_role.admin.admin import *
from handlers.admin_panel.create_user_role.content_manager.content_manager import *
from handlers.admin_panel.delete_user_role.delete_user_role import delete_user_role
from handlers.admin_panel.main_menu import *
from handlers.admin_panel.create_posts.states_post.post_name import *
from handlers.admin_panel.create_posts.states_post.post_tag import *
from handlers.admin_panel.create_posts.states_post.post_description import *
from handlers.admin_panel.create_posts.states_post.post_image import *
from handlers.admin_panel.change_post.get_post import *
from handlers.admin_panel.change_post.state_change_post.post_id import *
from handlers.admin_panel.change_post.state_change_post.post_image import *
from handlers.admin_panel.change_post.state_change_post.post_name import *
from handlers.admin_panel.change_post.state_change_post.post_description import *
from handlers.admin_panel.change_post.state_change_post.post_tag import *



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)