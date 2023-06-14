# Basic HTTP Server

This HTTP server authorizes users via GitHub OAuth App. 

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
You will be redirected to GitHub where you should log in with your credentials, and you will get authorized.
