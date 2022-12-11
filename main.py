from flask import Flask, render_template, request
from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.jobkorea import extract_jobkorea_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name='shin')


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobkorea = extract_jobkorea_jobs(keyword)
    jobs = jobkorea + indeed + wwr

    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("127.0.0.1")
