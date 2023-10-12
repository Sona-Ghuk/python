from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

search_input = driver.find_element(By.NAME, "search_query")
search_input.send_keys("Rihanna")
search_input.submit()

video_link = driver.find_element(By.CSS_SELECTOR, "a#video-title")
video_link.click()

time.sleep(10)

driver.quit()