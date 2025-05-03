from bs4 import BeautifulSoup
import requests
import lxml

with open('index.html','r') as html_file:
    content = html_file.read()
   
    soup = BeautifulSoup(content, 'lxml')

    course_card = soup.find_all('div')
    for course in course_card:
        course_name = course.h5.text
        course_cost = course.a.text

        print(f"{course_name} costs {course_cost}")

    # course_title_tag = soup.find_all('h5')

    # for course in course_title_tag:
    #     print(course.text)