from flask import Flask
from routes.entering import entering
from routes.home import home
from database.database import db
from database.models.user import User


app = Flask(__name__)

db.connect()
db.create_tables([User])
app.register_blueprint(entering, url_prefix="/entering")
app.register_blueprint(home)

app.run(debug=True)
