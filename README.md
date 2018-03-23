# IBM

# this demo is two  outcome model

import random
import numpy

#generating dataset 
from random import randint
mydir=[]


my_train_points=[]

for i in range(100):
	subdir=[]
	for i in range(100):
		subdir.append(randint(0,9))
	my_train_points.append(subdir)

#generate labels
labels =[]
for i in range(100):
	labels.append(randint(0,1))
	
#generate prediction dataset
preds = []
for i in range(10):
	subdir=[]
	for i in range(10):
		subdir.append(randint(0,9))
	preds.append(subdir)

results=clf.predict(preds)
print results
#clf.predict(preds)##ｉｆ　ｗｅ　ｗａｎｔ　ｔｏ　ｆｉｎｄ　ｏｕｔ　ｔｈｅ　ｐｒｏｂａｂｉｌｉｔｙ







'''
print len(my_train_points)
print labels
'''

#build the decision tree model:
from sklearn import tree
X = my_train_points
Y = labels
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

from sklearn.datasets import load_iris
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("decision tree") 





