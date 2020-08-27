import requests
from bs4 import BeautifulSoup
import os
from time import sleep
from playsound import playsound


def screen_clear():
    _ = os.system('cls')

screen_clear()

def coinbase():
    r1 = requests.get("https://blog.coinbase.com/latest")
    blogpage = r1.content
    soup = BeautifulSoup(blogpage, 'html.parser')
    title = soup.find_all('h3')
    subtitle = soup.find_all('h4')
    link = soup.find_all(class_='button button--smaller button--chromeless u-baseColor--buttonNormal')
    date = soup.find_all('time')

    title1 = title[0].get_text()

    print("LATEST POST:")
    print(title[0].get_text())
    print(subtitle[0].get_text())
    print(link[0]['href'])
    print("TIMESTAMP: " + date[0].get_text())
    return title1

def CheckPost():
    title1 = coinbase()
    r2 = requests.get("https://blog.coinbase.com/latest")
    blogpage2 = r2.content
    soup2 = BeautifulSoup(blogpage2, 'html.parser')
    title2 = soup2.find_all('h3')
    subtitle2 = soup2.find_all('h4')
    link2 = soup2.find_all(class_='button button--smaller button--chromeless u-baseColor--buttonNormal')
    date2 = soup2.find_all('time')

    if title1 == title2[0].get_text():
        #print("PING_REQ: ", count)
        #coinbase()
        #sleep(3)
        screen_clear()
    else:
        print("LATEST POST:")
        print(title2[0].get_text())
        print(subtitle2[0].get_text())
        print(link2[0]['href'])
        print("TIMESTAMP: " + date2[0].get_text())
        playsound('sound.mp3')
n = 5
count = 0
while n > 0:
    count = count + 1
    print("PING_REQ: ", count)
    CheckPost()

input("Press Enter to continue...")