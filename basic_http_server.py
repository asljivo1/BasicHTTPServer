import http.server
import socketserver
import base64
import webbrowser
import urllib.parse
import requests
import json

PORT = 8080
CLIENT_ID = '94e7c973ecaeb3068218'
CLIENT_SECRET = '279a8158f650e7b980b3bb2df11fe5fceb1061da'

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/token':
            # OAuth authentication logic
            # Retrieve the authorisation code and exchange it for access token
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

                # Check if we were granted user scope
                #scopes = response.json()['scope'].split(',')
                #has_user_email_scope = 'user' in scopes

                user_url = 'https://api.github.com/user'
                headers = {'Accept': 'application/vnd.github+json','Authorization': f"Bearer {access_token}"} #vnd.github+json   , "X-GitHub-Api-Version": "2022-11-28"
                response = requests.get(user_url, headers = headers)
                if response.status_code == 200:
                    user_data = response.json()
                    self.wfile.write(b'Authentication successful!')
                    return
                else:
                    print(f"Error: {response.json().get('message', 'unnknown error')}")
        else:
            super().do_GET()


with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Server running at http://localhost:{}".format(PORT))
    httpd.serve_forever()