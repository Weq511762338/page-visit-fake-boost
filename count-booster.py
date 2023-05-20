import requests
import time

# example user agent as proxy to send request to web page
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

print('Welcome! Enter the camo url for your visitor count picture: ')
url = input()

print('Number of boost on visitor counts: ')
num = int(input())

print('Working on it...')

start = time.time()
for i in range(1, num):
    response = requests.get(url, headers=header)
    # print(response.status_code)

print('Success!')