import requests
from bs4 import BeautifulSoup

def get_horoscope_today(zodiac_sign: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    res = requests.get(
        f"https://cafeastrology.com/{zodiac_sign}dailyhoroscope.html", headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    data = soup.find('div', attrs={'class': 'entry-content'})
    data2 = data.get_text() #get the text under this tag
    data3 = data2.splitlines() 
    data4 = data3[6] #get the actual horoscope

    cindex = data4.find("Creativity:")
    data5 = data4[:cindex] #cut off after description ends
    
    return data5

def get_horoscope_tomorrow(zodiac_sign: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    res = requests.get(
        f"https://cafeastrology.com/{zodiac_sign}dailyhoroscopetom.html", headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    data = soup.find('div', attrs={'class': 'entry-content'})
    data2 = data.get_text() #get the text under this tag
    data3 = data2.splitlines()
    data4 = data3[7] #get the actual horoscope

    cindex = data4.find("Creativity:")
    data5 = data4[:cindex] #cut off after description ends
    
    return data5

