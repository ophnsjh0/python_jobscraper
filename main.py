<<<<<<< HEAD
from flask import Flask, render_template
=======
from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.jobkorea import extract_jobkorea_jobs
>>>>>>> 80c1a3fd07ea247a44327e9078160d4793fbb804

app = Flask("JobScrapper")

<<<<<<< HEAD

@app.route("/")
def home():
    return render_template("home.html", name='shin')


@app.route("/search")
def search():
    return render_template("search.html")


app.run("127.0.0.1")
=======
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobkorea = extract_jobkorea_jobs(keyword)
jobs = jobkorea + indeed + wwr
       
file = open(f'{keyword}.csv', 'w', encoding='cp949')
file.write("Company, Position, Location, URL\n")

for job in jobs:
    file.write(
        f'{job["company"]},{job["position"]},{job["location"]},{job["link"]}\n'
    )
>>>>>>> 80c1a3fd07ea247a44327e9078160d4793fbb804
