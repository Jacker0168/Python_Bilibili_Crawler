import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
mpl.rcParams['font.size'] = 12  # 字体大小
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

top_data = pd.read_csv('./data/Top100.csv')
df = pd.DataFrame(top_data)

def pie():

    top_20 = top_data[['视频分类','播放量','点赞量']].head(20)
    value_20 = pd.Series(top_20['视频分类']).value_counts()
    myvalue_20 = pd.Series(top_20['视频分类'])

    # count_value = df['视频分类'].value_counts()
    myvalue_20 = pd.Series(top_20['视频分类']).value_counts()
    dupValue_20 = pd.Series(top_20['视频分类']).drop_duplicates()



    # 绘制饼状图
    fig = plt.figure(dpi=50)  # 创建空图
    plt.pie(myvalue_20, labels=dupValue_20, startangle=90, counterclock=False, autopct='%1.0f%%');

    plt.axis('equal')
    plt.title("热门视频排行榜前20名")  # 设置标题
    st.pyplot(fig)

# 综合热门前20 柱状图
def bar20():
    top_20_view = df[['视频分类','播放量']].head(20)
    newValue20 = top_20_view.sort_values(by="播放量", ascending=False)


    # classifyList = []
    # playCounts = []
    # classValue = pd.DataFrame(newValue20['视频分类'])
    # playValue = pd.DataFrame(newValue20['播放量'])

    fig1, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax = sns.barplot(x='播放量', y='视频分类', errwidth=0, data=newValue20, orient="h")

    plt.xlabel("播放量（百万）")
    plt.ylabel("视频分类")
    x = np.arange(0, 6000000, 1000000)
    plt.xticks(x, [format(i, ',') for i in x])
    st.pyplot(fig1)

# 综合热门前50
def bar50():

    top_50_view = df[['视频分类', '播放量']].head(50)
    # top_20
    newValue50 = top_50_view.sort_values(by="播放量", ascending=False)
    # newValue50

    fig2, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax = sns.barplot(x='播放量', y='视频分类', errwidth=0, data=newValue50, orient="h")

    plt.xlabel("播放量（百万）")
    plt.ylabel("视频分类")
    x = np.arange(0, 6000000, 1000000)
    plt.xticks(x, [format(i, ',') for i in x])
    st.pyplot(fig2)

def bar100():
    top_100_view = df[['视频分类', '播放量']].head(100)
    newValue100 = top_100_view.sort_values(by="播放量", ascending=False)

    fig3, ax = plt.subplots(figsize=(10,8), dpi=150)
    ax = sns.barplot(x='播放量', y='视频分类', errwidth=0, data=newValue100, orient="h")

    plt.title('综合热门前100', fontsize=20)
    plt.xlabel("播放量（百万）", fontsize=14)
    plt.ylabel("视频分类", fontsize=14)

    x = np.arange(0, 6000000, 1000000)
    plt.xticks(x, [format(i, ',') for i in x])
    st.pyplot(fig3)

if __name__ == '__main__':
    pie()
    bar20()
    bar50()
    bar100()