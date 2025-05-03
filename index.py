from bs4 import BeautifulSoup
import requests
import time
unfamilier_skill = input('Enter an skill that you are unfamilier: ')
print('Filtering out..')

def find_jobs():
    html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&cboWorkExp1=0&txtLocation=').text

    soup = BeautifulSoup(html_file, 'lxml')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):

        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('div', class_ = 'srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        skills = ', '.join(skills.split())
        if unfamilier_skill not in skills:
            with open(f"post/{index}.txt", 'w') as f:
                f.write(f"COMPANY NAME: {company_name} \n")
                f.write(f"REQUIRED SKILLS: {skills} \n")
                f.write(f"MORE INFO: {more_info}")
            print(f"File saved {index}!")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)