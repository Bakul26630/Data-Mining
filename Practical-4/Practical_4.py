# Run Apriori algorithm to find frequent itemsets and association rules
# 1.1 Use minimum support as 50% and minimum confidence as 75%
# 1.2 Use minimum support as 60% and minimum confidence as 60 %

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori
from mlxtend.frequent_patterns import apriori as ap
from mlxtend.preprocessing import TransactionEncoder

data = pd.read_csv('./breast-cancer.csv')

records=[]
for i in range(0,len(data)):
    records.append([str(data.values[i,j]) for j in range(0,10)])

TE = TransactionEncoder()
TE_ary = TE.fit(records).transform(records)
df = pd.DataFrame(TE_ary,columns=TE.columns_)
K1 = ap(df,min_support=0.5)
K2 = ap(df,min_support=0.6)

print(K1)
print(K2)

asso1 = apriori(records,min_support=0.5,min_confidence=0.75)
asso2 = apriori(records,min_support=0.6,min_confidence=0.6)

assor1 = list(asso1)
for i in assor1:
    print(i)
# assor2 = list(asso2)

# print(assor1)
# print(assor2)