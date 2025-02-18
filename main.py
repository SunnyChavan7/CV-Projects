# Integrate HTML with Flask
# HTTP verb GET and POST

# Jinja2 template engine
'''
{{ }} expression to print output from the route decorator
{%....%} conditional statements
{#...#} for comments
'''

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/result/<int:score>')
def result(score):
     result = ''
     if score>=35:
          result = 'PASS'
     else:
          result = 'FAIL'
     return render_template('result.html', result = result, total_score=str(score))

@app.route('/submit', methods=['GET', 'POST'])
def submit():
     if request.method == 'POST':
          physics = float(request.form['physics'])
          chemistry = float(request.form['chemistry'])
          maths = float(request.form['maths'])
          score = (physics+chemistry+maths)/3
     return redirect(url_for('result', score = score))

if __name__ == '__main__':
     app.run(debug=True)
