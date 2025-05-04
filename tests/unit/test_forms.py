import pytest
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange

class TestFormClasses:
    
    def test_property_form_structure(self):
        """Тест структуры формы PropertyForm"""
        class PropertyForm(FlaskForm):
            address = StringField('Address', validators=[DataRequired()])
            area = FloatField('Area', validators=[DataRequired(), NumberRange(min=1)])
            price = FloatField('Price', validators=[DataRequired(), NumberRange(min=1)])
            status = SelectField('Status', choices=[
                ('available', 'Available'),
                ('sold', 'Sold'), 
                ('rented', 'Rented')
            ])
        
        form = PropertyForm()
        assert hasattr(form, 'address')
        assert hasattr(form, 'area')
        assert hasattr(form, 'price')
        assert hasattr(form, 'status')

    def test_client_form_validation(self):
        """Тест валидации формы клиента"""
        class ClientForm(FlaskForm):
            name = StringField('Name', validators=[DataRequired()])
            phone = StringField('Phone', validators=[DataRequired()])
            client_type = SelectField('Type', choices=[
                ('owner', 'Owner'),
                ('buyer', 'Buyer')
            ])
        
        # Тест валидных данных
        valid_data = {
            'name': 'Иван Иванов',
            'phone': '+79161234567',
            'client_type': 'buyer'
        }
        form = ClientForm(data=valid_data)
        assert form.validate() is True
        
        # Тест невалидных данных
        invalid_data = {'name': '', 'phone': '', 'client_type': ''}
        form = ClientForm(data=invalid_data)
        assert form.validate() is False