# Basic HTTP Server

This HTTP server supports basic authentication only, and not OAuth2. User that has access to `/token` endpoint is:
```
username: amina
password: mysecret
```
## Requirements

- python3

## How to run

1. Clone this repo
```
git clone https://github.com/asljivo1/BasicHTTPServer.git
```
2. Navigate to `BasicHTTPServer` directory
```
cd BasicHTTPServer
```
3. Start the HTTP server on http://localhost:8080
```
python3 basic_http_server.py
```
4. In a web browser, navigate to http://localhost:8080/token
5. You will be asked to enter user credentials. Enter the credentials listed above.
