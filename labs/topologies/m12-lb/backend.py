"""Tiny HTTP backend that reports its name, the client IP it sees and X-Forwarded-For."""
import socket
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NAME = sys.argv[1] if len(sys.argv) > 1 else socket.gethostname()


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        if self.path == "/healthz":
            body = b"ok\n"
        else:
            body = (
                f"backend={NAME} path={self.path} peer={self.client_address[0]} "
                f"xff={self.headers.get('X-Forwarded-For', '-')}\n"
            ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "max-age=30")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):  # keep container logs short
        sys.stderr.write(f"{NAME} {self.address_string()} {fmt % args}\n")


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
