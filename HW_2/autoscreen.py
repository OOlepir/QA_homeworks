import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



def main():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Открытие страницы
        driver.get("https://itcareerhub.de/ru")
        time.sleep(3)

        payment_block = driver.find_element(
            By.CSS_SELECTOR,
            "div.t396__filter[data-artboard-recid='860584261']"
        )

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", payment_block)
        driver.execute_script("arguments[0].style.boxShadow='0 0 0 3px red';", payment_block)
        time.sleep(1)

        os.makedirs('screenshots', exist_ok=True)

        screenshot_path = os.path.join('screenshots', 'payment_methods_precise.png')
        payment_block.screenshot(screenshot_path)

        print(f"Screen saved: {screenshot_path}")

    except Exception as e:
        print("Error")

    finally:
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    main()