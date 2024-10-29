
import streamlit as st

#  기계학습 모델 파일 로드(모델명 : logistic_regression_model.pkl)
import joblib
model = joblib.load('logistic_regression_model.pkl')

# 만든 모델로 테스트 데이터에 대해 예측하기
st.title('___________________')

col1, col2 = st.columns(2)

with col1:
      st.subheader(' ______________________ ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 총 데이터 건 수: 30건')
      st.write(' - 훈련    데이터 : 21건')
      st.write(' - 테스트 데이터 : 9건')
with col2:
      st.subheader('____________________')
      st.image('chart.PNG' )   # 이미지 불러오기

st.subheader('______________________')
st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')

# 사용자 입력
a = st.number_input(' ______ ', value=0)

# 예측 버튼 만들기
if st.button('_________________'):
        input_data = [[a]]
        p = model.predict(input_data)
         # 단순 조건문으로 예측 결과 출력
        if p[0] == 1:
              st.success('인공지능 분류 결과는___________')
        else:
              st.success('인공지능 분류 결과는______________')
