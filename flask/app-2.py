from flask import Flask , redirect , url_for ,request
app=Flask(__name__)

@app.route('/blog/<name>')

def blog(name):
    return "welcome %s" % name
#app.add_url_rule('/blog/<name>' , 'blog' , blog)
#app.add_url_rule('/login' , methods = [ 'GET','POST'])

@app.route('/login',methods = ['POST', 'GET'])

def login():
    if request.method == 'POST':
       user = request.form['nm']
       return redirect(url_for('blog', name=user))
    else:
       user = request.args.get['nm']
       return redirect(url_for('blog', name=user))

if __name__ == '__main__':
   app.run(debug=True)

