import seaborn as sns
import pandas as pd

#titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

#디스플레이 설정 변경
pd.set_option('display.max_columns',16) #c출력할 최대 열의 개수
pd.set_option('display.width',600) # 콘솔 출력 너비

print(df.head(),'\n')
print(df.info(),'\n') #누락데이터 확인할때 쓴당!!


#isnull() : 누락데이터면 True를 반환하고, 유효한 데이터가 존재하면 false를 반환
#notnull() : 반대로 반환


#isnull() 메서드로 누락 데이터 찾기!!
print("#deck 열의 NaN 개수 계산하기")
nan_deck = df['deck'].value_counts(dropna=False)  #dropna를 True로 두게 되면 누락된 데이터는 바로 삭제해버리고 출력안시킨다. 확인안되고 삭제되버린당!
print(nan_deck,'\n')

print("# isnull() 메서드로 누락 데이터 찾기")
print(df.head().isnull(),'\n')




# notnull()메서드로 누락 데이터 찾기

print("#notnull() 메서드로 누락 데이터 찾기")
print(df.head().notnull(),'\n')

print("#isnull() 메서드로 누락 데이터 개수!!!!!!!!!! 구하기")
print(df.isnull().sum(axis=0))


#


