import sys
from flask import Flask, render_template
import psutil

app = Flask(__name__)

plat = sys.platform

memory = psutil.virtual_memory().percent

from bs4 import BeautifulSoup
from urllib2 import urlopen

a = urlopen('http://www.betplus355.com/sports/')

source = a.read()

soup = BeautifulSoup(source)

'''
for i in soup.findAll('a'):
    print i.text
'''
#odds = soup.findAll('span', attrs={'class':'num_right'})


@app.route("/", methods= ['GET'])
def home():
    return render_template('index.html', platform=plat, memory=memory )

if __name__ == "__main__":
    app.run()
