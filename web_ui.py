import time
import streamlit as st
from video_hot import top_run
from video_week import week_run
from top_analysis import pie, bar20, bar100, bar50
from week_analysis import bar_v, sanlian, bar_coin_counts
from excel_collection import excel_sheet_collect, excel_total_collect
st.title('基于Python的视频数据分析系统')



st.sidebar.title("菜单栏")
mode = ['日热门榜','每周必看']
option = st.sidebar.selectbox('选择',range(len(mode)), format_func=lambda x: mode[x])



st.sidebar.success("请选择界面")
if option == 0:
    # st.markdown(intro_text, unsafe_allow_html=True)
    if st.button('开始爬取'):
        top_run()
        st.text('爬取完成!')

    pie_box = st.sidebar.checkbox('热门前20个数')
    bar20_box = st.sidebar.checkbox('热门前20播放')
    bar50_box = st.sidebar.checkbox('热门前50播放')
    bar100_box = st.sidebar.checkbox('热门前100播放')
    if st.button('一键分析'):
        if pie_box:
            pie()
        if bar50_box:
            bar50()
        if bar20_box:
            bar20()
        if bar100_box:
            bar100()


if option == 1:
    if st.button('开始爬取'):
        week_run()
        st.text('合并数据中...')
        excel_sheet_collect()
        excel_total_collect()
        time.sleep(3)
        st.text('爬取完成！')


    bar50_v_box = st.sidebar.checkbox('每周必看前50硬币数')
    coin_box = st.sidebar.checkbox('热门分类硬币数')
    sanlian_box = st.sidebar.checkbox('热门分类三连总数')

    if st.button('一键分析'):
        if bar50_v_box:
            bar_v()
        if coin_box:
            bar_coin_counts()
        if sanlian_box:
            sanlian()



