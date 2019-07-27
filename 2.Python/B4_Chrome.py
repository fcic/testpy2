# 本地需要chromedriver驱动器文件，如果不配置环境变量的话，需要手动指定executable_path参数。
#https://sites.google.com/a/chromium.org/chromedriver/home

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver.get("https://www.baidu.com")
    print(driver.page_source)
    driver.close()


if __name__ == '__main__':
    main()
