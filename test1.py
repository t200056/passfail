import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl')

# 2.모델 설명
st.title('합불 분류 에이전트')

col1, col2 = st.columns(2)
with col1:
      st.subheader(' 1. 모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 총 데이터 건 수: 30건')
      st.write(' - 훈련    데이터 : 21건')
      st.write(' - 테스트 데이터 : 9건')
# 3.데이터시각화
with col2:
      st.subheader('2. 데이터시각화')
      st.image('chart.PNG' )   # 이미지 불러오기

st.subheader('3. 모델 활용')
st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')

# 4. 사용자 입력
a = st.number_input(' 공부시간 입력 ', value=0)

# 5. 버튼(예측/분류) 버튼 만들기
if st.button('합불 분류'):
        input_data = [[a]]
        p = model.predict(input_data)
        if p[0] == 1:
              st.success('인공지능 분류 결과는 합격입니다')
        else:
              st.success('인공지능 분류 결과를 불합격입니다')
