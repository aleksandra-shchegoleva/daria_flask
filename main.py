from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template("main.html")

@app.route("/products/<name>")
def products(name):
    return f"Hello {name}"

@app.route('/<name>')
def product(name):
    if name == 'main':
        return redirect(url_for('main'))
    else:
        return redirect(url_for('products', name=name))
    
@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        result = request.form
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)