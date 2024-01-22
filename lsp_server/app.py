from flask import Flask, send_file, request, abort
from werkzeug.utils import secure_filename
import logging
import sys

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET'])
def handle_get(path):
    file_path = './www/' + request.method + request.path
    try:
        return send_file(file_path, mimetype='application/octet-stream')
    except FileNotFoundError:
        logging.info("could not find '%s'\n", file_path)
        abort(404)

@app.route('/upload_server/upload.ashx', methods=['POST'])
def upload_file():
    if 'upload' not in request.files:
        return 'No file part', 400

    file = request.files['upload']
    if file.filename == '':
        return 'No selected file', 404

    filename = secure_filename(file.filename)
    content_type = request.headers['Content-Type']

    file.save('./www/' + request.method + '/uploads/' + filename)

    return f'File {filename} uploaded with content type {content_type}', 200

if __name__ == '__main__':
        app.run()
