import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

nickname = input(str(datetime.now().strftime('[%H:%M:%S] '))+"닉네임을 입력하고 Enter를 눌러 주세요> ")
print(str(datetime.now().strftime('[%H:%M:%S] '))+"예시: 종합 속보: breaking")
channel_name = input(str(datetime.now().strftime('[%H:%M:%S] '))+"채널 코드를 입력하고 Enter를 눌러 주세요> ")
search_mode = "all"
# search_mode = "nickname" ;자주쓰면 리밋걸림
timesleeplen=4 #4: 빠름, 6 보통, 10 권장

URL = 'https://arca.live/b/'+str(channel_name)+'?target='+str(search_mode)+'&keyword='+nickname+'&after=0'

driver = webdriver.Chrome(executable_path='chromedriver') #<- 크롬 기준
# driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver") #<- 파이어폭스 기준
driver.get("https://arca.live/u/login")
input(str(datetime.now().strftime('[%H:%M:%S] '))+"웹브라우저에서 로그인한 뒤 Enter를 눌러 주세요> ")


bottomart=int(47)

while True: #<- 이 부분에는 뭘 넣어야 할 지 아직 모르겠어서 first_article 못 찾으면 튕겨서 종료되게 함.
    driver.get(URL)
    time.sleep(timesleeplen)
    text='/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a['+str(bottomart)+']'
    try:
        first_article = driver.find_element(By.XPATH,text)
    except:
        input(str(datetime.now().strftime('[%H:%M:%S] '))+"웹브라우저에서 캡차를 해결해 주세요. ")
        driver.get(URL)
        time.sleep(timesleeplen)
        first_article = driver.find_element(By.XPATH,text)
    aaA = str(str(first_article.get_attribute('href')).split('?')[0])+"/delete"
    bbB = str(first_article.get_attribute('class'))
    ccC = str(first_article.get_attribute('href')).split('?')[0].split('/')[-1]
    driver.get(aaA)
    time.sleep(timesleeplen)
    if(bbB =="vrow column"):
        try:
            delbtn = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/article/div/div[2]/div/div/form/div[2]/button')
            delbtn.click()
            time.sleep(timesleeplen)
            print(str(datetime.now().strftime('[%H:%M:%S] '))+"글을 삭제했습니다. ("+str(ccC)+")")
        except:
            print(str(datetime.now().strftime('[%H:%M:%S] '))+"삭제할 수 없는 글을 패스했습니다. ("+str(ccC)+")")
            bottomart=bottomart-1
    if(bbB !="vrow column"):
        print(str(datetime.now().strftime('[%H:%M:%S] '))+"현재 페이지를 전부 삭제했습니다.")
        print(str(datetime.now().strftime('[%H:%M:%S] '))+"다음페이지로 넘어갑니다.")
        time.sleep(timesleeplen)
        driver.get(URL)
        time.sleep(timesleeplen)
        text='/html/body/div[2]/div[3]/article/div/nav[1]/ul/li[2]/a'
        try:
            next_page = driver.find_element(By.XPATH,text)
            URL = str(next_page.get_attribute('href'))
        except:
            input(str(datetime.now().strftime('[%H:%M:%S] '))+"보호를 위해 정지했습니다.")
        bottomart=int(47)
        # input("보호를 위해 정지했습니다.") #여기까지 가면 공지 라인
        
        # input("웹브라우저에서 캡차를 해결하고 글을 삭제한 뒤 Enter를 눌러 주세요> ")
        # delbtn = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/article/div/div[2]/div/div/form/div[2]/button')
        # delbtn.click()
        # time.sleep(timesleeplen)
    # if driver.current_url == aaA:
        # input("웹브라우저에서 캡차를 해결하고 글을 삭제한 뒤 Enter를 눌러 주세요> ")

# 댓글은 삭제 안 됨

# 삭제 불가능한 글 만나면 패스