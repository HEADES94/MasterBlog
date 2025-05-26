from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Hilfsfunktion zum Laden der Posts
def load_posts():
    with open('posts.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
