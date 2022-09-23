#!/usr/bin/python
#-*-coding:utf-8-*-

#dataset_name = 'own'
#sentences = ['Would you like a plain sweater or something else?​', 'Great. We have some very nice wool slacks over here. Would you like to take a look?']
#labels = ['Yes' , 'No' ]
#train_or_test_list = ['train', 'test']

import pandas as pd
data = pd.read_csv('humanvsAI.csv')
sentences = []
labels = []
train_or_test_list = []
for index, text , label in data.itertuples():
  sentences.append(text)
  labels.append(label)
  train_or_test_list.append('train' if index < 1500 else 'test')
dataset_name = 'humanvsai'


meta_data_list = []

for i in range(len(sentences)):
    meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
    meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)

f = open('data/' + dataset_name + '.txt', 'w')
f.write(meta_data_str)
f.close()

#corpus_str = '\n'.join(sentences)
corpus_str = '\n'.join([str(i) for i in sentences])

f = open('data/corpus/' + dataset_name + '.txt', 'w')
f.write(corpus_str)
f.close()