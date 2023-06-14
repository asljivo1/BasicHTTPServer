import http.server
import socketserver
import base64
import hashlib
import configparser

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        super().__init__(*args, **kwargs)

    def do_GET(self):
        #Basic authentication
        if self.path == '/token':
            # Check if the request has the Authorization header
            if 'Authorization' in self.headers and self.headers['Authorization'].startswith('Basic '):
                # Decode basic auth creds
                auth_type, auth_token = self.headers['Authorization'].split(' ')
                decoded_credentials = base64.b64decode(auth_token).decode('utf-8')
                read_client_id, read_client_secret = decoded_credentials.split(':')

                # Hash the client secret
                hashed_read_client_secret = hashlib.sha256(read_client_secret.encode()).hexdigest()
                myid = self.config.get('Credentials', 'client_id')
                mysecret = self.config.get('Credentials', 'hashed_client_secret')

                if read_client_id == myid and hashed_read_client_secret == mysecret:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'Authentication successful!')
                    return

            # Authentication failed
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="Authentication required"')
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Authentication failed!')
        else:
            # Handle other endpoints with the default behavior
            super().do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Server running at http://localhost:{}".format(PORT))
    httpd.serve_forever()
