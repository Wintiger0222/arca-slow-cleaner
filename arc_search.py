import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import math

timesleepload=3
timesleeplen=6 #4: 빠름, 6 보통, 10 권장
search_mode = "all"
# search_mode = "nickname" ;자주쓰면 리밋걸림

def channel_crawl(channel_URL,page_in,start_date,end_date):
    page=1
    flag=True
    remove_fail=0
    last_num=-1
    while flag:
        # page=page+1//delete is always 0
        driver.get(channel_URL+'?target='+str(search_mode)+'&keyword='+nickname+"&p="+str(page))
        time.sleep(timesleepload)
        article_id_xpath="//a[@class='vrow column']"
        articles = driver.find_elements(By.XPATH,article_id_xpath)
        if last_num < 0:
            articles_num=articles[0].find_element(By.XPATH,"//a[@class='vrow column']/div/div[1]/span[1]/span")
            last_num=int(articles_num.text)
            print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"최대 "+str(last_num)+"글 삭제 예정")
            print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"예상시간 "+str(math.ceil((last_num+last_num/40)*timesleeplen/60))+"분")
        article_id_list=[]
        article_date_list=[]
        if len(articles)==0:  
            break
        
        remove_fail=0
        for article in articles:
            article_date_driver = article.find_elements(By.TAG_NAME,"time")
            article_id=int(str(str(article.get_attribute('href')).split('/')[-1]).split('?')[0])
            str_article_date=str(article_date_driver[0].get_attribute('datetime')).replace("T", " ").replace(".000Z", "") 
            article_date=datetime.datetime.strptime(str_article_date, '%Y-%m-%d %H:%M:%S')
            article_id_list.append(article_id)
            article_date_list.append(article_date)
            
        time.sleep(timesleeplen)
        for article_id, article_date in zip(article_id_list,article_date_list):    
            print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"글 아이디:"+str(article_id) + " 작성일:"+article_date.strftime('%Y-%m-%d %H:%M:%S'))
            
            article_URL=str(channel_URL)+"/"+str(article_id)+"/delete"
            driver.get(article_URL)
            time.sleep(timesleeplen)
            try:
                delbtn = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/article/div/div[2]/div/div/form/div[2]/button')
                delbtn.click()
                print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"글을 삭제했습니다! ["+str(article_id)+"]"+'\033[0m')
                
            except:
                print('\033[91m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"삭제할 수 없는 글을 패스했습니다. ["+str(article_id)+"]"+'\033[0m')
                remove_fail=remove_fail+1
            time.sleep(1)
            # time.sleep(timesleeplen)
        if remove_fail>=len(articles):
            page=page+1
        
print("아카 글 삭제기 v0.1")
print("by 지금 배고픈데 라면 끓여줄 사람 없나.")
print()
print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"전체로 검색: 0 / 닉네임으로 검색: 1")
print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"모두 찾으면 다른사람것도 찾아지므로 느려집니다."+'\033[0m')
print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"닉네임으로 찾으면 빨라지나, 캡챠에 걸릴 가능성이 높습니다."+'\033[0m')
search_mode_int = input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"탐색모드을 입력하고 Enter를 눌러 주세요>")
if search_mode_int in {"1"}:
    search_mode = "nickname"
else:
    search_mode = "all"
    
print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"보통: 6/ 느림 10")
print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"탐색속도가 빠를수록 캡챠에 걸릴 가능성이 높습니다."+'\033[0m')
timesleeplen_str=input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"탐색속도를 입력하고 Enter를 눌러 주세요>")
timesleeplen=int(timesleeplen_str)

nickname = input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"닉네임을 입력하고 Enter를 눌러 주세요>")
print('\033[33m'+str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"예시: 종합 속보: breaking"+'\033[0m')
channel_name = input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"채널 코드를 입력하고 Enter를 눌러 주세요>")
if not channel_name:
    channel_name = "breaking"
# search_mode = "all"


# URL = 'https://arca.live/b/'+str(channel_name)+'?target='+str(search_mode)+'&keyword='+nickname+'&after=0'

driver = webdriver.Chrome(executable_path='chromedriver') #<- 크롬 기준
# driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver") #<- 파이어폭스 기준
driver.get("https://arca.live/u/login")
input(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"웹브라우저에서 로그인한 뒤 Enter를 눌러 주세요> ")

print(str(datetime.datetime.now().strftime('[%H:%M:%S] '))+"글삭제시 R-18오류가 뜰경우 반드시 앞으로 알리지 알림을 눌러주세요.")

channel_URL=str("https://arca.live/b/"+channel_name)
channel_crawl(channel_URL,1,0,0)
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