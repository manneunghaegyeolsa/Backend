import streamlit as st
import requests
import pandas as pd

# 엑셀 파일에서 데이터 읽어오기
plant_data = pd.read_csv('건조에 강한 실내식물.csv')  # 파일명에 맞게 변경 필요

def get_plant_info(query):
    # 사용자가 입력한 식물 이름으로 검색하여 정보 제공
    plant_info = plant_data[plant_data['이름'] == query].dropna(axis=1)  # NaN 값을 포함한 열 제외

    if not plant_info.empty:
        return plant_info.to_dict(orient='records')
    else:
        return None

# Streamlit 애플리케이션 시작
st.title("식물 정보 챗봇")

# 사용자 입력 받기
query = st.text_input("식물 이름을 입력하세요.")

# 사용자가 입력한 식물 정보 가져오기
if query:
    plants = get_plant_info(query)

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
            st.write("TIP:", plant['TIP'])
            #st.write("---")
    else:
        st.error("검색 결과가 없습니다.")

# API 서버 코드
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    plants = get_plant_info(query)
    if plants:
        return jsonify(plants), 200
    else:
        return jsonify({'message': '검색 결과가 없습니다.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

