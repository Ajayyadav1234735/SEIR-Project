import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def process_url(driver, url):
    try:
        driver.get(url)
        time.sleep(2)

        print("Title:")
        print(driver.title)

        print("\nBody Text:")
        body = driver.find_element(By.TAG_NAME, "body")
        print(body.text)

        print("\nLinks:")
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href:
                print(href)

        print("\n" + "="*60 + "\n")

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL1> <URL2>")
        sys.exit(1)

    options = Options()
    options.add_argument("--headless")  # remove if you want browser visible

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    process_url(driver, sys.argv[1])
    process_url(driver, sys.argv[2])

    driver.quit()


if __name__ == "__main__":
    main()