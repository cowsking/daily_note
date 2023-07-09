from flask import Flask
from src.send import send
from src.report import report
from flask_cors import CORS
from src.scheduler import scheduler

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.debug = True
    if test_config is not None:
        app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY'))
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(send)
    app.register_blueprint(report)

    # 启动定时任务
    scheduler.start()

    return app
