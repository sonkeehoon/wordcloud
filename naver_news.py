import requests
from bs4 import BeautifulSoup
# 블로그,카페 검색 결과를 축제명.txt에 저장한 후에 실행
# 뉴스검색결과 긁어오기
url=("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=\
    법성포단오제\
    &sort=1&photo=0&field=0&pd=3&ds=2019.05.16&de=2022.05.16&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:from20190516to20220516,a:all&start=00")
str_n=""

for i in range(5):
    url=url[:-2]+str(i)+"1"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")

    lck1=soup.find_all("a",attrs={"class":"news_tit"})
    lck2=soup.find_all("a",attrs={"class":"api_txt_lines dsc_txt_wrap"})
    lcks=lck1+lck2
    for l in lcks:
        str_n=str_n+l.get_text()

with open ("법성포단오제.txt",'r',encoding='utf8') as f:
    s=f.read().replace("문서 저장하기","")
with open ("법성포단오제.txt",'w',encoding='utf8') as f:
    f.write(s+str_n)
