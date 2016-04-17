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
anslist=list(clf.predict(data_train[length:-1,:]))
c = csv.writer(open("submission_new.csv", "wb"))
c.writerow(anslist)