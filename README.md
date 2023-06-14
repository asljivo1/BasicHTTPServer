# Basic HTTP Server

This HTTP server authorizes users via GitHub OAuth App. 

## Requirements

- python3
- GitHub account

## How to run

1. Set environment variables CLIENT_ID and CLIENT_SECRET

```
export CLIENT_ID='94e7c973ecaeb3068218'
export CLIENT_SECRET='279a8158f650e7b980b3bb2df11fe5fceb1061da'
```
To set the environment variables temporarily for the duration of the terminal session, you can do the two exports in a terminal.

To set the environment variables permanently, paste the two lines to ~/.bashrc and reload it with `source ~/.bashrc`

2. Clone this repo
```
git clone https://github.com/asljivo1/BasicHTTPServer.git
```
3. Navigate to `BasicHTTPServer` directory
```
cd BasicHTTPServer
```
4. Start the HTTP server on http://localhost:8080
```
python3 basic_http_server.py
```
5. In a web browser, navigate to http://localhost:8080/token
You will be redirected to GitHub where you should log in with your credentials, and you will get authorized.