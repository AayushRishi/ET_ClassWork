# Add module here using import
import greetings
#from greetings import hello
import utils
#from utils import hello

# Added by Pritesh Patel
import datetime

from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/student")
def students():
    return greetings.student1

@app.route("/hello")
def hello():
    res = greetings.hello() + " **** " + utils.print_hi("Pritesh Patel")
    return res

@app.route("/date")
def today():
    return '<h1>' + str(datetime.datetime.now()) + '</h1>'

if __name__ == '__main__':

    app.run()

    utils.print_hi('PyCharm')
    utils.hello()
    greetings.hello()

    print(greetings.student1)
    print(greetings.student1["first_name"])

    #Date Handling
    today = datetime.date.today()
    print(today)
    year = datetime.date.today().year
    print(year)
    print(today.month)
    today = datetime.datetime.now()
    print(today)

