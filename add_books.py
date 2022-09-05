from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def add_books_using_chrome_browser(base_url, book):
    # options = webdriver.ChromeOptions()
    # options.add_argument("--no-sandbox")
    # options.add_argument("--remote-debugging-port=9222")
    # options.headless = True
    # command_executor = "http://chrome:4444/wd/hub"
    # driver = webdriver.Remote(
    #     command_executor, desired_capabilities=DesiredCapabilities.CHROME)

    # # chrome_options.add_argument("--no-sandbox")
    # # chrome_options.add_argument("--headless")
    # # chrome_options.add_argument("window-size=1400,2100")
    # # chrome_options.add_argument("--disable-gpu")

    # # driver = webdriver.Chrome(chrome_options=chrome_options)
    # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(
    #     ChromeDriverManager().install(), options=chrome_options)

    options = Options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(base_url)

    nameInput = driver.find_element(By.ID, "Name")
    priceInput = driver.find_element(By.ID, "Price")
    authorInput = driver.find_element(By.ID, "Author")
    categorySelect = driver.find_element(By.ID, "CategoryId")

    nameInput.clear()
    priceInput.clear()
    authorInput.clear()

    nameInput.send_keys(book.name)
    priceInput.send_keys(book.price)
    authorInput.send_keys(book.author)

    for option in categorySelect.find_elements(By.TAG_NAME, "option"):
        if option.text == book.category:
            option.click()
            break

    submitBtn = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/form/button[1]')
    submitBtn.click()

    driver.close()
