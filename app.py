from flask import Flask, redirect, url_for

# WSGI Application : A WSGI (Web Server Gateway Interface) application is a Python application that interfaces with a WSGI-compatible web server to handle HTTP requests.
app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
     return "Hello World!"

# Building dynamic URL

@app.route('/success/<int:score>') # by default string
# while testing => http://127.0.0.1:5000/success/55
def success(score): # retrieve the score 
     return f"Th person passed and the score is {str(score)}"

@app.route('/failure/<int:score>')
def failure(score):
     return f"The person has failed and the score is {str(score)}"

@app.route('/result/<int:marks>')
def result(marks):
     result = ""
     if marks<35:
          result = "failure"
     else:
          result = "success"
     return redirect(url_for(result, score=marks))


if __name__=='__main__':
     app.run() # no need to again launch the app