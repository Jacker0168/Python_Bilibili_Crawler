'''每周必看每期合并sheet'''
import os
import pandas as pd
# 定义根目录
src_path = r'E:\Python_Projects\crawler_bili\data\每周必看'
# 定义一个空列表来存所有的excel
excels = []
def excel_sheet_collect():
    for episode in os.listdir(src_path):
        # 这里是每一个省份的
        province_path = os.path.join(src_path, episode)
        # print(province_path)
        excels.append(os.path.join(province_path))
    # print(excels)

    with pd.ExcelWriter(r'E:\Python_Projects\crawler_bili\data\每周必看合并.xlsx', engine='xlsxwriter') as writer:
        for ex in excels:
            df = pd.read_excel(ex, sheet_name=0)

            filename = os.path.splitext(os.path.split(ex)[-1])[0]
            df = df.rename(columns={'Unnamed: 0':'index'})

            df.to_excel(writer, sheet_name=filename, index=False)
        # print(filename)
    print('sheet合并完成！')

'''每周必看每期总合并'''
def excel_total_collect():
    dfs = [pd.read_excel("E:\Python_Projects\crawler_bili\data\每周必看合并.xlsx",sheet_name=index) for index in range(30)]

    pd.concat(dfs).to_excel("E:\Python_Projects\crawler_bili\data\合并最新.xlsx",index=False)

    xls_data = pd.read_excel("E:\Python_Projects\crawler_bili\data\合并最新.xlsx")
    xls_data.drop('index',axis=1,inplace=True)
    # xls_data.set_index('index',inplace=True)
    xls_data.to_excel("E:\Python_Projects\crawler_bili\data\合并最新.xlsx",index=False)


    print('总合并完成！')