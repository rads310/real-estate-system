from flask import Flask, redirect, url_for
from models import db
from routes.properties import properties_bp
from routes.clients import clients_bp
from routes.contracts import contracts_bp
from routes.inspection import inspection_bp
import os
from pathlib import Path

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    # Убедимся, что директория instance существует
    instance_path = Path(app.instance_path)
    instance_path.mkdir(exist_ok=True)
    
    db.init_app(app)
    
    # Регистрируем blueprint с правильными URL префиксами
    app.register_blueprint(properties_bp, url_prefix='/properties')
    app.register_blueprint(clients_bp, url_prefix='/clients')
    app.register_blueprint(contracts_bp, url_prefix='/contracts')
    app.register_blueprint(inspection_bp, url_prefix='/inspections')
    
    @app.route('/')
    def home():
        return redirect(url_for('properties.list_properties'))
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)