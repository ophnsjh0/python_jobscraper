from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name='shin')


@app.route("/search")
def search():
    return render_template("search.html")


app.run("127.0.0.1")
