from flask import Flask
from models import db
from routes.properties import properties_bp
from routes.clients import clients_bp
from routes.contracts import contracts_bp
from routes.inspection import inspection_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    db.init_app(app)
    
    app.register_blueprint(properties_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(contracts_bp)
    app.register_blueprint(inspection_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)