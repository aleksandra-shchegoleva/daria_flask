from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST', "GET"])
def main():
    if request.method == 'POST':
        result = request.form
        return render_template("main.html", result=result)
    return render_template("main.html", result=[])
    
@app.route('/form', methods=['POST', 'GET'])
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)