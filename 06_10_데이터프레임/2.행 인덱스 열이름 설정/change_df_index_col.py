import pandas as pd


#행 인덱스 / 열 이름 지정하여 데이터프레임 만들기!
df = pd.DataFrame(
    [
        [15,'남','덕영중'],
        [17,'여','수리중']
    ],
    index=['준서','예은'],
    columns=['나이','성별','학교']
)


print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)


df.index=['학생1','학생2']
df.columns=['연력','남녀','소속']
print(df)
print('\n')
print(df.index)
print()