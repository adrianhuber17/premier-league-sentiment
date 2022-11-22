from flask_restx import Api
from app.api.ping import ping_namespace

api = Api(version="1.0", title="APIs", doc="/docs/")

api.add_namespace(ping_namespace, path="/ping")