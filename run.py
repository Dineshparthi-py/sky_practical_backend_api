from flask_cors import CORS
import connexion


def create_app(instance_config=None):
    conn_app = connexion.FlaskApp(__name__, specification_dir='./app/openapi_v3')
    app = conn_app.app
    app.debug = True
    CORS(app)
    conn_app.add_api('swagger_serialization.yml')
    return conn_app


if __name__ == '__main__':
    app = create_app()
    # for development purpose configured single server(localhost) with debug
    app.run(host='0.0.0.0')
