import os
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from data.urls import BASE_URL


@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.add_argument("--window-size=2560,1440")
    options.set_capability("acceptInsecureCerts", True)
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVideo": False
    })

    driver = webdriver.Remote(
        command_executor=os.getenv("SELENOID_URI", "http://selenoid:4444/wd/hub"),
        options=options
    )

    driver.get(BASE_URL)
    yield driver
    driver.quit()
