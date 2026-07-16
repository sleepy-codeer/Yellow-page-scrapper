import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 
import time

def get_contact_info(url): 

    user = None 
    address = None
    site = None 

    try:
        res = requests.get(url=url, timeout=10)
        
        if res.status_code != 200:
            return user, address, site 
            
        parser = bs(res.content, 'html.parser')
        ul = parser.find('ul', class_="fa-ul pd-ci-list")
        
        if not ul:
            return user, address, site 
            
        list_items = ul.find_all('li')
        
        for li in list_items:
            link = li.find('a', href=True)
            if link:
                site = link['href']
            else:
                text = li.get_text(strip=True)
         
                if len(text) > 25 or "Delhi" in text or "Floor" in text:
                    address = text
                else:
                    user = text
                    
    except Exception as e:
        print(f"Error scraping {url}: {e}")

    return user, address, site


page = 1
RECRUITERS_DIRECTORY = []

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

print("Starting Scrape...")

while page <= 3:
    print(f"Fetching Page {page}...")
    API = f"https://www.indianyellowpages.com/delhi/job-recruitment-consultants.htm?pageno={page}&action=ajax_load_classified"

    response = session.get(url=API)

    if response.status_code != 200: 
        print("Failed to fetch page. Exiting.")
        break
    
    soup = bs(response.content, 'html.parser')

    caution = soup.find('p', class_="ttgbot")
    if caution:
        print("Reached the end of the directory.")
        break
    
    recruiters = soup.find('li')
    if not recruiters:
        break
        
    recruiters = [recruiters] + recruiters.find_next_siblings()
        
    for rec in recruiters:
        desc_div = rec.find("div", class_="pdp_service_info")
        service_div = rec.find("div", class_="serv_com_sec")

        if not desc_div or not service_div:
            continue

        desc = desc_div.get_text(strip=True)

        link = service_div.find("a", href=True)
        if not link:
            continue

        url = link["href"]
        user, address, site = get_contact_info(url=url)


        RECRUITERS_DIRECTORY.append({
            "Company Name": user, 
            "Address": address, 
            "About": desc, 
            "Website": site
        })
    
    time.sleep(1.4)
    page += 1

print("\nScrape Complete! Exporting to CSV...")
table = pd.DataFrame(RECRUITERS_DIRECTORY)
table.to_csv('recruiters_dir.csv', index=False)

print("Data successfully saved to recruiters_dir.csv!")
