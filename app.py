from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin

from resources.passwords import Password

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(Password, "/password/<psw>/<int:complexity>")

if __name__ == "__main__":
  app.run()