from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs

keyword = input("Enter a job to search for : ")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

file = open(f'{keyword}.csv', 'w', encoding='utf-8')
file.write("Position, Company, Location, URL\n")

for job in jobs:
    file.write(
        f'{job["position"]},{job["company"]},{job["location"]},{job["link"]}\n'
    )
print(len(jobs))
