from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__,
            static_folder='static',
            template_folder='Templates')
app.config["MONGO_URI"] = "mongodb+srv://Mattia:Ettore22@cluster-cp8xp.gcp.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

app.secret_key = 'dinesh richard gilfoyle'



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def Login():
    error = None
    if request.method == 'POST':
        user = users.find_one({'email' : request.form['email']})
        if user['password'] != request.form['password'].encode('utf-8'):
            error = 'Email o password errata.'
        else:
            session['logged_in'] = True
            return redirect(url_for('Results.html'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email' : request.form['email']})#sostituire con la mail

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'email' : request.form['email'], 'password' : hashpass})
            session['email'] = request.form['email']
            return redirect(url_for('Q1.html'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route("/Privacy")
def privacy():
    return render_template("Privacy.html")

@app.route("/Q1")
def Q1():
    return render_template("Q1.html")
@app.route("/Q2")
def Q2():
    return render_template("Q2.html")
@app.route("/Q3")
def Q3():
    return render_template("Q3.html")
@app.route("/Q4")
def Q4():
    return render_template("Q4.html")
@app.route("/Q5")
def Q5():
    return render_template("Q5.html")
@app.route("/Q6")
def Q6():
    return render_template("Q6.html")
@app.route("/Q7")
def Q7():
    return render_template("Q7.html")
@app.route("/Q8")
def Q8():
    return render_template("Q8.html")
@app.route("/Q9")
def Q9():
    return render_template("Q9.html")
@app.route("/Q10")
def Q10():
    return render_template("Q10.html")

@app.route("/Results")
def Results():
    return render_template("array-table.html")

if __name__=="__main__":
    app.run(debug=True)


#Cose da fare:
#implementare algoritmo
#attaccare il database al register
#creare pagina matchati:
    #nome
    #cognome
    #classe
