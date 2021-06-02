from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
   return render_template("hello.html")

@app.route('/welcome/<name>')
def welcome(name):
   return render_template("welcome.html", name=name)

@app.route("/name")
def print_name():
    name = "Aayush"
    return name

@app.route("/sum", methods = ['GET'])
def add_number():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return str(c)

@app.route('/user-data', methods=['POST'])
def user_data():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        #dict = {'fname':first_name,'lname':last_name}
        result =  '''
            <h1>First name: {}</h1>
            <h1>Last name: {}</h1>
        
        '''
    return result.format(first_name, last_name)
    #return dict


@app.route('/user')
def user_form():
    return '''
    <form method="POST" action="http://127.0.0.1:5000/user-data">
           <div><label>First Name: <input type="text" name="fname"></label></div>
           <div><label>Last Name: <input type="text" name="lname"></label></div>
           <input type="submit" value="Submit">
    </form>
    '''


if __name__ == '__main__':
    app.run()


