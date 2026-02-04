from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

log_file = "logfile.txt"

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

url = "https://rubenxi-website.streamlit.app/"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(url)

try:
    try:
        iframe_xpath = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div/iframe"))
        )

    except Exception as e:
        log_message(f"❌ No iframe: {e}")

    driver.switch_to.frame(iframe_xpath)

    WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-testid='stSidebarContent']"))
        )
    button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/div/div/section[2]/div[1]/div/div/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div/div/button"))
        )
    button.click()
    text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/p[1]/strong"))).text
    log_message("✅ Web correct: " + text)

except Exception as e:
    log_message(f"❌ Error: {e}")

finally:
    driver.switch_to.default_content()
    driver.quit()
