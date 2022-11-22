#app/__init__.py

import os
from flask import Flask,request,session
# from flask_socketio import SocketIO


def create_app(script_info=None):
    app_settings = os.getenv("APP_SETTINGS")

    #instantiate app
    app = Flask(__name__)
   
    #set config
    app.config.from_object(app_settings)
    
    from app.api import api
    api.init_app(app)


    @app.shell_context_processor
    def ctx():
        return {"app":app}
    
    return app