import os
import markdown

#Flask
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


class InventoryList(Resource):
    def get(self):

        return {'message' : 'Success'}

api.add_resource(InventoryList, '/inventory')