from selenium import webdriver
import allure
import pytest

@allure.title("Verify the Title of the webpage app.vwo.com")
def test_sample():
    driver=webdriver.Edge()
    driver.get("https://sdet.live")