class User:
    def __init__(self, username: str, passwordHash: str, isAdmin: bool, _id=None):
        self.username = username
        self.password_hash = passwordHash
        self.is_admin = isAdmin

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value
    
    @property
    def password_hash(self) -> str:
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, value):
        self._password_hash = value
    
    @property
    def is_admin(self) -> bool:
        return self._is_admin
    
    @is_admin.setter
    def is_admin(self, value):
        self._is_admin = value
    
    def get_document_mapping(self):
        return {
            "username": self.username,
            "passwordHash": self.password_hash,
            "isAdmin": self.is_admin
        }
    
def print_user_table(users: list[User]):
    username_col_width = 20
    isAdmin_col_width = 8
    username_heading = f"{"Username":<{username_col_width}}"
    isAdmin_heading = f"{"isAdmin":<{isAdmin_col_width}}"
    divider = " | "
    headings = username_heading + divider + isAdmin_heading

    print(headings)
    print('-' * len(headings))

    for user in users:
        print(f"{user.username:<{username_col_width}}{divider}{user.is_admin!s:<{isAdmin_col_width}}")