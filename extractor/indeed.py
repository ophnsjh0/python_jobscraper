from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from extractor.wwr import extract_wwr_jobs
# jobs = extract_wwr_jobs("python")
# print(jobs)


def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome('./chromedriver.exe')
    browser.get(f"{base_url}{keyword}")
    response = browser.page_source
    soup = BeautifulSoup(response, "html.parser")
    pagenation = soup.find('nav', class_="css-jbuxu0 ecydgvn0")
    if pagenation == None:
        return 1
    pages = pagenation.find_all("div", class_="css-tvvxwd ecydgvn1")
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


# get_page_count("python")


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)

    result = []
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        # print("page_num", page)
        # print(final_url)
        browser.get(final_url)
        response = browser.page_source

        soup = BeautifulSoup(response, "html.parser")
        job_list = soup.find('ul', class_="jobsearch-ResultsList css-0")
        jobs = job_list.find_all("li", recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find('span', class_="companyName").string
                location = job.find('div', class_="companyLocation").string
                job_data = {
                    "company": company.replace(',', ' '),
                    "location": location.replace(',', ' '),
                    "position": title.replace(',', ' '),
                    "link": f"https://www.indeed.com{link}"
                }
                result.append(job_data)
    return result
