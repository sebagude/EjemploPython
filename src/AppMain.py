from flask import Flask
from flask_cors import CORS

from src import controllers

app = Flask(__name__)
CORS(app)

app.register_blueprint(controllers.tamano_controller, url_prefix='/tamano')
app.register_blueprint(controllers.producto_controller, url_prefix='/producto')
app.register_blueprint(controllers.customer_controller, url_prefix='/customer')
app.run(debug=True)
