from flask import Flask, render_template
import requests
# from blog import Blog

blog_url = "https://api.npoint.io/955c1e57d6bfa98e22ae"
blog_ = requests.get(blog_url)
blog_res = blog_.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs = blog_res)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in blog_res:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", num=requested_post)

if __name__ == '__main__':
    app.run(debug=True)