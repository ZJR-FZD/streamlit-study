import streamlit as st

# 文字输入
name = st.text_input("请输入你的名字：")
if name:
    st.write(f"你好，{name}")

st.divider()

# 将text_input的type值定为password，就是输入密码了
password=st.text_input("请输入密码：",type="password")

st.divider()

# 输入长文本，要用到大区域，可以手动调节文本框的长度
paragraph = st.text_area("请输入你的自我介绍：")

st.divider()

# 数字输入
age=st.number_input("请输入你的年龄：",value=20,min_value=0,max_value=150,step=1)
st.write(f"你的年龄是：{age}岁")

st.divider()

# 勾选框
checked = st.checkbox("我同意以上条款") # 勾选了就返回true，否则是false
if checked:
    st.write("感谢您的同意！")

st.divider()

# 按钮
submitted = st.button("提交")
if submitted:
    st.write("提交成功！")