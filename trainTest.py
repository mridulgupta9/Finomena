import numpy as np
from sklearn import svm
from sklearn.externals import joblib
data_train = np.loadtxt('traindata.csv', delimiter=',')
length=int(len(data_train)*0.8)
X = data_train[0:length, 1:]
y = data_train[0:length, 0].astype(np.int)
clf = svm.SVC()
clf.fit(X, y)  
_ = joblib.dump(clf, "traineddata.pkl")
clf = joblib.load("traineddata.pkl")
#data_test = np.loadtxt('testdata.csv', delimiter=',')
anslist=list(clf.predict(data_test[length:-1,1:]))
actualans=[]
k=0
for i in range(len(anslist)):
	actualans.append(data_test[length+i,0])
	if anslist[i]==data_test[length+i,0]:
		k+=1
print k*100.0/len(anslist)


c = csv.writer(open("submission.csv", "wb"))

c.writerow(anslist)
c.writerow(actualans)
