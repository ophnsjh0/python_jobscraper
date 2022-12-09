from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.jobkorea import extract_jobkorea_jobs

keyword = input("Enter a job to search for : ")

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