from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, String,Integer,Column, DateTime
from datetime import datetime


app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

data_base = SQLAlchemy(app)

class Artic(data_base.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    name = Column(String(300), nullable=False)
    faname = Column(String(300), nullable=False)
    date = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Artic %r>' % self.id


@app.route('/')
@app.route('/main')
def index():
    return render_template("index.html")


@app.route('/posts')
def posts():
    #articl = Artic.query.grop_by(Artic.title).order_by(Artic.name).all()
    return render_template('posts.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/ui')
def uicomponents():
    return render_template('ui.html')


@app.route('/modals')
def modals():
    return render_template('modals.html')

@app.route('/pages')
def pages():
    return render_template('pages.html')


@app.route('/id<string:name>')
def user(name):
    return render_template("user.html")



if __name__ == '__main__':
    app.run(debug=True)