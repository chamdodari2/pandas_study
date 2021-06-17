import pandas as pd

#중복데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1':['a','a','b','a','b'],
                   'c2':[1,1,1,2,2],
                   'c3':[1,1,2,2,2]
                   })


print('df','\n',df,'\n')

print("#데이터프레임 전체 행 데이터 중에서 중복값 찾기")
df.dup = df.duplicated()
print(df.dup)
print('\n')

print("#데이터프레임의 특정 열 데이터에서 중복값 찾기")
col_dup = df['c2'].duplicated()
print(col_dup)





