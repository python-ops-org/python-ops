from flask import Flask, render_template
app = Flask(__name__)
@app.route('/helo/<user>')
def page(user):
    return render_template('hello-1.html', name = user)
if __name__ == '__main__':
    app.run(debug=True)    
