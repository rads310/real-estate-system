from flask import Blueprint, render_template, redirect, url_for
from models import db, Inspection

inspection_bp = Blueprint('inspection', __name__, template_folder='../templates/inspection')

@inspection_bp.route('/')
def list_inspections():
    inspections = Inspection.query.all()
    return render_template('inspection/list.html', inspections=inspections)

@inspection_bp.route('/add', methods=['GET', 'POST'])
def add_inspection():
    # Здесь будет логика добавления
    return redirect(url_for('inspection.list_inspections'))