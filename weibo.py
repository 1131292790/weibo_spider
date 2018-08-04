from urllib.parse import urlencode
import requests
import os
base_url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304135554309791_-_WEIBO_SECOND_PROFILE_WEIBO'
headers={
'Connection':'keep-alive',
'Cookie':'T_WM=5859d26744a2e87b4895ecb2d76ab7f6; WEIBOCN_FROM=1110006030; SSOLoginState=1533348450; ALF=1535940450; SCF=Au4hpLHTSzOxiHUCTbQzf6_GW1R9ifjVV4ME9BuX2SRUTQsHsmpFPjQQAoAiwIebzdEz1Llq0EdxbjBwfin3XbY.; SUB=_2A252YXoyDeRhGeNM7VQU-CnEyzuIHXVVqgZ6rDV6PUNbktAKLWPskW1NThIKTGDGrTSQASWjPLlQ5RME2qlTgzW3; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFj4I5ljA1-euY6rqKnUI.v5JpX5KMhUgL.Fo-ESoqf1hMRehM2dJLoIX-LxKMLBK-L1--LxK-L1-eLBKeLxKBLBonL12BLxK-L12qLB-qLxKBLB.-LBo-LxKML122LB-qLxKML1-2L1hx.qg4D9g7t; SUHB=0z1wHeFgPLbHMD; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174%26lfid%3D2304135266587807_-_WEIBO_SECOND_PROFILE_WEIBO%26uicode%3D20000174',
'Host':'m.weibo.cn',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
}
def parse_one(url):
    response = requests.get(url,headers=headers)
    json = response.json()
    cards = json.get('data').get('cards')
    for card in cards:
        try:
        #赞数
            comments_count = card.get('mblog').get('comments_count')
        #发布内容
            text = card.get('mblog').get('text')
        #发布时间
            created_at = card.get('mblog').get('created_at')
        #转发数
            reposts_count = card.get('mblog').get('reposts_count')
        except AttributeError:
            continue
        try:
            pics = card.get('mblog').get('pics')
            for pic in pics:
                # 图片链接
                pic_id = pic.get('pid')
                pic_url = pic.get('url')
                pic_source = requests.get(pic_url).content
                with open(pic_id + '.jpg', 'wb') as p:
                    p.write(pic_source)
        except TypeError:
            pass
        print(comments_count,created_at,reposts_count)

def get_page(page):
    params = {
        'page_type':'03',
        'page':page,
    }
    url = base_url + urlencode(params)
    parse_one(url)

def parse_index():
    try:
        parse_one(base_url)
    except AttributeError:
        pass
parse_index()