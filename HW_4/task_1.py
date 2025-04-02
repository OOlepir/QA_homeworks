from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_text_change():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")

    try:
        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.send_keys("ITCH")

        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        assert button.text == "ITCH", f"Button text did not change to 'ITCH'. Current text: {button.text}"
        print("Test passed: button text successfully changed to 'ITCH'")

    finally:
        driver.quit()


test_button_text_change()