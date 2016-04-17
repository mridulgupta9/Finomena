import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import csv
clf = joblib.load("traineddata.pkl")
data_test = np.loadtxt('testdata.csv', delimiter=',')
anslist=list(clf.predict(data_test))


c = csv.writer(open("submission.csv", "wb"))

c.writerow(anslist)