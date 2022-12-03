import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By




skill=input('Enter your work domain: ')

location=input('Enter your preferred location for work: ')


op=webdriver.ChromeOptions()
op.add_argument('headless')
#insert the location of your driver.exe here
driver = webdriver.Chrome('Address goes here',options=op)
driver.get('https://www.timesjobs.com/')
time.sleep(5)

skillInput=driver.find_element(By.NAME,'txtKeywords')
LocInput=driver.find_element(By.NAME,'txtLocation')

skillInput.send_keys(skill)
LocInput.send_keys(location)

driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[1]/form/button').click()
requrl=driver.current_url
driver.quit()

def find_jobs(url,skillName):
    html_text=requests.get(url).text
    soup=BeautifulSoup(html_text,'lxml')

    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    iter=1
    # print(job)
    with open(f'jobs/jobinfo{skillName}.txt','w') as f:

        for job in jobs:
            job_published_date=job.find('span',class_='sim-posted').text
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            comp_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')   #finds job name tags from inside the particular job card only
            link=job.header.h2.a['href']
            f.write(f'{iter} :\n')
            f.write(f'Company Name:{comp_name.strip()} \n')
            f.write(f'Skills Required:{skills.strip()} \n')
            f.write(f'Date Posted:{job_published_date.strip()} \n')
            f.write(f'Link : {link} \n \n')
            iter+=1   

find_jobs(requrl,skill)










