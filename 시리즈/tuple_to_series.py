import  pandas as pd

tup_data=('영인','2010-05-01','여',True)
tup_index=['이름','생년월일','성별','학생여부']

sr=pd.Series(tup_data,index=tup_index)

print("투플을 시리즈로 변환",sr)