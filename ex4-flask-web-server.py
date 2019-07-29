# Flask is a python framework for running a web application
# https://en.wikipedia.org/wiki/Flask_(web_framework)

# Import the flask library; this gives us a web server which
# we can connect to and view our website/web application
from flask import Flask

# Setup the app variable for flask
app = Flask(__name__)


# This sets up a path so when we navigate to our flask
# server (http://localhost:5000 from further down),
# we get the HTML document we define below
@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>This is a Flask app!</title>
        </head>
        <body style="background-color: LightSkyBlue;">
            <h1>Hello Ladies Learning Code!</h1>
            <p>Welcome to Flask running on Python!</p>
            <p>You can learn more about flask by clicking 
                <a href="https://en.wikipedia.org/wiki/Flask_(web_framework)">here</a>
            </p>
        </body>
        </html>
    '''


# Flask runs it's server on localhost with a default
# port of 5000
# http://localhost:5000
if __name__ == '__main__':
    app.run(host='localhost')
