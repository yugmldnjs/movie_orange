import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# anaconda prompt
# > conda activate cnu_python
# > pip install beautifulsoup
# > pip install selenium
# > pip install webdriver_manager

# Selenium: 동적 페이지에서 웹 크롤링 가능!
#             → 원래 용도: 웹 브라우저

# http: 웹
# ftp: 파일 전송
# ssh: 터미널 접속
# smtp: 메일 전송

#####################################
# 1.Install CromDriver for selenium #
#####################################
# Selenium -> 개인 웹브라우저 사용!(우리는 웹 브라우저 중 chrome 사용)
# selenium -> webdriver(chrom)
# 1. 최신버전 사용해서 code로 다운로드 (최신버전)
# 2.chrom driver 다운로드 후 주입 (구버전)
# 주소: https://sites.google.com/chromium.org/driver/downloads


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


movie_id = 160244
url = "https://movie.daum.net/moviedb/main?movieId=160244"

