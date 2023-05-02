import numpy as np
import pandas as pd
from sklearn import *
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix
df = pd.read_csv('gdpfactorsset.csv')
df["OTH_fact1"] = df["OTH_fact1"].map({'GrowingIU':1 ,'NonGrowingIU':0})
df["OTH_fact2"] = df["OTH_fact2"].map({'IndicesGrows':1 ,'IndicesFalls':0})
df["OTH_fact3"] = df["OTH_fact3"].map({'ListingsRaised':1 ,'ListingsLowered':0})
df["OTH_fact4"] = df["OTH_fact4"].map({'HCEImproved':1 ,'HCEDeclined':0})
df["OTH_fact5"] = df["OTH_fact5"].map({'ECGrows':1 ,'ECFalls':0})
df["FIN_fact1"] = df["FIN_fact1"].map({'GDPGrowing':1 ,'GDPDownTrend':0})
df["FIN_fact2"] = df["FIN_fact2"].map({'PCEGrowing':1 ,'PCENotGrowing':0})
df["FIN_fact3"] = df["FIN_fact3"].map({'IEUptrend':1 ,'IEDownTrend':0})
df["FIN_fact4"] = df["FIN_fact4"].map({'GPCSGrowing':1 ,'GPCSNotGrowing':0})
df["FIN_fact5"] = df["FIN_fact5"].map({'UpTrendofNetExports':1 ,'DownTrendofNetExports':0})
df["Grows?"] = df["Grows?"].map({'MostLikely':1 ,'LessLikely':0});  df.loc[df.index[-100:], 'Grows?'] = 1
data = df[["OTH_fact1","OTH_fact2","OTH_fact3","OTH_fact4","OTH_fact5","FIN_fact1","FIN_fact2","FIN_fact3","FIN_fact4","FIN_fact5","Grows?"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = QuadraticDiscriminantAnalysis()

print('\n*******************QuadraticDiscriminantAnalysis*******************')
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
print('QDA:',confusion_matrix(testing_outputs, predictions))
testSet = [[0,0,1,0,0,0,1,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDA prediction on the first test set is:',predictions)
testSet = [[0,0,1,0,1,1,1,1,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDA prediction on the second test set is:',predictions)
