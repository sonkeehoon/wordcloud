import requests
from bs4 import BeautifulSoup

url=("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=\
    과자\
    &sort=1&photo=0&field=0&pd=3&ds=2019.01.08&de=2022.01.08&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:from20190108to20220108,a:all&start=00")

str_n=""

for i in range(4):
    url=url[:-2]+str(i)+"1"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")

    lck1=soup.find_all("a",attrs={"class":"news_tit"})
    lck2=soup.find_all("a",attrs={"class":"api_txt_lines dsc_txt_wrap"})
    # lck3=soup.find_all("a",attrs={"class":"elss sub_tit"})
    lcks=lck1+lck2
    # +lck3
    for lck in lcks:
        str_n=str_n+lck.get_text()  
        
with open ("bigdata.hwp","w",encoding="utf8") as f:
    f.write(str_n)
    
    






