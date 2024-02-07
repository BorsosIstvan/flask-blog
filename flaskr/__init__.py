import os

from flask import Flask

def create_app(test_config=None):
    # creeren en configureren de app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    if test_config is None:
        # laden de exemplaarconfiguratie, als deze bestaat, wanneer u niet test
        app.config.from_pyfile('confyg.py', silent=True)
    else:
        # laden de test config als het past
        app.config.from_mapping(test_config)

    # zorg ervoor dat de exemplaarmap bestaat
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

#    from . import db
#    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

    # een eenvoudig blad zeg Hoi wereld!
    @app.route('/hello')
    def hello():
        return 'Hoi Wereld!'
    return app

