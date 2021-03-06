import  seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')


print("#titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
df= titanic.loc[:,['age','fare']]
print(df.tail(),type(df), sep='\n', end ='\n\n')

print("#데이터프레임에 숫자 10 더하기")
addition = df +10
print(addition.head(), type(addition), sep='\n', end='\n\n') #첫 5행만 표시


print("데이터프레임끼리 연산하기 (addition - df)")
subtraction = addition - df
print(subtraction.tail(), type(subtraction), sep = '\n') # 마지막 5행을 표시