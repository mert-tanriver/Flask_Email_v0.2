from flask import Flask, render_template, redirect, url_for,request
import forms,secrets
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GarbageValue' #secrets.token_bytes()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class General(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(150), nullable = False)
    text = db.Column(db.String(500))
    
    def __repr__(self):
        return f'{self.title} and {self.text}'


@app.route('/')
@app.route('/index',methods = ['POST','GET'])
def index():
    form = forms.GeneralForm(request.form)
    form2 = forms.AddContact(request.form)
    if request.method == 'POST' and form.validate():
        print("Title : ",form.title.data)
        print("E-Mail : ",form.email.data)
        print("Text : ",form.text.data)
        g = General(title = form.title.data, text = form.text.data)
        print(g)
        return redirect(url_for("index"))
    
    if request.method == 'POST' and form2.validate():
        print("Username :",form2.username.data)
        print("E-Mail:",form2.add_email.data)
        return render_template("index.html",form=form,form2 = form2)
   
    return render_template("index.html",form=form,form2=form2)


if __name__ == "__main__":
    app.run(debug = True)
    
