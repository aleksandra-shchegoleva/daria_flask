from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'fseffesfsfsefs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/', methods=['POST', "GET"])
def main():
    products = Product.query.all()
    return render_template("main.html", products=products)
    
@app.route('/form', methods=['POST', 'GET'])
def form():
    return render_template("form.html")

with app.app_context():
    db.create_all()
    product = Product(name='Стул', price=1.4)
    db.session.add(product)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)