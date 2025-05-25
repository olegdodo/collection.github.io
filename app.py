from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///giftscoll.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    text = db.Column(db.Text, nullable = False)


@app.route('/')
def index():
    global likes_count
    return render_template('posts.html', likes=likes_count)

likes_count = 0

@app.route('/like', methods=['POST'])
def like():
    global likes_count
    likes_count += 1
    return jsonify({'likes': likes_count})

@app.route("/top")
def top():
    return render_template('top.html')


@app.route("/favorite")
def favorite():
    return render_template('favorite.html')


if __name__ == '__main__':
    app.run(debug=True)