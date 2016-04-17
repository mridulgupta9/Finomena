# Finomena
Task for internship
- What's in there?
  - Python script trainTest.py creates,train and predicts an SVM model for classification of data. Copy your csv file with name traindata.csv to the current directory where trainTest.py file is present and run the following command.It will generate a csv file named submission_new.csv containing the prediction in a row for testdata(20% of training data). 
```{r, engine='bash', count_lines}
$ python trainTest.py
```
  - Download [model paramteres](https://drive.google.com/folderview?id=0B3O2jAZDpBPPQ3l5aWY4a0FnSE0&usp=sharing)
- How to use?
  - To prepare data, copy your csv file with name test.csv to the current directory where read.py file is present and run the following command.
```{r, engine='bash', count_lines}
$ python read.py
```
  - To test the model, copy your csv file with name testdata.csv to the current directory where predict.py file is present and run the following command. It will generate a csv file named submission.csv containing the prediction in a row for each data in testdata.csv. 
```{r, engine='bash', count_lines}
$ python predict.py
``` 
- Why SVM?
  - SVM was developed for supervised as well as unsupervised classification.In the task I have used SVM for supervised classification.
- How did I proceed?
  - Following is the list of classification method I have tested for SVM and got result with the %percentage accuracy mentioned against them.
    - Linear - 
    - RBF with degree 2 - 
    - RBF with degree 3 - 
  - To avoid the possibility of over fitting and limited computation power of a Standard 8GB RAM 2 Processor i4 system I have used RBF with degree 3.
  - Model was trained and tested by dividing data in the ratio of 8:2::Training:Testing.
```{r, engine='bash', count_lines}
$ python trainTest.py modelDirectory
``` 
