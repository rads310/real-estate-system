from flask import Blueprint, render_template, redirect, url_for
from models import db, Client

clients_bp = Blueprint('clients', __name__, template_folder='../templates/clients')

@clients_bp.route('/')
def list_clients():
    clients = Client.query.all()
    return render_template('clients/list.html', clients=clients)

@clients_bp.route('/add', methods=['GET', 'POST'])
def add_client():
    # Здесь будет логика добавления
    return redirect(url_for('clients.list_clients'))