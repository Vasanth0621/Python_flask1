from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('register.html')
@app.route("/submit",methods=['POST'])
def suubmit():
    name = request.form['name']
    email = request.form['email']
    return redirect(url_for('success',name=name, email=email))
@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    return f"Form submitted successfully!<br>Name:"


if __name__ =="__main__":
    app.run(debug=True)        

