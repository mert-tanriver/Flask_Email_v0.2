from flask import Flask, render_template, redirect, url_for,request
import forms,secrets,mail_demo
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

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(150), nullable = False)
    mailadd = text = db.Column(db.String(500))

    def __repr__(self):
        return f'{self.username} and {self.mailadd}'


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
        
        if form.title.data is not None:
            mail_demo.mail_sender(form.title.data,form.email.data,form.text.data)
        
        return redirect(url_for("index"))
    
    if request.method == 'POST' and form2.validate():
        print("Username :",form2.username.data)
        print("E-Mail:",form2.add_email.data)
        c = Contact(username = form2.username.data, mailadd = form2.add_email.data)
        print(c)
        return redirect(url_for("index"))

    return render_template("index.html",form=form,form2=form2)



if __name__ == "__main__":
    app.run(debug = True)
    
