#app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()

def create_app(script_info=None):

    #instantiate app
    app = Flask(__name__)
   
    app_settings = os.getenv("APP_SETTINGS")
    #set config
    app.config.from_object(app_settings)

    #set up extensions
    cors.init_app(
    app,
    resources={r"*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}},
    supports_credentials=True,
    )
    db.init_app(app)
    
    #register api
    from app.api import api
    api.init_app(app)


    @app.shell_context_processor
    def ctx():
        return {"app":app,"db":db}
    
    return app