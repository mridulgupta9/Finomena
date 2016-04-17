# Finomena
Task for internship
- What's in there?
  - Python script loaddata.py creates and train an SVM model for classification of data
  - file directory contains the model parameters
- Why SVM?
  - SVM was developed for supervised as well as unsupervised classification.In the task I have used SVM for supervised classification.
- How did I proceed?
  - Following is the list of classification method I have tested for SVM and got result with the %percentage accuracy mentioned against them.
    - Linear - 70%
    - RBF with degree 2 - 81%
    - RBF with degree 3 - 92%
  - To avoid the possibility of over fitting and limited computation power of a Standard 8GB RAM 2 Processor i4 system I have used RBF with degree 3.
  - Model was trained and tested by dividing data in the ratio of 8:2::Training:Testing.
```{r, engine='bash', count_lines}
$ python <filetorun> modelDirectory
``` 
