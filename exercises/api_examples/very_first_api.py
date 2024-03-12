'''
IMPORTANT:

We will be using Flask to create our very first API in python. 

Flask is a microweb framework for Python. Flask is popular for creating APIs and web development.
Of course there is so much to Flask, we could spend days studying it. But for the purpose of this
exercise, we will utilize to create a very simple API.

To install Flask framework to utilize in our Python file we do the following command in our VsCode terminal

pip install flask


From here the syntax will look odd at first since now we are starting to get in the stage of intermediate programming.
All code will be documented to the best of my ability to ensure everything makes sense. 
However never forget rule #1 of programming, make google your best friend!

Let's get started.
'''


# importing 3 modules from flask framework.
#Flask - the main Flask class that allows you to create a web app
#request - provides access to incoming request data
#jsonify - a function that converts Python dictionaries or lists into JSON format for HTTP responses
from flask import Flask, request, jsonify

# creating our web app object
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Home Page"

if __name__ == "__very_first_api__":
    web_app.run(debug=True)

#adding something new

