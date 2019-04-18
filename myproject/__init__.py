###########################################################
#### CREATE THE NECCESSARY IMPORTS FOR THE INIT FILE ######
###########################################################

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#############################################
#### CREATE THE DATABASE CONNECTION #########
#############################################

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "AAaakkJL123##$$%&@%)*(*!@#$%^&*)waMUgiKajoseNgeth@#$E"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)


####################################################
#### IMPORT THE BLUEPRINTS #######
####################################################
from myproject.regschool.views import regschool_blueprints


####################################
#### REGISTER THE BLUEPRINTS ######
####################################

app.register_blueprint(regschool_blueprints, url_prefix = "/regschool")
