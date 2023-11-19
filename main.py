from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOGS_API = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    response = requests.get(BLOGS_API)
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def get_posts(post_id):
    response = requests.get(BLOGS_API)
    posts = response.json()
    return render_template("post.html", post_id=post_id, posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
