from selenium import webdriver
import chromedriver_binary
import time

for auto_click in range(1000):

    page_url = "https://soty.staff-start.com/staffs/320"
    driver = webdriver.Chrome(executable_path='chromedriver')

    # ページを開く
    driver.get(page_url)

    #待機時間
    time.sleep(3)
    # ボタンの情報取得
    yell_button = driver.find_element_by_xpath("/html/body/wrapper/div[2]/div[2]/a/img[1]")

    # 自動クリック
    for counter in range(10):
        yell_button.click()
        time.sleep(3.2)
    driver.close()

    #実行回数
    print(auto_click)
