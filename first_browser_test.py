from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    print("Page title:", driver.title)

    assert driver.title == "Google"
    print("Test passed.")
finally:
    driver.quit()