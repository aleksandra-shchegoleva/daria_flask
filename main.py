from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'fseffesfsfsefs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/', methods=['POST', "GET"])
def main():
    
    
@app.route('/form', methods=['POST', 'GET'])
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)