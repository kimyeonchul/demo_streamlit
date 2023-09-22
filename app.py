import openai
import streamlit as st

# OpenAI API 키 입력
api_key = st.text_input('OpenAI API Key')
if api_key:
    openai.api_key = api_key

# 번역할 언어 목록
lang_list = ('영어', '중국어', '일본어', '아랍어', '한국어')

st.header('번역기')

col1, col2 = st.columns(2)
result = ''
with col1:
    option = st.selectbox('Lang', lang_list)
    q = st.text_area('번역할 텍스트 입력')
    if q:
        # 번역을 위한 프롬프트 생성
        if option == '영어':
            target_lang = 'en'
        elif option == '중국어':
            target_lang = 'zh'
        elif option == '일본어':
            target_lang = 'ja'
        elif option == '아랍어':
            target_lang = 'ar'
        elif option == '한국어':
            target_lang = 'ko'
        
        prompt = f"번역: {target_lang} >> {q}"  # 프롬프트 생성

        # GPT-3 API를 사용하여 번역 요청
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None,
        )

        result = response.choices[0].text.strip()

with col2:
    st.text_area('번역 결과', value=result)
