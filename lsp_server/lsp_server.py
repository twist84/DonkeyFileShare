from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class S(BaseHTTPRequestHandler):
	def _set_response(self, content_type, content_length):
		self.send_response(200)
		self.send_header('Content-Type', content_type)
		self.send_header('Content-Length', str(content_length))
		self.end_headers()

	def do_GET(self):
		logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
		file_path = '.' + str(self.path)
		try:
			with open(file_path, 'rb') as file:
				logging.info("found '%s'\n", file_path)
				binary_data = file.read()
				self._set_response('application/octet-stream', len(binary_data))
				self.wfile.write(binary_data)
		except FileNotFoundError:
			logging.info("could not find '%s'\n", file_path)
			self.send_response(404)
			self.send_header('Content-Length', '0')
			self.end_headers()

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)
		logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\n",str(self.path), str(self.headers))
		self._set_response("text/plain", '0')

def run(server_class=HTTPServer, handler_class=S, port=8000):
	logging.basicConfig(level=logging.INFO)
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	logging.info('Starting httpd...\n')
	print(httpd)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	logging.info('Stopping httpd...\n')

if __name__ == '__main__':
	from sys import argv
	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()
