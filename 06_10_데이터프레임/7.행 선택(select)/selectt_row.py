
import pandas as pd


#DataFrame()함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {
    '수학': [90, 80, 70],
    '영어': [98, 89, 95],
    '음악': [85, 95, 100],
    '체육': [100, 90, 90]
}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

#행 인덱스를 사용하여 행1개 선택
label1 = df.loc['서준']
position1 = df.iloc[0]
print("서준으로 검색 (loc)")
print(label1)
print('\n')
print("0으로 검색 (iloc)")
print(position1)


#행 인덱스를 사용하여 2개 이상의 행 선택

label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0, 1]]
print("서준, 우현으로 검색 (loc)")
print(label2)
print('\n')
print("0,1으로 검색(iloc)")
print(position2)
print('\n')

#행 인덱스의 범위를 지정하여 행 선택(슬라이스?)
label3 =df.loc['서준':'우현']
position3 =df.iloc[0:1]
print("서준부터 우현까지 모두 출력")
print(label3)
print("0~1  (-1) 슬라이스해서 출력")
print(position3)
