print("Script started")

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://github.com/msvivekranjan")

for i in range(200):
    time.sleep(0.2)
    driver.refresh()
    print(f"Refresh {i+1}")

driver.quit()

print("Script finished")