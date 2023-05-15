import requests
from bs4 import BeautifulSoup as bs
import json
import csv

f = open('navergt.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B7%B8%EB%A6%BD%ED%86%A1&pagingIndex={}&pagingSize=80&productSet=total&query=%EA%B7%B8%EB%A6%BD%ED%86%A1&sort=rel&timestamp=&viewType=thumb'.format(i)
    # url = 'https://search.shopping.naver.com/search/all?query=%EC%9E%A5%EC%9E%91'
    res = requests.get(url)
    html = res.text
    soup = bs(html, 'html.parser')

    item_json = json.loads(soup.select_one('#__NEXT_DATA__').get_text())['props']['pageProps']['initialState']['products']['list']

    # f = open('navershopping_griptalk.csv', 'w', encoding='utf-8', newline='')
    # wr = csv.writer(f)
    # wr.writerow(['goods_name', 'txt'])
    item_href = []
    for i in item_json:
        item = i['item']
        # print(item['characterValue'])
        try:
            print(item['characterValue'])
            if len(item['characterValue']) > 1:
                f.write(item['characterValue'])
                f.write('\n')
        except:
            pass

f.close()

