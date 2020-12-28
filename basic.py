from flask import Flask, redirect, render_template, request, url_for
from flask_moment import Moment

app = Flask(__name__)

comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("example.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

#https://blog.pythonanywhere.com/121/
