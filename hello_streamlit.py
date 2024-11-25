import streamlit as st

st.write('Hello World!')

import streamlit as st
st.header('st.button')

if st.button('Say hello'):
    st.write("Why hello there")
else:
    st.write('Goodbye')

st.header('st.slider')
st.subheader('slider')
like=st.slider('가은이를 얼만큼 조아하시나요',0,200,100)
st.write("바로바로",like,'이만큼~~~~~')

emotion=st.slider('오늘 기분은 몇 점??',0,100,0)
st.write("오늘 기분",emotion,'점~~~~~ 힘을 내세용')

option=st.selectbox('가장 좋아하는 음식은?',('방어','타코','삼겹살'))
st.write("당신이 제일 좋아하는 음식은",option,'입니당')

st.write("다음 간식 중 가장 맛있는 것은?")

icecream=st.checkbox('아이스크림')
coffee=st.checkbox('커피')
cola=st.checkbox('콜라')