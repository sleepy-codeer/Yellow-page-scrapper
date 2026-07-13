B2B Lead Generation Scraper (AJAX & Session Handling) 



📌 Project Overview

This project is an automated data extraction pipeline designed to scrape business-to-business (B2B) leads from dynamic directory
YellowPages. The project scrapes recruitment agencies in Delhi, it scrapes the agencie's about section, name, address and the website
from the YellowPages - directory that lists businesses, services, and professionals grouped by category. 

It bypasses frontend UI limitations by intercepting backend AJAX requests, ensuring high-speed, structured data extraction.

This tool is ideal Business who wants to bulk hire employee and doesn't have resources to do by themselves This gets them 
recruitment agencies data at scale without manually clicking through hundreds of pages.

⚙️ Technical Highlights

AJAX Interception: Bypasses heavy HTML/ad rendering by targeting the raw backend data endpoints.

Session Management: Utilizes requests.Session() to maintain cookies and prevent bot-detection during pagination.

Defensive Parsing: Implements graceful fallbacks (try/except) for missing data fields (e.g., missing websites or addresses) to guarantee zero script crashes during long-running extractions.

recruiters_dir.csv file, and the README.md I provided.Data Structuring: Outputs cleanly formatted Pandas DataFrames to CSV, automatically handling nested commas and unstructured text blocks.

🛠️ Tech Stack

Python 3.x

BeautifulSoup4 (DOM Parsing)

Requests (HTTP & Session management)

Pandas (Data structuring and export)

📊 Data Extracted

***
The pipeline currently extracts the following data points into a clean CSV:

Company Name
Address / Location
About / Company Description
Direct Corporate Website
***

🚀 Usage

# 1. Clone the repository
git clone [https://github.com/YourUsername/b2b-directory-scraper.git](https://github.com/YourUsername/b2b-directory-scraper.git)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python yellowpages_scraper.py



⚠️ Disclaimer

This script is strictly for educational purposes and portfolio demonstration. Web scraping should always be done in compliance with a website's robots.txt and Terms of Service.