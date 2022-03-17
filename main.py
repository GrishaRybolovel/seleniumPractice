from selenium import webdriver
import time
from fake_useragent import UserAgent


url = "https://vk.com/feed/"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=HelloWorld:)")

driver = webdriver.Chrome(executable_path="/Users/grisharybolovlev/PycharmProjects/selenium/chrome/chromedriver",
                          options=options)


try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    driver.save_screenshot("vk_feed.png")
    time.sleep(20)

except Exception as ex:
    print ex

finally:
    driver.close()
    driver.quit()
