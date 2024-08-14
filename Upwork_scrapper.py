import pandas as pd
from bs4 import BeautifulSoup
import requests 
import undetected_chromedriver as uc
import time
def upworkjobs(search , page_no, driver):
  job = search.split()
  new_job = '%20'.join(job)
  title = []
  link = []
  desc = []
  details = []
  url = f'https://www.upwork.com/nx/search/jobs/?page={page_no}&q={new_job}&sort=recency'
  driver.get(url = url)
  soup = BeautifulSoup(driver.page_source,'html.parser')  
  x = soup.find_all('article')
  for h in x:
    title.append(h.a.get_text())
    link.append('https://www.upwork.com'+h.a.get('href'))
    desc.append(h.find('p', class_ = 'mb-0').get_text())
    details.append(h.ul.text)
  return title,link,desc,details
  
  

if __name__ == '__main__':
  search = input('enter work to search for: ') 
  number_of_pages = int(input('enter numer of pages: '))
  headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language": "en-US,en;q=0.5",
  "Accept-Encoding": "gzip, deflate",
  "DNT": "1",
  "Connection": "close",
  "Upgrade-Insecure-Requests": "1"}
  
  options = uc.ChromeOptions()
  options.add_argument('--headless')
  
  for i,j in headers.items():
    options.add_argument(f'--{i}={j}')
    
  driver = uc.Chrome(options=options)
  
  title = []
  link = []
  desc = []
  details = []
  for i in range(1,number_of_pages+1):
    all_data = upworkjobs(search, i,driver)
    title.extend(all_data[0])
    link.extend(all_data[1])
    desc.extend(all_data[2])
    details.extend(all_data[3])

  driver.quit()
  data = pd.DataFrame({'Title': title, 'Description': desc, 'Details': details  ,'Link': link })
  data.index = data.index + 1
  data.to_csv(r'C:\Users\omars\OneDrive\Desktop\scrappers\Scrapper_upwork1.csv')
  print(data)