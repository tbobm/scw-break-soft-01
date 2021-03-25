"""Base example application."""
import socket

import flask


def create_app():
    app = flask.Flask(__name__)


    @app.route('/health')
    def base_healthcheck_route():
        """Hello-world route."""
        return {"message": "flask is operational", "error": False}, 200


    @app.route('/')
    def render_homepage():
        """Render the index template with the application hostname."""
        message = f"Hello from {socket.gethostname()}"
        return flask.render_template('index.html', content=message)

    return app

def main():
    """Main entrypoint."""
    app = create_app()
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
