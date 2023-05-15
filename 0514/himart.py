import requests
from bs4 import BeautifulSoup as bs
import json
import time
import csv
from random import randrange, random
from math import ceil

url = "http://www.e-himart.co.kr/app/display/bestStore/Ajax?dispLrgNo=1015000000&dispMidNo=1015020000&setNo=4"
res = requests.get(url)
soup = bs(res.text, 'html.parser')

items = soup.select('.prdItem > a')
item_href = []

for i in items:
    item_href.append(i['href'])

f = open('himart.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['item_name', 'item_price', 'item_max_discounted_price', 'user_id', 'star_rating', 'review_date', 'review_cont', 'img_addrs_str'])


def getItemReviewCount(item_url):
    item_no = item_url[-10:]

    cookies = {
        'citrusSessionId': 'ci20230503050543404',
        'PCID': '16831011476990572642776',
        'RB_PCID': '1683101147736290590',
        '_gid': 'GA1.3.448942796.1683101148',
        'MyKeywordWN': '',
        '__fromShop': 'drfKEAqUevBLU9udVTNIP+9bOVDiipBAltSBc2J7hFFyB3ma9p5KQIHk1+o1AfifpVq6p0DYPInFeRQnJBsK7S/Cjg+4tONb7Yjcf956yFGHAwNTQ6PHypuwfrwNKK4YVeAtyHF8SJFdRIcduS/wAA==',
        'EG_GUID': '57d62c95-a2c3-48ff-8093-647d14a02b28',
        '_fbp': 'fb.2.1683101150172.591782888',
        '_gac_UA-86296807-1': '1.1683101151.CjwKCAjwjMiiBhA4EiwAZe6jQ6h-0NDYWQ2EUg18FNuBbCbh5c0tpiLnXeeUJg3_QN2ZNstoHO7ckhoC7poQAvD_BwE',
        'PCID': '16831011476990572642776',
        'JSESSIONID': '5257a3a0-e989-11ed-b755-0050569d70a3',
        '_wp_uid': '2-3c65acdcad044243d60828314e9799a6-s1683101150.88568|windows_10|chrome-1owtg2j',
        'himartGoods': '0016433371:0019837180:0001380570:',
        'cto_bundle': 'ESx0q19JNEx4dFdLJTJGcmhlcnFXdWQ4bGd4SmNrTlJ1UVJxODhrUTNhJTJGNVVQJTJGcU1sJTJGM3VkczBHWG9oQzJJZmFYRjRlcVdlUkVoMXBOOXJLcG9YUTdUSEdxaVRZUzVWWFVIaDVaMVUwU3MyeVh6cXUlMkZTZ2VhN3gxTndNcEg3TFd3RUlRN0tnMkZ3ZkR4OWhBYkd2cU5MT0pEak1nJTNEJTNE',
        '_ga': 'GA1.3.685011081.1683101148',
        '_ga_YQ83MQRW9Z': 'GS1.1.1683101150.1.1.1683102875.4.0.0',
        'wcs_bt': 's_2cafe37f3587:1683102875',
        'RB_SSID': 'oSCivqcFXI',
        '_dc_gtm_UA-86296807-1': '1',
        # '__csFP': 'JfchYMpLlYooTTqxvWCzO7WJKqSudW3eCOyhLAKxCr0bLwmfBsqjM+cI6rNR/BuF7ZbNguI++AvabqtJ2PXq92YMie5JHtmb/y2IC2Yb1czUCxqNF396pofco7wggqHXi4SDiXSqi6QQ+yCzbbRT0r1rdfTy9n69bQ5dOUU8mV5cB2UK3ac5bY/7djBakwRi5ZhjHBXVf/6Ht3rJ+Nk3cV+FgIURTEjW6akZKof4zvkXT37/EE6yT30Yt6GU3XRsjsrRkCW4Xe8flLc0c2kxhFlKlYYuSuH+bP5/pOPJ1pm6pmjiWSzC3q/2xYMvQaf89rM3sLEJpZfIqyksMUB4XpLQdxHnULe/odMvG6ZN7UEX6pmM+XyptzRsVqSurJeL9X/JiUo56b1IMvCr2kN8vSCo2ndkmNUXYZ2WrQtOTCUBSqE61gshvIT2C+UMb+yS374vqajafP2rfi3Y6chNhw==',
        'TS0154a0aa': '0194c11545336c6a1fdeece0d0cdeee2e6239d7d1518b16b3e3cbabb6dd122ebc1c97546ffb25ef9ca734d8cd0bbc681f2022e4dc6',
        'TS015866e0': '0194c11545fb94c27c78711ecd55ef89fb2a964abe55d547934a7fdfed58b7949bb2446a05e24d15a633774c48f8f5f54a089b826a8c5a79f95301edb35591f9f7ad4b783642c3d4517e3c35c1b2883a6c7060a6c35771fb6a518420f39576dac4d0a9b96d',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'citrusSessionId=ci20230503050543404; PCID=16831011476990572642776; RB_PCID=1683101147736290590; _gid=GA1.3.448942796.1683101148; MyKeywordWN=; __fromShop=drfKEAqUevBLU9udVTNIP+9bOVDiipBAltSBc2J7hFFyB3ma9p5KQIHk1+o1AfifpVq6p0DYPInFeRQnJBsK7S/Cjg+4tONb7Yjcf956yFGHAwNTQ6PHypuwfrwNKK4YVeAtyHF8SJFdRIcduS/wAA==; EG_GUID=57d62c95-a2c3-48ff-8093-647d14a02b28; _fbp=fb.2.1683101150172.591782888; _gac_UA-86296807-1=1.1683101151.CjwKCAjwjMiiBhA4EiwAZe6jQ6h-0NDYWQ2EUg18FNuBbCbh5c0tpiLnXeeUJg3_QN2ZNstoHO7ckhoC7poQAvD_BwE; PCID=16831011476990572642776; JSESSIONID=5257a3a0-e989-11ed-b755-0050569d70a3; _wp_uid=2-3c65acdcad044243d60828314e9799a6-s1683101150.88568|windows_10|chrome-1owtg2j; himartGoods=0016433371:0019837180:0001380570:; cto_bundle=ESx0q19JNEx4dFdLJTJGcmhlcnFXdWQ4bGd4SmNrTlJ1UVJxODhrUTNhJTJGNVVQJTJGcU1sJTJGM3VkczBHWG9oQzJJZmFYRjRlcVdlUkVoMXBOOXJLcG9YUTdUSEdxaVRZUzVWWFVIaDVaMVUwU3MyeVh6cXUlMkZTZ2VhN3gxTndNcEg3TFd3RUlRN0tnMkZ3ZkR4OWhBYkd2cU5MT0pEak1nJTNEJTNE; _ga=GA1.3.685011081.1683101148; _ga_YQ83MQRW9Z=GS1.1.1683101150.1.1.1683102875.4.0.0; wcs_bt=s_2cafe37f3587:1683102875; RB_SSID=oSCivqcFXI; _dc_gtm_UA-86296807-1=1; __csFP=JfchYMpLlYooTTqxvWCzO7WJKqSudW3eCOyhLAKxCr0bLwmfBsqjM+cI6rNR/BuF7ZbNguI++AvabqtJ2PXq92YMie5JHtmb/y2IC2Yb1czUCxqNF396pofco7wggqHXi4SDiXSqi6QQ+yCzbbRT0r1rdfTy9n69bQ5dOUU8mV5cB2UK3ac5bY/7djBakwRi5ZhjHBXVf/6Ht3rJ+Nk3cV+FgIURTEjW6akZKof4zvkXT37/EE6yT30Yt6GU3XRsjsrRkCW4Xe8flLc0c2kxhFlKlYYuSuH+bP5/pOPJ1pm6pmjiWSzC3q/2xYMvQaf89rM3sLEJpZfIqyksMUB4XpLQdxHnULe/odMvG6ZN7UEX6pmM+XyptzRsVqSurJeL9X/JiUo56b1IMvCr2kN8vSCo2ndkmNUXYZ2WrQtOTCUBSqE61gshvIT2C+UMb+yS374vqajafP2rfi3Y6chNhw==; TS0154a0aa=0194c11545336c6a1fdeece0d0cdeee2e6239d7d1518b16b3e3cbabb6dd122ebc1c97546ffb25ef9ca734d8cd0bbc681f2022e4dc6; TS015866e0=0194c11545fb94c27c78711ecd55ef89fb2a964abe55d547934a7fdfed58b7949bb2446a05e24d15a633774c48f8f5f54a089b826a8c5a79f95301edb35591f9f7ad4b783642c3d4517e3c35c1b2883a6c7060a6c35771fb6a518420f39576dac4d0a9b96d',
        'Origin': 'http://www.e-himart.co.kr',
        'Referer': 'http://www.e-himart.co.kr/app/goods/goodsDetail?goodsNo={}'.format(item_no),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'goodsNo': item_no,
        'goodsCmpsCode': '01',
    }
    res = requests.post(
        'http://www.e-himart.co.kr/app/goods/reviewSummaryAjax',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    print(res.text)
    return json.loads(res.text)['gdasTotalCnt']

def getItemReview(item_url):
    item_no = item_url[-10:]
    url = "http://www.e-himart.co.kr{}".format(item_url)
    html = requests.get(url).text
    soupp = bs(html, 'html.parser')
    item_name = soupp.select_one('.detailHeader h2').get_text().lstrip().rstrip()
    item_price = int(soupp.select_one('.price').get_text().replace(',', ''))
    item_max_discounted_price = 0
    try:
        item_max_discounted_price = int(soupp.select('.price')[1].get_text().replace(',', ''))
    except:
        item_max_discounted_price = item_price


    cookies = {
        'citrusSessionId': 'ci20230503050543404',
        'PCID': '16831011476990572642776',
        'RB_PCID': '1683101147736290590',
        '_gid': 'GA1.3.448942796.1683101148',
        'MyKeywordWN': '',
        '__fromShop': 'drfKEAqUevBLU9udVTNIP+9bOVDiipBAltSBc2J7hFFyB3ma9p5KQIHk1+o1AfifpVq6p0DYPInFeRQnJBsK7S/Cjg+4tONb7Yjcf956yFGHAwNTQ6PHypuwfrwNKK4YVeAtyHF8SJFdRIcduS/wAA==',
        'EG_GUID': '57d62c95-a2c3-48ff-8093-647d14a02b28',
        '_fbp': 'fb.2.1683101150172.591782888',
        '_gac_UA-86296807-1': '1.1683101151.CjwKCAjwjMiiBhA4EiwAZe6jQ6h-0NDYWQ2EUg18FNuBbCbh5c0tpiLnXeeUJg3_QN2ZNstoHO7ckhoC7poQAvD_BwE',
        'PCID': '16831011476990572642776',
        'JSESSIONID': '5257a3a0-e989-11ed-b755-0050569d70a3',
        '_wp_uid': '2-3c65acdcad044243d60828314e9799a6-s1683101150.88568|windows_10|chrome-1owtg2j',
        'himartGoods': '0016433371:0019837180:0001380570:',
        'JSESSIONID': 'xwLl1zfpfEaKtR00bAf1Rns3jBeuYvaK2VYCHXjxlDwRPSjSxyu7pC1qA5hac2ov.Zm9fZG9tYWluL0ZPMg==',
        '_dc_gtm_UA-86296807-1': '1',
        'TS0154a0aa': '0194c115459f90274db138d5cfe901f058b97d43b1f3363ce1e143572366c1e6599cea62d1be83e42dc3ea175ffcd523e6c6f48d11',
        'cto_bundle': 'twSttl9JNEx4dFdLJTJGcmhlcnFXdWQ4bGd4SmNtclkzUkx2VElOcGZuY3hXSTFqS3RDdjFlYlF1eWY1OE1BMmtXS0FRcXl5d3Bob3R5bFNyNzNGZ29va0lMeEJLSDR6VXZ2bXZhbWZSTUQ4NnRmZHUwczhNWjlTMFpYWk53TGsyRVl6OWd5YWVWNVElMkZucEFlJTJGZzBQT2dYMVlqWFElM0QlM0Q',
        '_ga_YQ83MQRW9Z': 'GS1.1.1683101150.1.1.1683105160.60.0.0',
        'wcs_bt': 's_2cafe37f3587:1683105160',
        '_ga': 'GA1.3.685011081.1683101148',
        'RB_SSID': 'oSCivqcFXI',
        '__csFP': 'JfchYMpLlYooTTqxvWCzO4k5IUSrwWfvf8Lf0PL+88GpjoNu8YuqnG+rIGTaWcZIh1zfoDUguMwuz/UWQiOE+C/ui4IHXHM1MZ4CLM+t7JCIeK3cnMufBTOuhuW0asOKNZoVKzhgKF+g98g2ttBCFzODngP6N/jq89MGwBwExIIrP5MSAFGFOhRTBSu2mN2dN8fzAvxiadLR0LvzHzTIfJpZalgJy4qkTkN8jppvJfocSE5sto4rpeNGKDCIGCwIx+JWV0AtTXOJa3qkmB3jgekRTGSlAt8jNT93giOAYxBVL4aMeHKIrA3ptQGf4lYsK1AfRKW6cQrAp0Nc9FL0kZciBxAYyozkx5T8Lxt9IVZXY/5JaWeekr/0th0vbpXroyrOIfaZZqO559TYe3H79+lSbScEtLH5wqD+wiefbHwttMf8EzZEY26Vm/b1GXN4rxcIl1u09Rvz99sn7/cDvg==',
        'TS015866e0': '0194c11545b42b0f9ddae614aa34796606384511d655d547934a7fdfed58b7949bb2446a052343161a64dbde526e77b9eac22888d097358a72f0cd83dd4ccc75b34cc2f175eaa739fd13951f1d849eced19c88b62fa91c7e314607d4804557ee7e77f8df10',
    }
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'citrusSessionId=ci20230503050543404; PCID=16831011476990572642776; RB_PCID=1683101147736290590; _gid=GA1.3.448942796.1683101148; MyKeywordWN=; __fromShop=drfKEAqUevBLU9udVTNIP+9bOVDiipBAltSBc2J7hFFyB3ma9p5KQIHk1+o1AfifpVq6p0DYPInFeRQnJBsK7S/Cjg+4tONb7Yjcf956yFGHAwNTQ6PHypuwfrwNKK4YVeAtyHF8SJFdRIcduS/wAA==; EG_GUID=57d62c95-a2c3-48ff-8093-647d14a02b28; _fbp=fb.2.1683101150172.591782888; _gac_UA-86296807-1=1.1683101151.CjwKCAjwjMiiBhA4EiwAZe6jQ6h-0NDYWQ2EUg18FNuBbCbh5c0tpiLnXeeUJg3_QN2ZNstoHO7ckhoC7poQAvD_BwE; PCID=16831011476990572642776; JSESSIONID=5257a3a0-e989-11ed-b755-0050569d70a3; _wp_uid=2-3c65acdcad044243d60828314e9799a6-s1683101150.88568|windows_10|chrome-1owtg2j; himartGoods=0016433371:0019837180:0001380570:; JSESSIONID=xwLl1zfpfEaKtR00bAf1Rns3jBeuYvaK2VYCHXjxlDwRPSjSxyu7pC1qA5hac2ov.Zm9fZG9tYWluL0ZPMg==; _dc_gtm_UA-86296807-1=1; TS0154a0aa=0194c115459f90274db138d5cfe901f058b97d43b1f3363ce1e143572366c1e6599cea62d1be83e42dc3ea175ffcd523e6c6f48d11; cto_bundle=twSttl9JNEx4dFdLJTJGcmhlcnFXdWQ4bGd4SmNtclkzUkx2VElOcGZuY3hXSTFqS3RDdjFlYlF1eWY1OE1BMmtXS0FRcXl5d3Bob3R5bFNyNzNGZ29va0lMeEJLSDR6VXZ2bXZhbWZSTUQ4NnRmZHUwczhNWjlTMFpYWk53TGsyRVl6OWd5YWVWNVElMkZucEFlJTJGZzBQT2dYMVlqWFElM0QlM0Q; _ga_YQ83MQRW9Z=GS1.1.1683101150.1.1.1683105160.60.0.0; wcs_bt=s_2cafe37f3587:1683105160; _ga=GA1.3.685011081.1683101148; RB_SSID=oSCivqcFXI; __csFP=JfchYMpLlYooTTqxvWCzO4k5IUSrwWfvf8Lf0PL+88GpjoNu8YuqnG+rIGTaWcZIh1zfoDUguMwuz/UWQiOE+C/ui4IHXHM1MZ4CLM+t7JCIeK3cnMufBTOuhuW0asOKNZoVKzhgKF+g98g2ttBCFzODngP6N/jq89MGwBwExIIrP5MSAFGFOhRTBSu2mN2dN8fzAvxiadLR0LvzHzTIfJpZalgJy4qkTkN8jppvJfocSE5sto4rpeNGKDCIGCwIx+JWV0AtTXOJa3qkmB3jgekRTGSlAt8jNT93giOAYxBVL4aMeHKIrA3ptQGf4lYsK1AfRKW6cQrAp0Nc9FL0kZciBxAYyozkx5T8Lxt9IVZXY/5JaWeekr/0th0vbpXroyrOIfaZZqO559TYe3H79+lSbScEtLH5wqD+wiefbHwttMf8EzZEY26Vm/b1GXN4rxcIl1u09Rvz99sn7/cDvg==; TS015866e0=0194c11545b42b0f9ddae614aa34796606384511d655d547934a7fdfed58b7949bb2446a052343161a64dbde526e77b9eac22888d097358a72f0cd83dd4ccc75b34cc2f175eaa739fd13951f1d849eced19c88b62fa91c7e314607d4804557ee7e77f8df10',
        'Origin': 'http://www.e-himart.co.kr',
        'Referer': 'http://www.e-himart.co.kr/app/goods/goodsDetail?goodsNo={}'.format(item_no),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'goodsNo': item_no,
        'goodsCmpsCode': '01',
        'satisfiedOrderYn': 'Y',
        'optionalCondition': '',
        'starPoint': '',
        'reviewYn': '',
        'page': '2',
        'size': '10',
        'selectedGoodsNo': '',
    }

    review_no = getItemReviewCount(item_url)
    for i in range(ceil(review_no//10)+1):
        data['page'] = str(i)
        res = requests.post(
            'http://www.e-himart.co.kr/app/goods/findListGoodsAssessment/ajax',
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False,
        )
        soup2 = bs(res.text, 'html.parser')
        review_items = soup2.select('.product_review')

        for ri in review_items:
            soup3 = bs(str(ri), 'html.parser')
            user_id = soup3.select_one('.idArea').get_text().lstrip().rstrip()
            star_rating = int(soup3.select_one('.score')['style'][-4:-2])//20
            if star_rating == 0:
                star_rating = 5
            review_date = soup3.select_one('.dateArea').get_text()
            review_cont = soup3.select_one('.new_userCon').get_text().lstrip().rstrip()
            img_addr_li = soup3.select('.btnViewImg > img')
            img_addrs = []
            for i in img_addr_li:
                img_addrs.append(i['onerror'][21:-16])
            img_addrs_str = '|'.join(img_addrs)
            #print(item_name, item_price, item_max_discounted_price, user_id, star_rating, review_date, review_cont, img_addrs_str)
            wr.writerow([item_name, item_price, item_max_discounted_price, user_id, star_rating, review_date, review_cont, img_addrs_str])


for iurl in item_href:
    print(iurl)
    getItemReview(iurl)
f.close()
