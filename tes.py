# part of Zaid-Userbot

import os

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Greeting(Resource):
    def get(self):
        return "Running..."


api.add_resource(Greeting, "/")
app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000), debug=False, use_reloader=False)

