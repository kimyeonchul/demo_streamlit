import openai
import streamlit as st

api_key = st.text_input('openai api key')
if api_key:
    openai.api_key = api_key

lang_list = ('영어', '중국어', '일본어', '아랍어', '한국어')

st.header('번역기')

col1, col2 = st.columns(2)
result = ''
with col1:
    option = st.selectbox('Lang', lang_list)
    q = st.text_area('From')
    if q:

				# :+:+:+:+: prompt format 을 만들어보세요 :+:+:+:+:
				# option = 영어, 중국어.. 중 하나 
				# q = 입력 문구
        prompt = q # <- 코드를 수정하세요

        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0,
            max_tokens=100,
            top_p=1,
        )
        print(response.choices[0].text.strip())
        result = response.choices[0].text.strip()

with col2:
    st.text_area('To', value=result)