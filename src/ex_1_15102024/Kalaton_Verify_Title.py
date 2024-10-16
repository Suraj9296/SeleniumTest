from selenium import webdriver
import allure
import pytest
@allure.title("Verify the Title/URL/Page Source of the webpage https://katalon-demo-cura.herokuapp.com/")
def test_open_CURA_login():
    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(service=chromeService)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    ##Verify Title
    print("**----Starting To Verify Title----**")
    print(driver.title)
    assert driver.title == "CURA Healthcare Service"
    print("**----Title Verification Completed----**")
    ##Verify URL
    print("**----Starting To Verify URL----**")
    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    print("**----URL Verification Completed----**")
    #Verify page source
    print("**----Starting To Verify PageSource----**")
    content =driver.page_source
    assert  "CURA Healthcare Service" in content
    #print(content)
    print("**----PageSource Verification Completed----**")
