from http.server import BaseHTTPRequestHandler, HTTPServer

class Request_handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    message = "Hello world"
    self.wfile.write(bytes(message, "utf8"))
    return

def run():
  server_address = ('127.0.0.1', 80)
  httpd = HTTPServer(server_address, Request_handler)
  print('running server...')
  httpd.serve_forever()


run()