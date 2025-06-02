
"""
Crea proyecto y configuracion
inicializa y configuracion de proyecto, adiciona registra blueprints
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app2 = Flask(__name__)

    #Configuracion del proyecto
    app2.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )

    db.init_app(app2)

    #Registro de Blueprint
    from . import todo #import bp
    app2.register_blueprint(todo.bp) #registra bp

    from . import auth
    app2.register_blueprint(auth.bp)

    @app2.route('/') #ruta raiz
    def index():
        return render_template('index.html')
    
    with app2.app_context():
        db.create_all()
    
    return app2 #devuelve aplicaicon configurada