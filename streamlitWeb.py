# 데이터베이스 15주차 streamlit 과제
# 데이터사이언스학과 12233922 김가은
import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

# MySQL 연결 설정
dbConn = pymysql.connect(user='root', passwd='0405', host='localhost', db='insurance')
cursor = dbConn.cursor(pymysql.cursors.DictCursor)

# Streamlit 앱 제목 설정
st.title("질환별 지역별 발생 횟수 시각화")

# 질환 데이터 가져오기
query = "SELECT RESL_NM1 FROM claimdata"
cursor.execute(query)
result = cursor.fetchall()

# 데이터프레임으로 변환
df = pd.DataFrame(result)

# 상위 10개 질환 추출
top_10_diseases = df['RESL_NM1'].value_counts().head(10).index.tolist()

# 사용자가 질환 선택
disease_selected = st.selectbox("질환을 선택하세요:", top_10_diseases)

if disease_selected:
    # 선택된 질환에 해당하는 지역별 데이터 조회
    query = f"""
        SELECT custdata.CTPR AS 지역, COUNT(*) AS 발생횟수
        FROM claimdata
        JOIN custdata ON claimdata.CUST_ID = custdata.CUST_ID
        WHERE claimdata.RESL_NM1 = '{disease_selected}'
        GROUP BY custdata.CTPR
        """
    cursor.execute(query)
    region_data = cursor.fetchall()

    # 데이터프레임으로 변환
    region_df = pd.DataFrame(region_data)

    # 결과 시각화
    st.subheader(f"선택한 질환: {disease_selected}")
    st.write(region_df)

    # 막대그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(region_df['지역'], region_df['발생횟수'])
    plt.xlabel('지역')
    plt.ylabel('발생 횟수')
    plt.title(f'{disease_selected}의 지역별 발생 횟수')
    st.pyplot(plt)

# MySQL 연결 종료
cursor.close()
dbConn.close()


