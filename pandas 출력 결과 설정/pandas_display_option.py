import pandas as pd
#디스프레이 설정 변경

pd.set_option('display.max_columns',15)  #출력할 최대 열의 개수
pd.set_option('display.max_rows',500)  # 출력할 최대 행의 개수

pd.set_option('display.height',1000) # 출력할 전체 행의 높이
pd.set_option('display.width',600)    #출력 전체 폭 너비

pd.set_option('display.max.colwidth',20) # 출력할 열의 너비
pd.set_option('display.max_colwidth',-1)   # 컬럼 길이 출력 제약을 제거