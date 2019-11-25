import socketserver
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from primality import Primality_test

primality = Primality_test()

PORT = 80

class Request_handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    query = urlparse(self.path).query
    query_components = dict(qc.split("=") for qc in query.split("&"))
    candidate_number = query_components["number"]

    if candidate_number:
      prime = primality.isPrime(int(candidate_number))

      if prime:
        message = "Given number " + str(candidate_number) + " is prime."
      else:
        message = "Given number " + str(candidate_number) + " is NOT prime."
      self.wfile.write(bytes(message, "utf8"))
      return
    return

class Server():
  def __init__(self):
    pass

  def run(self):
    with socketserver.TCPServer(("", PORT), Request_handler) as httpd:
      print("serving at port", PORT)
      httpd.serve_forever()