from selenium import webdriver
import allure
import pytest
@allure.title("Verify the Title of the webpage app.vwo.com")
def test_open_vwo_login():
    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(service=chromeService)
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"