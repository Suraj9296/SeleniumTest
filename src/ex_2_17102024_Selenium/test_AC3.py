import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_action_keyboard():
    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(service=chromeService)
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # draggable
    element_to_hold = driver.find_element(By.ID, "draggable")

    # click - Normal Driver, will find the element and click on it. release it.
    # click and Hold - Actions Chains - Click and Hold (don'T RELEASE)

    time.sleep(2)


    # KEY_DOWN
    actions = ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()


    time.sleep(10)
    driver.quit()