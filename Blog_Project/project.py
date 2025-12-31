from flask import Flask, render_template, request
from datetime import datetime
import requests
import smtplib as st
import os
from dotenv import load_dotenv

load_dotenv()
blog_pass = os.environ.get('blog_post')
current_year = datetime.now().year
blog_url = "https://api.npoint.io/955c1e57d6bfa98e22ae"
blog_ = requests.get(blog_url)
blog_res = blog_.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs = blog_res, year=current_year)
@app.route("/about")
def about():
    return render_template("about.html", year=current_year)

@app.route("/login", methods=['POST', 'GET'])
def data_received():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        ph = request.form["phone"]
        password = blog_pass
        my_mail = "awsdineshdini@gmail.com"
        with st.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=my_mail, password=password)
            connect.sendmail(
                from_addr=my_mail,
                to_addrs= email,
                msg= message
            )
        return render_template("login.html", name=name, email=email, mssg=message, phone=ph , msg_sent=True, )
    return render_template("login.html", msg_sent=False, year=current_year)

@app.route("/contact")
def contact():
    return render_template("contact.html", year=current_year)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in blog_res:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", num=requested_post, year=current_year)

if __name__ == '__main__':
    app.run(debug=True)