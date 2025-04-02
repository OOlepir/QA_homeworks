from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_image_loading():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )

        images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
        third_image_alt = images[2].get_attribute("alt")

        assert third_image_alt == "award", f"The alt attribute of the third image is not 'award'. Current value: {third_image_alt}"
        print("Test passed: The alt attribute of the third image is 'award'.")

    finally:
        driver.quit()


test_image_loading()