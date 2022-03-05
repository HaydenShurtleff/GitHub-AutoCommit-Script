from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set user information
username = "Username Here"
password = "Password here"
repository = "URL to repository here"
file_title = "Title of file to change here"

# Set the path to chromedriver
PATH = "/usr/bin/chromedriver"
counter =(10)
while counter >= 1:
    # Open a Browser Session
    driver = webdriver.Chrome(PATH)

    # Navigate to GitHub Login
    driver.get("https://github.com/login")


    # Locate the login fields and submit button
    user_box = driver.find_element(By.ID, "login_field")
    pass_box = driver.find_element(By.ID, "password")
    submit = driver.find_element(By.NAME, "commit")

    # Input login information and submit
    user_box.send_keys(username)
    pass_box.send_keys(password)
    submit.click()

    # Navigate to Repository
    driver.get(repository)

    # Open file in repository
    file = driver.find_element_by_link_text(file_title)
    file.click()
    body = driver.find_element_by_tag_name("body")
    body.send_keys("e")

    # Click on edit button
    driver.implicitly_wait(1)
    edit = driver.find_element_by_css_selector("button.btn-octicon.tooltipped.tooltipped-nw")
    edit.click()

    # Change text of first line
    driver.implicitly_wait(1)
    text = driver.find_element_by_css_selector('#code-editor > div:nth-child(1) > pre > span > span')
    driver.implicitly_wait(1)
    driver.execute_script("arguments[0].innerText = 'Changed baby'", text)

    # Click Form and fill out
    commit_title = driver.find_element_by_id("commit-summary-input")
    commit_title.send_keys("Commitment issues")

    # Click Submit
    submit_file = driver.find_element_by_id("submit-file")
    driver.execute_script("arguments[0].removeAttribute('disabled')", submit_file)
    submit_file.click()

    # Close Session
    driver.quit()
    counter -= 1
