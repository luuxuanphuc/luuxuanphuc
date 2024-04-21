import random
import subprocess
import time
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

for k in range(1,10000):
    for a in range(91, 271, 25):
        def initDriver(a):
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.binary_location = "C:\\Users\\ANPHUC\\.gologin\\browser\\orbita-browser-121\\chrome.exe"
            chromeOptions.add_argument("--user-data-dir=D:\\Profiles\\" + str(a))  # Path to your chrome profile
            chromeOptions.add_argument('--disable-application-cache')  # không lưu cache
            chromeOptions.add_argument('--disable-gpu')  # Corrected spacing
            chromeOptions.add_argument('window-size=400,675')
            chromeOptions.add_argument('--blink-settings=imagesEnabled=false')
            #chromeOptions.add_argument('--load-extension=D:\\1extensoin\\proxyomega')
            driver = webdriver.Chrome(options=chromeOptions)
            return driver

        def view(a):
            def doing(a):
                if a <= 270:
                    time.sleep(random.randint(1, 5))
                    driver = initDriver(a)


                def onlyview(a,link=None,idtw=None):
                    # Đi đến trang
                    try:
                        driver.get(link)
                        time.sleep(random.randint(7, 11))
                    except:
                        pass
                    # random_number = random.randint(10, 25)  # Chọn một con số ngẫu nhiên từ 200 đến 500
                    # if k % random_number == 0 and k >= random_number:                        # Nếu đếm đủ số lần và là bội số của con số ngẫu nhiên, gọi hàm repply
                    #     repply(a, idtw)

                def repply(a, idtw):
                    with open('text.txt', 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        text = random.choice(lines)
                    url = "https://twitter.com/intent/tweet?in_reply_to=" + str(idtw) + '&text=' + text
                    try:
                        driver.get(url)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div[2]/div/span/span'))).click()
                        time.sleep(2)
                    except:
                        pass

                #hàm like
                def like(a,idtw=None):
                    driver.get('https://twitter.com/intent/like?tweet_id='+idtw)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span'))).click()
                    time.sleep(1)

                #hàm retweet
                def retwweer(a, idtw=None):
                    driver.get('https://twitter.com/intent/retweet?tweet_id=' + idtw)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span'))).click()
                    time.sleep(1)

                # hàm quotetweet
                def quote(a,linkquote=None):
                    with open('text.txt', 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        text = random.choice(lines)
                    url = "https://twitter.com/intent/tweet?text="+' '  +  linkquote +' '+ text
                    driver.get(url)
                    #time.sleep(444444)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div[2]/div/span/span'))).click()
                    time.sleep(2)


                onlyview(a,link="https://twitter.com/Elias11333/status/1781504843888369783",idtw=1781504843888369783)
                onlyview(a,link="https://twitter.com/edieramonay2lp/status/1781508512792948943",idtw=1781508512792948943)
                onlyview(a,link="https://twitter.com/gabrieldarosasi/status/1781489306991001687",idtw=1781489306991001687)

                # like(a,idtw="1781489306991001687")
                # retwweer(a,idtw="1781489306991001687")
                # quote(a,linkquote="https://twitter.com/gabrieldarosasi/status/1781489306991001687")
                # repply(a,idtw=1781489306991001687)
                # time.sleep(3)

            doing(a)


        def lap_pool():
            p = Pool(25)


            args = [(a + i) for i in range(25)]

            p.map_async(view, args)
            p.close()
            p.join()


        if __name__ == '__main__':
            lap_pool()
