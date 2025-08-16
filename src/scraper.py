# src/scraper.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def scrape_internshala(job_type, location, category):
    # Configure Selenium for headless operation
    options = Options()
    options.add_argument("--headless=new")  # Use new headless mode for recent ChromeDriver
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)

    search_type = 'internships' if job_type.lower() == 'internship' else 'jobs'
    url = f"https://internshala.com/{search_type}/{location.lower()}/"
    driver.get(url)
    time.sleep(3)  # Let page fully load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Find relevant job/internship cards (these classes may change if Internshala updates their site)
    if job_type.lower() == 'internship':
        cards = soup.find_all('div', class_='individual_internship')
    else:
        cards = soup.find_all('div', class_='container-fluid individual_job')

    listings = []
    for card in cards:
        title_tag = card.find('a', class_='profile')
        company_tag = card.find('a', class_='link_display_like_text')
        if title_tag and company_tag:
            title = title_tag.text.strip()
            company = company_tag.text.strip()
            # Filter by category keyword in title
            if category.lower() in title.lower():
                listings.append({'Title': title, 'Company': company})

    return pd.DataFrame(listings)