import streamlit as st

# 创建标签页界面的函数。它接收一个列表作为参数，列表中的每个元素代表一个标签页的标题。
# 返回值是一个包含多个标签页对象的元组
(tab1,tab2,tab3) = st.tabs(["性别","联系方式","喜好水果"])

with tab1:
    gender = st.radio("你的性别是什么", 
                ["男性","女性","跨性别"], 
                index=None) 
    if gender:
        st.write(f"你选择的性别是{gender}")


with tab2:
    contact = st.selectbox("你希望通过什么方式联系？",
                ["微信","QQ","邮箱","电话","其它"])
    st.write(f"好的，我们会通过{contact}联系你")


with tab3:
    fruits = st.multiselect("你喜欢的水果是什么？",
                            ["苹果","西瓜","橙子","香蕉"]) 
    for fruit in fruits:
        st.write(f"你选择的水果是{fruit}")

st.divider()

# 折叠展开组件：展示非关键信息，平时折叠，需要时展开，提高页面上的信息展示效率
# with st.expander("展开区域标题"):
with st.expander("身高信息"):
    height = st.slider("你的身高是多少厘米？",value=160.0,
            min_value=100.0,max_value=230.0,step=0.5)
    st.write(f"你的身高是{height}厘米")

st.divider()


uploaded_file = st.file_uploader("请上传你的文件",
                 type=["py"]) 
if uploaded_file:
    st.write(f"你上传的文件是{uploaded_file.name}")
    st.write(f"文件内容如下：{uploaded_file.read().decode('utf_8')}")
