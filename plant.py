import streamlit as st
import requests

ENDPOINT_LAMBDA_URL = "YOUR LAMBDA FUNCTION URL"

# Streamlit 애플리케이션 시작
st.title("어떤 식물이 궁금하신가요?")

# 사용자 입력 받기
query = st.text_input("식물 이름을 입력하세요.")

# 사용자가 입력한 식물 정보 가져오기
if query:
    # Lambda 함수에 요청 보내기
    response_raw = requests.post(ENDPOINT_LAMBDA_URL, json={"query": query})
    response_json = response_raw.json()
    
    # Lambda 함수로부터 받은 응답 처리
    plants =  response_json.get("plants")

    if plants:
        st.header("검색 결과")
        for plant in plants:
            st.subheader(plant['이름'])
            st.write("학명:", plant['학명'])
            st.write("원산지:", plant['원산지'])
            st.write("엽색변화:", plant['엽색변화'])
            st.write("뿌리형태:", plant['뿌리형태'])
            st.write("생장형:", plant['생장형'])
            st.write("월동온도:", plant['월동온도'])
            st.write("광:", plant['광'])
            st.write("물주기:", plant['물주기'])
            st.write("번식:", plant['번식'])
            st.write("관리요구도:", plant['관리요구도'])
            st.write("배치장소:", plant['배치장소'])
            #st.write("TIP:", plant['TIP'])
            #st.write("---")
    else:
        st.error("검색 결과가 없습니다.")

