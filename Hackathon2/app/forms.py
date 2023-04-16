import flask_wtf
import wtforms


class LoginForm(flask_wtf.FlaskForm):
    mail = wtforms.StringField("Your mail", [wtforms.validators.DataRequired()])
    password = wtforms.StringField("Your password", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")


class RegisterForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Your username", [wtforms.validators.DataRequired()])
    mail = wtforms.StringField("Your mail", [wtforms.validators.DataRequired()])
    password = wtforms.StringField("Your password", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")
