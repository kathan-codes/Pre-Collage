from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

## This program works better with proxies

def get_job(num):
    number = int(num)
    all_job_data = []
    print("🤖 Launching automated browser...")
    driver = webdriver.Chrome() 
    driver.implicitly_wait(5)
    try:
        for i in range(1,number+1):
            print(f"\n🌐 Fetching Data From Category Page {i}...")            
            url = f"https://weworkremotely.com/remote-jobs/search?search_uuid=&sort=&term=&categories_chosen=&categories%5B%5D={i}&countries_chosen=&chosen-salary_range=&skills_chosen="
            driver.get(url)
            time.sleep(2)
            job_cards = driver.find_elements(By.CLASS_NAME, "new-listing-container")
            print(f"📊 Found {len(job_cards)} job cards on page {i}")
            for card in job_cards:
                try:
                    title_el = card.find_elements(By.CLASS_NAME, "new-listing__header__title__text")
                    company_el = card.find_elements(By.CLASS_NAME, "new-listing__company-name")
                    location_el = card.find_elements(By.CLASS_NAME, "new-listing__company-headquarters")
                    link_el = card.find_elements(By.TAG_NAME, "a")
                    title = title_el[0].text.strip() if title_el else "Unknown Title"
                    company = company_el[0].text.strip() if company_el else "Unknown Company"
                    location = location_el[0].text.strip() if location_el else "Remote"
                    link = link_el[0].get_attribute("href") if link_el else "No Link"
                    all_job_data.append({
                            "Job Title": title,
                            "Company": company,
                            "Location": location,
                            "Link": link
                        })    
                except Exception as e:
                    # Skips a corrupted card row without crashing the whole process
                    continue
                
    except Exception as main_error:
        print(f"❌ Critical automation error: {main_error}")
        
    finally:
        print("\n🔌 Closing automated browser window...")
        driver.quit()   
    if all_job_data:
        print("📊 Processing consolidated database...")
        df = pd.DataFrame(all_job_data)
        output_path = "Day03_04_Automated_Job_Scraper/Master_Remote_Jobs.xlsx"
        
        df.to_excel(output_path, index=False)
        print(f"🎉 Success! Exported {len(all_job_data)} total jobs to {output_path}")
    else:
        print("⚠️ No data was collected.")

if __name__ == "__main__":
    get_job(11)