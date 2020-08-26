#https://www.javatpoint.com/flask-app-routing
#https://overiq.com/flask-101/flask-basics/

from flask import Flask
app = Flask(__name__)

"""
#@app.route('/')
def hello(name):
    return "Hello %s" % name
#app.add_url_rule('/helo', 'helo', hello)
app.add_url_rule('/helo/<name>', 'helo', hello)
if __name__ == '__main__':
   app.run(debug=True)
"""
#def blog(post):
def blog(rv):    
#    return "blog number %d" % post
    return "blog number %f" % rv
#app.add_url_rule('/blog/<int:post>', 'blog', blog)
app.add_url_rule('/rev/<float:rv>', 'blog' , blog)
if __name__ == '__main__':
    app.run()



