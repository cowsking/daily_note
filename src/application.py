from flask import Flask
import os
from src.auth import auth
from flask_cors import CORS

def create_app(test_config=None):
    
    app = Flask(__name__,instance_relative_config=True)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.debug = True
    if test_config is not None:
        app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY'))
    else:
        app.config.from_mapping(test_config)
    
    
    app.register_blueprint(auth)

    

    return app