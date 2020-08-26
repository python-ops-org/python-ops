from flask import Flask, render_template

app = Flask(__name__)
@app.route('/result')
def page():
    dict = {'che':70,'phy':80,'math':90}
    return render_template('result.html', result=dict)

if __name__ == '__main__':
    app.run(debug=True)    
