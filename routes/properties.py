from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import db, Property

properties_bp = Blueprint('properties', __name__, template_folder='../templates/properties')

@properties_bp.route('/')
def list_properties():
    properties = Property.query.all()
    return render_template('properties/list.html', properties=properties)

@properties_bp.route('/add', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        try:
            new_property = Property(
                address=request.form['address'],
                area=float(request.form['area']),
                price=float(request.form['price']),
                status=request.form.get('status', 'available')
            )
            db.session.add(new_property)
            db.session.commit()
            flash('Property added successfully!', 'success')
            return redirect(url_for('properties.list_properties'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding property: {str(e)}', 'danger')
    
    return render_template('properties/add.html')
