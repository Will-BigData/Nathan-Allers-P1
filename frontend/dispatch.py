from model import User
from .admin import admin_menu
from .store import store_menu

def dispatch_user(user: User):
    if user.is_admin:
        admin_menu(user)
    else:
        store_menu(user)