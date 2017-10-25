# -*- coding: utf-8 -*-
import pandas as pd
s = pd.Series([1,2,3],index=['a','b','c'])#创建一个序列
d = pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])#创建一个表
d2 = pd.DataFrame(s)#使用已有序列创建一个表格
print(d.head())#预览前5行数据
d.describe()#数据基本统计量

#读取文件。注意文件的存储路径不能带中文，否则可能读取出错
#pd.read_excel("")#读取execle文件，创建DataFrame。
#pd.read_csv("")#读取文本格式的数据，一般用encoding指定编码