import streamlit as st

# 单选按钮
gender = st.radio("你的性别是什么", 
               ["男性","女性","跨性别"], #options选项：可迭代对象，列表或元组
               index=None) #index设置初始选中的选项索引，默认为0，设置等于None值时无初始设置
if gender:
    st.write(f"你选择的性别是{gender}")

st.divider()

# 单选框
contact = st.selectbox("你希望通过什么方式联系？",
             ["微信","QQ","邮箱","电话","其它"])
st.write(f"好的，我们会通过{contact}联系你")

st.divider()

# 多选框
fruits = st.multiselect("你喜欢的水果是什么？",
                        ["苹果","西瓜","橙子","香蕉"]) #返回的是选中元素组成的列表
for fruit in fruits:
    st.write(f"你选择的水果是{fruit}")

st.divider()


# 滑块（通过拖动来选择数字）
height = st.slider("你的身高是多少厘米？",value=160.0,
          min_value=100.0,max_value=230.0,step=0.5)
st.write(f"你的身高是{height}厘米")

st.divider()


# 文件上传器
uploaded_file = st.file_uploader("请上传你的文件",
                 type=["py"]) #type参数限制了可以上传的文件类型，"py"表示python代码文件
## 如果用户没有上传文件，uploaded_file 的值为 None；如果用户上传了文件，uploaded_file 是 UploadedFile 类的一个实例，该实例包含了上传文件的相关信息，如文件名、文件内容等。
if uploaded_file:
    st.write(f"你上传的文件是{uploaded_file.name}")
    st.write(f"文件内容如下：{uploaded_file.read().decode('utf_8')}")
## uploaded_file.read() 是 UploadedFile 类的一个方法，用于读取上传文件的内容。该方法返回一个字节字符串（bytes 类型），表示文件的二进制内容。
## 由于 uploaded_file.read() 返回的是字节字符串，如果文件是文本文件，在显示时可能需要进行解码操作，例如使用 uploaded_file.read().decode('utf-8') 将字节字符串解码为 Unicode 字符串，以确保中文等非 ASCII 字符能够正确显示。