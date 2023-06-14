import http.server
import socketserver
import base64
import webbrowser
import urllib.parse
import requests
import json
import os

PORT = 8080
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
access_token = None

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global access_token

        if self.path == '/token':
            # Check if user is already authorized
            if access_token:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Authentication successful!')
                return
            else:
                # Redirect the user to GitHub for authorization               
                auth_url = f'https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=user'
                webbrowser.open(auth_url)

        if self.path.startswith('/callback'):
            # Parse the authorisation code for the callback URL
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            code = params['code'][0]
            
            # Exchange the authorisation code for an access token
            token_url = 'https://github.com/login/oauth/access_token'
            payload = {
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'code': code
            }
            headers = {'Accept': 'application/json'}
            response = requests.post(token_url, data=payload, headers=headers)

            data = response.json()
            if 'access_token' in data:
                access_token = response.json()['access_token']

                # Redirect to the '/token' endpoint
                self.send_response(302)
                self.send_header('Location', '/token')
                self.end_headers()
                return
                
        super().do_GET()


with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    socketserver.allow_reuse_address = True
    print("Server running at http://localhost:{}".format(PORT))
    httpd.serve_forever()