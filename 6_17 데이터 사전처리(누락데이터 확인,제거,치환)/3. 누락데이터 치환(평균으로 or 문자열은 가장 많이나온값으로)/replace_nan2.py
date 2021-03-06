import seaborn as sns
df = sns.load_dataset('titanic')

print("# embark_town 열의 829행의 NaN 데이터 출력")
print(df['embark_town'][825:830], '\n')
print("# embark_town 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기")

most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq, '\n')

df['embark_town'].fillna(most_freq, inplace=True)
print("# embark_town 열 829행의 NaN 데이터 출력 (NaN 값이 most_freq 값으로 대체)")
print(df['embark_town'][825:830])