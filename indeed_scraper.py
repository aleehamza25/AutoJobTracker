from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_indeed_jobs(query, location):
    driver = webdriver.Chrome()
    driver.get(f"https://www.indeed.com/jobs?q={query}&l={location}")
    time.sleep(3)
    jobs = []
    for job_card in driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')[:10]:
        title = job_card.find_element(By.CLASS_NAME, 'jobTitle').text
        company = job_card.find_element(By.CLASS_NAME, 'companyName').text
        location = job_card.find_element(By.CLASS_NAME, 'companyLocation').text
        jobs.append({'title': title, 'company': company, 'location': location})
    driver.quit()
    return jobs