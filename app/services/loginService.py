from werkzeug.security import check_password_hash, generate_password_hash
from uuid import uuid4

class LoginService:
    def __init__(self, db) -> None:
        self.db = db
        
    def try_login(self, login, password):
        
        user = self.db.getFirst('SELECT u.uuid, u.Login, u.PasswordHash FROM UserAcc u WHERE u.Login = %s', (login,))
        
        if user == None or not check_password_hash(user[2], password):
            return None
        usr = list(user)
        usr.pop()
        return tuple(usr)
        
    def check_login(self, login):
        return self.db.getFirst('SELECT COUNT(*) FROM UserAcc WHERE Login = %s', (login,))
        
    def register_user(self, login, password):
        uuid = uuid4().hex
        p_hash = generate_password_hash(password)
        self.db.execute('INSERT INTO UserAcc VALUES (%s, %s, %s)', (uuid, login, p_hash))
        
    