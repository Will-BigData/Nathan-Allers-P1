from dao import UserDAO

if __name__ == "__main__":
    user_dao = UserDAO()
    print(user_dao.get_user_by_username("test"))