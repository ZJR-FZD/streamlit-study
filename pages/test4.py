import streamlit as st

# 侧边栏
with st.sidebar:
    name = st.text_input("请输入你的名字：")
    if name:
        st.write(f"你好，{name}")

# 多列布局
# (column1,column2,column3) = st.columns(3) 将布局划分为三列，并且将这三列分别赋值给变量 column1、column2 和 column3
(column1,column2,column3) = st.columns([1,2,1]) #当st.columns()的参数是一个数字列表时，列表中的每个元素代表对应列的相对宽度

# 第一列里有什么（有缩进的才是）：
with column1:
    password=st.text_input("请输入密码：",type="password")

with column2:
    paragraph = st.text_area("请输入你的自我介绍：")

with column3:
    age=st.number_input("请输入你的年龄：",value=20,min_value=0,max_value=150,step=1)
    st.write(f"你的年龄是：{age}岁")

st.divider()


checked = st.checkbox("我同意以上条款") 
if checked:
    st.write("感谢您的同意！")

st.divider()


submitted = st.button("提交")
if submitted:
    st.write("提交成功！")