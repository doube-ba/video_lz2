from parsel import Selector
from urllib import parse
import re
import requests
from bs4 import BeautifulSoup
url_list = [
    'https://lzizy1.com',
    'https://lzizy3.com',
    'https://lzizy4.com',
    'https://lzizy5.com',
    'https://lzizy6.com',
    'https://lzizy7.com',
    'https://lzizy8.com'
]
session = requests.Session()
def data_lists(x,y,z):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    response = ''
    if x == '0':
        for url in url_list:
            response = session.get(url + f'/index.php/vod/search/page/{z}/wd/{y}.html', headers=headers)
            if response.status_code == 200:
                print(response.status_code)
                print('搜索')
                break
            else:
                print(response.status_code)
                continue
    else:
        for url in url_list:
            response = session.get(url + f'/index.php/vod/type/id/{y}/page/{z}.html', headers=headers)
            if response.status_code == 200:
                print(response.status_code)
                print('分类')
                break
            else:
                print(response.status_code)
                continue
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    num1 = int(re.findall('共(.*?)条数据', response.text)[0])
    num2 = len(soup.select('ul.videoContent li'))
    nums = [num1, num2]
    # print(nums)
    data_list1 = []
    for a in soup.select('ul.videoContent li'):
        data_list2 = {}
        name = a.select('a.videoName')[0].text
        name_ji = a.select('a.videoName i')[0].text
        name_diqu = a.select('span.region')[0].text
        name_lei = a.select('span.category')[0].text
        name_url = a.select('a.videoName')[0]['href']
        name_douban = a.select('a.address')[0].text
        name_time = a.select('span.time1')[0].text
        data_list2['name'] = name[:-len(name_ji)]
        data_list2['name_ji'] = name_ji
        data_list2['name_diqu'] = name_diqu
        data_list2['name_lei'] = name_lei
        data_list2['name_url'] = name_url
        data_list2['name_douban'] = name_douban
        data_list2['name_time'] = name_time
        data_list1.append(data_list2)
    data_list = [nums, data_list1]
    return data_list

def data_url(x):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    response = ''
    for url in url_list:
        response = session.get(url + f'{x}',headers=headers)
        if response.status_code == 200:
            print(response.status_code)
            print('视频地址')
            break
        else:
            print(response.status_code)
            continue
    soup = BeautifulSoup(response.text, 'html.parser')
    data_list1 = []
    for a in soup.select('div.playlist.lzm3u8 li')[:-1]:
        # print(a)
        data_list2 = {}
        name = a.select('li a')[0]['title']
        name_url = a.select('li a')[0]['href']
        data_list2['name'] = name
        data_list2['name_url'] = name_url
        data_list1.append(data_list2)
        # print(name,name_url)
        # break
    return data_list1


# data = data_lists(0,'第一序列',1)
# print(data)
# a = data_url('/index.php/vod/detail/id/51084.html')
# print(a)