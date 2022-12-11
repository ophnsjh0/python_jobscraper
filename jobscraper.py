from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.jobkorea import extract_jobkorea_jobs
from extractor.file import save_to_file

keyword = input("Enter a job to search for : ")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobkorea = extract_jobkorea_jobs(keyword)

jobs = jobkorea + indeed + wwr

save_to_file(keyword, jobs)
