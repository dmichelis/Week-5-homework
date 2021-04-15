import secrets

from flask_login import LoginManager, UserMixin

from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model):
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(100), nullable = True, default = '')
    last_name = db.Column(db.String(100), nullable = True, default = '')
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String, nullable = False, default = '')
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    car = db.relationship('Car', backref = 'owner', lazy = True)


    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = ''):
@@ -37,4 +48,33 @@ def set_password(self, password):
        return self.pw_hashed

    def __repr__(self):
        return f'User {self.email} has been created and you may now start your collection' 
        return f'User {self.email} has been created and you may now start your collection'

class Car(db.Model):
    id = db.Column(db.String, primary_key=True)
    car_make = db.Column(db.String(150))
    car_model = db.Column(db.String(150))
    car_year = db.Column(db.String(150))
    car_color = db.Column(db.String(150))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, car_make, car_model, car_year, car_color, user_token, id=''):
        self.id = self.set_id()
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.car_color = car_color
        self.user_token = user_token

    def __repr__(self):
        return f'The following car has been added: {self.car_model}'

    def set_id(self):
        return secrets.token_urlsafe()

class CarSchema(ma.Schema):
    class Meta:
        fields = ['id','car_make','car_model','car_year','car_color']

car_schema = CarSchema()
cars_schema = CarSchema(many = True)  