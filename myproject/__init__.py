import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


#########################
## Database Section ####
############################


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

###################
####### Login Setup ########
########################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'



##############################
###################################

from myproject.core.view import core
from myproject.user.views import users
from myproject.error_pages.handler import error_pages
from myproject.blog_posts.view import blog_posts
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)



