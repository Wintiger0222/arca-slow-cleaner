import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import math

timesleeplen=10 #4: 빠름, 6 보통, 10 권장
timesleepload=1 #4: 빠름, 6 보통, 10 권장

def channel_crawl(channel_URL):
   
    first_flag=True
    flag=True
    while True:
        URL=channel_URL
        
        first_flag=False
        
        print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"유저정보 재로드"+'\033[0m')
        driver.get(URL)  
        article_id_xpath="//div[@class='user-recent']"
        articles = driver.find_elements(By.XPATH,article_id_xpath)
    
        article_id_list=[]
        article_date_list=[]
        article_URL_list=[]
        print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"유저정보 로드완료"+'\033[0m')
        i=0
        flag_test=False
        for article in articles:
            i=i+1
            if i<=15+1:#+14:
                continue    #댓글이 아님
            flag_test=True
            article_date_driver = article.find_elements(By.TAG_NAME,"time")
            article_id_driver = article.find_element(By.XPATH,"./div[1]/a[2]")
            
            article_id=str(str(article_id_driver.get_attribute('href')).split('/')[5])
            str_article_date=str(article_date_driver[0].get_attribute('datetime')).replace("T", " ").replace(".000Z", "") 
            article_URL=str(str(article_id_driver.get_attribute('href')).split('#')[0])
            
            article_date=datetime.datetime.strptime(str_article_date, '%Y-%m-%d %H:%M:%S')
            article_id_list.append(article_id)
            article_date_list.append(article_date)
            article_URL_list.append(article_URL)
            
        # time.sleep(timesleeplen)
        # time.sleep(timesleeplen/2)
        if flag_test is False:
            break
        for article_URL, article_id, article_date in zip(article_URL_list, article_id_list,article_date_list):    
            comment_id=str(article_URL.split('/')[-1])
            
            print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"본글 아이디:"+str(article_id) +" 댓글 아이디:"+str(comment_id)+ " 시간:"+article_date.strftime('%Y-%m-%d %H:%M:%S'))
            
            # article_URL=str(channel_URL)+"/"+str(article_id)
            # comment_crawl(article_URL)
            # time.sleep(timesleeplen)
            
            delete_URL=str(article_URL)+"/delete"
            driver.get(delete_URL)
            time.sleep(1)
            try:
                delbtn = driver.find_element(By.XPATH,"//button[@class='btn btn-danger']")
                # delbtn = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/article/div/div[2]/div/div/form/div[2]/button')
                delbtn.click()
                print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"댓글을 삭제했습니다! ["+str(comment_id)+"]"+'\033[0m')
                time.sleep(3.5)
            except:
                print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"댓글삭제 실패 재시도 ["+str(comment_id)+"]"+'\033[0m')
                try:
                    delbtn = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/article/div/div[2]/div/div/form/div[2]/button")
                    delbtn.click()
                    print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"댓글을 삭제했습니다! ["+str(comment_id)+"]"+'\033[0m')
                    # time.sleep(1)
                except:
                    temp=input('\033[91m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"삭제할수없습니다 재시도 바람. ["+str(comment_id)+"]"+'\033[0m')
                    # time.sleep(1000)
                # time.sleep(3)
            
            
print("아카 댓글 삭제기 v0.1")
print("by 지금 배고픈데 라면 끓여줄 사람 없나.")
print()

# print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"보통: 6/ 느림 10")
# print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"탐색속도가 빠를수록 캡챠에 걸릴 가능성이 높습니다."+'\033[0m')
# timesleeplen_str=input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"탐색속도를 입력하고 Enter를 눌러 주세요>")
# timesleeplen=int(timesleeplen_str)

print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"예시: 종합 속보: breaking"+'\033[0m')
channel_name = input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"유저이름를 입력하고 Enter를 눌러 주세요> ")
if not channel_name:
    channel_name = "breaking"
# search_mode = "all"


# URL = 'https://arca.live/b/'+str(channel_name)+'?target='+str(search_mode)+'&keyword='+nickname+'&after=0'

options = webdriver.ChromeOptions()
options.add_argument("user-agent=live.arca.android/0.8.331")

driver = webdriver.Chrome(options=options) #<- 크롬 기준
# driver = webdriver.Chrome(executable_path='chromedriver') #<- 크롬 기준
# driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver") #<- 파이어폭스 기준
driver.get("https://arca.live/u/login")
input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"웹브라우저에서 로그인한 뒤 Enter를 눌러 주세요> ")


channel_URL=str("https://arca.live/u/@"+channel_name)
# print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"예상시간 "+str(math.ceil(((end_page-start_page)*2*40)*(timesleeplen+1)/60))+"분")
channel_crawl(channel_URL)
# comment_crawl(article_URL)


# while True: #<- 이 부분에는 뭘 넣어야 할 지 아직 모르겠어서 first_article 못 찾으면 튕겨서 종료되게 함.
    # driver.get(URL)
    # time.sleep(timesleeplen)
    # text='/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a['+str(bottomart)+']'
    # try:
        # first_article = driver.find_element(By.XPATH,text)
    # except:
        # input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"웹브라우저에서 캡차를 해결해 주세요. ")
        # driver.get(URL)
        # time.sleep(timesleeplen)
        # first_article = driver.find_element(By.XPATH,text)
    # aaA = str(str(first_article.get_attribute('href')).split('?')[0])+"/delete"
    # bbB = str(first_article.get_attribute('class'))
    # ccC = str(first_article.get_attribute('href')).split('?')[0].split('/')[-1]
    # driver.get(aaA)
    # time.sleep(timesleeplen)
    # if(bbB =="vrow column"):
        # try:
            # delbtn = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/article/div/div[2]/div/div/form/div[2]/button')
            # delbtn.click()
            # time.sleep(timesleeplen)
            # print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"글을 삭제했습니다. ("+str(ccC)+")")
        # except:
            # print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"삭제할 수 없는 글을 패스했습니다. ("+str(ccC)+")")
            # bottomart=bottomart-1
    # if(bbB !="vrow column"):
        # print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"현재 페이지를 전부 삭제했습니다.")
        # print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"다음페이지로 넘어갑니다.")
        # time.sleep(timesleeplen)
        # driver.get(URL)
        # time.sleep(timesleeplen)
        # text='/html/body/div[2]/div[3]/article/div/nav[1]/ul/li[2]/a'
        # try:
            # next_page = driver.find_element(By.XPATH,text)
            # URL = str(next_page.get_attribute('href'))
        # except:
            # input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"보호를 위해 정지했습니다.")
        # bottomart=int(47)
        # input("보호를 위해 정지했습니다.") #여기까지 가면 공지 라인
        
        # input("웹브라우저에서 캡차를 해결하고 글을 삭제한 뒤 Enter를 눌러 주세요> ")
        # delbtn = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/article/div/div[2]/div/div/form/div[2]/button')
        # delbtn.click()
        # time.sleep(timesleeplen)
    # if driver.current_url == aaA:
        # input("웹브라우저에서 캡차를 해결하고 글을 삭제한 뒤 Enter를 눌러 주세요> ")

# 댓글은 삭제 안 됨

# 삭제 불가능한 글 만나면 패스