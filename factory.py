from flask import Flask
from src.api.controller import reports_app


def create_app(domo, mode='PRODUCTION') -> Flask:
    """Create a flask app instance."""

    flask_app = Flask('pdp_domo')
    flask_app.config['JSON_SORT_KEYS'] = False
    flask_app.config['APP_MODE'] = mode

    #flask_app.config.from_object(config_object)

    # import blueprints
    flask_app.cassandra_client = domo
    flask_app.register_blueprint(reports_app)

    return flask_app
