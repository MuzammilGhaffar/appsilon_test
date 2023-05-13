import os
from flask import Flask
from flask_appbuilder import AppBuilder, SQLA, Model
from flask_appbuilder.models.sqla.interface import SQLAInterface
from sqlalchemy import Column, Integer, String
from flask_appbuilder.views import ModelView

app = Flask(__name__, static_url_path='/static')
base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'muzammilghaffar32@gmail.com'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'movies.db'
app.config['CSRF_ENABLED'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['APP_NAME'] = 'Movies Data'
app.config['APP_ICON'] = '/static/logo.png'
app.config['APP_THEME'] = "cosmo.css"

db = SQLA(app)

class Movies(Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    imdb_id = Column(String(255), unique=True)
    release_date = Column(String(255))

class MoviesModelView(ModelView):
    datamodel = SQLAInterface(Movies)
    list_columns = ['id', 'title', 'imdb_id', 'release_date']
    base_permissions = ['can_list', 'can_show']
    route_base = "/movies"

appbuilder = AppBuilder(app, db.session)
appbuilder.add_view(MoviesModelView, "List Movies", icon="fa-table")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000')