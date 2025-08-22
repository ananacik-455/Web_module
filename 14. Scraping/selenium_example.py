from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

URL = "https://www.google.com"

driver = webdriver.Chrome()

driver.get(URL)

try:
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Selenium Python")

    search_box.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 20)
    wait.until(ec.visibility_of_element_located(("id", "search")))

    print(f"Title of our web search: {driver.title}")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()