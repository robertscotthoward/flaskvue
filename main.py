'''

'''

import os
import sys
from flask import Flask, jsonify, render_template, abort
#from flask_cors import CORS

root = os.path.dirname(__file__)
webFolder = '.'
staticFolder = os.path.join(root, 'static')
templatesFolder = os.path.join(root, 'templates')

app = Flask(__name__, static_folder=staticFolder,)
#CORS(app)  # Enable CORS for all routes


def readFile(fn):
  with open(fn) as f:
    return f.read()


@app.route('/api/books')
def get_data():
    data = [
      {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "description": "A classic novel set in the Jazz Age"
      },
      {
      "id": 2,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "description": "A powerful story about racial injustice"
      },
      {
      "id": 3,
      "title": "1984",
      "author": "George Orwell",
      "description": "A dystopian novel depicting a totalitarian society"
      },
      {
      "id": 4,
      "title": "Pride and Prejudice",
      "author": "Jane Austen",
      "description": "A classic romance novel"
      }
    ]
    return jsonify(data)


# Define a catch all route that will return the index.html, and defer to the static folder otherwise
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
  if not path:
    path = 'index.html'
  fp = os.path.join(staticFolder, path)
  if not os.path.isfile(fp):
    abort(404)
  return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
