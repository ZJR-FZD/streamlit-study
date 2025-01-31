import streamlit as st
import pandas as pd

# 可以传markdown语法的参数
st.write("### 新年快乐")

# 省略.write也可以直接打印
123

a=10
a

[11,22,33]

{"a":"1","b":"2","c":3}

# 大标题
st.title("我的个人网站💡")

# 图片
st.image("E:\streamlit\source\image.png",width=300)

# 表格
data={ #创建一个包含学生信息的字典（键是列名）
    '姓名': ['张三', '李四', '王五'],
    '年龄': [20, 21, 22],
    '成绩': [85, 90, 78]
}

df=pd.DataFrame(data) #使用字典创建DataFrame

st.dataframe(df) #显示表格，直接写df也可以————交互式表格
df

st.divider() #分割线

st.table(df) #非交互式静态表格



