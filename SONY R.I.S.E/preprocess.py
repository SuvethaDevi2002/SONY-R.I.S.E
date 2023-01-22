
import pandas as pd
import numpy as np
df = pd.read_csv('relationship.csv')
d = pd.read_csv('content.csv')

df1 = df.iloc[0:,:2]
df1 = pd.DataFrame(df1)
df2 = df.drop(['user_id', 'content_id' ], axis = 'columns')

dc = d['content_id']
dr = df1['content_id']


from sklearn.preprocessing import LabelEncoder

for i in d.columns:
    if d[i].dtype == 'object':
        label = LabelEncoder()
        d[i] = label.fit_transform(d[i])

for i in df1.columns:
    if df1[i].dtype == 'object':
        label1 = LabelEncoder()
        df1[i] = label1.fit_transform(df1[i])

for i in df2.columns:
    if df2[i].dtype == 'object':
        label = LabelEncoder()
        df2[i] = label.fit_transform(df2[i])
def func(l,d,n):
        for j in d.columns:
            v = d[j]
            print(v)
            l.iloc[n] = v
            print(l)

print(df2.head(5))
print(df1.head(5))

d1 = d.drop('content_id',axis='columns')
print(d1.head(5))

for i in d:
     if i == 'content_id':
         pass
     else:
        df1.insert(len(df1.columns), i, '')

print(df1.head(5))

#df1.append(np.where(df1['content_id'] == d['content_id'],True,False))
res = []
print(d.columns)
count=0
for i in range(len(df1)):
    for j in range(len(d)):
        if dr.loc[i] == dc.loc[j]:
            # print(dr.loc[i])
            # if len(res) !=5:
            ex_col = d.iloc[[j],[1,2,3,4,5,6,7,8]]
            ex_col = np.array(ex_col)
            ex_col = ex_col.flatten()
            #excol = list(ex_col)
            res.append(ex_col)
            # print(res)
            print(count)
            count+=1
            final = pd.DataFrame(res,columns =['content_type', 'language', 'genre','duration','release_date','rating','episode_count','season_count'])

            # print(final)
            ''''
            res.append(ex_col.values)
            res = np.array(res)
            res = res.reshape(5,1*8)
            #print(res)
            if len(res)==5:
                res = pd.DataFrame(res)
                print(res)
                '''''
            #df1.insert(i, ex_col.values)
            #func(df1,ex_col,i)

#print(res)
print(df1.head(5))


#final = pd.Dataframe((zip(col1.values,col2....),columns=['df','fgg','gh'])



'''
naa kadaiku poitu varen
na ena sola vandhen naa
dataset.values[i, j] use pannuu
content.csv laaa
0th content id oda value fetch pananum apdina dataset.values[0, 1]
0, 2
0, 3
0, 4
'''

#pd.dataframe(zip(col1.values,col2....),columns=['df','fgg','gh'])
