from flask import Flask, render_template
"""
app = Flask(__name__)
@app.route('/') 
def index():
    return '<html><body><h1>hello world</h1></body></html>'
if __name__ == '__main__':
   app.run(debug = True) 
"""
"""
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('hello.html')
if __name__ == '__main__':
    app.run(debug=True)       
"""

    
    