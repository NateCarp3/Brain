from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import brains
from flask_app.models import user
from flask_app.models import brain
from flask_app.models import cart

if __name__=="__main__":
    app.run(debug=True)