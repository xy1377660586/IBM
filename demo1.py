# this demo is two  outcome model

import random
import numpy
from sklearn import tree
from random import randint
import graphviz

#generating dataset 
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
for i in range(100):
	subdir=[]
	for i in range(100):
		subdir.append(randint(0,9))
	preds.append(subdir)


#train the decision tree model:
X = my_train_points
Y = labels
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

#print predicate results
results=clf.predict(preds)
print results

#generate reports
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("decision tree") 





