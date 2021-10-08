# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def init_excel(path):
    data = pd.DataFrame({'序号': [1, 2, 3], '姓名':['张三', '李四', '王五']})
    data = data.set_index('序号')  # 设置索引列为'序号'列
    data.to_excel(path)


def sort_excel(path):
    data = pd.read_excel(path, index_col='序号')
    # data.sort_index(inplace=True)
    print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sort_excel('./src.xlsx')


