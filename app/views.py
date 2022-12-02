from app import app
from flask import render_template, session, redirect, url_for
from app.forms.loginForm import LoginForm
from app.forms.regForm import RegForm
from app.services.Db import Db
from app.services.loginService import LoginService

db = Db.db
login_service = LoginService(db)



@app.route('/')
@app.route('/index')
def index():
    
    tovars = db.getData("SELECT * FROM Tovars")    
    return render_template('index.html', data = tovars, userData = session.get('user'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    message = None
    if form.validate_on_submit():
        user = login_service.try_login(form.login.data, form.password.data)
        if user != None:
            session['user'] = {'uuid': user[0], 'login': user[1]}
            return redirect(url_for('index'))
        else:
            message = 'Пользователь не найден'
            
    return render_template('login.html', form = form, userData = session.get('user'), msg = message)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    
    if form.validate_on_submit():
        count = login_service.check_login(form.login.data)[0]        
        
        if count == 0:
            login_service.register_user(form.login.data, form.password.data)
            return redirect(url_for('index'))
        else:
            form.errors['login'] = 'Такой логин уже есть'
            
    return render_template('register.html', form = form, userData = session.get('user'))
    

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))