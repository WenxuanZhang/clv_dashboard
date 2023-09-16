from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    from .functions import views
    app.register_blueprint(views, url_prefix='/')
    return app

if __name__ == '__main__':
    app.run(debug = True)


