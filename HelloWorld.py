from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Start the Chrome browser
driver = webdriver.Chrome()

try:
    # 2. Go to a website
    driver.get("https://www.python.org")

    # 3. Print the page title to the console
    print("Page Title:", driver.title)

    # 4. Find the search input box using its HTML name attribute (<input name="q">)
    search_box = driver.find_element(By.NAME, "q")

    # 5. Type text into the search box and press ENTER
    search_box.send_keys("asyncio")
    search_box.send_keys(Keys.RETURN)

    # 6. Pause for 3 seconds so you can see the result
    time.sleep(3)

finally:
    # 7. Close the browser and end the session
    driver.quit()