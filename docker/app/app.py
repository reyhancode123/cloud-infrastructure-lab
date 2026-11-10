from http.server import BaseHTTPRequestHandler, HTTPServer
import json
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

        body = json.dumps(response, indent=4).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))


def create_server(host="0.0.0.0", port=8000):
    return HTTPServer((host, port), Handler)


def main():
    server = create_server()
    print("Python backend running on port 8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
