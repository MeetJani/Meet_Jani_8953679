#Import libraries for testing

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setup web driver
driver = webdriver.Chrome()

# Navigate to the Indeed home page
driver.get("https://ca.indeed.com/")
time.sleep(2)

# Click on Company reviews button
company_review = driver.find_element("id","CompanyReviews")
company_review.click()
time.sleep(3)

# Find search bar and add company name
company_search = driver.find_element("id", "ifl-InputFormField-:R3b5:")
company_search.send_keys("TCS")

# Submit the find companies form
company_search.send_keys(Keys.RETURN)
time.sleep(3)

assert "TCS" in driver.title

# Select the TCS company from available list
company_select = driver.find_element("xpath","/html/body/div[2]/div/main/div/div[2]/section/div[2]/div[1]/div[1]/div[2]/div[1]/a")
company_select.click()
time.sleep(2)

# Select the Jobs tab from the list
company_job = driver.find_element("xpath","/html/body/div[2]/div/div[1]/header/div[2]/div[3]/div/div/div/div[2]/nav/div/ul/li[5]/a")
company_job.click()
time.sleep(5)

# Go back to the previous page
driver.back()
time.sleep(2)

# Click on the company follow button
company_follow = driver.find_element("xpath","/html/body/div[2]/div/div[1]/header/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/button")
company_follow.click()
time.sleep(3)

# Close webdriver
driver.close()