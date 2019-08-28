from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engin = create_engine('sqlite:///:memory:', echo=True)
basedir = os.path.abspath(os.path.dirname(__file__))
Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app. config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True)

  def __repr__(self):
    return '<Role %r>' % self.name

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Colum(db.String(64), unique=True, index=True)

  def __repr__(self):
    return '<User %r>' % self.username

class Role(db.Model):
  #....
  users = db.relationship('User', backref='role')

class User(db.Model):
  #...
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

class NameForm(Form):
  name = StringField('What is your name?', validators=[Required()])
  submit = SubmitField('Submit')
  
app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

@app.route('/', methods=['GET', 'POST'])
def index():
  name = None
  form = NameForm()
  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
  return render_template('index.html', form=form, name=name)

if __name__ == '__main__':
	app.run(debug=True)



