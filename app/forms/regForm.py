
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class RegForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(message='Заполните'), Length(min=2, max=20, message="Логин должен быть от 2 до 20 симв")])
    password = PasswordField('Пароль', validators=[DataRequired()])