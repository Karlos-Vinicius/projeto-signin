from flask import Flask
from routes.entering import entering
from routes.home import home


app = Flask(__name__)

app.register_blueprint(entering, url_prefix="/entering")
app.register_blueprint(home)

app.run(debug=True)
