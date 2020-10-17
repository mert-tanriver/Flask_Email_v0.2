from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email
from wtforms.fields.html5 import EmailField 

class GeneralForm(FlaskForm):
    title = StringField('Başlık Ekle', validators=[DataRequired()])
    email = StringField('Kullanıcı Ekle', validators=[DataRequired()])
    text = TextAreaField('Text')
    submit = SubmitField('Gönder')

class AddContact(FlaskForm):
    username = StringField("Kullanıcı Adı",validators=[DataRequired()])
    add_email = EmailField("Adres Ekle",validators=[DataRequired(),Email()])
    add = SubmitField("Bağlantı Ekle")
