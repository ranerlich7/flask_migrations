from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(500))
    phone = db.Column(db.String(50), nullable=False)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String(400))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_post_user'), nullable=False)

# user_id ???

@app.route("/test_add_user")
def test_add():
    new_user = User(name="Ofer", phone="050-4443333")
    db.session.add(new_user)
    db.session.commit()
    return "ADDED!"

@app.route("/test_add_post")
def test_add_post():
    new_post = Post(title="Adam's post", content="This is Adam post", user_id=3)
    db.session.add(new_post)
    db.session.commit()
    return "ADDED POST!"
   
with app.app_context():
    db.create_all()


if __name__ == '__main__':
   app.run(debug=True, port=9000)