'''排行榜'''
import bilibili_api
import requests
import os
import csv
from bilibili_api import video, sync

POPULAR_URL = "https://api.bilibili.com/x/web-interface/popular"
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.bilibili.com/',
    'x-csrf-token': '',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': ''
    ,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


def method_get_videos_info(bvid):
    # 实例化 Video 类
    v = video.Video(bvid=bvid)
    # 获取视频信息
    info = sync(v.get_info())
    return info


def get_popular_list():
    """
    获取排行榜1-100
    :param pn:
    :return: All bvid_list
    """
    bvidList = []
    for i in range(1, 6):
        query = "pn=" + str(i)
        r = requests.get(POPULAR_URL, headers=HEADERS, params=query)
        resultList = r.json()['data']['list']
        for item in resultList:
            bvidList.append(
                bilibili_api.aid2bvid(
                    item['aid']
                )
            )
    return bvidList


def method_save_to_csv(filename_last, video_info):
    file_path = ("./data/%s.csv" % filename_last)
    # 判断路径是否存在
    if not os.path.exists("./data/"):
        os.makedirs("./data/")
    # 如果文件存在，则覆盖写入
    f = open(file_path, mode="w", encoding='utf-8', newline='')
    csv_writer1 = csv.DictWriter(f,
                                 fieldnames=[
                                     '视频bvid', '视频aid', 'videos', '视频分类', '版权所有',
                                     '视频封面', '视频标题', '上传时间', '公开时间', '视频描述',
                                     '播放量', '点赞量']
                                 )
    csv_writer1.writeheader()
    for info in video_info:
        info = method_get_videos_info(info)
        data_dict1 = {
            '视频bvid': info.get('bvid', "None"),
            '视频aid': info.get('aid', "None"),
            'videos': info.get('videos', "None"),
            '视频分类': info.get('tname', "None"),
            '版权所有': info.get('copyright', "None"),
            '视频封面': info.get('pic', "None"),
            '视频标题': info.get('title', "None"),
            '上传时间': info.get('ctime', "None"),
            '公开时间': info.get('pubdate', "None"),
            '视频描述': info.get('desc', "None"),
            '播放量': info.get('stat', "None").get('view', "None"),
            '点赞量': info.get('stat', "None").get('like', "None"),
            # '目录': info.get('rcmd_reason', "None").get('content', "None")
        }
        # print(data_dict1['播放量'])
        csv_writer1.writerow(data_dict1)
    f.close()


def top_run():
    print('正在爬取数据...')
    method_save_to_csv('Top100', get_popular_list())
    print('爬取完成！')

if __name__ == '__main__':
    top_run()