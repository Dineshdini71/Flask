from flask import Flask, render_template
import random
from datetime import datetime
import requests

requests.get('https://api.agify.io')

dt = datetime.now().year
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1 ,10)
    return render_template("index.html", number=random_number, date=dt)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_resp = requests.get(gender_url)
    gender_data = gender_resp.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_resp = requests.get(age_url)
    age_data = age_resp.json()
    age = age_data["age"]
    return render_template("name.html", nm=name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_resp = requests.get(blog_url)
    all_post = blog_resp.json()
    return render_template("Blog.html", posts=all_post)


if __name__ == '__main__':
    app.run(debug=True)