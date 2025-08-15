# src/scraper.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from src.config import INTERN_SHALA_BASE_URL

def scrape_internshala(job_type, location, category):
    options = Options()
    options.headless = True  # Run browser in headless mode for efficiency
    driver = webdriver.Chrome(options=options)  # Ensure chromedriver is installed and in PATH

    search_type = 'internships' if job_type.lower() == 'internship' else 'jobs'
    url = f"{INTERN_SHALA_BASE_URL}/{search_type}/{location.lower()}/"
    driver.get(url)

    time.sleep(3)  # Wait for the page to load completely

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Select cards containing job/internship postings
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
            # Filter results by category keyword
            if category.lower() in title.lower():
                listings.append({'Title': title, 'Company': company})

    return pd.DataFrame(listings)
