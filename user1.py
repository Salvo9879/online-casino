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

create_me()