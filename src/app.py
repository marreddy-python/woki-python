from flask import Flask
# from flask_cors import CORS
from flask.ext.cors import CORS
from .config import app_config
from .models import db
from .views.BlogpostView import user_api as user_blueprint
from .views.Query import query_api as query_blueprint
from .views.Users_details import user_details_api as user_details_blueprint


def create_app(env_name):
  
  
  # app initiliazation
  app = Flask(__name__)
  CORS(app)

  app.config.from_object(app_config[env_name])
  
  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api')
  app.register_blueprint(query_blueprint,url_prefix='/api')
  app.register_blueprint(user_details_blueprint,url_prefix='/users')
  
  @app.route('/', methods=['GET','POST'])
  
  def index():
    
    return 'my end point is working' 

  return app

