import os
import redis

from flask import Flask

from . import settings


""" Redis Pool Connection on global scope """
redis_pool = redis.ConnectionPool(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB)

""" Redis client on global scope """
redis_client = redis.Redis(connection_pool=redis_pool)


def create_flask(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object("src.settings")
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/health-check/")
    def heath_check():
        return {
            "status": "OK"
        }
    
    @app.route("/")
    def index():
        file_content = list()

        try:
            with open('logs/log.log', 'r') as file:
                file_content = [
                    line.strip()
                    for line in file
                ]
        except FileNotFoundError:
            pass

        return {
            "message": "MBA - Devops",
            "file_content": file_content
        }

    return app


application = create_flask()
