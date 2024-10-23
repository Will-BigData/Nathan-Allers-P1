class User:
    def __init__(self, username: str, passwordHash: str, isAdmin: bool):
        self._username = username
        self._password_hash = passwordHash
        self._is_admin = isAdmin

    @property
    def username(self) -> str:
        return self._username
    
    @property
    def password_hash(self) -> str:
        return self._password_hash
    
    @property
    def is_admin(self) -> bool:
        return self._is_admin
    
    def get_document_mapping(self):
        return {
            "username": self.username,
            "passwordHash": self.password_hash,
            "isAdmin": self.is_admin
        }