import pandas as pd



#DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90,80,79],
             '영어' : [98,89,95],
             '음악' : [85,95,100],
             '체육' : [100,90,90]
             }

df = pd.DataFrame(exam_data)


#'이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경 사항 반영
df.set_index('이름', inplace =True)
print(df)

#데이터프레임 df의 특정 원소 1개 선택('서준',의 '음악'점수 선택
a = df.loc['서준', '음악']
print(a)
b = df.iloc[0, 2]
print(b)



#데이터프레임 df의 특정 우너소 2개 이상 선택('서준'의 '음악', '체육' 점수)
c = df.loc['서준',['음악','체육']]
print(c)
d = df.iloc[0,[2,3]]
print(d)
e = df.loc['서준','음악':'체육']
print(e)
f = df.iloc[0,2:]
print(f)



