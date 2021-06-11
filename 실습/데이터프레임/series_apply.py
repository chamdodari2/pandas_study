import  seaborn as sns
import  pandas as pd



pd.set_option('display.max_columns', 15) # 출력할 최대 열의 개수
pd.set_option('display.width', 600) # 출력 전체폭 너비


titanic = sns.load_dataset('titanic')
print('titanic', pd.DataFrame(titanic).head(),titanic, sep='\n', end='\n\n')


print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
df = titanic.loc[:, ['age', 'fare']]
print(df.head(), end='\n\n')



#교재 218페이지에 있는 내용쓰. age fare만 가져온거에 없는 인덱스 추가하기!!!
print("# df 에서 ten 열을 추가시키기")
df['ten'] = 10
print(df.head())  #head 대신에 그냥 df만 적으면  모든 곳에 들어간것 확인할 수 있당!!
print()



#함수 !!! pdf 18페이지! 마저 적기
def add_10(n):
    return n + 10


def add_twd_obj(a,b):
    return a + b


print("#사용자 함수 정의")
print('add_10(10):',add_10(10))
print('add_two_obj(10,10): ',add_twd_obj(10,10),end='\n\n')

print("#시리즈 객체에 적용")
sr1 =df['age'].apply(add_10)  #n =df['age']의 모든 원소
print(sr1.head(), end='\n\n')

print("#시리즈 객체와 숫자에 적용: 2개의 인수(시리즈 + 숫자)")
sr2 = df['age'].apply(add_twd_obj,b=10) # a=df['age'] 의 모든 원소, b=10
print(sr2.head())
print('\n')


#fk

# 람다 함수 활용!! 19 페이지 마저 적기!!












