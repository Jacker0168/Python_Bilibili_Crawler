''' 每周必看 '''

import requests
import pandas as pd


def getUrl(url):
    # 请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    }
    # 解析url
    html = requests.get(url, headers=header).json()
    # 返回json数据
    return html


def getData(html):
    # 从json中取出需要的数据
    data = html['data']['list']
    # 转成DataFrame格式
    datadf = pd.DataFrame(data)

    stat_list = []
    for i in range(0, len(data)):
        stat = html['data']['list'][i]['stat']
        stat_list.append(stat)

    # print(type(stat))
    statdf = pd.DataFrame(stat_list)

    # 获取期数
    number = html['data']['config']['number']


    # 从data取出想要的字段以及对应数据
    weeklydf = datadf[['title', 'tname', "bvid", 'desc', 'dynamic', 'rcmd_reason', ]]
    # 拼接动画链接
    # weeklydf['bvid'] = 'https://www.bilibili.com/video/' + weeklydf['bvid']
    return weeklydf,statdf,number

def week_run():
    for i in range(116, 146):
        url = 'https://api.bilibili.com/x/web-interface/popular/series/one?number={}'.format(i)
        html = getUrl(url)
        weeklydf,statdf, number = getData(html)
        # 索引从1开始
        weeklydf.index = weeklydf.index + 1
        statdf.index = statdf.index + 1
        print('合并数据中...')
        newData = pd.concat([weeklydf, statdf], axis=1)

        newData.to_excel('E:\\Python_Projects\\crawler_bili\\data\\每周必看\\' + str(number) + '.xlsx')
    print('爬取完成！')

if __name__ == '__main__':
    week_run()

