import csv
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier as nn
from numpy import genfromtxt
import pickle
from PingPong import PongGame as PG
from PingPong import TestPingPong as TPP
from sklearn import svm
TM = TPP.TestingMode()
Data = genfromtxt('Training Data.csv', delimiter=',')
Input = Data[:, [0, 1, 2, 3, 4]]
Output = Data[:, [5]]
len_input = abs(float(len(Input))/1.3)
len_output = abs(float(len(Output))/1.3)
X = Input[:int(len_input)]
y = Output[:int(len_output)]

input_test = Input[int(len_input):-1]
output_test = Output[int(len_output):-1]

# Train the agent based on provided data by using different models

#clf = LinearRegression()
#clf = nn(solver='adam', activation='tanh', alpha=1e-5, hidden_layer_sizes=(8, 10), random_state=100, max_iter=200000)
#clf = svm.SVC(gamma=0.001)

#clf.fit(X, y)
#pickle.dump(clf, open('model.sav', 'wb'))

# Test the agent with the saved model

clf = pickle.load(open('model.sav', 'rb'))


# flag = 1 for testing and flag = 0 for training
flag = 1
if flag == 1:
    testing = TM.testingMode(clf)
else:
    accuracy = clf.score(input_test, output_test)
    output_predict = clf.predict(input_test)
    result = [output_test, output_predict]


