import requests
url = "https://www.baidu.com/s?ie=UTF-8&wd=a"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
req = requests.get(url, headers=headers).content