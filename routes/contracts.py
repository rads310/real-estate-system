from flask import Blueprint, render_template, redirect, url_for
from models import db, Contract

contracts_bp = Blueprint('contracts', __name__, template_folder='../templates/contracts')

@contracts_bp.route('/')
def list_contracts():
    contracts = Contract.query.all()
    return render_template('contracts/list.html', contracts=contracts)

@contracts_bp.route('/add', methods=['GET', 'POST'])
def add_contract():
    # Здесь будет логика добавления
    return redirect(url_for('contracts.list_contracts'))