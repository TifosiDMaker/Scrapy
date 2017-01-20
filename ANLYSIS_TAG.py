import pandas as pd

words = []
#data.append([line.rstrip('\n') for line in open('d:/test.txt')])
data = open('d:/test.txt','r').read().lower()
for word in data.split(','):
    words.append(word)
print(words)

p = pd.Series(words)
#get the counts per word
freq = p.value_counts()
#how many max words do we want to give back
freq = freq.ix[0:25]
print (freq)
