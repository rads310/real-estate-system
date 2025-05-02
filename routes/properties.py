from flask import Blueprint, render_template, redirect, url_for
from models import db, Property

properties_bp = Blueprint('properties', __name__, template_folder='../templates/properties')

@properties_bp.route('/')
def list_properties():
    properties = Property.query.all()
    return render_template('properties/list.html', properties=properties)

@properties_bp.route('/add', methods=['GET', 'POST'])
def add_property():
    # Здесь будет логика добавления
    return redirect(url_for('properties.list_properties'))