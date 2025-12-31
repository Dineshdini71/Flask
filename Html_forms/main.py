from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def data_received():
    username = request.form['username']
    passw = request.form['password']
    return render_template('login.html', name=username, password=passw)

if __name__ == '__main__':
    app.run(debug=True, port=5001)