from flask import Flask, send_file, request, abort
import logging
import sys

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET'])
def handle_get(path):
    file_path = '.' + request.path
    try:
        return send_file(file_path, mimetype='application/octet-stream')
    except FileNotFoundError:
        logging.info("could not find '%s'\n", file_path)
        abort(404)

@app.route('/upload_server/upload.ashx', methods=['POST'])
def handle_post():
    post_data = request.data
    logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\n",str(request.path), str(request.headers))
    return '', 200

if __name__ == '__main__':
        app.run(port=8000)
