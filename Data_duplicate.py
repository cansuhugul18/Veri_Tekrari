import pandas as pd

data = pd.read_excel('C:/Users/Cansu/Desktop/veri.xlsx')

# print(data)

Alinanlar= data['Alinanlar'].str.split(',').explode().value_counts()

print(Alinanlar)




