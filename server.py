from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import random
app = Flask(__name__)
CORS(app)
FILES_DIRECTORY = '.'
@app.route('/<path:filename>')
def serve_file(filename):
    file_path = os.path.join(FILES_DIRECTORY, filename)
    if os.path.exists(file_path):
        return send_from_directory(FILES_DIRECTORY, filename)
    return "File not found", 404
@app.route('/')
def index():
    return send_from_directory(FILES_DIRECTORY, "index.html")
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
