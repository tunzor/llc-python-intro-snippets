# Flask is a python framework for running a web application
# https://en.wikipedia.org/wiki/Flask_(web_framework)

# Import the flask library; this gives us a web server which
# we can connect to and view our website/web application
from flask import Flask
# This allows us to access date and time functions
import datetime

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
            <h3>Today is <span style="color: Firebrick;">{}</span> 
                and the current time is <span style="color: Firebrick;">{}</span></h3>
            <p>Welcome to Flask running on Python!</p>
            <p>You can learn more about flask by clicking 
                <a href="https://en.wikipedia.org/wiki/Flask_(web_framework)">here</a>
            </p>
        </body>
        </html>
    '''.format(datetime.datetime.now().strftime('%B %d, %Y'), datetime.datetime.now().strftime('%H:%M:%S'))
# datetime.datetime.now().strftime('%B %d %Y') gets the current date/time
# and formats it as MONTH DAY, YEAR (eg. July 25, 2019);
# datetime.datetime.now().strftime('%H:%M:%S') formats the time as HH:MM:SS (eg.12:01:11)

# The format function used above takes the formatted date and substitutes it
# in for the first occurrence of the curly braces {} on this line:
# <h3>Today is <span style="color: Firebrick;">{}</span>
# and does the same for the second part for the time as 12:01:22 here:
# the current time is <span style="color: Firebrick;">{}</span></h3>


# Flask runs it's server on localhost with a default
# port of 5000
# http://localhost:5000
if __name__ == '__main__':
    app.run(host='localhost')
