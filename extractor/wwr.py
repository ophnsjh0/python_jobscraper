from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="

    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('section', class_="jobs")
        results = []
        for jobs_section in jobs:
            jobs_posts = jobs_section.find_all('li')
            jobs_posts.pop(-1)
            for post in jobs_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                companys = anchor.find_all('span', class_="company")
                company = companys[0]
                region = anchor.find('span', class_="region company")
                title = anchor.find('span', class_='title')
                job_data = {
                    'company': company.string.replace(',', ' '),
                    'location': region.string.replace(',', ' '),
                    'position': title.string.replace(',', ' '),
                    'link': f"https://weworkremotely.com{link}"
                }
                results.append(job_data)

        return results
