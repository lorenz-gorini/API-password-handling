from flask import Flask
from flask_restful import Api

from resources.passwords import Password

app = Flask(__name__)
api = Api(app)

api.add_resource(Password, "/password/<str:psw>/<str:complexity>")

if __name__ == "__main__":
  app.run()