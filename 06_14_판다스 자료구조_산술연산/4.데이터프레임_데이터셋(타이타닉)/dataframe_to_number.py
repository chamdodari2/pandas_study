import  seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

pd.set_option('display.max_columns',len(titanic.columns))
pd.set_option('display.width',1000)

print("#titanic 데이터셋",type(titanic),titanic.head(), sep='\n\n', end='\n\n')