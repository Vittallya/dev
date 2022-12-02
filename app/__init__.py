from flask import Flask
from app.services.Db import Db
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()
app = Flask(__name__)
app.config.from_object('config')
csrf.init_app(app)
Db('lampochki_db', 'user2', 'parol')



from app import views