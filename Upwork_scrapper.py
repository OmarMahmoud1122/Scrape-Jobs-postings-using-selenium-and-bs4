import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

xx = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language": "en-US,en;q=0.5",
  "Accept-Encoding": "gzip, deflate",
  "DNT": "1",
  "Connection": "close",
  "Upgrade-Insecure-Requests": "1"
}
def upworkjobs(job_title, no_of_pages):
    job = job_title.split()
    new_job = '%20'.join(job)
    title = []
    link = []
    desc = []
    details = []
    pages = no_of_pages
    for i in range(1,pages+1):
        
        website = requests.get(f'https://www.upwork.com/nx/search/jobs/?page={i}&q={new_job}&sort=recency', headers= xx)
        soup = BeautifulSoup(website.text,'html.parser')
        
        x = soup.find_all('article')
        for h in x:
            title.append(h.a.get_text())
            link.append('https://www.upwork.com'+h.a.get('href'))
            desc.append(h.find('p', class_ = 'mb-0').get_text())
            details.append(h.ul.text)
    
    data = pd.DataFrame({'Title': title, 'Description': desc, 'Details': details  ,'Link': link })
    return data
    
yy = upworkjobs('data', 2)
yy.to_csv(r'C:\Users\omars\OneDrive\Desktop\upworkjobs.csv')
