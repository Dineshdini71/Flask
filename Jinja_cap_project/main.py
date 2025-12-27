from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(blog_url).json()

post_object = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_object.append(post_obj)

app = Flask(__name__)

@app.route('/')
def get_allpost():
    return render_template("index.html", all_post=post_object)

@app.route('/post/<int:index>')
def show_post(index):
    request_post = None
    for blog_post in post_object:
        if blog_post.id == {index}:
            request_post = blog_post
    return render_template("index.html", post=request_post)

if __name__ == "__main__":
    app.run(debug=True)
