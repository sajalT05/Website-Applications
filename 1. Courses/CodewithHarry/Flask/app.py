from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# APP INIIALISATION
app=Flask(__name__)

# DATABASE
# create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'sqlite:///database.db'
db=SQLAlchemy(app)
# define database schema
class Form(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    description=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self)->str:
        return f"Form('{self.title}')"


# end points
@app.route('/', methods=['GET', 'POST'])
def index():
    # handle form
    # take input from form
    if request.method == 'POST':
        title=request.form.get('title')
        description=request.form.get('description')
    # create new form
    form=Form(title=title, description=description)
    # insert form into database
    db.session.add(form)
    # commit changes
    db.session.commit()
    # query database
    allform=Form.query.all()  
    return render_template('index.html', allform=allform)
# product page
@app.route('/database')
def database():
    # query database
    allform=Form.query.all()
    return '<h1>database</h1>'
# update database
@app.route('/update')
def update():
    # query database
    allform=Form.query.all()
    return '<h1>update</h1>'
# delete database
@app.route('/delete<int:sno>')
def delete(sno):
    # query database
    allform=Form.query.filter_by(sno=sno).first()
    db.session.delete(allform)
    db.session.commit()
    return redirect('/')


# run app
if __name__ == '__main__':
    app.run(debug=True, port=8000)