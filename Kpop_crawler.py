import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm.auto import tqdm

# 크롤링 전 세팅
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36")
# chrome_options.add_argument('headless')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
# driver.maximize_window()

# excel 저장
filename = datetime.datetime.now().strftime("%Y-%m-%d %H-%M")
modified_date = datetime.datetime.now().strftime("%Y-%m-%d")

# 크롤링 URL
melon_base_url = "https://www.melon.com/chart/index.htm"
# n = 1

# 리스트 생성
melon_titles_lst=[]
melon_artists_lst = []
melon_albums_lst = []

# 크롤링 시작
for melon in range(1):
    url_path = melon_base_url
    wait = WebDriverWait(driver, 20)
    driver.get(url_path) 
    time.sleep(3)

    # 곡제목
    try:
        for melon_title in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rank01')))): 
            if melon_title.text != '':
                melon_title_temp = melon_title.text.replace('\n', ' ')
                melon_titles_lst.append(melon_title_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

    # 가수
    try:
        for melon_artist in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rank02')))): 
            if melon_artist.text != '':
                melon_artist_temp = melon_artist.text
                melon_artists_lst.append(melon_artist_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0
        
    # 앨범명
    try:
        for melon_album in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rank03')))): 
            if melon_album.text != '':
                melon_album_temp = melon_album.text.replace('\n', ' ')
                melon_albums_lst.append(melon_album_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

print("melon 크롤링 완료 (1/5)")

# Flo
flo_base_url = "https://www.music-flo.com/detail/chart/a"
# n = 1

# 리스트 생성
flo_titles_lst=[]
flo_artists_lst = []
flo_albums_lst = []

# 크롤링 시작
for flo in range(1):
    url_path = flo_base_url
    wait = WebDriverWait(driver, 20)
    driver.get(url_path) 
    time.sleep(3)

    # 곡제목
    try:
        for flo_title in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'tit__text')))): 
            if flo_title.text != '':
                flo_title_temp = flo_title.text.replace('\n', ' ')
                flo_titles_lst.append(flo_title_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

    # 가수
    try:
        for flo_artist in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'last')))): 
            if flo_artist.text != '':
                flo_artist_temp = flo_artist.text
                flo_artists_lst.append(flo_artist_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

    # 앨범명
    try:
        for flo_album in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'album')))): 
            if flo_album.text != '':
                flo_album_temp = flo_album.text.replace('\n', ' ')
                flo_albums_lst.append(flo_album_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

print("flo 크롤링 완료 (2/5)")

# Vibe
vibe_base_url = "https://vibe.naver.com/chart/total"
# n = 1

# 리스트 생성
vibe_title_txt_lst=[]
vibe_artist_txt_lst=[]
vibe_titles_lst = []
vibe_artists_lst = []

# 크롤링 시작
for vibe in range(1):
    url_path = vibe_base_url
    wait = WebDriverWait(driver, 20)
    driver.get(url_path) 
    time.sleep(3)

    input("팝업삭제+스크롤움직이기 후 엔터")

    # 전체 제목 텍스트
    try:
        for vibe_t_txt in tqdm(wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td.song > div.title_badge_wrap')))): 
            if vibe_t_txt.text != '':
                vibe_t_txt_temp = vibe_t_txt.text.replace('\n', ' ')
                vibe_title_txt_lst.append(vibe_t_txt_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0
    # 전체텍스트
    try:
        for vibe_a_txt in tqdm(wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ' td.song > div.artist_sub')))): 
            if vibe_a_txt.text != '':
                vibe_a_txt_temp = vibe_a_txt.text.replace('\n', ' ')
                vibe_artist_txt_lst.append(vibe_a_txt_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

for vibe_title in vibe_title_txt_lst:
    vibe_titles_lst.append(vibe_title)

for vibe_artist in vibe_artist_txt_lst:
    vibe_artist_temp = vibe_artist[0:-6]
    vibe_artists_lst.append(vibe_artist_temp)

print("Vibe 크롤링 완료 (3/5)")

# Genie
genie_base_url = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220702&hh=18&rtm=N&pg="
g = 1

# 리스트 생성
genie_titles_lst=[]
genie_artists_lst = []
genie_albums_lst = []

# 크롤링 시작
for genie in range(2):
    url_path = genie_base_url + str(g)
    wait = WebDriverWait(driver, 20)
    driver.get(url_path) 
    time.sleep(3)

    # 곡제목
    try:
        for genie_title in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'title.ellipsis')))): 
            if genie_title.text != '':
                genie_title_temp = genie_title.text.replace('\n', ' ')
                genie_titles_lst.append(genie_title_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

    # 가수
    try:
        for genie_artist in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'artist.ellipsis')))): 
            if genie_artist.text != '':
                genie_artist_temp = genie_artist.text
                genie_artists_lst.append(genie_artist_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

    # 앨범명
    try:
        for genie_album in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'albumtitle.ellipsis')))): 
            if genie_album.text != '':
                genie_album_temp = genie_album.text.replace('\n', ' ')
                genie_albums_lst.append(genie_album_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0
    g += 1

print("genie 크롤링 완료 (4/5)")

# bugs
bugs_base_url = "https://music.bugs.co.kr/chart/track/day/total"
# n = 1

# 리스트 생성
bugs_titles_lst=[]
bugs_artists_lst = []
bugs_albums_lst = []

# 크롤링 시작
for bugs_ in range(1):
    url_path = bugs_base_url
    wait = WebDriverWait(driver, 20)
    driver.get(url_path) 
    time.sleep(3)

    # 곡제목
    try:
        for bugs_title in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'title')))): 
            if bugs_title.text != '':
                bugs_title_temp = bugs_title.text.replace('\n', ' ')
                bugs_titles_lst.append(bugs_title_temp)
            else:
                pass
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

    # 가수
    try:
        for bugs_artist in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'artist')))): 
            if bugs_artist.text != '':
                bugs_artist_temp = bugs_artist.text
                bugs_artists_lst.append(bugs_artist_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

    # 앨범명
    try:
        for bugs_album in tqdm(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'album')))): 
            if bugs_album.text != '':
                bugs_album_temp = bugs_album.text.replace('\n', ' ')
                bugs_albums_lst.append(bugs_album_temp)
            else:
                continue
    except:
        # 크롤링 값이 없을 경우에
        # text_lst.append('')
        xyz = 0

bugs_title_lst = bugs_titles_lst[1:]
bugs_artist_lst = bugs_artists_lst[1:]
bugs_album_lst = bugs_albums_lst[2:]

print("bugs 크롤링 완료 (5/5)")

# 데이터프레임으로 변환
melon_df = pd.DataFrame(
    {   '곡제목': melon_titles_lst,
        '가수명': melon_artists_lst,
        '앨범명': melon_albums_lst,
        '추출날짜': modified_date
    })

flo_df = pd.DataFrame(
    {   '곡제목': flo_titles_lst,
        '가수명': flo_artists_lst,
        '앨범명': flo_albums_lst,
        '추출날짜': modified_date
    })

vibe_df = pd.DataFrame(
    {   '곡제목': vibe_titles_lst,
        '가수명': vibe_artists_lst,
        '추출날짜': modified_date
    })

genie_df = pd.DataFrame(
    {   '곡제목': genie_titles_lst,
        '가수명': genie_artists_lst,
        '앨범명': genie_albums_lst,
        '추출날짜': modified_date
    })

bugs_df = pd.DataFrame(
    {   '곡제목': bugs_title_lst,
        '가수명': bugs_artist_lst,
        '앨범명': bugs_album_lst,
        '추출날짜': modified_date
    })

# 인덱스 1부터 실행
melon_df.index = melon_df.index+1
flo_df.index = flo_df.index+1
vibe_df.index = vibe_df.index+1
genie_df.index = genie_df.index+1
bugs_df.index = bugs_df.index+1

# 새로운 엑셀 파일 생성
writer = pd.ExcelWriter("Kpop_data" +filename+ ' .xlsx' , engine='xlsxwriter')
melon_df.to_excel(writer, sheet_name='melon')
flo_df.to_excel(writer, sheet_name='flo')
vibe_df.to_excel(writer, sheet_name='vibe')
genie_df.to_excel(writer, sheet_name='genie')
bugs_df.to_excel(writer, sheet_name='bugs')

writer.save()
driver.close()

print('done!')