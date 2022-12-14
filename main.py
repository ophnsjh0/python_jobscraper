from flask import Flask, render_template, request, redirect, send_file
from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.jobkorea import extract_jobkorea_jobs
from extractor.file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobkorea = extract_jobkorea_jobs(keyword)
        jobs = jobkorea + indeed + wwr
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    print(keyword)
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), {"Refresh": "2; url=/"}


app.run("127.0.0.1")
