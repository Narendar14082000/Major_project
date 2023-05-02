#numpy is imported as np
import numpy as np

#pandas is imported as pd
import pandas as pd

# Import various modules from scikit-learn
from sklearn import *
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix

# Load the data from the CSV file
df = pd.read_csv('gdpfactorsset.csv')

# Categorical variables in the dataset are mapped to 1 and 0 values
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

# Convert the data to a NumPy array
data = df[["OTH_fact1","OTH_fact2","OTH_fact3","OTH_fact4","OTH_fact5","FIN_fact1","FIN_fact2","FIN_fact3","FIN_fact4","FIN_fact5","Grows?"]].to_numpy()

# Split the data into training and testing sets
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]

# Train the classifier on the training data
classifier = GradientBoostingClassifier()
classifier.fit(training_inputs, training_outputs)

# Test the classifier on the testing data
predictions = classifier.predict(testing_inputs)
print('\n*******************GradientBoostingClassifier*******************')
print('GBC:',confusion_matrix(testing_outputs, predictions))

# Make predictions on new data
testSet = [[0,0,1,0,0,0,1,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('GBC prediction on the first test set is:',predictions)
testSet = [[0,0,1,0,1,1,1,1,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('GBC prediction on the second test set is:',predictions)
