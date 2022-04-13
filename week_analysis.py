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


filepath = r'E:\Python_Projects\crawler_bili\data\合并最新.xlsx'

data = pd.read_excel(filepath)
df = pd.DataFrame(data)

def bar_v():
    sanlian_data = df[['coin','tname']].head(50)
    tname_data = sanlian_data['tname']
    coin_counts = sanlian_data['coin']

    fig1,ax = plt.subplots(figsize=(10,6),dpi=200)
    ax = sns.barplot(x='tname',y='coin',errwidth=0,data=sanlian_data, orient="v")

    plt.xlabel("视频分类")
    plt.ylabel("硬币数（万）")

    y=np.arange(0,3000000,150000)
    plt.xticks(rotation=60)
    plt.yticks(y,[format(i,',') for i in y])
    st.pyplot(fig1)


def bar_coin_counts():
    coin_list = []

    rc_data = df[df.tname == '日常']
    rc_coin_data = rc_data['coin'].sum()
    coin_list.append(rc_coin_data)

    gx_data = df[df.tname == '搞笑']
    gx_coin_data = gx_data['coin'].sum()
    coin_list.append(gx_coin_data)

    zh_data = df[df.tname == '综合']
    zh_coin_data = zh_data['coin'].sum()
    coin_list.append(zh_coin_data)

    ys_data = df[df.tname == '影视杂谈']
    ys_coin_data = ys_data['coin'].sum()
    coin_list.append(ys_coin_data)

    sm_data = df[df.tname == '数码']
    sm_coin_data = sm_data['coin'].sum()
    coin_list.append(sm_coin_data)

    colu = ['硬币数']
    ind = ['日常', '搞笑', '综合', '影视杂谈', '数码']

    coindf = pd.DataFrame(data=coin_list, index=ind, columns=colu)
    fig2, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax = sns.barplot(x=ind, y='硬币数', data=coindf, palette="deep")
    plt.xlabel("视频分类")
    plt.ylabel("硬币数（万）")

    y = np.arange(0, 30000000, 1500000)
    plt.xticks(rotation=60)
    plt.yticks(y, [format(i, ',') for i in y])
    st.pyplot(fig2)


def sanlian():
    sanlian_list = []

    rc_data = df[df.tname == '日常']
    rc_coin_data = rc_data['coin'].sum()
    rc_like_data = rc_data['like'].sum()
    rc_favor_data = rc_data['favorite'].sum()
    rc_sanlian_counts = rc_coin_data + rc_like_data + rc_favor_data
    # print(rc_sanlian_counts)
    # print(rc_coin_data)
    sanlian_list.append(rc_sanlian_counts)

    gx_data = df[df.tname == '搞笑']
    gx_coin_data = gx_data['coin'].sum()
    gx_like_data = gx_data['like'].sum()
    gx_favor_data = gx_data['favorite'].sum()
    gx_sanlian_counts = gx_coin_data + gx_like_data + gx_favor_data
    # print(gx_sanlian_counts)
    # print(gx_coin_data)
    sanlian_list.append(gx_sanlian_counts)

    zh_data = df[df.tname == '综合']
    zh_coin_data = zh_data['coin'].sum()
    zh_like_data = zh_data['like'].sum()
    zh_favor_data = zh_data['favorite'].sum()
    zh_sanlian_counts = zh_coin_data + zh_like_data + zh_favor_data
    # print(zh_coin_data)
    sanlian_list.append(zh_sanlian_counts)

    ys_data = df[df.tname == '影视杂谈']
    ys_coin_data = ys_data['coin'].sum()
    ys_like_data = ys_data['like'].sum()
    ys_favor_data = ys_data['favorite'].sum()
    ys_sanlian_counts = ys_coin_data + ys_like_data + ys_favor_data
    # print(ys_coin_data)
    sanlian_list.append(ys_sanlian_counts)

    sm_data = df[df.tname == '数码']
    sm_coin_data = sm_data['coin'].sum()
    sm_like_data = sm_data['like'].sum()
    sm_favor_data = sm_data['favorite'].sum()
    sm_sanlian_counts = sm_coin_data + sm_like_data + sm_favor_data
    sm_coin_data = sm_data['coin'].sum()
    # print(sm_coin_data)
    sanlian_list.append(sm_coin_data)

    # print(sanlian_list)

    colu = ['一键三连']
    ind = ['日常', '搞笑', '综合', '影视杂谈', '数码']

    data = {"视频分类": ['日常', '搞笑', '综合', '影视杂谈', '数码'],
            "一键三连": sanlian_list}
    sanliandf = pd.DataFrame(data)
    new_sanliandf = sanliandf.sort_values('一键三连', ascending=False)

    # 半年一键三连合计
    fig3, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax = sns.barplot(x='视频分类', y='一键三连', data=new_sanliandf, palette="deep")
    plt.xlabel("视频分类")
    plt.ylabel("一键三连（万）")

    y = np.arange(0, 300000000, 15000000)
    plt.xticks(rotation=60)
    plt.yticks(y, [format(i, ',') for i in y])
    st.pyplot(fig3)

if __name__ == '__main__':
    pass
