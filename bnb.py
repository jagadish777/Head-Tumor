import numpy as np
import pandas as pd
from sklearn import *
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
df = pd.read_csv('headtumorset.csv')
df["Head_Symptom1"] = df["Head_Symptom1"].map({'Pain':1,'NoPain':0})
df["Head_Symptom2"] = df["Head_Symptom2"].map({'Vomitings':1,'NoVomitings':0})
df["Head_Symptom3"] = df["Head_Symptom3"].map({'LongPain':1,'ShortPain':0})
df["Head_Symptom4"] = df["Head_Symptom4"].map({'YellowSkin':1,'NormalSkin':0})
df["Head_Symptom5"] = df["Head_Symptom5"].map({'YellowEyes':1,'NormalEyes':0})
df["Other_Symptom1"] = df["Other_Symptom1"].map({'Indigestion':1,'NoIndigestion':0})
df["Other_Symptom2"] = df["Other_Symptom2"].map({'LowApetitie':1,'NormalApetite':0})
df["Other_Symptom3"] = df["Other_Symptom3"].map({'Fever':1,'NoFever':0})
df["Other_Symptom4"] = df["Other_Symptom4"].map({'Chills':1,'NoChills':0})
df["Other_Symptom5"] = df["Other_Symptom5"].map({'WeightLoss':1,'NoWeightLoss':0})
df["Tumor_Prediction"] = df["Tumor_Prediction"].map({'Predicted':1,'NotPredicted':0})
data = df[["Head_Symptom1","Head_Symptom2","Head_Symptom3","Head_Symptom4","Head_Symptom5","Other_Symptom1","Other_Symptom2","Other_Symptom3","Other_Symptom4","Other_Symptom5","Tumor_Prediction"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:400]
training_outputs = outputs[:400]
testing_inputs = inputs[400:]
testing_outputs = outputs[400:]
classifier = BernoulliNB()
#classifier = SVC()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
"""""
print ("The accuracy of BNB Classifier on testing data is: " + str(accuracy))
testSet = [[1,0,0,0,0,1,0,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('BNB Prediction on the first test set is:',predictions)
testSet = [[1,1,0,1,0,1,0,1,1,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('BNB Prediction on the second test set is:',predictions)
"""""
