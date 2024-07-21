import pandas as pd
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
urls = []
img = []
Name = []
commonName = []
sciName = []
about = []
family = []
audio = []

def is_page_loaded():
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  
    new_height = driver.execute_script("return document.body.scrollHeight")
    return new_height > last_height

def scrape(link):
    driver = webdriver.Chrome()
    driver.get(link)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "audio"))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        images = soup.find_all('img')
        img.append(images[1]['src'])
        Name.append(images[1]['alt'])
        info = soup.find('div', class_='w-full mb-6')
        text = info.text.splitlines()
        commonName.append(text[2] if len(text) > 2 else '')
        sciName.append(text[11] if len(text) > 11 else '')
        about.append(text[15] if len(text) > 15 else '')
        family.append(text[24] if len(text) > 24 else '')
        auds = soup.find_all(['audio', 'source'])
        for aud in auds:
            if aud.get('src'):
                audio.append(aud)
            else:
                audio.append('')
        
    except Exception as e:
        commonName.append('')
        sciName.append('')
        family.append('')
        about.append('')
        audio.append('')

try:
    url = 'https://indianbirdsong.org/birds'
    driver.get('https://indianbirdsong.org/birds')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ember59"))
    )
    while is_page_loaded():
        links = driver.find_elements(By.XPATH, '//a[contains(@href, "/birds")]')
        for link in links:
            url2 = link.get_attribute('href')
            urls.append(url2)
        filtered_urls = [url for url in urls if 'filter' not in url]
        print(len(filtered_urls))
        for link in filtered_urls:     
            scrape(link)

    data = {'CommonName': commonName, 'SciName': sciName, 'Family': family, 'About': about, 'Audios': audio}
    df = pd.DataFrame(data)
    df.to_csv('birds.csv', index=False)

except Exception as e:
    print(f"Failed to scrape {url}: {str(e)}")
finally:
    driver.quit()

            






        
          
            
