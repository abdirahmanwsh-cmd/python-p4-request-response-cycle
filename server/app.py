#!/usr/bin/env python3

import os
# Used to get the absolute path of the application

from flask import Flask, request, current_app, g, make_response
# Flask core objects:
# request → holds incoming HTTP request data
# current_app → refers to the active Flask app
# g → stores data during a single request
# make_response → builds a response object

# Create the Flask application instance
app = Flask(__name__)


# Before Request Hook
# This runs BEFORE every request
# It stores the application path in the g object
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())


# Index Route
# Handles requests to "/"
@app.route('/')
def index():
    # Get the Host header from the request
    host = request.headers.get('Host')

    # Get the application name
    appname = current_app.name

    # HTML response body
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    # HTTP status code
    status_code = 200

    # headers dictionary
    headers = {}

    # Return a proper Flask response object
    return make_response(response_body, status_code, headers)


if __name__ == '__main__':
    app.run(port=5555, debug=True)