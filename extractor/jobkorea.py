from requests import get
from bs4 import BeautifulSoup

def get_page_count(keyword):
    base_url = "https://www.jobkorea.co.kr/Search/?stext="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        total_find = soup.find('div', class_='list-filter-wrap-text')
        total_str = soup.find('strong', class_='dev_tot').string
        total_num = total_str.replace(',', "")
        page_num = round(int(total_num) / 20)
        if page_num >= 15:
            return 15
        else: 
            return page_num


def extract_jobkorea_jobs(keyword):
    pages = get_page_count(keyword)
    print(pages)
    results = []
    for page in range(pages):
        print(page)
        base_url = "https://www.jobkorea.co.kr/Search/?stext="
        final_url = f"{base_url}{keyword}&Page_No={page+1}"
        response = get(final_url)
        print("page_num", page)
        print(final_url)
        if response.status_code != 200:
            print("Can't request website")
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            job_list = soup.find('div', class_='list-default')
            jobs = job_list.find_all('li', class_='list-post')         
            for job in jobs:
                job_name_list = job.find('a', class_="name dev_view")
                job_name = job_name_list['title']
                location = job.find('span', class_="loc long").string
                position_list = job.find('a', class_="title dev_view")
                position = position_list['title']
                link = position_list['href']
                job_data = {
                                'company': job_name.replace(',', ' '),
                                'location': location.replace(',', ' '),
                                'position': position.replace(',', ' '),
                                'link': f"https://www.jobkorea.co.kr{link}"
                            }
                results.append(job_data)
    return results





