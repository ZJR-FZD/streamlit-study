import streamlit as st

if "a" not in st.session_state: # 如果a还没在会话状态中
    st.session_state.a=0 # 则把a加入会话状态，并赋值为0

clicked = st.button("加1")
if clicked:
    st.session_state.a += 1
st.write(st.session_state.a)   

print(st.session_state) #{'a': 10}