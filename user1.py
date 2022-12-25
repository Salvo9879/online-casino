from gambol.databases import Users, db
from gambol.helpers import iso_dt

from app import app

def create_me():
    u = Users()
    u.forename = 'Salvatore'
    u.surname = 'La Paglia'
    u.birthdate = iso_dt()
    u.email = 'salvatorelapaglia@icloud.com'
    u.username = 'Salvo9879'
    u.password = '1234'

    with app.app_context():
        db.session.add(u)
        db.session.commit()

def delete_me():
    
    with app.app_context():
        u = Users.query.filter_by(id=1).first()
        db.session.delete(u)
        db.session.commit()

delete_me()