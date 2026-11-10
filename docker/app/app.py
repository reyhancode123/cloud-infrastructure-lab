from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            "project": "Cloud Infrastructure Lab",
            "service": "Python Backend",
            "hostname": socket.gethostname(),
            "status": "healthy",
            "message": "Backend is running successfully"
        }

        body = json.dumps(response, indent=4).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))

server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Python backend running on port 8000")
server.serve_forever()
